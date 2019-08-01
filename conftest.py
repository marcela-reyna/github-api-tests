import pytest


def pytest_addoption(parser):
    parser.addoption("--base_url", action="store", help="base url",default="https://api.github.com")


@pytest.fixture(scope="session")
def context(request):
    return Context(request)


class Context(object):
    def __init__(self, request):
        self.base_url = request.config.getoption("--base_url")
