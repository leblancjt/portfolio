## Author: John LeBlanc™
## Date: 02/20/2020

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from progress.bar import IncrementalBar

driver = webdriver.Chrome(ChromeDriverManager().install()) # creating the webdriver using chromedriver
driver.get("https://www.tripadvisor.com/Attraction_Review-g48975-d2171255-Reviews-Foggy_Mountain_Gem_Mine-Boone_North_Carolina.html") # driver gets the TripAdvisor page.

def circles(rating): # function to create rating 'circles', takes a float input for rating.
    circles = '' # initializes empty string variable 'circles'.
    if (float(rating) % 1 == 0): # When rating is an integer.
        if (int(rating) < 5): # If rating isn't 5 stars.
            for i in range(int(rating)): # Iterate n times, n = rating.
                circles += '◉ ' # Adds full circle symbol to string variable 'circles' each iteration.
            for i in range(5 - int(rating)): # Iterate 5 - n times.
                circles += '◯ ' # Adds empty circle symbol to string variable 'circles' each iteration.
        else: # If rating is 5 stars.
            circles = '◉ ◉ ◉ ◉ ◉ ' # Sets string variable 'circles' to 5 full circle symbols.
            
    if (float(rating) % 1 != 0): # When rating is a float.
        if (int(rating) < 4): # If rating is less than 4.
            for i in range(int(rating)): # Iterate n times, n = rating.
                circles += '◉ ' # Adds full circle symbol to string variable 'circles' each iteration.
            circles += '◐ ' # Adds a half circle symbol to string variable 'circles'.
            for i in range(4 - int(rating)): # Iterate 4 - n times.
                circles += '◯ ' # Adds empty circle symbol to string variable 'circles' each iteration.
        else: # If rating is greater than 4.
            for i in range(int(rating)): # Iterate n times, n = rating.
                circles += '◉ ' # Adds full circle symbol to string variable 'circles' each iteration.
            circles += '◐ ' # Adds a half circle symbol to string variable 'circles'.
    return circles # returns string variable 'circles'.

# Gets title element, converts it to a string and stores it to variable 'title'.
title = driver.find_element(By.XPATH, '//h1[@id="HEADING"]').text
# Gets address element, converts it to a string and stores it to variable 'address'.
address = driver.find_element(By.XPATH, '//span[@class="street-address"]').text
# Gets City, State and Zip-Code, converts it to a string and stores it to variable 'locality'.
locality = driver.find_element(By.XPATH, '//span[@class="locality"]').text
# Concatenates variable 'address' and variable 'locality', then stores it to variable 'address'.
address += ', ' + locality
driver.find_element(By.XPATH, '//*[text() = "Website"]').click() # Finds website link and clicks it.
driver.switch_to.window(driver.window_handles[-1]) # Switches driver to the second window.
website = str(driver.current_url) # Gets second window's URL and stores it as a string to variable 'website'.
driver.switch_to.window(driver.window_handles[0]) # Switches driver back to original window.
# Gets phone number element, converts it to a string and stores it to variable 'phone'.
phone = driver.find_element(By.XPATH, '//div[@class="detail_section phone"]').text
# Finds 'See All Hours' element and clicks it.
driver.find_element(By.XPATH, '//div[@class="public-location-hours-LocationHours__hoursLink--2wAQh"]').click() # 
# Gets hours element, converts it to a string and stores it to variable 'hours'.
hours = driver.find_element(By.XPATH, '//div[@class="all-open-hours"]').text
# Gets total # of reviews element, converts it to a string and stores it to variable 'numberOfTotalReviews'.
numberOfTotalReviews = int(driver.find_element(By.XPATH, '//a[@class="seeAllReviews taLnk"]').text[9:12])
# Gets # of reviews by rating element, and stores it to variable 'numberOfReviewsByRating'.
numberOfReviewsByRating = driver.find_elements(By.XPATH, '//span[@class="location-review-review-list-parts-ReviewRatingFilter__row_num--3cSP7"]')
# Gets rating element, converts it to a string and stores it to variable 'rating'.
rating = float(driver.find_element(By.XPATH, '//span[@class="overallRating"]').text)
total = int(numberOfTotalReviews) # Converts variable 'numberOfTotalReviews' to integer and stores it in 'total'.
# Converts 'numberOfReviewsByRating[0].text' to integer and stores it in 'excellent'.
excellent = int(numberOfReviewsByRating[0].text)
# Converts 'numberOfReviewsByRating[1].text' to integer and stores it in 'verygood'.
verygood = int(numberOfReviewsByRating[1].text)
# Converts 'numberOfReviewsByRating[2].text' to integer and stores it in 'average'.
average = int(numberOfReviewsByRating[2].text)
# Converts 'numberOfReviewsByRating[3].text' to integer and stores it in 'poor'.
poor = int(numberOfReviewsByRating[3].text)
# Converts 'numberOfReviewsByRating[4].text' to integer and stores it in 'terrible'.
terrible = int(numberOfReviewsByRating[4].text)

print('Title: ' + title) # Prints 'title' variable.
print('Address: ' + address) # Prints 'address' variable.
print('Website: ' + website) # Prints 'website' variable.
print('Phone #: ' + phone) # Prints 'phone' variable.
print('Hours of Operation: ') # Prints heading for hours.
# Prints variable hours.
print(hours[:9] + ': ' + hours[10:28])
print(hours[29:32] + ':       ' + hours[33:51])
print(hours[52:55] + ':       ' + hours[56:74])
print(hours[75:84] + ': ' + hours[85:103])
print('Review Overview: ') # Prints heading for Reviews.
# Calls 'circles' function and prints what it returns and the variable 'rating'.
print(circles(rating) + ': ' + str(rating) + ' Rating')  

excellentBar = IncrementalBar('Excellent: ', max = total) # Creates an IncrementalBar item.
for i in range(excellent): # Iterates n times, n = number of excellent reviews.
    excellentBar.next() # Updates bar length.
print(' : ' + str(int(round(excellent / total, 2) * 100)) + '%') # Prints number of reviews and percentage.

verygoodBar = IncrementalBar('Very Good: ', max = total) # Creates an IncrementalBar item.
for i in range(verygood): # Iterates n times, n = number of very good reviews.
    verygoodBar.next() # Updates bar length.
print(' : ' + str(int(round(verygood / total, 2) * 100)) + '%') # Prints number of reviews and percentage.

averageBar = IncrementalBar('Average:   ', max = total) # Creates an IncrementalBar item.
for i in range(average): # Iterates n times, n = number of average reviews.
    averageBar.next() # Updates bar length.
print(' : ' + str(int(round(average / total, 2) * 100)) + '%') # Prints number of reviews and percentage.

poorBar = IncrementalBar('Poor:      ', max = total) # Creates an IncrementalBar item.
for i in range(poor): # Iterates n times, n = number of poor reviews.
    poorBar.next() # Updates bar length.
print(' : ' + str(int(round(poor / total, 2) * 100)) + '%') # Prints number of reviews and percentage.

terribleBar = IncrementalBar('Terrible:  ', max = total) # Creates an IncrementalBar item.
for i in range(terrible): # Iterates n times, n = number of terrible reviews.
    terribleBar.next() # Updates bar length.
print(' : ' + str(int(round(terrible / total, 2) * 100)) + '%') # Prints number of reviews and percentage.