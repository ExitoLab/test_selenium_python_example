import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def test_open_google():
    # Use WebDriver Manager to get the correct driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()
