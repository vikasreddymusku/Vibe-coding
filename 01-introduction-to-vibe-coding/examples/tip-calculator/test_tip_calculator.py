"""Browser test for the tip calculator. Run: python test_tip_calculator.py"""
from pathlib import Path
from playwright.sync_api import sync_playwright

PAGE = (Path(__file__).parent / "index.html").resolve().as_uri()

def check(page, bill, tip, people, expected_text, expected_error=""):
    page.fill("#bill", bill)
    page.fill("#tip", tip)
    page.fill("#people", people)
    assert page.inner_text("#result") == expected_text, page.inner_text("#result")
    assert page.inner_text("#error") == expected_error, page.inner_text("#error")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(PAGE)
    check(page, "100", "15", "1", "Each person pays 115.00")
    check(page, "100", "20", "4", "Each person pays 30.00")
    check(page, "0", "15", "2", "Each person pays 0.00")
    msg = "Enter a bill of 0 or more, a tip of 0 or more, and at least 1 person."
    check(page, "100", "15", "0", "", msg)
    check(page, "-5", "15", "2", "", msg)
    page.fill("#bill", "")
    assert page.inner_text("#result") == "" and page.inner_text("#error") == ""
    browser.close()
print("All 6 checks passed")
