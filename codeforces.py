from selenium.webdriver import Chrome

driver = Chrome(executable_path='C:/Users/Ewis/Downloads/chromedriver.exe')
driver.get('https://codeforces.com/register')

element_names = ['handle', 'email', 'password', 'passwordConfirmation']
input_values = ['Anu2006', 'ranilcd@gmail.com', 'ranil1974', 'ranil1974']

elements = (driver.find_element_by_name(element_name)
            for element_name in element_names)

for element, val in zip(elements, input_values):
    element.send_keys(val)

driver.find_element_by_class_name('submit').click()
