from flask import Flask,jsonify
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
from random_word import RandomWords
import time


def loadDriver():
  chrome_options = webdriver.ChromeOptions()
  chrome_options.binary_location = os.environ.get("CHROME_BINARY_PATH")
  chrome_options.add_argument("--headless")
  chrome_options.add_argument("--disable-dev-shm-usage")
  chrome_options.add_argument("--no-sandbox")
  driver = webdriver.Chrome(executable_path=os.environ.get("CHROME_DRIVER_PATH"), chrome_options=chrome_options)
  return driver

def getNewAccount():
  
  r = RandomWords()

  email = "tamuhack" + r.get_random_word() + "@gmail.com"

  browser = loadDriver()
  print("browser loaded")
  browser.set_window_size(600, 800)
  browser.get('https://mypiada.com/rewards')
  print("Page navigated")

  elem = browser.find_element(By.ID, 'fname')
  elem.send_keys('New')
  print("found first")

  elem = browser.find_element(By.ID, 'lname')
  elem.send_keys('Account')

  elem = browser.find_element(By.ID, 'email')
  elem.send_keys(email)

  elem = browser.find_element(By.ID, 'phone_number')
  elem.send_keys('6143456980')

  elem = browser.find_element(By.ID, 'password')
  elem.send_keys('newpass1234')

  elem = browser.find_element(By.ID, 'confirm_password')
  elem.send_keys('newpass1234')

  elem = browser.find_element(By.ID, 'terms')
  elem.click()

  elem = browser.find_element(By.ID, 'reward_submission')
  elem.click()
  time.sleep(5)
  
  browser.quit()
  print("DONE!")
  return email

app = Flask(__name__)

@app.route("/")
def index():
  email = getNewAccount()
  return jsonify({"email": email}) 

