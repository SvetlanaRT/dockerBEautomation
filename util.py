import time

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass


class UtilClass(BaseClass):

    def perform_login(driver):
        email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
        email.send_keys("admin@kaymera.com")
        password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
        password.send_keys("password")

        sendAccessCode = driver.find_element(By.ID, "submit")
        sendAccessCode.click()
        driver.find_element(By.ID, "accessCode").send_keys("")
        sendAccessCode = driver.find_element(By.ID, "submit")
        sendAccessCode.click()

    def perform_logout(driver):
        userButton = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "userSettingsButton")))
        userButton.click()
        signoutButton = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.LINK_TEXT, "Sign Out")))
        signoutButton.click()

    def trigger_reactivate_CA(self, imei):
        self.perform_login()
        self.driver.execute_script("window.devMode=true;")
        ## go to device
        ## click on rectivate CA
        self.driver.execute_script("window.devMode=false;")

    def devices_page(driver):

        action = ActionChains(driver)
        devicesButton = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.LINK_TEXT, "Devices")))
        devicesButton = devicesButton
        action.move_to_element(devicesButton).click().perform()

        try:
            WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "edit-search")))
        except TimeoutException:
            print("Error! devices_page")

    """
    Need to refresh the webpage in order to apply
    """

    def toggle_developer_tools(driver, toggle):
        driver.execute_script(f"window.devMode={str(toggle).lower()};")
