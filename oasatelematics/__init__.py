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
    query = f'?act=webGetRoutes&p1={linecode}'
    return telematics_request(query)


def webRouteDetails(routecode):
    query = f'?act=webRouteDetails&p1={routecode}'
    return telematics_request(query)


def webGetStops(routecode):
    query = f'?act=webGetStops&p1={routecode}'
    return telematics_request(query)


def webRoutesForStop(stopcode):
    query = f'?act=webRoutesForStop&p1={stopcode}'
    return telematics_request(query)


def webGetRoutesDetailsAndStops(routecode):
    query = f'?act=webGetRoutesDetailsAndStops&p1={routecode}'
    return telematics_request(query)


def getStopArrivals(stopcode):
    query = f'?act=getStopArrivals&p1={stopcode}'
    return telematics_request(query)


def getBusLocation(routecode):
    query = f'?act=getBusLocation&p1={routecode}'
    return telematics_request(query)


def getScheduleDaysMasterline(linecode):
    query = f'?act=getScheduleDaysMasterline&p1={linecode}'
    return telematics_request(query)


def getLinesAndRoutesForMl(mlcode):
    query = f'?act=getLinesAndRoutesForMl&p1={mlcode}'
    return telematics_request(query)


def getRoutesForLine(linecode):
    query = f'?act=getRoutesForLine&p1={linecode}'
    return telematics_request(query)


def getMLName(mlcode):
    query = f'?act=getMLName&p1={mlcode}'
    return telematics_request(query)


def getLineName(linecode):
    query = f'?act=getLineName&p1={linecode}'
    return telematics_request(query)


def getRouteName(routecode):
    query = f'?act=getRouteName&p1={routecode}'
    return telematics_request(query)


def getStopNameAndXY(stopcode):
    query = f'?act=getStopNameAndXY&p1={stopcode}'
    return telematics_request(query)


def getSchedLines(mlcode, linecode, sdc_code):
    query = f'?act=getddSchedLines&p1={mlcode}&p2={sdc_code}&p3={linecode}'
    return telematics_request(query)


def getClosestStops(lon, lat):
    query = f'?act=getClosestStops&p1={lon}&p2={lat}'
    return telematics_request(query)
