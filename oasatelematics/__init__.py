import requests

def telematics_request(query: str):
    api_endpoint = 'http://telematics.oasa.gr/api/'

    req = requests.post(api_endpoint + query)

    if req.text == 'null':
        # even though server returns null,
        # IT STILL RETURNS A 200 STATUS CODE FOR SOME REASON.
        req.status_code = 404

    try:
        req.raise_for_status()

    except (requests.exceptions.HTTPError,
            requests.exceptions.ConnectionError,
            requests.exceptions.Timeout):

        return []

    return req.json()


def webGetLines():
    query = '?act=webGetLines'
    return telematics_request(query)


def webGetLinesWithMLInfo():
    query = '?act=webGetLinesWithMLinfo'
    return telematics_request(query)


def webGetRoutes(linecode):
    query = '?act=webGetRoutes&p1={}'.format(linecode)
    return telematics_request(query)


def webRouteDetails(routecode):
    query = '?act=webRouteDetails&p1={}'.format(routecode)
    return telematics_request(query)


def webGetStops(routecode):
    query = '?act=webGetStops&p1={}'.format(routecode)
    return telematics_request(query)


def webRoutesForStop(stopcode):
    query = '?act=webRoutesForStop&p1={}'.format(stopcode)
    return telematics_request(query)


def webGetRoutesDetailsAndStops(routecode):
    query = '?act=webGetRoutesDetailsAndStops&p1={}'.format(routecode)
    return telematics_request(query)


def getStopArrivals(stopcode):
    query = '?act=getStopArrivals&p1={}'.format(stopcode)
    return telematics_request(query)


def getBusLocation(routecode):
    query = '?act=getBusLocation&p1={}'.format(routecode)
    return telematics_request(query)


def getScheduleDaysMasterline(linecode):
    query = '?act=getScheduleDaysMasterline&p1={}'.format(linecode)
    return telematics_request(query)


def getLinesAndRoutesForMl(mlcode):
    query = '?act=getLinesAndRoutesForMl&p1={}'.format(mlcode)
    return telematics_request(query)


def getRoutesForLine(linecode):
    query = '?act=getRoutesForLine&p1={}'.format(linecode)
    return telematics_request(query)


def getMLName(mlcode):
    query = '?act=getMLName&p1={}'.format(mlcode)
    return telematics_request(query)


def getLineName(linecode):
    query = '?act=getLineName&p1={}'.format(linecode)
    return telematics_request(query)


def getRouteName(routecode):
    query = '?act=getRouteName&p1={}'.format(routecode)
    return telematics_request(query)


def getStopNameAndXY(stopcode):
    query = '?act=getStopNameAndXY&p1={}'.format(stopcode)
    return telematics_request(query)


def getSchedLines(mlcode, linecode, sdc_code):
    query = '?act=getddSchedLines&p1={}&p2={}&p3={}'.format(mlcode, sdc_code, linecode)
    return telematics_request(query)


def getClosestStops(lon, lat):
    query = '?act=getClosestStops&p1={}&p2={}'.format(lon, lat)
    return telematics_request(query)

def getDailySchedule(linecode):
    query = '?act=getDailySchedule&line_code={}'.format(linecode)
    return telematics_request(query)
