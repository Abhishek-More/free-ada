from flask import Flask
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import os


def  loadDriver():
	options = webdriver.FirefoxOptions()
	options.log.level = "trace"
	options.add_argument("-remote-debugging-port=9224")
	options.add_argument("-headless")
	options.add_argument("-disable-gpu")
	options.add_argument("-no-sandbox")
	binary = FirefoxBinary(os.environ.get('FIREFOX_BIN'))
	firefox_driver = webdriver.Firefox(
		firefox_binary=binary,
		executable_path=os.environ.get('GECKODRIVER_PATH'),
		options=options)

	return firefox_driver

def getNewAccount():
  browser = loadDriver()
  browser.set_window_size(600, 800)
  browser.get('https://mypiada.com/rewards')

  elem = browser.find_element(By.ID, 'fname')
  elem.send_keys('New')

  elem = browser.find_element(By.ID, 'lname')
  elem.send_keys('Account')

  elem = browser.find_element(By.ID, 'email')
  elem.send_keys('emailrandomtestingman@gmail.com')

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

app = Flask(__name__)

@app.route("/")
def index():
  #getNewAccount()
  return "Hello World!"

