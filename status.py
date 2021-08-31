from subprocess import check_output, CalledProcessError

def procStat(procName):
    # enum pids
    try:
        pidlist = map(int, check_output(["pgrep", procName]).split())
        pidcount = str(len(list(pidlist)))
    except CalledProcessError:
        pidlist = []
        pidcount = str(len(list(pidlist)))

    # create objects to add to array
    if int(pidcount) < 1:
        statusOut = {'Process Name': procName, 'status': 'Not Running', 'status (boolean)': 'False',
                     'Thread Count': '0'}
        return statusOut
    else:
        statusOut = {'Process Name': procName, 'status': 'Running', 'status (boolean)': 'True',
                     'Thread Count': str(pidcount)}
        return statusOut
