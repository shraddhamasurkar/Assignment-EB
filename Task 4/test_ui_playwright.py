"""Playwright UI checks for the Rahul Shetty Academy practice page."""

from playwright.sync_api import Page, expect

URL = "https://rahulshettyacademy.com/AutomationPractice/"


def test_practice_page_radio_dropdown_and_checkbox(page: Page) -> None:
    page.goto(URL, wait_until="domcontentloaded")

    # Radio buttons: select Radio2 and verify its checked state.
    radio2 = page.locator("input[type='radio'][value='radio2']")
    radio2.check()
    expect(radio2).to_be_checked()

    # Dropdown: select Option2 and verify the selected value.
    dropdown = page.locator("select#dropdown-class-example")
    dropdown.select_option("option2")
    expect(dropdown).to_have_value("option2")

    # Checkbox: select Option1 and verify it is checked.
    option1 = page.locator("input[type='checkbox'][value='option1']")
    option1.check()
    expect(option1).to_be_checked()


def test_hide_show_example(page: Page) -> None:
    page.goto(URL, wait_until="domcontentloaded")

    textbox = page.locator("#displayed-text")
    hide_button = page.locator("#hide-textbox")
    show_button = page.locator("#show-textbox")

    expect(textbox).to_be_visible()
    hide_button.click()
    expect(textbox).to_be_hidden()
    show_button.click()
    expect(textbox).to_be_visible()
