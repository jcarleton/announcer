from subprocess import check_output, CalledProcessError


def procStat(procName):

    # enum pids
    try:
        pidlist = map(int, check_output(["pgrep", procName]).split())
        hostname = check_output(["hostname"])
        hostname = hostname.decode("utf-8").strip('\n')
        pidcount = str(len(list(pidlist)))
    except CalledProcessError:
        pidlist = []
        hostname = check_output(["hostname"])
        hostname = hostname.decode("utf-8").strip('\n')
        pidcount = str(len(list(pidlist)))

    # create objects to add to array
    if int(pidcount) < 1:
        statusOut = {'Hostname': hostname, 'Process Name': procName, 'status': 'Not Running',
                     'status (boolean)': 'False', 'Thread Count': '0'}
        return statusOut
    else:
        statusOut = {'Hostname': hostname, 'Process Name': procName, 'status': 'Running', 'status (boolean)': 'True',
                     'Thread Count': str(pidcount)}
        return statusOut
