from Lib.browser_utils import HighlightPageWrapper

# Pages/front login
def va_login(page):
    from Lib.common_utils import LOGIN_CREDENTIALS # 함수 내부에서 임포트

    # 로그인 정보 가져오기 (전역 변수 LOGIN_CREDENTIALS 사용)
    dev_va_username = LOGIN_CREDENTIALS["va_username"]
    dev_va_password = LOGIN_CREDENTIALS["va_password"]

    # 로그인 요소 정의 및 동작
    username_input = page.locator('input[formcontrolname="userName"]')
    username_input.type(dev_va_username)
    password_input = page.locator('input[formcontrolname="password"]')
    password_input.type(dev_va_password)

    # SECURE LOGIN
    page.locator('.btn.btn-blue.width-100p.btn-login').click()

    # FG Free Shipping 팝업 x버튼
    page.locator('i.modal-close-btn').click()

    # FG Free Shipping 팝업2 x버튼
    page.locator('i.modal-close-btn').click()

    # 페이지 로딩 상태를 기다림
    page.wait_for_load_state('networkidle')

    # 로딩 상태가 완료될 때까지 기다림
    # page.wait_for_load_state()
