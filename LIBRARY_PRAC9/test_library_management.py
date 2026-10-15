from pathlib import Path
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

APP_URL = (Path(__file__).parent / 'index.html').as_uri()
@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(APP_URL)
    yield browser
    browser.quit()

def login(driver, user='admin', password='admin123'):
    driver.find_element(By.ID,'username').send_keys(user)
    driver.find_element(By.ID,'password').send_keys(password)
    driver.find_element(By.ID,'login-button').click()

def test_homepage_loads(driver):
    assert 'Library Management System' in driver.title

def test_invalid_login(driver):
    login(driver,'wrong','wrong')
    assert 'Invalid' in driver.find_element(By.ID,'login-error').text

def test_valid_login(driver):
    login(driver)
    assert driver.find_element(By.ID,'dashboard').is_displayed()

def test_add_search_delete_book(driver):
    login(driver)
    driver.find_element(By.ID,'book-title').send_keys('Python Basics')
    driver.find_element(By.ID,'book-id').send_keys('B101')
    driver.find_element(By.ID,'add-book-button').click()
    driver.find_element(By.ID,'search-book').send_keys('Python')
    assert 'Python Basics' in driver.find_element(By.ID,'book-list').text
    driver.find_element(By.XPATH,"//button[text()='Delete']").click()
    assert driver.find_element(By.ID,'book-list').text == '' 
