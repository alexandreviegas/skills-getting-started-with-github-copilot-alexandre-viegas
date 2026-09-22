from copy import deepcopy
import importlib

import pytest
from fastapi.testclient import TestClient


app_module = importlib.import_module("src.app")


@pytest.fixture
def client():
    with TestClient(app_module.app) as test_client:
        yield test_client


@pytest.fixture(autouse=True)
def reset_activities():
    original_activities = deepcopy(app_module.activities)
    try:
        yield
    finally:
        app_module.activities.clear()
        app_module.activities.update(original_activities)
