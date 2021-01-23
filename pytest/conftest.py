import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--log", action="store", default="log.txt", help="Logging"
    )


@pytest.fixture
def log_file(request):
    return request.config.getoption("--log")
