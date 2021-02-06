#!/usr/bin/python3
import os
import sys
import time
import signal
import atexit
"""define the daemon function
    only run in linux, windows can't  use os.fork"""


def daemonize(pid_file, *, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
    # check the pid file exist or not
    if os.path.exists(pid_file):
        raise RuntimeError('Program is already running!')
    # first fork a child progress
    try:
        if os.fork() > 0:
            raise SystemExit(0)
    except OSError:
        raise RuntimeError('fork child progress failed!')
    # change the work dir,reset the umask,create new session for child progress
    os.chdir('/')
    os.umask(0)
    os.setsid()
    # second fork a child progress
    try:
        if os.fork() > 0:
            raise SystemExit(0)
    except OSError:
        raise RuntimeError('second fork child progress failed!')
    # Flush Error(stderr)、Output(stdout) buffer(stdin不用重置)
    sys.stderr.flush()
    sys.stdout.flush()
    # replace file descriptors for stdin, stdout,stderr
    with open(stdin, 'rb', buffering=0) as f:
        os.dup2(f.fileno(), sys.stdin.fileno())
    with open(stdout, 'ab', buffering=0) as f:
        os.dup2(f.fileno(), sys.stdout.fileno())
    with open(stderr, 'ab', buffering=0) as f:
        os.dup2(f.fileno(), sys.stderr.fileno())
    # write the pid file
    with open(pid_file, 'w') as f:
        print(os.getpid(), file=f)
    # when receive a signal or on exit, remove the pidfile
    atexit.register(lambda: os.remove(pid_file))
    # signal hander for termination
    def sigterm_hander(signo, frame):
        raise SystemExit(1)

    signal.signal(signal.SIGTERM, sigterm_hander)


def main():
    sys.stdout.write('Daemon started with PID: %s\n,' % os.getpid())
    while True:
        sys.stdout.write('Daemon is alive! %s \n' % time.ctime())
        time.sleep(3)


if __name__ == '__main__':
    PID_FILE = '/tmp/daemon01.pid'
    
    if len(sys.argv) != 2:
        print('Usage: {} [start|stop]'.format(sys.argv[0], file=sys.stderr))
        raise SystemExit(1)

    if sys.argv[1] == 'start':
        try:
            daemonize(PID_FILE, stdout='/tmp/daemon.log', stderr='/tmp/daemon.log')
        except RuntimeError as e:
            print(e, sys.stderr)
            raise SystemExit(1)
        main()

    elif sys.argv[1] == 'stop':
        if os.path.exists(PID_FILE):
            with open(PID_FILE, encoding='utf-8') as f:
                os.kill(int(f.read()), signal.SIGTERM)
        else:
            print('Daemon is dead,No running!', file=sys.stderr)
            raise SystemExit(1)
    else:
        print('Unknown command {!r}'.format(sys.argv[1]), file=sys.stderr)
        raise SystemExit(1)

