import json

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse=True)
def setup(request):
    with open('conf/conf.json') as json_file:
        conf = json.load(json_file)

        options = Options()
        # options.add_argument('--headless')
        options.add_argument("--disable-gpu")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--crash-dumps-dir=/tmp')
        options.add_argument("--start-maximized")
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        # options.add_argument("--incognito")
        options.set_capability('acceptInsecureCerts', True)
        driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                                  options=options)
        #--------------------------------------------------------------------------
        setup.domain = conf['baseUrl']
        url = f'{setup.domain}/assets/welcome.html'
        driver.get(url)
        #--------------------------------------------------------------------------
        # print(driver.page_source)
        print(driver.title)
        driver.save_screenshot('./save_screenshot_method.png')  # Capture the screen
        #--------------------------------------------------------------------------

        driver.implicitly_wait(10)
        driver.maximize_window()
        request.cls.driver = driver

        yield
        driver.quit()
