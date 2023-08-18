import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from seleniumwire import webdriver as wirewebdriver
import pandas, time



chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location =r"C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_options.add_argument("--user-data-dir=C:/Users/91932/AppData/Local/Google/Chrome/User Data/Profile 1")

chrome_options.add_argument("--disable-blink-features=AutomationControlled")


cd_path = "C:/chrome driver/"

os.environ["PATH"] += os.pathsep + cd_path

# def modify_recaptcha_response(request):
#     if "google.com/recaptcha/api2/payload" in request.path:
#         request.body = request.body.replace(b"false", b"true")
#     return request




driver = wirewebdriver.Chrome(options=chrome_options)
# driver.request_interceptor = modify_recaptcha_response


driver.get("https://seller.jiomart.com/cat/catalog#!/manage_manufacturers")


# FOR LOGIN AND CAPTCHA BYIPASS

username = driver.find_element(By.ID, 'user_user_id')
password = driver.find_element(By.ID, 'user_password')
username.send_keys('ayurprevenciaclinic@gmail.com')
password.send_keys('Jio@1234')
th_elements = driver.find_elements(By.TAG_NAME, "th")

# Iterate over the <th> elements and print their text content
for th in th_elements:
    print(th.text)

input("Please solve the CAPTCHA manually")
recaptcha_checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "g-recaptcha")))
recaptcha_checkbox.click()
print("captcha done")

login_button = driver.find_element(By.XPATH, '//*[@id="new_user"]/div[5]/input')
login_button.click()



# CREATING TABLE FOR STORAGE
df = pandas.DataFrame(columns=["S.No", "Name", "code", "address","email", "mobile","website", "actions" ])
file_path = 'data.csv'
df.to_csv(file_path, index=False)
time.sleep(1)

# SKIPING 10 PAGES
pagenum = driver.find_element(By.XPATH, '//*[@id="tabs"]/div/div/div[1]/manufacturer-list/div[2]/div/nav/ul/li[13]/a')
print(pagenum.text)

for _ in range(10):

    next_button = driver.find_element(By.XPATH,
                                      '//*[@id="tabs"]/div/div/div[1]/manufacturer-list/div[2]/div/nav/ul/li[14]')
    next_button.click()
    time.sleep(2)


# SAVING DATA TILL THE LAST PAGE
while True:

    # print(i)
    # creating data dataframe
    df = pandas.DataFrame(columns=["S.No", "Name", "code", "address", "email", "mobile", "website", "actions"])
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tabs"]/div/div/div[1]/manufacturer-list/div[2]/div/table/tbody')))

    # new_page = pandas.DataFrame(columns=["S.No", "Name", "code", "address", "email", "mobile", "website", "actions"])
    table = driver.find_element(By.XPATH, '//*[@id="tabs"]/div/div/div[1]/manufacturer-list/div[2]/div/table/tbody')

    # Find all rows in the table
    rows = table.find_elements(By.TAG_NAME, "tr")

    # Iterate over the rows and retrieve cell data

    for row in rows:
        # Find all cells in the current row
        cells = row.find_elements(By.TAG_NAME, "td")
        values = []
        # Extract data from each cell
        for cell in cells:
            values.append(cell.text)

        df.loc[len(df)] = values

    # save file
    df.to_csv(file_path, mode='a', header=False, index=False)


    # Add a separator between rows
    # '//*[@id="tabs"]/div/div/div[1]/manufacturer-list/div[2]/div/nav/ul/li[14]'
    # '//*[@id="tabs"]/div/div/div[1]/manufacturer-list/div[2]/div/nav/ul/li[14]/a'
    # '//*[@id="tabs"]/div/div/div[1]/manufacturer-list/div[2]/div/nav/ul/li[16]/a'
    # '//*[@id="tabs"]/div/div/div[1]/manufacturer-list/div[2]/div/nav/ul/li[16]'
    #
    # '//*[@id="tabs"]/div/div/div[1]/manufacturer-list/div[2]/div/nav/ul/li[14]/a'
    next_button = driver.find_element(By.XPATH, '//*[@id="tabs"]/div/div/div[1]/manufacturer-list/div[2]/div/nav/ul/li[16]')
    next_button.click()





