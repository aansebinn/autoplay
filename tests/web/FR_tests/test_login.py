import pytest
from Lib.browser_utils import lunch_browser, close_browser, HighlightPageWrapper
from Pages.web.FR_Pages.login_page import login
from Lib.common_pages import dev_front_url

@pytest.fixture(scope="module")
def login_fixture():
    # Playwright 컨텍스트와 브라우저를 초기화
    p, browser = lunch_browser()
    page = HighlightPageWrapper(browser.new_page())  # 래핑된 페이지 사용
    page.goto(dev_front_url)
    # 페이지 뷰포트를 최대화 크기로 설정
    page.set_viewport_size({"width": 1680, "height": 900})

    # 로그인 함수 호출
    login(page)

    # 로그인 후 URL 검증
    expected_url = 'https://dev-www.fashiongo.net/login?returnUrl=%2F'
    
    # assert를 사용하여 성공 시 메시지 출력
    assert page.url == expected_url, f"Fail: Expected URL {expected_url}, but got {page.url}."
    
    # 성공적으로 통과하면 출력
    print("Success: Login successful, URL matches expected.")

    yield page #로그인된 페이지를 반환    
    close_browser(p, browser) # Playwright 컨텍스트와 브라우저 닫기