from pages.base_page import MainScreenPage


def test_check_gallery_element_on_main_screen_navigate_to_gallery_app(driver):
    main_page = MainScreenPage(driver)
    main_page.open_gallery_widget()
    assert driver.current_package in "com.android.gallery3d"

def test_check_phone_element_on_main_screen_navigate_to_phone_app(driver):
    main_page = MainScreenPage(driver)
    main_page.open_phone_widget()
    assert driver.current_package in "com.android.dialer"

def test_check_user_can_make_photo_on_camera(driver):
    main_page = MainScreenPage(driver)
    main_page.open_camera_widget()
    assert driver.current_package in "com.android.camera2"
    main_page.make_photo()
    main_page.open_last_photo()
    assert driver.current_package in "android:id/decor_content_parent"
