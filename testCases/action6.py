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

    def test_case1(self, setup):
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

        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "embed-responsive-item"))
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='box-success']/div[1]/div/button"))).click()
        lists = self.driver.find_elements(By.XPATH, "//*[@id='box-success']/div[1]/div/div/ul/li/a")
        for list in lists:
            if list.text == "Hi":
                list.click()
                break
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='responseAssistantModal']/div[2]/div[2]/div[1]/button[2]"))).click()
        #shown the text "Copied"
        copi = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='responseAssistantModal']/div[2]/div[2]/div[1]/div[3]/p/strong")))
        assert copi.text == "Copied"
        #message one more thing ...
        one = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='responseAssistantModal']/div[2]/div[2]/div[1]/div[4]/h2")))
        assert one.text == "One more thing…"

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='responseAssistantModal']/div[2]/div[2]/div[1]/div[4]/div/a"))).click()
        after_window = self.driver.window_handles[1]
        self.driver.switch_to.window(after_window)
        self.driver.close()
        self.driver.switch_to.window(before_window)

        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "embed-responsive-item"))
        yes = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='r_mark_response']")))
        assert yes.text == "YES, I'VE SUBMITTED"

        no = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='responseAssistantModal']/div[2]/div[2]/div[2]/button[2]")))
        assert no.text == "NO, I HAD A PROBLEM"

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='r_mark_response']"))).click()

        modal = WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.XPATH, "//*[@class='modal-content']")))
        assert modal == True
        self.driver.close()
    def test_case2(self, setup):
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

        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "embed-responsive-item"))
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='box-success']/div[1]/div/button"))).click()
        lists = self.driver.find_elements(By.XPATH, "//*[@id='box-success']/div[1]/div/div/ul/li/a")
        for list in lists:
            if list.text == "Hi":
                list.click()
                break
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='responseAssistantModal']/div[2]/div[2]/div[1]/button[2]"))).click()

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='responseAssistantModal']/div[2]/div[2]/div[1]/div[4]/div/a"))).click()
        after_window = self.driver.window_handles[1]
        self.driver.switch_to.window(after_window)
        self.driver.close()
        self.driver.switch_to.window(before_window)

        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "embed-responsive-item"))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='responseAssistantModal']/div[2]/div[2]/div[2]/button[2]"))).click()

        #check text show
        edit = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='responseAssistantModal']/div[2]/div[2]/div[2]/div/button[1]")))
        assert edit.text == "EDIT/VIEW RESPONSE"
        launch = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='responseAssistantModal']/div[2]/div[2]/div[2]/div/a[1]")))
        assert launch.text == "LAUNCH TRIPADVISOR"
        login = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='responseAssistantModal']/div[2]/div[2]/div[2]/div/a[2]")))
        assert login.text == "Login Trouble?"
        cancel = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='responseAssistantModal']/div[2]/div[2]/div[2]/div/button[2]")))
        assert cancel.text == "CANCEL ALL"

        #check click edit and shown response section
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='responseAssistantModal']/div[2]/div[2]/div[2]/div/button[1]"))).click()

        response = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='box-success']/div[1]/label")))
        assert response.text == "Your response:"
        self.driver.close()
    def test_case2_3_4(self, setup):
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

        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "embed-responsive-item"))
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='box-success']/div[1]/div/button"))).click()
        lists = self.driver.find_elements(By.XPATH, "//*[@id='box-success']/div[1]/div/div/ul/li/a")
        for list in lists:
            if list.text == "Hi":
                list.click()
                break
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='responseAssistantModal']/div[2]/div[2]/div[1]/button[2]"))).click()

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='responseAssistantModal']/div[2]/div[2]/div[1]/div[4]/div/a"))).click()
        after_window = self.driver.window_handles[1]
        self.driver.switch_to.window(after_window)
        self.driver.close()
        self.driver.switch_to.window(before_window)

        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "embed-responsive-item"))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='responseAssistantModal']/div[2]/div[2]/div[2]/button[2]"))).click()

        #check verify launch
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='responseAssistantModal']/div[2]/div[2]/div[2]/div/a[1]"))).click()
        after_window = self.driver.window_handles[1]
        self.driver.switch_to.window(after_window)
        act_title = self.driver.title
        assert act_title == "Tripadvisor"

        self.driver.close()
        self.driver.switch_to.window(before_window)
        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "embed-responsive-item"))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='responseAssistantModal']/div[2]/div[2]/div[2]/div/a[2]"))).click()
        time.sleep(4)
        after_window = self.driver.window_handles[1]
        #check page login
        self.driver.switch_to.window(after_window)
        act_title = self.driver.title
        assert act_title == "Log in to Revinate"
        self.driver.close()
        self.driver.switch_to.window(before_window)
        #check close
        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "embed-responsive-item"))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='responseAssistantModal']/div[2]/div[2]/div[2]/div/button[2]"))).click()

        modal = WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.XPATH, "//*[@class='modal-content']")))
        assert modal == True

        self.driver.quit()



