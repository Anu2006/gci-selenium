from multiprocessing.pool import ThreadPool
from selenium.webdriver import Chrome
import getpass

def get_elements():
    yield from (driver.find_element_by_name(element_name)
                for element_name in element_names)

pool = ThreadPool(processes=1)
async_result = pool.apply_async(get_elements)
element_names = 'handle email password passwordConfirmation'.split()
# input_values = ['Anu2006', 'ranilcd@gmail.com', 'ranil1974', 'ranil1974']
input_values = []
for info in ['user name'] + element_names[1:]:
    if 'password' in info:
        input_values.append(getpass.getpass(f'{info}: '))

    else:
        input_values.append(input(f'{info}: '))

if not input_values[2] == input_values[3]:
    raise ValueError('Enter similar passwords to last two fields')
# do some other stuff in the main process

elements = async_result.get()

driver = Chrome(executable_path='C:/Users/Ewis/Downloads/chromedriver.exe')
driver.get('https://codeforces.com/register')

for element, val in zip(elements, input_values):
    element.send_keys(val)

driver.find_element_by_class_name('submit').click()
