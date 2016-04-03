#TODO: Import the module that will allow you to use Selenium
from selenium import webdriver
#TODO: Import the module that will allow you to use the up, down, left, and right keys on your keyboard
from selenium.webdriver.common.keys import Keys

def play2048( times ):
    #TODO: write code in this function that:
    # 1. opens a game of 2048 from the URL: https://gabrielecirulli.github.io/2048/
    # 2. uses the parameter 'times' to determine how many times your code will try to play the game
    # 3. for each 'time', press these keys in this order: UP, RIGHT, DOWN, LEFT
    # 4. print the final score after all tries to the screen 

    browser = webdriver.Firefox() 
    browser.open('https://gabrielecirulli.github.io/2048/') 

    htmltagElem = browser.find_element_by_tag_name('html') 
    scoreElem = browser.find_element_by_class_name('score-container') 

    moves = 0 

    while moves < times: 
        htmltagElem.send_keys(Keys.UP)
        htmltagElem.send_keys(Keys.RIGHT) 
        htmltagElem.send_keys(Keys.DOWN) 
        htmltagElem.send_keys(Keys.LEFT) 

        moves += 1
 
    print('Your final score is: ' +scoreElem.text) 
