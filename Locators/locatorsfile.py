from selenium.webdriver.common.by import By

#LoginPage

userNameLocator = (By.ID, "ap_email")
continueButtonLocator = (By.CLASS_NAME, "a-button-input")

#PasswordPage

passwordNameLocator = (By.ID, "ap_password")
keepSingedInLocator = (By.NAME, "rememberMe")
signInLocator = (By.ID, "signInSubmit")

#MainPage

cartPressButtonLocator = (By.ID, "nav-cart-count-container")

#ShoppingCartPage

firstItemLocator = (By.XPATH, "(//input[@value='Delete'])[1]")

pageCardCountLocator = (By.ID, "nav-cart-count")







