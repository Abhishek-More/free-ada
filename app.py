from selenium.webdriver.common.by import By
from selenium import webdriver
from seleniumrequests import Chrome
from seleniumrequests import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constants
from random_word import RandomWords
import random
import time




def loadDriver():
  #Comment this line out if you have chrome webdriver
  return Firefox() 

  return Chrome()

def getNewAccount(wait=False):
  
  r = RandomWords()
  email = "th" + r.get_random_word() + "@gmail.com"
  
  #Create random phone number
  randomNum = random.randint(1001234,9999999)
  
  #input text into browser using selenium and create new account
  #Browser MUST be mobile-sized since the discount only spawns on mobile
  #Whoever designed that needs to be fired
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
    #Wait until the barcode is seen.
    #If barcode isn't seen within 10 seconds, throw error. 
    elem = WebDriverWait(browser, 10).until(
      EC.presence_of_element_located((By.CLASS_NAME, "text-barcode"))
    )

    print("Email: ", email)
    print("Password: newpass1234")
    print("done")

    #yes, this is necessary
    browser.get("https://mypiada.com/order/restaurants/college-station/set")
    time.sleep(5)
    browser.get("https://mypiada.com/order/restaurants/college-station/set")

    #POST the order to checkout (i order the same thing everytime)
    if constants.order != None and constants.order != '':
      browser.request('POST', 'https://mypiada.com/products/', data=constants.order)
      print("Order request sent")
      browser.get("https://mypiada.com/order/checkout")
    

    if wait:
        while True:
            pass

  except:
    browser.quit()
    print("Error!")

if __name__ == "__main__":
    getNewAccount(wait=True)
    

