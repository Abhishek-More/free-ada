from flask import Flask, send_file
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from random_word import RandomWords
import random
import time
from bs4 import BeautifulSoup


def loadDriver():
  opts = webdriver.FirefoxOptions()
  return webdriver.Firefox(options=opts)


  chrome_options = webdriver.ChromeOptions()
  chrome_options.binary_location = os.environ.get("CHROME_BINARY_PATH")
  chrome_options.add_argument("--headless")
  chrome_options.add_argument("--disable-dev-shm-usage")
  chrome_options.add_argument("--no-sandbox")
  driver = webdriver.Chrome(executable_path=os.environ.get("CHROME_DRIVER_PATH"), chrome_options=chrome_options)
  return driver

def getNewAccount():
  
  r = RandomWords()

  email = "th" + r.get_random_word() + "@gmail.com"
  randomNum = random.randint(1001234,9999999)
  

  #input text into browser (using selenium :( ) and create new account
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
  elem.send_keys('614' + str(randomNum))

  elem = browser.find_element(By.ID, 'password')
  elem.send_keys('newpass1234')

  elem = browser.find_element(By.ID, 'confirm_password')
  elem.send_keys('newpass1234')

  elem = browser.find_element(By.ID, 'terms')
  elem.click()

  elem = browser.find_element(By.ID, 'reward_submission')
  elem.click()
  
  try:
    elem = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "text-barcode"))
    )

    soup = BeautifulSoup(browser.page_source, 'lxml')
    barcode = str(soup.find(class_="text-barcode"))
    barcode = barcode.split("<script")[0] + "</div>"
    time.sleep(1)
    print("done")
    browser.quit()
    return barcode
  except:
    browser.quit()
    return "<h1>ERROR...Try again later</h1>"


  #start parsing

app = Flask(__name__)

@app.route("/")
def index():
  #send_file("thinterwhistled.png")
  barcode = getNewAccount()
  #return jsonify({"email": email}) 
  return barcode
