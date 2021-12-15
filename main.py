from selenium.webdriver.common.by import By
from selenium import webdriver


count = 800                 # last 3 digit of your seat number to automate
seat = ("Seat_number")      # seat number except last 3 digit
mother = "mother_name"      # mother's name

# url of your result site
urls = ('http://results.unipune.ac.in/BBABCA.aspx?Course_Code=70414&Course_Name=BE+2015+PERCENTAGE+PATTERN+EXAM+PERIOD+APR-MAY+2020')

while count < 803:
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome("C:/Program Files/Google/Chrome/Application/chromedriver.exe")
    driver.get(urls)

# add website's element placeholder name or id and their value
    countStr = str(count)
    ele1 = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtSeatno")
    ele1.send_keys(seat + countStr)

# add website's element placeholder name or id and their value
    ele2 = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtMother")
    ele2.send_keys(mother)

# add website's element placeholder name or id
    submit = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnSubmit")
    submit.click()

# If there is any alert or warning for Invalid details
    alerted = driver.switch_to.alert
    alertedText = alerted.text

# If the details are Invalid the window will close automatically
# And If there is any Valid details It'll will print the correct seat number
    if len(alertedText) > 0:
        alerted.accept()
        driver.close()
    else:
        print(seat + countStr)

    count = count + 1