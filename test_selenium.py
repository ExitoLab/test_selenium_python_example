import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_google_title():
    # Set up ChromeDriver
    chrome_service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode (no GUI)
    driver = webdriver.Chrome(service=chrome_service, options=options)
    
    # Navigate to Google
    driver.get("https://www.google.com")
    
    # Assert that the page title contains "Google"
    assert "Google" in driver.title
    
    # Find the search box element and verify it exists
    search_box = driver.find_element(By.NAME, "q")
    assert search_box is not None
    
    # Close the browser
    driver.quit()

# Run the test
if __name__ == "__main__":
    test_google_title()
