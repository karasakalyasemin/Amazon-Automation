
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        element = self.find_element(*locator)
        element.click()

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def clickByIndex(self, *locator, index):
        elements = self.find_elements(*locator)
        if len(elements) > index:
            element = elements[index]
            element.click()