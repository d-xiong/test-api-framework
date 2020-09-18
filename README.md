# test-api-framework

### Welcome to the QA Challenge v20200918!
The goal is to teach you a few important things, including:
1. Using git
1. Set up your python environment
1. Setting up a local test api
1. Making some POSTMAN calls

### Grab this repo.
1. Navigate to, and use git to grab the code from this repo:
https://github.com/d-xiong/test-api-framework
1. Hint:
`git clone`

### Set up your python environment
1. Verify you have python3 installed, by typing this into your terminal:
`python3 --version`
1. If you do not, then this site should help you get it installed properly:
https://docs.python-guide.org/starting/install3/osx/

### Setting up your local test api
1. First, you need to ensure you have the correct python modules installed
1. Run the following command, to install the module:
`pip3 install flask`
1. After installing the module, you will need to start the application.
1. Use this command to run the application:
`python3 {{path to the runner.py file}}`
    1. So, example, it might be something like `python3 \Users\myuser\code\test-api-framework\python\runner.py`
1. The local test api should now be running. Do not close this terminal window until your done with this tutorial, 
since the terminal window IS acting as the local test api.
1. The Base URL for the environment will be displayed onscreen in the terminal window.

### Making some POSTMAN calls
1. Open POSTMAN
1. Make a GET call to test endpoint: `/test`
1. Then, make a POST call to the test endpoint with some JSON data: `/test`
1. This should add your JSON data to stored the data.
1. Make another GET call to the test endpoint: `/test`
1. Verify the data you added now appears in the response data.
1. Take a screenshot of this, and post it into the #qa-internal chat.