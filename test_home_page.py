
import conftest
from util import *
from utilities.BaseClass import BaseClass
import pytest

# #-------------------------------------------------------------------------------
class TestHomePage(BaseClass):
    def test_login_page(self):

        driver = self.driver

        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "km-welcome-promo"))) #gui bug

        current_url = driver.current_url
        assert current_url == f'{conftest.setup.domain}/assets/welcome.html'

    def test_dashboard(self):

        driver = self.driver

        UtilClass.perform_login(driver)  # call a function from util



        if __name__ == "__main__":
            # the main entry point, a web app or whatever
            pass

        time.sleep(5)
        current_url = driver.current_url
        assert current_url == f'{conftest.setup.domain}/assets/index.html#/dashboard/system'


    def test_devices(self):
        driver = self.driver
        UtilClass.perform_login(driver)  # call a function from util

        UtilClass.devices_page(driver)  # call a function from util

        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "km-outlet-toolbar")))

        Current_URL = driver.current_url

        assert Current_URL == f'{conftest.setup.domain}/assets/index.html#/devices/list/org/549c19b4892bc759e9647adc/detailed'



    def test_add_device_drop_down_menu(self):
        driver = self.driver

        UtilClass.perform_login(driver)  # call a function from util

        UtilClass.devices_page(driver)  # call a function from util

        action = ActionChains(driver)
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='dropdown km-animated-dropdown ng-scope'][2]/button/span")))
        element = element  # 'value not used ' solution
        try:
            AddDevice = driver.find_element(By.XPATH,
                                            "//div[@class='dropdown km-animated-dropdown ng-scope'][2]/button/span")
            action.move_to_element(AddDevice).click().perform()

            expected_list = ["Add CipherFort 2.0", "Add CipherFort", "Add CipherBond", "Add CipherWatch", "Upload CSV"]
            curent_list = [element.text for element in
                           driver.find_elements(By.XPATH, '//ul[@class="dropdown-menu right"]/li')]

            assert expected_list == curent_list

        except Exception as e:

            self.log_error(e)  # call function from BaseClass utilities

    def test_add_bond(self):
        driver = self.driver
        try:
            UtilClass.perform_login(driver)  # call a function from util

            UtilClass.devices_page(driver)  # call a function from util

            add_device_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//div[@class='dropdown km-animated-dropdown ng-scope'][2]/button")))
            add_device_button.click()

            addBond = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Add CipherBond")))
            addBond.click()

            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[placeholder='First Name']"))
            )
            element.send_keys("Bond")

            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[placeholder='Last Name']"))
            )
            element.send_keys("CreatedBy_Postman")

            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[placeholder='Email']"))
            )
            element.send_keys("svetlana.kalchenko@kaymera.com")

            driver.find_element(By.ID, "group").click()
            groupName = driver.find_element(By.XPATH, "//*[@id='group']/option[18]")
            groupName.click()

            driver.find_element(By.ID, "config").click()
            config = driver.find_element(By.XPATH, "//*[@id='config']/option[27]")
            config.click()

            driver.find_element(By.ID, "expirationDateSelection").click()
            exp_date = driver.find_element(By.XPATH, "//*[@id='expirationDateSelection']/option[2]")
            exp_date.click()

            ok = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='modal-footer ng-scope']/button[1]")))
            ok.click()

        except Exception as e:

            self.log_error(e)  # call function from BaseClass utilities

    def test_find_by_email(self):
        driver = self.driver
        try:
            UtilClass.perform_login(driver)  # call a function from util

            UtilClass.devices_page(driver)  # call a function from util

            search_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id='edit-search']/div/form/input")))

            search_field.send_keys("svetlana.kalchenko@kaymera.com")

        except Exception as e:

            self.log_error(e)  # call function from BaseClass utilities

    # TODO! no option to delete

    # def test_DeleteByEmail(self):
    #     driver = self.driver
    #
    #     UtilClass.toggle_developer_tools() # call function from ...
    #
    #     checkBox=driver.find_element(By.XPATH,"//*[@id='edit-devices']/ui-view/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/i")
    #     checkBox.click()
    #
    #     bulk_Change=driver.find_element(By.XPATH,"//*[@id='edit-devices']/ui-view/div[1]/div[2]/div/div[1]/span[2]/ksc-bulk-operations/button")
    #     bulk_Change.click()

    def test_reset_SIM(self):
        driver = self.driver

        UtilClass.perform_login(driver)  # call a function from util

        UtilClass.devices_page(driver)  # call a function from util
        try:
            # search for device
            search_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id='edit-search']/div/form/input")))

            search_field.send_keys("svetlana.kalchenko@kaymera.com")
            # -----------------

            checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                       "//*[@id='edit-devices']/ui-view/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/i")))

            actions = ActionChains(driver)
            actions.move_to_element(checkbox).perform()
            driver.execute_script("arguments[0].click();", checkbox)

            bulk_Change = driver.find_element(By.XPATH,
                                              "//*[@id='edit-devices']/ui-view/div[1]/div[2]/div/div[1]/span[2]/ksc-bulk-operations/button")
            bulk_Change.click()

            reset_Sim = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div/div/div/div[1]/ul/li[4]")))
            reset_Sim.click()

            alertOK = driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div[3]/button[1]")
            alertOK.click()

        except Exception as e:

            self.log_error(e)  # call function from BaseClass utilities

    # TODO  asertion
    def test_edit_bond(self):
        driver = self.driver

        UtilClass.perform_login(driver)  # call a function from util

        UtilClass.devices_page(driver)  # call a function from util

        # search for device
        search_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='edit-search']/div/form/input")))

        search_field.send_keys("svetlana.kalchenko@kaymera.com")
        # -----------------

        checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                   "//*[@id='edit-devices']/ui-view/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/i")))

        actions = ActionChains(driver)
        actions.move_to_element(checkbox).perform()
        driver.execute_script("arguments[0].click();", checkbox)

        deviceBond = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='edit-devices']/ui-view/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[2]")))
        deviceBond.click()

        editButton = driver.find_element(By.XPATH, "//*[@id='device-details']/div/div[1]/span[2]/div/button[2]")
        editButton.click()

        lastNameInput =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@id='lastname']")))
        lastNameInput.send_keys(u'\ue009' + u'\ue003')

        lastNameInput.send_keys("updatedBy_Postman")

        saveButton = driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div[3]/button[1]")
        saveButton.click()

        fullName = driver.find_element(By.XPATH,
                                       "//*[@id='device-details']/div/div[2]/div/div/div[1]/div[2]/label[1]/span")
        updatedName = fullName.text


        try:
            assert updatedName == "Bond updatedBy_Postman"

        except Exception as e:

            self.log_error(e)  # call function from BaseClass utilities

    def test_add_fort(self):
        driver = self.driver

        UtilClass.perform_login(driver)  # call a function from util

        UtilClass.devices_page(driver)  # call a function from util

        action = ActionChains(driver)
        try:
            AddDevice = driver.find_element(By.XPATH,
                                            "//div[@class='dropdown km-animated-dropdown ng-scope'][2]/button/span")
            action.move_to_element(AddDevice).click().perform()

            addFort = driver.find_element(By.LINK_TEXT, "Add CipherFort")
            addFort.click()

            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='First Name']")))
            element.send_keys("Fort")

            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[placeholder='Last Name']"))
            )
            element.send_keys("CreatedBy_Postman")

            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[placeholder='IMEI']"))
            )
            element.send_keys("356112100551640")

            driver.find_element(By.ID, "group").click()
            groupName = driver.find_element(By.XPATH, "//*[@id='group']/option[18]")
            groupName.click()

            driver.find_element(By.ID, "policy").click()
            policy = driver.find_element(By.XPATH, "//*[@id='policy']/option[3]")
            policy.click()

            driver.find_element(By.ID, "config").click()
            config = driver.find_element(By.XPATH, "//*[@id='config']/option[27]")
            config.click()

            driver.find_element(By.ID, "expirationDateSelection").click()
            expDate = driver.find_element(By.XPATH, "//*[@id='expirationDateSelection']/option[2]")
            expDate.click()

            ok = driver.find_element(By.XPATH, "//div[@class='modal-footer ng-scope']/button[1]")
            ok.click()

        except Exception as e:

            self.log_error(e)  # call function from BaseClass utilities

    def test_find_by_IMEI(self):
        driver = self.driver

        UtilClass.perform_login(driver)  # call a function from util

        UtilClass.devices_page(driver)  # call a function from util

        searchField = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='edit-search']/div/form/input")))

        searchField.send_keys("356112100551640")

        imei = driver.find_element(By.XPATH,
                                   "//*[@id='edit-devices']/ui-view/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div[6]")

        try:

            assert imei.text == ' 356112100551640'

        except Exception as e:

            self.log_error(e)  # call function from BaseClass utilities

    def test_broadcast(self):
        driver = self.driver

        UtilClass.perform_login(driver)  # call a function from util

        UtilClass.devices_page(driver)  # call a function from util

        searchField = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='edit-search']/div/form/input")))

        searchField.send_keys("356112100551640")

        checkbox = driver.find_element(By.XPATH,
                                       "//*[@id='edit-devices']/ui-view/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/i")

        actions = ActionChains(driver)
        actions.move_to_element(checkbox).perform()
        driver.execute_script("arguments[0].click();", checkbox)

        bulk_Change = driver.find_element(By.XPATH,
                                          "//*[@id='edit-devices']/ui-view/div[1]/div[2]/div/div[1]/span[2]/ksc-bulk-operations/button")
        bulk_Change.click()

        reset_Sim = driver.find_element(By.XPATH, "// ul[@class='list-unstyled'][1]/li[4]")
        reset_Sim.click()

        inputText = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[2]/b/textarea")
        inputText.send_keys("test")

        send = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[3]/button[1]")
        send.click()

    def test_Bulk_aplllyOTA(self):

        driver = self.driver

        UtilClass.perform_login(driver)  # call a function from util

        UtilClass.devices_page(driver)  # call a function from util
        try:
            # search for device
            searchField = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id='edit-search']/div/form/input")))

            searchField.send_keys("356112100551640")
            # -----------------

            checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                       "//*[@id='edit-devices']/ui-view/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/i")))

            actions = ActionChains(driver)
            actions.move_to_element(checkbox).perform()
            driver.execute_script("arguments[0].click();", checkbox)

            bulk_Change = driver.find_element(By.XPATH,
                                              "//*[@id='edit-devices']/ui-view/div[1]/div[2]/div/div[1]/span[2]/ksc-bulk-operations/button")
            bulk_Change.click()

            apply_OTA = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div/div/div/div[4]/ul/li[1]")))
            apply_OTA.click()
        # unavailable for "not activated" device
        # selectOTA = driver.find_element(By.ID, "//*[@id='configuration']")
        # selectOTA.click()
        #
        # OTA = driver.find_element(By.XPATH, "//*[@id='configuration']/option")
        # OTA.click()

        except Exception as e:

            self.log_error(e)  # call function from BaseClass utilities
# -------------------------------------------------------------------
