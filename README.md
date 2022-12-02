## Installation + Config

* Install Python Libraries with \
`pip3 install -r requirements.txt`

* Install a webdriver for your browser and add it to PATH\
Example: https://github.com/mozilla/geckodriver/releases

* Change contants.py as desired

## How to run 

There are two ways to run this program: you can choose to run the script or setup a flask server. Running the script alone creates a new account and leaves the browser window running, allowing you to submit an order. Setting up a flask server allows for multiple people to get accounts (given that they know your local IP). All they need to do is enter the following address into their browser:

`[YOUR_IP]:[PORT #(probably 5000)]`


####Commands
Initialize the flask server\
`flask run`

OR

Run the script\
`python3 app.py`
