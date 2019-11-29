import requests
import checkurl.nagios


def testurl(url, warn=1.0, crit=5.0):
    """Checks URL and returns a nagios code and a message"""
    #try:
    #    r = requests.get(url)
    #except Exception as e:
    #    return(checkurl.nagios.UNKNOWN, str(e))
   # 
    r = requests.get(url)
    if r.status_code >= 400:
        return(checkurl.nagios.CRITICAL, "status code: {}".format(r.status_code))

    elapsed = r.elapsed.total_seconds()
    if  elapsed > crit:
        return(checkurl.nagios.CRITICAL, "latency: {}".format(elapsed))
    
    # test stuff
    return(checkurl.nagios.OK, "Elapsed time: {}, status code: {}".format(elapsed, r.status_code))