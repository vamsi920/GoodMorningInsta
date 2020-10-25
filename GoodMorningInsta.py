from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains as AC
import time 
import schedule
TimeOfMessage = "Enter time (24hr format)"
def send_Text():
    print("started")
    LoginIdText = "Input your insta email id "
    PasswordText = "Input your Insta password"
    TargetUser = ["user1", "user2"] ####### any number users
    TargetMessage = "Enter your message here"
    
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)
    # driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/")
    LoginId = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))
    )
    LoginId.send_keys(LoginIdText)
    Password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    Password.send_keys(PasswordText)
    Submit = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
    Submit.click()
    ######ignore saving passwords
    NotNowButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button'))
    )
    NotNowButton.click()

    ##### ignoring notification button 
    # time.sleep(2)
    # driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
    #### Search for target user 
    messageIcon = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a')
    messageIcon.click()
    for x in TargetUser:
        
        compose = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button'))
        )
        compose.click()

        time.sleep(1)
    
        targetUserName = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/input'))
        )
        targetUserName.send_keys(x)
        SelectTargetUser = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[2]/div[2]/div[1]/div/div[3]/button/span'))
        )
        SelectTargetUser.click()
        ClickNext = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/div/button")
        ClickNext.click()

        #####compose message and send
        time.sleep(1)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea'))
        ).send_keys(TargetMessage)

        SendMessage = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button'))
        )
        SendMessage.click()
        time.sleep(2)
    print("done")
    driver.quit()
schedule.every().day.at(TimeOfMessage).do(send_Text)

while True:
    schedule.run_pending()
    time.sleep(1)