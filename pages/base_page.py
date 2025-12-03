from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainScreenPage:
    gallery_widget = (AppiumBy.ACCESSIBILITY_ID, "Gallery")
    phone_widget = (AppiumBy.ACCESSIBILITY_ID, "Phone")
    camera_widget = (AppiumBy.ACCESSIBILITY_ID, "Camera")
    photo_click_button = (AppiumBy.ACCESSIBILITY_ID, "Shutter")
    new_photo = (AppiumBy.ID, 'com.android.camera2:id/rounded_thumbnail_view')
    last_photo = (AppiumBy.XPATH, "(//android.widget.ImageView)[last()]")


    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, 20)

    def open_gallery_widget(self):
        self.wait.until(EC.element_to_be_clickable(self.gallery_widget)).click()

    def is_gallery_visible(self):
        assert self.wait.until(EC.visibility_of_element_located(self.gallery_widget))

    def open_phone_widget(self):
        self.wait.until(EC.element_to_be_clickable(self.phone_widget)).click()

    def is_phone_visible(self):
        assert self.wait.until(EC.visibility_of_element_located(self.phone_widget))

    def make_photo(self):
        self.wait.until(EC.element_to_be_clickable(self.photo_click_button)).click()

    def open_camera_widget(self):
        self.wait.until(EC.element_to_be_clickable(self.camera_widget)).click()

    def is_camera_visible(self):
        assert self.wait.until(EC.visibility_of_element_located(self.camera_widget))

    def open_new_photo(self):
        new_photo = self.wait.until(EC.visibility_of_element_located(self.new_photo))
        new_photo.click()
        return new_photo

    def last_photo_is_displayed(self):
        last_photo = self.wait.until(EC.visibility_of_element_located(self.last_photo))
        assert last_photo.is_displayed()
