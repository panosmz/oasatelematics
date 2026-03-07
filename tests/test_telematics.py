from unittest.mock import Mock, patch

import pytest
import requests.exceptions

import oasatelematics


# --- Core telematics_request tests ---


@patch("oasatelematics.requests.post")
def test_request_happy_path(mock_post):
    response = Mock()
    response.text = '[{"key": "value"}]'
    response.json.return_value = [{"key": "value"}]
    response.raise_for_status = Mock()
    mock_post.return_value = response

    result = oasatelematics.telematics_request("?act=test")

    assert result == [{"key": "value"}]
    mock_post.assert_called_once_with("https://telematics.oasa.gr/api/?act=test")


@patch("oasatelematics.requests.post")
def test_request_uses_https(mock_post):
    response = Mock()
    response.text = "[]"
    response.json.return_value = []
    response.raise_for_status = Mock()
    mock_post.return_value = response

    oasatelematics.telematics_request("?act=test")

    url = mock_post.call_args[0][0]
    assert url.startswith("https://")


@patch("oasatelematics.requests.post")
def test_request_null_response_returns_empty(mock_post):
    response = Mock()
    response.text = "null"
    response.status_code = 200
    response.raise_for_status = Mock(
        side_effect=requests.exceptions.HTTPError()
    )
    mock_post.return_value = response

    result = oasatelematics.telematics_request("?act=test")

    assert result == []


@patch("oasatelematics.requests.post")
def test_request_http_error_returns_empty(mock_post):
    response = Mock()
    response.text = "error"
    response.raise_for_status = Mock(
        side_effect=requests.exceptions.HTTPError()
    )
    mock_post.return_value = response

    result = oasatelematics.telematics_request("?act=test")

    assert result == []


# --- Home Assistant critical functions ---


@patch("oasatelematics.requests.post")
def test_getRouteName_ha_compat(mock_post):
    response = Mock()
    response.text = "ok"
    response.json.return_value = [
        {"route_departure_eng": "PIRAEUS - KIFISIA"}
    ]
    response.raise_for_status = Mock()
    mock_post.return_value = response

    result = oasatelematics.getRouteName("1234")

    assert isinstance(result, list)
    assert result[0].get("route_departure_eng") == "PIRAEUS - KIFISIA"


@patch("oasatelematics.requests.post")
def test_getStopNameAndXY_ha_compat(mock_post):
    response = Mock()
    response.text = "ok"
    response.json.return_value = [
        {"stop_descr_matrix_eng": "SYNTAGMA"}
    ]
    response.raise_for_status = Mock()
    mock_post.return_value = response

    result = oasatelematics.getStopNameAndXY("340088")

    assert isinstance(result, list)
    assert result[0].get("stop_descr_matrix_eng") == "SYNTAGMA"


@patch("oasatelematics.requests.post")
def test_getStopArrivals_ha_compat(mock_post):
    response = Mock()
    response.text = "ok"
    response.json.return_value = [
        {"route_code": "5331", "veh_code": "59789", "btime2": "13"},
        {"route_code": "5332", "veh_code": "59790", "btime2": "25"},
    ]
    response.raise_for_status = Mock()
    mock_post.return_value = response

    result = oasatelematics.getStopArrivals("340088")

    assert isinstance(result, list)
    assert len(result) == 2
    assert "route_code" in result[0]
    assert "btime2" in result[0]


# --- Parameterized wrapper function tests ---


@pytest.mark.parametrize(
    "func,args,expected_query",
    [
        (oasatelematics.webGetLines, (), "?act=webGetLines"),
        (oasatelematics.webGetLinesWithMLInfo, (), "?act=webGetLinesWithMLinfo"),
        (oasatelematics.webGetRoutes, ("L1",), "?act=webGetRoutes&p1=L1"),
        (oasatelematics.webRouteDetails, ("R1",), "?act=webRouteDetails&p1=R1"),
        (oasatelematics.webGetStops, ("R1",), "?act=webGetStops&p1=R1"),
        (oasatelematics.webRoutesForStop, ("S1",), "?act=webRoutesForStop&p1=S1"),
        (oasatelematics.webGetRoutesDetailsAndStops, ("R1",), "?act=webGetRoutesDetailsAndStops&p1=R1"),
        (oasatelematics.getStopArrivals, ("S1",), "?act=getStopArrivals&p1=S1"),
        (oasatelematics.getBusLocation, ("R1",), "?act=getBusLocation&p1=R1"),
        (oasatelematics.getScheduleDaysMasterline, ("L1",), "?act=getScheduleDaysMasterline&p1=L1"),
        (oasatelematics.getLinesAndRoutesForMl, ("ML1",), "?act=getLinesAndRoutesForMl&p1=ML1"),
        (oasatelematics.getRoutesForLine, ("L1",), "?act=getRoutesForLine&p1=L1"),
        (oasatelematics.getMLName, ("ML1",), "?act=getMLName&p1=ML1"),
        (oasatelematics.getLineName, ("L1",), "?act=getLineName&p1=L1"),
        (oasatelematics.getRouteName, ("R1",), "?act=getRouteName&p1=R1"),
        (oasatelematics.getStopNameAndXY, ("S1",), "?act=getStopNameAndXY&p1=S1"),
        (oasatelematics.getClosestStops, ("23.7", "37.9"), "?act=getClosestStops&p1=23.7&p2=37.9"),
        (oasatelematics.getDailySchedule, ("L1",), "?act=getDailySchedule&line_code=L1"),
    ],
)
@patch("oasatelematics.requests.post")
def test_wrapper_builds_correct_query(mock_post, func, args, expected_query):
    response = Mock()
    response.text = "ok"
    response.json.return_value = [{"data": "test"}]
    response.raise_for_status = Mock()
    mock_post.return_value = response

    result = func(*args)

    mock_post.assert_called_once_with(
        f"https://telematics.oasa.gr/api/{expected_query}"
    )
    assert result == [{"data": "test"}]


# --- Edge cases ---


@patch("oasatelematics.requests.post")
def test_getSchedLines_parameter_ordering(mock_post):
    """getSchedLines(mlcode, linecode, sdc_code) maps to p1=mlcode, p2=sdc_code, p3=linecode."""
    response = Mock()
    response.text = "ok"
    response.json.return_value = [{"sched": "data"}]
    response.raise_for_status = Mock()
    mock_post.return_value = response

    oasatelematics.getSchedLines("ML1", "L1", "SDC1")

    mock_post.assert_called_once_with(
        "https://telematics.oasa.gr/api/?act=getddSchedLines&p1=ML1&p2=SDC1&p3=L1"
    )


@patch("oasatelematics.requests.post")
def test_null_response_propagates_through_wrapper(mock_post):
    response = Mock()
    response.text = "null"
    response.status_code = 200
    response.raise_for_status = Mock(
        side_effect=requests.exceptions.HTTPError()
    )
    mock_post.return_value = response

    assert oasatelematics.getStopArrivals("999") == []
    assert oasatelematics.getRouteName("999") == []
