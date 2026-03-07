"""Integration tests that hit the real OASA Telematics API.

Run with: pytest -m integration
"""

import pytest

import oasatelematics

pytestmark = pytest.mark.integration


def test_webGetLines():
    result = oasatelematics.webGetLines()
    assert isinstance(result, list)
    assert len(result) > 0


def test_webGetLinesWithMLInfo():
    result = oasatelematics.webGetLinesWithMLInfo()
    assert isinstance(result, list)
    assert len(result) > 0


def test_webGetRoutes():
    lines = oasatelematics.webGetLines()
    assert len(lines) > 0
    line_code = lines[0].get("line_code") or lines[0].get("LineCode")
    result = oasatelematics.webGetRoutes(line_code)
    assert isinstance(result, list)


def test_getRouteName():
    """Verifies the response format used by Home Assistant."""
    lines = oasatelematics.webGetLines()
    assert len(lines) > 0
    line_code = lines[0].get("line_code") or lines[0].get("LineCode")
    routes = oasatelematics.webGetRoutes(line_code)
    assert len(routes) > 0
    route_code = routes[0].get("route_code") or routes[0].get("RouteCode")
    result = oasatelematics.getRouteName(route_code)
    assert isinstance(result, list)
    assert len(result) > 0
    assert "route_departure_eng" in result[0] or "RouteDepartureEng" in result[0]


def test_getStopNameAndXY():
    """Verifies the response format used by Home Assistant."""
    lines = oasatelematics.webGetLines()
    line_code = lines[0].get("line_code") or lines[0].get("LineCode")
    routes = oasatelematics.webGetRoutes(line_code)
    route_code = routes[0].get("route_code") or routes[0].get("RouteCode")
    stops = oasatelematics.webGetStops(route_code)
    assert len(stops) > 0
    stop_code = stops[0].get("StopCode") or stops[0].get("stop_code")
    result = oasatelematics.getStopNameAndXY(stop_code)
    assert isinstance(result, list)
    assert len(result) > 0


def test_getStopArrivals():
    """Verifies the response format used by Home Assistant.

    Note: may return [] if no buses are running (e.g. late at night).
    """
    lines = oasatelematics.webGetLines()
    line_code = lines[0].get("line_code") or lines[0].get("LineCode")
    routes = oasatelematics.webGetRoutes(line_code)
    route_code = routes[0].get("route_code") or routes[0].get("RouteCode")
    stops = oasatelematics.webGetStops(route_code)
    stop_code = stops[0].get("StopCode") or stops[0].get("stop_code")
    result = oasatelematics.getStopArrivals(stop_code)
    assert isinstance(result, list)


def test_getClosestStops():
    # Coordinates near central Athens
    result = oasatelematics.getClosestStops("23.7275", "37.9838")
    assert isinstance(result, list)
    assert len(result) > 0


def test_getDailySchedule():
    lines = oasatelematics.webGetLines()
    line_code = lines[0].get("line_code") or lines[0].get("LineCode")
    result = oasatelematics.getDailySchedule(line_code)
    # This endpoint returns a dict with 'come' and 'go' keys, not a list
    assert isinstance(result, dict)
    assert "come" in result
    assert "go" in result


def test_api_uses_https():
    """Verify the endpoint is HTTPS (issue #2)."""
    assert oasatelematics.API_ENDPOINT.startswith("https://")
