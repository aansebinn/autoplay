from playwright.sync_api import sync_playwright

# Lib/browser_util.py 크롬 브라우저 런처

def lunch_browser():
    # Playwright 컨텍스트를 반환
    p = sync_playwright().start()
    browser = p.chromium.launch(headless = False, args = ["--kiosk"]) # headless 여부
    return p, browser

def close_browser(p, browser): # browser 객체가 위에 외부로 있기 떄문에 close 내부 객체를 전달
    browser.close() # 전달된 브라우저 객체를 닫음
    p.stop()

class HighlightPageWrapper:
    """
    locator Highlight 표시
    """ 
    def __init__(self, page):
        self._page = page  # 원래 Playwright의 page 객체를 저장

    def locator(self, selector, *args, **kwargs):
        """
        locator 호출 시 자동으로 하이라이트
        *args는 주로 인수가 여러 개일 수 있는 경우에 사용, 
        **kwargs는 키워드 인수로 전달된 값을 받아서 유연하게 처리
        """
        locator = self._page.locator(selector, *args, **kwargs)
        self._page.evaluate("""
        (selector) => {
            const element = document.querySelector(selector);
            if (element) {
                element.style.border = '2px solid red';  // 빨간색 테두리 추가
                setTimeout(() => {
                    element.style.border = '';  // 일정 시간 후 테두리 제거
                }, 1000);
            }
        }
    """, selector)
        
        # 요소가 DOM에 존재하는지 체크 (is_visible 대신 사용)
        if locator.count() > 0:
            print(f"{selector} found")
        else:
            print(f"{selector} not found")
        return locator
    
    def locator_popup(self, selector, *args, **kwargs):
        """
        locator 호출 시 자동으로 하이라이트
        *args는 주로 인수가 여러 개일 수 있는 경우에 사용, 
        **kwargs는 키워드 인수로 전달된 값을 받아서 유연하게 처리
        """
        locator = self._page.locator(selector, *args, **kwargs)
        self._page.evaluate("""
        (selector) => {
            const element = document.querySelector(selector);
            if (element) {
                element.style.border = '2px solid red';  // 빨간색 테두리 추가
                setTimeout(() => {
                    element.style.border = '';  // 일정 시간 후 테두리 제거
                }, 1000);
            }
        }
    """, selector)
               
        if locator.count() == 0: # 요소가 0이 아니면
            print(f"{selector} not found, skipping.")
            return self._page.locator("body")  # 빈 요소 반환하여 skip하기

        return locator

    def wait_for_load_state(self, *args, **kwargs):
        """
        페이지의 로딩 상태가 완료될 때까지 기다립니다.
        """
        return self._page.wait_for_load_state(*args, **kwargs)
    
    def wait_for_element(self, selector, timeout=5000):
        """
        지정된 selector가 페이지에 로드될 때까지 기다립니다.
        """
        self._page.wait_for_selector(selector, timeout=timeout)
        return self._page.locator(selector)
    
    def __getattr__(self, name):
        """
        원래 Playwright의 page 메서드 및 속성에 접근 가능하도록 래핑
        __getattr__의 역할: HighlightPageWrapper가 가진 속성이나 메서드가 아닌 경우, Playwright의 원래 page 객체의 속성이나 메서드를 반환합니다.
        이를 통해 page.goto()와 같은 호출이 직접적으로 가능해집니다.
        """
        return getattr(self._page, name)
    
    """
    locator.click() 으로 사용하는게 나아서 주석처리
    
    def click_locator(self, selector, *args, **kwargs):
        self.wait_for_load_state() # 페이지 로드 될 때까지 기다리기

        try:
            locator = self.locator(selector, *args, **kwargs)  # 하이라이트 추가 후 locator 반환
            if locator.is_visible() and locator.count() > 0: # 요소 존재하는지 확인
                locator.click()  # 클릭 수행
                print(f"{selector} Clicked")
            else:
                print(f"{selector} Not found. Skipping.")
        except Exception as e:
            print(f"Error: Failed to click on {selector}. Exception: {e}")
            # raise  # 필요하면 예외를 다시 발생시켜 호출자에게 알림 raise 주석처리로 예외 발생하더라고 중단되지 않도록 처리
    """
    
custom_devices = {
"""
모바일 디바이스 추가
context = browser.new_context(**custom_devices["Galaxy S24"])로 실행
new_context는 playwright에서 제공하는 내장 함수
"""
    "Galaxy S24": {
        "user_agent": "Mozilla/5.0 (Linux; Android 14; SM-S921B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
        "viewport": {"width": 412, "height": 915},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
    },
    "iPhone 16": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/537.36",
        "viewport": {"width": 430, "height": 932},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
    }
}
