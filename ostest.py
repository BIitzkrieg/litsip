from subprocess import (PIPE, Popen)


def invoke(command):
    '''
    Invoke command as a new system process and return its output.
    '''
    return Popen(command, stdout=PIPE, shell=True).stdout.read()


result = invoke('echo Hi, bash!')
