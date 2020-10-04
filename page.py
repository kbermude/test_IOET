from locators import MainPageLocators
import time


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.filename = "Careers_ESPOL"
        self.locator = "FACULTADES"
        self.faculty = []
        self.info_complete = {}


class MainPage(BasePage):
    def loaded(self):
        return self.locator in self.driver.page_source

    def get_faculty(self):
        faculties = self.driver.find_element(*MainPageLocators.faculties)
        for f in faculties.text.split("("):
            if ")" in f: self.faculty.append(f.split(")")[0])

    def get_info_career(self, value):
        lan = 1 if value.upper() == "ES" else 2
        for i, facul in enumerate(self.faculty):
            if i == 0:
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight/4);")
            elif i < len(self.faculty) - 1:
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight/2);")
            else:
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            self.info_complete.setdefault(facul, [])
            time.sleep(3)
            element = self.driver.find_element(*MainPageLocators.faculty_collapsable(facul))
            print(element)
            element.click()
            time.sleep(5)
            careers = self.driver.find_element(*MainPageLocators.faculty_careers(facul, lan))
            total_careers = int(len(careers.text.split("\n")) / 2)
            time.sleep(5)
            for n in range(1, total_careers + 1):
                name = self.driver.find_element(*MainPageLocators.career_name(facul, lan, n))
                code = self.driver.find_element(*MainPageLocators.career_code(facul, lan, n))
                link = self.driver.find_element(*MainPageLocators.career_link(facul, lan, n))
                val = (name.text.split("(")[0], code.text, link.get_attribute('href'))
                self.info_complete[facul].append(val)

    def write_file(self):
        file = open(self.filename + ".csv", "w")
        head = "career_name_en,career_code,faculty_name,link_to_career_curriculum\n"
        file.write(head)
        for faculty, info_faculty in self.info_complete.items():
            for career in info_faculty:
                file.write(f"{career[0]};{career[1]},{faculty};{career[2]}\n")
        file.close()


