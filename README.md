# oasatelematics

[![PyPI version](https://img.shields.io/pypi/v/oasatelematics.svg)](https://pypi.org/project/oasatelematics/)
![PyPI Downloads](https://img.shields.io/pypi/dm/oasatelematics)
[![Python](https://img.shields.io/pypi/pyversions/oasatelematics.svg)](https://pypi.org/project/oasatelematics/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Python wrapper for the [OASA Telematics API](http://telematics.oasa.gr/) (Athens public transit).

## Installation

```bash
pip install oasatelematics
```

## Usage

```python
import oasatelematics

# Get all lines
lines = oasatelematics.webGetLines()

# Get routes for a line
routes = oasatelematics.webGetRoutes(line_code)

# Get real-time arrivals at a stop
arrivals = oasatelematics.getStopArrivals(stop_code)

# Get closest stops to coordinates
stops = oasatelematics.getClosestStops(longitude, latitude)

# Get bus location on a route
buses = oasatelematics.getBusLocation(route_code)
```

## Available Functions

| Function | Parameters | Description |
|---|---|---|
| `webGetLines()` | — | Get all lines |
| `webGetLinesWithMLInfo()` | — | Get lines with master line info |
| `webGetRoutes(linecode)` | line code | Get routes for a line |
| `webRouteDetails(routecode)` | route code | Get route details |
| `webGetStops(routecode)` | route code | Get stops for a route |
| `webRoutesForStop(stopcode)` | stop code | Get routes serving a stop |
| `webGetRoutesDetailsAndStops(routecode)` | route code | Get route details and stops |
| `getStopArrivals(stopcode)` | stop code | Get real-time arrivals at a stop |
| `getBusLocation(routecode)` | route code | Get bus locations on a route |
| `getScheduleDaysMasterline(linecode)` | line code | Get schedule days for a master line |
| `getLinesAndRoutesForMl(mlcode)` | master line code | Get lines and routes for a master line |
| `getRoutesForLine(linecode)` | line code | Get routes for a line |
| `getMLName(mlcode)` | master line code | Get master line name |
| `getLineName(linecode)` | line code | Get line name |
| `getRouteName(routecode)` | route code | Get route name |
| `getStopNameAndXY(stopcode)` | stop code | Get stop name and coordinates |
| `getSchedLines(mlcode, linecode, sdc_code)` | master line, line, schedule day code | Get schedule lines |
| `getClosestStops(lon, lat)` | longitude, latitude | Get closest stops to coordinates |
| `getDailySchedule(linecode)` | line code | Get daily schedule |

## Development

```bash
pip install -e ".[dev]"         # install with dev dependencies
pytest -v                        # run unit tests (mocked)
pytest -m integration -v        # run integration tests (hits real API)
```

## License

[GPL-3.0](LICENSE.txt)
