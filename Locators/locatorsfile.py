from selenium.webdriver.common.by import By

#LoginPage
userNameLocator = (By.ID, "ap_email")
continueButtonLocator = (By.ID, "continue")
userNameErrorLocator = (By.CLASS_NAME, 'a-list-item')

#PasswordPage
passwordNameLocator = (By.ID, "ap_password")
keepSingedInLocator = (By.NAME, "rememberMe")
signInLocator = (By.ID, "signInSubmit")
passwordNameErrorLocator = (By.CLASS_NAME, 'a-list-item')

#MainPage
cartPressButtonLocator = (By.ID, "nav-cart-count-container")
homeButtonLocator = (By.ID, "nav-logo-sprites")
searchFieldLocator = (By.ID, "twotabsearchtextbox")
searchButtonLocator = (By.ID, "nav-search-submit-button")
accountAndListsLocator = (By.ID, "nav-link-accountList")
signOutLocator = (By.ID, "nav-item-signout")

#SearchResultPage
thirdProductLocator = (By.XPATH, "(//img[@class='s-image'])[3]")

#ItemsPage
addToCartButtonLocator = (By.ID, "add-to-cart-button")

#ShoppingCartPage
firstItemLocator = (By.XPATH, "(//input[@value='Delete'])[1]")
pageCardCountLocator = (By.ID, "nav-cart-count")
