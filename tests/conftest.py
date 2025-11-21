import pytest
from appium import webdriver
from appium.options.common import AppiumOptions




@pytest.fixture()
def driver():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "12",
        "deviceName": "Pixel_8_API_31",
        "automationName": "UiAutomator2",
    }

    options = AppiumOptions()
    options.load_capabilities(desired_caps)

    driver = webdriver.Remote(
        command_executor="http://localhost:4723",
        options=options
    )

    yield driver

    driver.quit()