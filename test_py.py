import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    page.get_by_role("button", name="Customer Login").click()
    page.locator("#userSelect").select_option("2")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Deposit").click()
    page.get_by_placeholder("amount").click()
    page.get_by_placeholder("amount").fill("4000")
    page.get_by_role("form").get_by_role("button", name="Deposit").click()
    page.get_by_role("button", name="Withdrawl").click()
    page.get_by_placeholder("amount").click()
    page.get_by_placeholder("amount").fill("2000")
    page.get_by_role("button", name="Withdraw", exact=True).click()
    page.get_by_role("button", name="Transactions").click()
    page.get_by_role("button", name="Back").click()
    page.get_by_role("button", name="Withdrawl").click()
    page.get_by_placeholder("amount").click()
    page.get_by_placeholder("amount").fill("3000")
    page.get_by_role("button", name="Withdraw", exact=True).click()
    page.get_by_role("button", name="Transactions").click()
    page.get_by_role("button", name="Back").click()
    page.get_by_role("button", name="Withdrawl").click()
    page.get_by_placeholder("amount").click()
    page.get_by_placeholder("amount").fill("1000")
    page.get_by_role("button", name="Withdraw", exact=True).click()
    page.get_by_role("button", name="Logout").click()
    expect(page.locator(page.get_by_role("button", name="Home").click()))

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
