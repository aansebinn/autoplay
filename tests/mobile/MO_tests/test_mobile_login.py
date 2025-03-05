import pytest
from Lib.browser_utils import lunch_browser, close_browser, HighlightPageWrapper, custom_devices
from Pages.mobile.MO_Pages.mobile_login_page import login
from Lib.common_pages import dev_front_url, dev_mobile_url

@pytest.fixture(scope="module")
def login_fixture():
    # Playwright 컨텍스트와 브라우저를 초기화
    p, browser = lunch_browser()
    
    # 모바일 디바이스 에뮬레이션 추가
    context = browser.new_context(**custom_devices["iPhone 16"])  # iPhone 16 환경 적용
    page = HighlightPageWrapper(context.new_page())  # 래핑된 페이지 사용
    page.goto(dev_front_url)


    # 로그인 함수 호출
    login(page)

    # 로그인 후 URL 검증
    expected_url = dev_mobile_url
    
    # assert를 사용하여 성공 시 메시지 출력
    assert page.url == expected_url, f"Fail: Expected URL {expected_url}, but got {page.url}."
    
    # 성공적으로 통과하면 출력
    print("Success: Login successful, URL matches expected.")

    yield page #로그인된 페이지를 반환    
    close_browser(p, browser) # Playwright 컨텍스트와 브라우저 닫기