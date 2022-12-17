# from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard
import write_dates as wd
import time
import csv

# Semi-automating the collection of Radar data: when storms occur over Chicago

# URL/Date setup
date_list = open('dates.txt', 'r')
DATES = date_list.readlines()
currentYear = 2018
currentDay = 183
datesToInclude = []
# DATE = f'{currentYear}' + DATES[currentDay]
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


# Navigate site
def navSite():
    RC_tag = driver.find_element(By.LINK_TEXT, 'RadarComposites')
    RC_tag.click()

    UM_tag = driver.find_element(By.LINK_TEXT, 'RadarComposites upper_missvly')
    UM_tag.click()


def btnControl():
    next_frame = driver.find_element(By.XPATH, '/html/body/map[1]/area[5]')
    prev_frame = driver.find_element(By.XPATH, '/html/body/map[1]/area[3]')
    continue_anim = driver.find_element(By.XPATH, '/html/body/map[1]/area[6]')
    fast_forward = driver.find_element(By.XPATH, '/html/body/map[1]/area[7]')
    if (keyboard.is_pressed('.') and not keyboard.is_pressed('shift')):
        next_frame.click()
        time.sleep(0.075)
                 
    if (keyboard.is_pressed(',')):
        prev_frame.click()
        time.sleep(0.075)

    if (keyboard.is_pressed('m')):
        continue_anim.click()

    if (keyboard.is_pressed('f')):
        fast_forward.click()

# Script
driver.get("https://www2.mmm.ucar.edu/imagearchive/dates/" + f'{currentYear}' + DATES[currentDay] + ".html")
navSite()

        
while True:
    if keyboard.is_pressed('n'):
        if currentDay == 0:
            currentDay = 364
            currentYear = currentYear - 1
        else:
            currentDay = currentDay - 1

        DATE = f'{currentYear}' + DATES[currentDay]
        driver.get("https://www2.mmm.ucar.edu/imagearchive/dates/" + DATE + ".html")
        navSite()


    if keyboard.is_pressed('c'):
        datesToInclude.append(wd.properDates[currentDay] + "/" + f'{currentYear}')
        time.sleep(0.5)

    if keyboard.is_pressed('s'):
        break

    if keyboard.is_pressed('p'):
        currentDay = currentDay + 1

    btnControl()


# CSV editing

with open('data.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['Start Date', 'Start Time'])
    for i in range(len(datesToInclude)):
        thewriter.writerow([datesToInclude[i], '0:00'])

# Close tab
driver.close()

