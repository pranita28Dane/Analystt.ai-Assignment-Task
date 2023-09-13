# Automated Login Script using Selenium and Python

This Python script demonstrates how to automate the login process on a website using the Selenium WebDriver library. In this example, we navigate to a login page, enter the username and password, click the login button, and verify if the login was successful.

## Prerequisites

Before running this script, make sure you have the following dependencies installed:

- Python
- Selenium
- Chrome WebDriver


## Installing
1. Clone this repository to your local machine:  

```
git clone https://github.com/pranita28Dane/Analystt.ai-Assignment-Task.git

```

2. Navigate to the project directory:
  
``` 
cd Analystt.ai-Assignment-Task

```

3. Open the python_automate_login.py script in a text editor and update the following variables:

```
login_url: Set the URL of the login page.
username: Set your username.
password: Set your password.
Save your changes.

```

4.Run the script:

```
python python_automate_login.py

```

The script will automate the login process, wait for 5 seconds to check if the login is successful, and then print the result to the console.

## Explanation of the Automation Process
1. Import the necessary libraries, including time for  `waiting` and  `webdriver` from Selenium for browser automation.

2. Declare the URL of the login page and your login credentials (username and password).

3. Create a new instance of the Chrome WebDriver using  `webdriver.Chrome()`.

4. Navigate to the login page using  `driver.get(login_url)`.

5. Find the username input field on the page by its ID and enter your username.

6. Find the password input field on the page by its ID and enter your password.

7. Locate the login button by its ID and click it.

8. Wait for 5 seconds using  `time.sleep(5)` to allow the login process to complete.

9. Check if the user is logged in successfully by finding an element with the ID "logged-in". If found, print "Login successful"; otherwise, print "Login failed".

10. Finally, close the browser using  `driver.quit()`.

