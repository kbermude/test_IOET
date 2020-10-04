import unittest
import page
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class test_careers(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument('--no-sandbox')
        options.add_argument("--headless")
        self.driver = webdriver.Chrome("E:\Documents\Karen\IOET\chromedriver.exe", options=options)
        self.driver.get("http://www.espol.edu.ec/es/educacion/grado/catalogo")
        self.driver.maximize_window()

    def test_careers(self):
        main_page = page.MainPage(self.driver)
        assert main_page.loaded(), "Page not found"
        main_page.get_faculty()
        main_page.get_info_career("EN")
        main_page.write_file()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

