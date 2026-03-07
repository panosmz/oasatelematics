import requests

__version__ = "0.4"

API_ENDPOINT = "https://telematics.oasa.gr/api/"


def telematics_request(query: str):
    req = requests.post(API_ENDPOINT + query)

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
    return telematics_request('?act=webGetLines')


def webGetLinesWithMLInfo():
    return telematics_request('?act=webGetLinesWithMLinfo')


def webGetRoutes(linecode):
    return telematics_request(f'?act=webGetRoutes&p1={linecode}')


def webRouteDetails(routecode):
    return telematics_request(f'?act=webRouteDetails&p1={routecode}')


def webGetStops(routecode):
    return telematics_request(f'?act=webGetStops&p1={routecode}')


def webRoutesForStop(stopcode):
    return telematics_request(f'?act=webRoutesForStop&p1={stopcode}')


def webGetRoutesDetailsAndStops(routecode):
    return telematics_request(f'?act=webGetRoutesDetailsAndStops&p1={routecode}')


def getStopArrivals(stopcode):
    return telematics_request(f'?act=getStopArrivals&p1={stopcode}')


def getBusLocation(routecode):
    return telematics_request(f'?act=getBusLocation&p1={routecode}')


def getScheduleDaysMasterline(linecode):
    return telematics_request(f'?act=getScheduleDaysMasterline&p1={linecode}')


def getLinesAndRoutesForMl(mlcode):
    return telematics_request(f'?act=getLinesAndRoutesForMl&p1={mlcode}')


def getRoutesForLine(linecode):
    return telematics_request(f'?act=getRoutesForLine&p1={linecode}')


def getMLName(mlcode):
    return telematics_request(f'?act=getMLName&p1={mlcode}')


def getLineName(linecode):
    return telematics_request(f'?act=getLineName&p1={linecode}')


def getRouteName(routecode):
    return telematics_request(f'?act=getRouteName&p1={routecode}')


def getStopNameAndXY(stopcode):
    return telematics_request(f'?act=getStopNameAndXY&p1={stopcode}')


def getSchedLines(mlcode, linecode, sdc_code):
    return telematics_request(f'?act=getddSchedLines&p1={mlcode}&p2={sdc_code}&p3={linecode}')


def getClosestStops(lon, lat):
    return telematics_request(f'?act=getClosestStops&p1={lon}&p2={lat}')


def getDailySchedule(linecode):
    return telematics_request(f'?act=getDailySchedule&line_code={linecode}')
