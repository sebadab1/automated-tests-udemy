# import pytest
# from pytest_steps import test_steps, depends_on
# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# # driver = webdriver.Firefox()
#
#
# def setup():
#     # driver.maximize_window()
#     # driver.get("https://www.udemy.com/")
#
#
# @depends_on(setup)
# def click_on_signup():
#     element = WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[4]/div[7]/div/button")))
#     element.click()
#
#
# @depends_on(click_on_signup)
# def complete_fields():
#     full_name = driver.find_element_by_id("form-item-fullname")
#     email = driver.find_element_by_id("form-item-email")
#     password = driver.find_element_by_id("form-item-password")
#
#     full_name.send_keys("Abcd")
#     email.send_keys("mail@massafsam.pl")
#     password.send_keys("TestPassword1")
#
#
# # @pytest.mark.skip
# # @test_steps(
# #     # setup,
# #     # click_on_signup,
# #     # complete_fields
# # )
# # def test_registration_form(test_step):
# #     test_step()
