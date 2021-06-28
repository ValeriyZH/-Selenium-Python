'''
import math
fun = lambda x : 1 if x == 1 else math.ceil(math.sinh(fun (x-1)))
print(fun(5))



import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста
textarea = driver.find_element_by_css_selector(".textarea")

# Напишем текст ответа в найденное поле
textarea.send_keys("get()")
time.sleep(5)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_css_selector(".submit-submission")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(5)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()


Найти кнопку со значением id="submit_button" на странице http://suninjuly.github.io/simple_form_find_task.html

from selenium import webdriver
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element_by_id("submit_button")

Есть второй способ для поиска элементов с помощью универсального метода find_element() и полей класса By из библиотеки selenium. Пример:

from selenium import webdriver

from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, "submit_button")

Необходимо всегда добавлять в конце команду закрытия окна браузера, чтобы в памяти не оставались висеть ненужные процессы процессы.

from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.ID, "submit_button")
button.click()

# закрываем браузер после всех манипуляций
browser.quit()

Для того чтобы гарантировать закрытие, даже если произошла ошибка в предыдущих строках, проще всего использовать конструкцию try/finally: 

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()


Вам нужно открыть страницу по ссылке и заполнить форму на этой странице с помощью Selenium. 
Если всё сделано правильно, то вы увидите окно с проверочным кодом. Это число вам нужно ввести в качестве ответа в этой задаче.

from selenium import webdriver
import time 

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

На указанной ниже странице вам нужно найти зашифрованную ссылку и кликнуть по ней

from selenium import webdriver
import math
import time
link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()
    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


Мы уже упоминали, что метод find_element_by возвращает только первый из всех элементов, которые подходят под условия поиска. 
Иногда возникает ситуация, когда у нас есть несколько одинаковых по сути объектов на странице, например, иконки товаров в корзине интернет-магазина.
В тесте нам нужно проверить, что отображаются все выбранные для покупки товары. Для этого существуют методы find_elements_by, 
которые в отличие от find_element_by вернут список всех найденных элементов по заданному условию. Проверив длину списка, мы можем удостовериться, 
что в корзине отобразилось правильное количество товаров. Пример кода (код приведен только для примера, сайта fake-shop.com скорее всего не существует):


# подготовка для теста
# открываем страницу первого товара
# данный сайт не существует, этот код приведен только для примера
browser.get("https://fake-shop.com/book1.html")

# добавляем товар в корзину
add_button = browser.find_element_by_css_selector(".add")
add_button.click()

# открываем страницу второго товара
browser.get("https://fake-shop.com/book2.html")

# добавляем товар в корзину
add_button = browser.find_element_by_css_selector(".add")
add_button.click()

# тестовый сценарий
# открываем корзину
browser.get("https://fake-shop.com/basket.html")

# ищем все добавленные товары
goods = browser.find_elements_by_css_selector(".good")

# проверяем, что количество товаров равно 2
assert len(goods) == 2

В этой задаче вам нужно заполнить форму (http://suninjuly.github.io/huge_form.html). С помощью неё отдел маркетинга компании N
захотел собрать подробную информацию о пользователях своего продукта. В награду за заполнение формы становится доступен код на скидку. 
Но маркетологи явно переусердствовали, добавив в форму 100 обязательных полей и ограничив время на ее заполнение. Теперь эта задача под силу только роботам ﻿🤖﻿.
Используйте WebDriver и подходящий метод find_elements_by. Введите полученный код в качестве ответа к этой задаче.
Используйте приведенный ниже шаблон: в цикле for мы можем последовательно взять каждый элемент из найденного списка текстовых полей
и отправить произвольный текст в каждое поле. Если скрипт не успевает заполнить форму, выберите текст покороче. 

from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name('input')
    for element in elements:
        element.send_keys("Мой ответ")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла

На этот раз воспользуемся возможностью искать элементы по XPath. 


На странице http://suninjuly.github.io/find_xpath_form вы найдете такую же форму регистрации, как в шаге 3, 
при этом в нее добавилась куча одинаковых кнопок отправки. Но сработает только кнопка с текстом "Submit", и наша задача нажать в коде именно на неё. 

from selenium import webdriver
import time 

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath('//input[@name="first_name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//input[@name="last_name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('//input[@class="form-control city"]')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_xpath('//input[@id="country"]')
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

Попробуем реализовать один из автотестов из предыдущего шага. Вам дана страница с формой регистрации. Проверьте, что можно зарегистрироваться на сайте,
заполнив только обязательные поля, отмеченные символом *: First name, last name, email. Текст для полей может быть любым.
Успешность регистрации проверяется сравнением ожидаемого текста "Congratulations! You have successfully registered!" с текстом на странице, 
которая открывается после регистрации.

from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
    input3.send_keys("test@mail.ru")
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)  # чтобы дождаться загрузки следующей страницы, прежде чем выполнять проверки

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


Попробуйте запустить код из предыдущего шага, указав в качестве начальной страницы новую ссылку. 
Если ваш тест упал с ошибкой NoSuchElementException, это означает, что вы выбрали правильные селекторы и смогли обнаружить баг,
который создали разработчики. Это хорошо! Значит, ваши тесты сработали как надо. Пугаться не стоит, здесь ошибка в приложении которое вы тестируете, а не в вашем тесте. 

from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
    input3.send_keys("test@mail.ru")
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)  # чтобы дождаться загрузки следующей страницы, прежде чем выполнять проверки

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

Ваша программа должна выполнить следующие шаги:
Открыть страницу http://suninjuly.github.io/math.html.
Считать значение для переменной x.
Посчитать математическую функцию от x (код для этого приведён ниже).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку Submit.
Для этой задачи вам понадобится использовать атрибут .text для найденного элемента. 

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(str(y))

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option1 = browser.find_element_by_id("robotsRule")
    option1.click()

    button = browser.find_element_by_class_name("btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании. Но теперь значение переменной х спрятано в "сундуке", точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.

Ваша программа должна:

Открыть страницу http://suninjuly.github.io/get_attribute.html.
Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
Посчитать математическую функцию от x (сама функция остаётся неизменной).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку "Submit".
Для вычисления значения выражения в п.4 используйте функцию calc(x) из предыдущей задачи    


from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(str(y))

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option1 = browser.find_element_by_id("robotsRule")
    option1.click()

    button = browser.find_element_by_class_name("btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


Напишите код, который реализует следующий сценарий:
Открыть страницу http://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"

from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath('//span[@id="num1"]')
    y_element = browser.find_element_by_id('num2')
    x = str(int(x_element.text) + int(y_element.text))
    

    option = browser.find_element_by_id("dropdown")
    option.click()

    option = browser.find_element_by_xpath("//div/select/option[@value='{}']".format(x))
    option.click() 

    browser.find_element_by_xpath("//button[@type='submit']").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером, 
который дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:

Открыть страницу http://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit".
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. 
Отправьте полученное число в качестве ответа для этого задания.

Для этой задачи вам понадобится использовать метод execute_script, чтобы сделать прокрутку в область видимости элементов, перекрытых футером.

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
    x = x_element.text
    x = calc(x)

    input_str = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_str)
    input_str.send_keys(x)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option1 = browser.find_element_by_id("robotsRule")
    option1.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


В этом задании в форме регистрации требуется загрузить текстовый файл.

Напишите скрипт, который будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"
Если все сделано правильно и быстро, вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.

from selenium import webdriver
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath('//input[@name="firstname"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//input[@name="lastname"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('//input[@name="email"]')
    input3.send_keys("test@mail.ru")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'Test.txt')           # добавляем к этому пути имя файла 
    element.send_keys(file_path)
    
    button = browser.find_element_by_tag_name("button")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
    x = x_element.text

    answ = browser.find_element_by_xpath('//input[@id="answer"]')
    answ.send_keys(str(calc(int(x))))

    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.
Сценарий для реализации выглядит так:
Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
    x = x_element.text

    answ = browser.find_element_by_xpath('//input[@id="answer"]')
    answ.send_keys(str(calc(int(x))))

    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit() 


Какую ошибку вы увидите в консоли, если попытаетесь выполнить команду browser.find_element_by_id("button") после открытия страницы http://suninjuly.github.io/cats.html?

from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit() 

Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене. 
Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button_true = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    #expected_conditions.text_to_be_present_in_element((By.ID, "price"), "$100"))
    if button_true == True:
        button = browser.find_element_by_id('book')
        button.click()
    
    x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
    x = x_element.text

    answ = browser.find_element_by_xpath('//input[@id="answer"]')
    answ.send_keys(str(calc(int(x))))
    
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit() 
'''

