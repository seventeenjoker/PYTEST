from pytest import mark



def test_television_turns_on(tv_brand):
    print(f"{tv_brand} turns on as expected")

def test_browser_can_navigate_to_trainig_ground(browser):
    browser.get("http://udemy.com")