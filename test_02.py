from pytest_steps import test_steps, depends_on
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.gry-online.pl/")

# def setup():
#     driver.maximize_window()
#     driver.get("https://www.gry-online.pl/")


# @depends_on(setup)
def click_on_signup():
    cookies = WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element_by_xpath("button.qc-cmp-button:nth-child(2)")))
    cookies.click()
    driver.implicitly_wait(time_to_wait=10)
    element = WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element_by_xpath("/html/body/div[2]/nav/div[1]/div[4]/a")))
    element.click()


@depends_on(click_on_signup)
def complete_fields():
    login = driver.find_element_by_css_selector(".td1 > p:nth-child(3) > input:nth-child(1)")
    password = driver.find_element_by_css_selector(".td1 > p:nth-child(5) > input:nth-child(1)")
    password2 = driver.find_element_by_css_selector(".td1 > p:nth-child(7) > input:nth-child(1)")
    nick = driver.find_element_by_css_selector(".td1 > p:nth-child(9) > input:nth-child(1)")
    email = driver.find_element_by_css_selector(".td1 > p:nth-child(11) > input:nth-child(1)")

    login.send_keys("Abcd")
    password.send_keys("TestPassword1")
    password2.send_keys("mail@massafsam.pl")
    nick.send_keys("TestowyNick123NG")
    email.send_keys("TestowyNick123NG")

    checkbox = driver.find_element_by_xpath(".//*[@id='ZGODA1']")
    checkbox.click()


@test_steps(
    # setup,
    click_on_signup,
    complete_fields
)
def test_registration_form(test_step):
    test_step()
