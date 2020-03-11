## Author: John LeBlanc™
## Date: 02/20/2020
from math import sqrt
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import matplotlib.pyplot as plt

driver = webdriver.Chrome(ChromeDriverManager().install()) # creating the webdriver using chromedriver
driver.implicitly_wait(10)
driver.get("https://stats.nba.com/events/?flag=3&CFID=33&CFPARAMS=2019-20&PlayerID=1628369&ContextMeasure=FGA&Season=2019-20&section=player&sct=hex")
plotlink = driver.find_element_by_css_selector('a.stats-shotchart__link')
plotlink.click()

misses = driver.find_elements_by_css_selector('g.shotplot__shot.shotplot__miss')
makes = driver.find_elements_by_css_selector('g.shotplot__shot.shotplot__make')

missesLen = len(misses)
makesLen = len(makes)

missesX = []
missesY = []

makesX = []
makesY = []

for mi in range(missesLen):
    missesY.append(int(misses[mi].get_attribute('data-y')) / 10)
    missesX.append(int(misses[mi].get_attribute('data-x')) / 10)
    
for ma in range(makesLen):
    makesY.append(int(makes[ma].get_attribute('data-y')) / 10)
    makesX.append(int(makes[ma].get_attribute('data-x')) / 10)

missesSum = 0
makesSum = 0

for i in range(missesLen):
    missesSum += sqrt(missesX[i] ** 2 + missesY[i] ** 2)
for i in range(makesLen):
    makesSum += sqrt(makesX[i] ** 2 + makesY[i] ** 2)

AvgDisMiss = round(missesSum / missesLen, 1)
AvgDisMake = round(makesSum / makesSum, 1)

print('The average distance for made shots is ' + str(AvgDisMake) + 'ft')
print('The average distance for misses shots is ' + str(AvgDisMiss) + 'ft')

fig, ax = plt.subplots()
for i in range(missesLen):
    x = missesX[i]
    y = missesY[i]
    scale = 25
    ax.scatter(x, y, c = 'red', s = scale, label = 'Miss' if i == 0 else "", alpha = 0.4, marker = 'x')

for i in range(makesLen):
    x = makesX[i]
    y = makesY[i]
    scale = 25
    ax.scatter(x, y, c = 'green', s = scale, label = 'Make' if i == 0 else "", alpha = 0.4)
ax.legend()
plt.show()
