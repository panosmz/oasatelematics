# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`oasatelematics` is a Python wrapper for the OASA Telematics API (Greek public transit system). Published on PyPI as `oasatelematics` (v0.4). Licensed under GPL-3.0. Requires Python >= 3.9.

## Architecture

Single-module package. All API wrapper functions live in `oasatelematics/__init__.py`:

- `API_ENDPOINT` — module-level constant: `https://telematics.oasa.gr/api/`
- `telematics_request(query)` — core HTTP function that POSTs to the API endpoint and returns parsed JSON (or `[]` on error). The API returns HTTP 200 even for null responses, so the wrapper manually sets 404 in that case.
- All other functions (e.g., `webGetLines`, `getStopArrivals`, `getBusLocation`) are thin wrappers that build a query string and call `telematics_request`.

Dependency: `requests`.

## Home Assistant Compatibility

This package is used by the [Home Assistant oasa_telematics integration](https://github.com/home-assistant/core/tree/dev/homeassistant/components/oasa_telematics). The integration calls `getRouteName`, `getStopNameAndXY`, and `getStopArrivals`. All function names, signatures, and return types must remain stable.

## Build & Test

```bash
pip install -e ".[dev]"    # install in editable mode with pytest
pytest -v                   # run 27 unit tests (mocked, offline)
pytest -m integration -v   # run 9 integration tests (hits real API)
python -m build             # build sdist + wheel
twine upload dist/*         # publish to PyPI
```

Packaging uses `pyproject.toml` with setuptools backend. Version is set in both `pyproject.toml` and `oasatelematics/__init__.__version__`.

## Tests

- `tests/test_telematics.py` — unit tests using `unittest.mock.patch("oasatelematics.requests.post")`, no network calls
- `tests/test_integration.py` — integration tests hitting the real OASA API, marked with `@pytest.mark.integration`, skipped by default
- Note: `getDailySchedule` returns a dict (`{come: [], go: []}`) unlike other endpoints which return lists

## Conventions

- Function names mirror the OASA Telematics API action names exactly (e.g., `webGetRoutes`, `getStopArrivals`).
