import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
    yield driver
    driver.quit()
