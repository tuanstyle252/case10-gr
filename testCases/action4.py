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

    def test_action3_1_1(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
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
        self.driver.find_element(By.XPATH, "//*[@id='ticketNumber']").send_keys("14601")
        time.sleep(4)
        menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[7]")
        respond = self.driver.find_element(By.XPATH,"//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[2]/button")
        ActionChains(self.driver).move_to_element(menu).click(respond).perform()
        #header is show
        title = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr/td[4]")))
        mess = f'Respond to Survey of {title.text}'

        header = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[1]/div")))
        assert header.text == mess

        self.driver.close()

    def test_action3_1_2(self, setup):
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
        self.driver.find_element(By.XPATH, "//*[@id='ticketNumber']").send_keys("14601")
        time.sleep(4)
        menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[7]")
        respond = self.driver.find_element(By.XPATH,"//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[2]/button")
        ActionChains(self.driver).move_to_element(menu).click(respond).perform()

        #switch survey modal page
        time.sleep(3)
        self.driver.execute_script("window.open('https://guest-feedback-test.revinate.com/review/66347/74433986')")
        after_window = self.driver.window_handles[1]
        self.driver.switch_to.window(after_window)
        #check txt page
        posted = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='reviewList']/div/div/div/div/div/div[1]/div/ul/li[1]")))
        assert posted.text == "Posted: May 10, 2022"

        trip_tpe = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='reviewList']/div/div/div/div/div/div[1]/div/ul/li[2]")))
        assert trip_tpe.text == "Trip type: friends"

        survey = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='reviewList']/div/div/div/div/div/div[1]/div/ul/li[3]")))
        assert survey.text == "Survey: Test Survey Updated"

        survey_type = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='reviewList']/div/div/div/div/div/div[1]/div/ul/li[4]")))
        assert survey_type.text == "Survey Type: Post-Stay"

        rivew_id = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='reviewList']/div/div/div/div/div/div[1]/div/ul/li[5]")))
        assert rivew_id.text == "Review ID: 74433986"

        header_title = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='reviewList']/div/div/div/div/div/div[2]/div[1]/h2")))
        assert header_title.text == "Test Survey Updated"

        author = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='reviewList']/div/div/div/div/div/div[2]/div[1]/span")))
        assert author.text == "Ian Poulter, Cologne, North Rhine-Wesphalia, Germany (5/10/22)"

        self.driver.switch_to.window(before_window)
        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "embed-responsive-item"))
        # check txt modal
        posted = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='responseAssistantModal']/div[2]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div/ul/li[1]")))
        assert posted.text == "Posted: May 10, 2022"

        trip_tpe = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='responseAssistantModal']/div[2]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div/ul/li[2]")))
        assert trip_tpe.text == "Trip type: friends"

        survey = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='responseAssistantModal']/div[2]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div/ul/li[3]")))
        assert survey.text == "Survey: Test Survey Updated"

        survey_type = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='responseAssistantModal']/div[2]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div/ul/li[4]")))
        assert survey_type.text == "Survey Type: Post-Stay"

        rivew_id = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='responseAssistantModal']/div[2]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div/ul/li[5]")))
        assert rivew_id.text == "Review ID: 74433986"

        header_title = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='responseAssistantModal']/div[2]/div[1]/div/div/div/div/div/div/div[1]/div/div[2]/div[1]/h2")))
        assert header_title.text == "Test Survey Updated"

        author = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='responseAssistantModal']/div[2]/div[1]/div/div/div/div/div/div/div[1]/div/div[2]/div[1]/span")))
        assert author.text == "Ian Poulter, Cologne, North Rhine-Wesphalia, Germany (5/10/22)"

        self.driver.quit()

    def test_action3_1_3(self, setup):
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
        self.driver.find_element(By.XPATH, "//*[@id='ticketNumber']").send_keys("14601")
        time.sleep(4)
        menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[7]")
        respond = self.driver.find_element(By.XPATH,"//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[2]/button")
        ActionChains(self.driver).move_to_element(menu).click(respond).perform()

        time.sleep(1)
        self.driver.execute_script("window.open('https://guest-feedback-test.revinate.com/all-surveys/66347/66347/10002/all/no_tickets/[%22all%22]/[%22all%22]/all/all/all/all/all?older_than_filter=none&page=1')")
        after_window = self.driver.window_handles[1]
        self.driver.switch_to.window(after_window)

        try:
            while True:
                list = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@class='container-fluid mg-t-md']/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/a[1]")))
                for i in list:
                    if i.text == "Create a Ticket":
                        self.driver.execute_script("argument[0].scrollIntoView(); ", i)
                        i.click()
                        break
                    time.sleep(1)
            else:
                self.driver.find_element(By.XPATH,"/html/body/div[1]/main/div/div/div[2]/div[2]/nav/ul/li[2]/a").click()







