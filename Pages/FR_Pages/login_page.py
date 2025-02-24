from Lib.browser_utils import HighlightPageWrapper

# Pages/front login
def login(page):
    from Lib.common_utils import LOGIN_CREDENTIALS # 함수 내부에서 임포트

    # 로그인 정보 가져오기 (전역 변수 LOGIN_CREDENTIALS 사용)
    def_front_username = LOGIN_CREDENTIALS["fr_username"] # common_utils.py "fr_username": os.getenv("Dev_fr_username") 참조
    dev_front_password = LOGIN_CREDENTIALS["fr_password"] # common_utils.py "fr_password": os.getenv("Dev_fr_password") 참조

    # 로그인 요소 정의 및 동작
    page.locator('#onetrust-accept-btn-handler').click()
    page.locator('a.header_signIn').click()
    
    username_input = page.locator('input[name="userName"]') # fill은 채우기만 해서 이벤트가 트리거가 안됨
    username_input.type(def_front_username)
    password_input = page.locator('input[name="password"]')
    password_input.type(dev_front_password)
    
    page.locator('.signin_btn').click()

    # 페이지 로딩 상태를 기다림
    page.wait_for_load_state('networkidle')
