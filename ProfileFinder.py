from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from tkinter import messagebox


def getProfile(link, account, password):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.linkedin.com")

    # Logging in
    driver.find_element_by_name("session_key").send_keys(account)
    driver.find_element_by_name("session_password").send_keys(password)
    driver.find_element_by_class_name("sign-in-form__submit-button").click()
    driver.implicitly_wait(5)

    # Verify correct log in
    try:
        driver.find_element_by_class_name("share-box-feed-entry__wrapper").is_displayed()
    except NoSuchElementException:
        driver.close()
        messagebox.showerror('Cuenta no valida', 'Por favor revisa que el correo y la contraseña de la cuenta sean '
                                                 'correctos')
        return

    # Searching candidate
    try:
        driver.get(link)
    except:
        driver.close()
        messagebox.showerror('Link no valido', 'Por favor revisa que el link del perfil sea correcto')
        return

    profileName = driver.find_element_by_class_name("t-24").text
    profilePosition = driver.find_element_by_xpath(
        "/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[1]/h2").text
    profileId = link.split("/")[4]
    driver.close()
    return profileName, profilePosition, profileId
