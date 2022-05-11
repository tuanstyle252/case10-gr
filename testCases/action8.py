from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.loginPage import Loginpage
import time
from utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By


class Testaction:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassWord()

    def test_case3_2_9(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        before_window = self.driver.window_handles[0]
        self.driver.maximize_window()
        #login user
        self.lp = Loginpage(self.driver)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lock']/div/div/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div/div[1]/div/a[1]"))).click()
        time.sleep(2)
        self.lp.setUsername(self.username)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='identifierNext']/div/button/span"))).click()
        time.sleep(2)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        #process group
        time.sleep(2)
        click_ = self.driver.find_element(By.XPATH, "//*[@id='gfb-property-selector']/a")
        ActionChains(self.driver).move_to_element(click_).perform()
        time.sleep(3)
        gjp = self.driver.find_elements(By.XPATH, "//*[@class='sc-hKMtZM dpbvJz dropdown-menu']/a")
        for i in gjp:
            if i.text == "GJP Hotels & Resorts":
                i.click()
                break
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='nav-tabs-tickets']"))).click()

        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='ticketNumber']").send_keys("14318")
        time.sleep(4)
        menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[7]")
        respond = self.driver.find_element(By.XPATH,"//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[2]/button")
        ActionChains(self.driver).move_to_element(menu).click(respond).perform()

        #click x check close modal
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div[1]/button"))).click()
        modal = WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.XPATH, "//*[@class='modal-content']")))
        assert modal == True

        time.sleep(4)
        menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[7]")
        respond = self.driver.find_element(By.XPATH,"//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[2]/button")
        ActionChains(self.driver).move_to_element(menu).click(respond).perform()
        # click cancel check close modal
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div[3]/button"))).click()
        modal = WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.XPATH, "//*[@class='modal-content']")))
        assert modal == True

        self.driver.quit()