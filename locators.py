from selenium.webdriver.common.by import By

class MainPageLocators(object):
    faculties = (By.XPATH, "//*[@id=\"accordion\"]")
    #To find faculty name
    def faculty_name(self, value,language):
        if value != "" or value != None:
            return (By.XPATH,f"//*[@id=\"heading{value.upper()}\"]/h4/a/strong/text()[{str(language)}]")
    # To find faculty data
    def faculty_collapsable(value):
        if value != "" or value != None:
             return (By.XPATH,f"//*[@id=\"heading{value.upper()}\"]/h4/a/strong")
    # To find faculty careers
    def faculty_careers(value,language):
        if value != "" or value != None:
            return (By.XPATH,f"//*[@id=\"collapse{value.upper()}\"]/div/ul[{str(language)}]")
    # To find careers name
    def career_name(value,language,posicion):
        if value != "" or value != None:
            return (By.XPATH,f"//*[@id=\"collapse{value.upper()}\"]/div/ul[{str(language)}]/li[{str(posicion)}]")
    # To find the link with more information about career
    def career_link(value,language,posicion):
        if value != "" or value != None:
            return (By.XPATH,f"//*[@id=\"collapse{value.upper()}\"]/div/ul[{str(language)}]/li[{str(posicion)}]/a")
    # To find the code of the career
    def career_code(value, language, posicion):
        if value != "" or value != None:
            return (
            By.XPATH, f"//*[@id=\"collapse{value.upper()}\"]/div/ul[{str(language)}]/li[{str(posicion)}]/span")

