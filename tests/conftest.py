import json

from pytest import fixture
from config import Config
from selenium import webdriver

data_path = 'test_data.json'

def load_test_data(path):
    with open(path) as data_file:
        return json.load(data_file)

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        help="Environment to run tests against"
    )

@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")

@fixture(scope='session')
def app_config(env):
    return Config(env)

@fixture(params=[webdriver.Chrome, webdriver.Firefox])
def browser(request):
    driver = request.param
    drvr = driver()
    yield drvr
    drvr.quit()


@fixture(params=load_test_data(data_path))
def tv_brand(request):
    data = request.param
    return data
