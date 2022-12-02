from flask import Flask, send_file
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constants
import os
from random_word import RandomWords
import random
import time
from bs4 import BeautifulSoup



def loadDriver():
  #Comment this line out if you have chrome webdriver
  #return webdriver.Firefox()

  return webdriver.Chrome()

def getNewAccount(wait=False):
  
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
  elem.send_keys(constants.first_name)
  print("found first")
  time.sleep(0.5)

  elem = browser.find_element(By.ID, 'lname')
  elem.send_keys(constants.last_name)
  time.sleep(0.5)

  elem = browser.find_element(By.ID, 'email')
  elem.send_keys(email)
  time.sleep(0.5)

  elem = browser.find_element(By.ID, 'phone_number')
  elem.send_keys('614' + str(randomNum))
  time.sleep(0.5)

  elem = browser.find_element(By.ID, 'password')
  elem.send_keys(constants.password)
  time.sleep(0.5)

  elem = browser.find_element(By.ID, 'confirm_password')
  elem.send_keys(constants.password)
  time.sleep(0.5)

  elem = browser.find_element(By.ID, 'terms')
  elem.click()
  time.sleep(0.5)

  elem = browser.find_element(By.ID, 'reward_submission')
  elem.click()
  
  try:
    elem = WebDriverWait(browser, 10).until(
      EC.presence_of_element_located((By.CLASS_NAME, "text-barcode"))
    )

    soup = BeautifulSoup(browser.page_source, 'lxml')
    barcode = str(soup.find(class_="text-barcode"))
    barcode = barcode.split("<script")[0] + "</div>"

    print("Email: ", email)
    print("Password: newpass1234")
    print("done")

    if wait:
      time.sleep(100000)

    #browser.quit()
    return barcode, email
  except:
    browser.quit()
    return "<h1>ERROR...Try again later</h1>", "none"

if __name__ == "__main__":
    _, email = getNewAccount(wait=True)
    

app = Flask(__name__)

@app.route("/")
def index():
  #send_file("thinterwhistled.png")
  barcode, email = getNewAccount()
  #return jsonify({"email": email}) 
  return "<div>" + barcode + "<p>Email: " + email + "</p><p>Password: newpass1234</p></div>"




