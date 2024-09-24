import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature('Menu Navigation')
@allure.suite('UI Tests')
@allure.title('Test Menu Item Navigation')
@allure.description('Verifies that each menu item on the homepage navigates to the correct page and displays the correct heading.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_menu_item(driver):
    with allure.step('Navigate to homepage'):
        driver.get("https://tutorialsninja.com/demo/")
        expected_menu_items = ["Desktops", "Laptops & Notebooks", "Components", "Tablets", "Software", "Phones & PDAs", "Cameras", "MP3 Players"]

    with allure.step('Click on Desktops menu item'):
        menu_item1 = driver.find_element(By.LINK_TEXT, expected_menu_items[0])
        menu_item1.click()

    with allure.step('Click on Laptops & Notebooks menu item'):
        menu_item2 = driver.find_element(By.LINK_TEXT, expected_menu_items[1])
        menu_item2.click()

    with allure.step('Click on Components menu item'):
        menu_item3 = driver.find_element(By.LINK_TEXT, expected_menu_items[2])
        menu_item3.click()

    with allure.step('Click on Tablets menu item and verify heading'):
        menu_item4 = driver.find_element(By.LINK_TEXT, expected_menu_items[3])
        menu_item4.click()
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[3]

    with allure.step('Click on Software menu item and verify heading'):
        menu_item5 = driver.find_element(By.LINK_TEXT, expected_menu_items[4])
        menu_item5.click()
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[4]

    with allure.step('Click on Phones & PDAs menu item and verify heading'):
        menu_item6 = driver.find_element(By.LINK_TEXT, expected_menu_items[5])
        menu_item6.click()
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[5]

    with allure.step('Click on Cameras menu item and verify heading'):
        menu_item7 = driver.find_element(By.LINK_TEXT, expected_menu_items[6])
        menu_item7.click()
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[6]

    with allure.step('Click on MP3 Players menu item'):
        menu_item9 = driver.find_element(By.LINK_TEXT, expected_menu_items[7])
        menu_item9.click()


@allure.feature('Menu Navigation')
@allure.suite('UI Tests')
@allure.title('Test Nested Menu Navigation')
@allure.description('Verifies that submenu items under different menu categories are displayed and clickable.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
@pytest.mark.parametrize("menu_locator, submenu_locator, result_text", [
    (
        (By.PARTIAL_LINK_TEXT, 'Desktops'),
        (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[1]/a'),
        'PC'
    ),
    (
        (By.PARTIAL_LINK_TEXT, 'Desktops'),
        (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[2]/a'),
        'Mac'
    ),
    (
        (By.PARTIAL_LINK_TEXT, 'Laptops & Notebooks'),
        (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/div/div/ul/li[1]/a'),
        'Macs'
    ),
    (
        (By.PARTIAL_LINK_TEXT, 'Laptops & Notebooks'),
        (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/div/div/ul/li[2]/a'),
        'Windows'
    ),
    (
        (By.PARTIAL_LINK_TEXT, 'Components'),
        (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[3]/div/div/ul/li[1]/a'),
        'Mice and Trackballs'
    ),
    (
        (By.PARTIAL_LINK_TEXT, 'Components'),
        (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[3]/div/div/ul/li[2]/a'),
        'Monitors'
    ),
    (
        (By.PARTIAL_LINK_TEXT, 'Components'),
        (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[3]/div/div/ul/li[3]/a'),
        'Printers'
    ),
    (
        (By.PARTIAL_LINK_TEXT, 'Components'),
        (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[3]/div/div/ul/li[4]/a'),
        'Scanners'
    ),
    (
        (By.PARTIAL_LINK_TEXT, 'Components'),
        (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[3]/div/div/ul/li[5]/a'),
        'Web Cameras'
    )
])
def test_nested_menu(driver, menu_locator, submenu_locator, result_text):
    with allure.step('Navigate to homepage'):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step('Hover over menu and click submenu'):
        menu = driver.find_element(*menu_locator)
        submenu = driver.find_element(*submenu_locator)
        ActionChains(driver).move_to_element(menu).click(submenu).perform()

    with allure.step(f'Verify heading text matches expected result: {result_text}'):
        assert driver.find_element(By.TAG_NAME, 'h2').text == result_text


@allure.feature('Search Functionality')
@allure.suite('UI Tests')
@allure.title('Test Product Search')
@allure.description('Verifies that searching for a product returns relevant results.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
def test_search_product(driver):
    with allure.step('Navigate to homepage'):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step('Locate search bar'):
        search = driver.find_element(By.NAME, 'search')

    with allure.step('Enter search term and submit'):
        search.send_keys('MacBook')

    with allure.step('Click search button'):
        button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-default.btn-lg')
        button.click()

    with allure.step('Verify relevant products are displayed'):
        products = driver.find_elements(By.TAG_NAME, 'h4')

    with allure.step('Filter products based on search term and assert results'):
        new_list = [elem.text for elem in products if 'MacBook' in elem.text]

    with allure.step('Assert that all displayed products match the search term'):
        assert len(products) == len(new_list), "Not all displayed products match the search term"


@allure.feature('Cart Management')
@allure.suite('UI Tests')
@allure.title('Test Add Product to Cart')
@allure.description('Verifies that a product can be added to the cart and displayed correctly.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_add_to_cart(driver):
    with allure.step('Navigate to the homepage'):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step('Locate and add the product to the cart'):
        product = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[1]')
        product.click()

    with allure.step('Wait for the success message to appear'):
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible"))
        )

    with allure.step('Verify the success message is correct'):
        assert "Success: You have added MacBook to your shopping cart!" in success_message.text

    with allure.step('Wait for the cart total to update'):
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "cart-total"), "1 item(s)")
        )

    with allure.step('Open the cart'):
        cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'cart'))
        )
        cart_button.click()

    with allure.step('Wait for the cart contents to be visible'):
        cart_contents = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'ul.dropdown-menu.pull-right'))
        )

    with allure.step('Verify that the cart contains the added product'):
        assert "MacBook" in cart_contents.text, f"Expected MacBook in cart, but got {cart_contents}"


@allure.feature('Cart Management')
@allure.suite('UI Tests')
@allure.title('Test Remove Product from Cart')
@allure.description('Verifies that a product can be removed from the cart successfully.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_delete_item_from_cart(driver):
    with allure.step('Navigate to the homepage'):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step('Open the cart'):
        cart = driver.find_element(By.XPATH, '//*[@id="cart"]/button')
        cart.click()

    with allure.step('Wait for the cart contents to be visible'):
        cart_contents = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'ul.dropdown-menu.pull-right'))
        )

    with allure.step('Verify that the cart contains "MacBook"'):
        assert "MacBook" in cart_contents.text, f"Expected 'MacBook' in cart, but got{cart_contents}"

    with allure.step('Locate and click the remove button for the product'):
        cart_remove = driver.find_element(By.XPATH, '//*[@id="cart"]/ul/li[1]/table/tbody/tr/td[5]/button')
        cart_remove.click()

    with allure.step('Wait for the cart total to update'):
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "cart-total"), "0 item(s)")
        )


@allure.feature('Homepage Slider')
@allure.suite('UI Tests')
@allure.title('Test Slider Functionality')
@allure.description('Verifies that the homepage slider functions correctly, allowing navigation between images.')
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.smoke
@pytest.mark.regression
def test_slider_functionality(driver):
    with allure.step('Navigate to the homepage'):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step('Locate the slider element'):
        slider = driver.find_element(By.CLASS_NAME, 'swiper-container')

    with allure.step('Verify the slider is visible'):
        assert slider.is_displayed(), "Slider is not visible on the page"

    with allure.step('Get the source of the first slide image'):
        first_slide = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img")
        first_slide_src = first_slide.get_attribute("src")

    with allure.step('Locate the next arrow button'):
        next_arrow = driver.find_element(By.CLASS_NAME, "swiper-button-next")

    with allure.step('Click the next arrow to navigate to the next slide'):
        ActionChains(driver).move_to_element(slider).click(next_arrow).perform()

    with allure.step('Wait for the slide transition to complete'):
        WebDriverWait(driver, 10).until_not(
            EC.element_to_be_clickable(first_slide)
        )

    with allure.step('Get the source of the new slide image'):
        new_slide = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img")
        new_slide_src = new_slide.get_attribute("src")

    with allure.step('Verify that the new slide is different from the first slide'):
        assert first_slide_src != new_slide_src, "Slider did not move to the next image."

    with allure.step('Click the previous arrow to return to the first slide'):
        previous_arrow = driver.find_element(By.CLASS_NAME, 'swiper-button-prev')
        previous_arrow.click()

    with allure.step('Wait for the slide transition to complete'):
        WebDriverWait(driver, 10).until_not(
            EC.element_to_be_clickable(new_slide)
        )

    with allure.step('Get the source of the currently active slide after navigating back'):
        reverted_slide_src = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img").get_attribute("src")

    with allure.step('Verify that the slider has returned to the first image'):
        assert reverted_slide_src == first_slide_src, "Slider did not return to the first image."


@allure.feature('Wishlist Functionality')
@allure.suite('UI Tests')
@allure.title('Test Add Product to Wishlist without Login')
@allure.description('Verifies that adding a product to the wishlist without logging in prompts a login message.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
def test_wishlist_functionality_without_login(driver):
    with allure.step('Navigate to the homepage'):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step('Locate the first product on the page'):
        first_product = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div[1]'))
            )

    with allure.step('Verify that the first product is displayed'):
        assert first_product.is_displayed(), "The first product is not displayed."

    with allure.step('Click on the wishlist button for the first product'):
        wishlist_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[2]'))
        )
        wishlist_button.click()

    with allure.step('Wait for and capture the login prompt message'):
        login_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible"))
        )

    with allure.step('Verify the login prompt message is displayed'):
        assert "You must login or create an account to save MacBook to your wish list!" in login_message.text, \
            f"Expected login prompt, but got: {login_message.text}"

    with allure.step('Wait for the wishlist total to update'):
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'wishlist-total'), "Wish List (1)")
        )

    with allure.step('Locate the wishlist total element'):
        wish_list_total = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'wishlist-total'))
        )

    with allure.step('Click on the wishlist total to view the wishlist'):
        ActionChains(driver).move_to_element(wish_list_total).click().perform()

    with allure.step('Click on the heart icon to view the wishlist'):
        heart_icon = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="top-links"]/ul/li[3]'))
        )
        heart_icon.click()

    with allure.step('Wait for the URL to change to the login page'):
        WebDriverWait(driver, 10).until(EC.url_contains("account/login"))

    with allure.step('Verify that the current URL is the login page'):
        assert "account/login" in driver.current_url, f"Expected to be on the login page, but current URL is: {driver.current_url}"

    with allure.step('Locate the username field on the login page'):
        username_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'input-email'))
        )

    with allure.step('Locate the password field on the login page'):
        password_field = driver.find_element(By.ID, 'input-password')

    with allure.step('Verify the username field is displayed on the login page'):
        assert username_field.is_displayed(), "Username field is not displayed on the login page."

    with allure.step('Verify the password field is displayed on the login page'):
        assert password_field.is_displayed(), "Password field is not displayed on the login page."

    with allure.step('Locate the login button on the login page'):
        login_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')

    with allure.step('Verify the login button is displayed on the login page'):
        assert login_button.is_displayed(), "Login button is not displayed on the login page."


@allure.feature('Wishlist Functionality')
@allure.suite('UI Tests')
@allure.title('Test Add Product to Wishlist after Login')
@allure.description('Verifies that a logged-in user can add a product to the wishlist successfully.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_add_item_to_wishlist(driver, login):
    with allure.step('Navigate to the homepage'):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step('Locate the wishlist button for the first product'):
        wishlist_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[2]'))
        )
        wishlist_button.click()

    with allure.step('Wait for the success message to appear'):
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.alert.alert-success'))
        )

    with allure.step('Verify the success message for adding to wishlist'):
        assert "Success: You have added MacBook to your wish list!" in success_message.text, "Adding item to wishlist failed: Success message not found."

    with allure.step('Click on the wishlist link to view the wishlist'):
        wishlist_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="wishlist-total"]'))
        )
        wishlist_link.click()

    with allure.step('Verify that the wishlist page is displayed'):
        assert driver.find_element(By.TAG_NAME, 'h2').text == 'My Wish List'

    with allure.step('Wait for the wishlist contents to load'):
        wishlist_contents = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/table'))
        )

    with allure.step('Verify that MacBook is present in the wishlist'):
        assert "MacBook" in wishlist_contents.text, "MacBook not found in wishlist"


@allure.feature('Footer Links')
@allure.suite('UI Tests')
@allure.title('Test Footer Links')
@allure.description('Verifies that all footer links navigate to the correct page and display the expected heading.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.parametrize("button_locator, header_locator, expected_text", [
    ((By.LINK_TEXT, "About Us"), (By.XPATH, '//*[@id="content"]/h1'), "About Us"),
    ((By.LINK_TEXT, "Delivery Information"), (By.XPATH, '//*[@id="content"]/h1'), "Delivery Information"),
    ((By.LINK_TEXT, "Privacy Policy"), (By.XPATH, '//*[@id="content"]/h1'), "Privacy Policy"),
    ((By.LINK_TEXT, "Terms & Conditions"), (By.XPATH, '//*[@id="content"]/h1'), "Terms & Conditions"),
    ((By.LINK_TEXT, "Contact Us"), (By.XPATH, '//*[@id="content"]/h1'), "Contact Us"),
    ((By.LINK_TEXT, "Returns"), (By.XPATH, '//*[@id="content"]/h1'), "Product Returns"),
    ((By.LINK_TEXT, "Site Map"), (By.XPATH, '//*[@id="content"]/h1'), "Site Map"),
    ((By.LINK_TEXT, "Brands"), (By.XPATH, '//*[@id="content"]/h1'), "Find Your Favorite Brand"),
    ((By.LINK_TEXT, "Gift Certificates"), (By.XPATH, '//*[@id="content"]/h1'), "Purchase a Gift Certificate"),
    ((By.LINK_TEXT, "Affiliate"), (By.XPATH, '/html/body/div[2]/div/div/h2[3]'), "My Affiliate Account"),
    ((By.LINK_TEXT, "Specials"), (By.XPATH, '//*[@id="content"]/h2'), "Special Offers"),
    ((By.XPATH, '/html/body/footer/div/div/div[4]/ul/li[1]/a'), (By.XPATH, '//*[@id="content"]/h2[1]'), "My Account"),
    ((By.LINK_TEXT, "Order History"), (By.XPATH, '//*[@id="content"]/h1'), "Order History"),
    ((By.LINK_TEXT, "Wish List"), (By.XPATH, '//*[@id="content"]/h2'), "My Wish List"),
    ((By.LINK_TEXT, "Newsletter"), (By.XPATH, '//*[@id="content"]/h1'), "Newsletter Subscription")
])
def test_footer(driver, button_locator, header_locator, expected_text):
    with allure.step('Navigate to the homepage'):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step('Locate and click the footer link'):
        footer_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(button_locator)
        )
        footer_button.click()

    with allure.step('Wait for the expected text page to load and verify the header'):
        header_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(header_locator)
        )
        header_text = header_element.text

    with allure.step('Verify the page header matches expected text'):
        assert header_text == expected_text, f"Expected '{expected_text}', but got '{header_text}'"

    with allure.step('Navigate back to the homepage'):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step('Wait for the footer to be visible on the homepage'):
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))