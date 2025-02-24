from Lib.browser_utils import HighlightPageWrapper

# Pages/front login
def login(page):
    from Lib.common_utils import LOGIN_CREDENTIALS # 함수 내부에서 임포트

    # 로그인 정보 가져오기 (전역 변수 LOGIN_CREDENTIALS 사용)
    def_front_username = LOGIN_CREDENTIALS["fr_username"] # common_utils.py "fr_username": os.getenv("Dev_fr_username") 참조
    dev_front_password = LOGIN_CREDENTIALS["fr_password"] # common_utils.py "fr_password": os.getenv("Dev_fr_password") 참조

    # Accept All Cookies 선택
    page.locator('#onetrust-accept-btn-handler').click()

    # Footer Account 선택
    page.locator('ion-tab-button span.icon.account').click()

    # 페이지를 맨 아래로 스크롤
    # page.evaluate('window.scrollTo(0, document.body.scrollHeight);')

    # 로그인 요소 정의 및 동작
    page.locator('h1.ttl_h1', has_text='Sign In').click()
    page.wait_for_load_state('networkidle') # 로딩대기
    
    username_input = page.locator('input[formcontrolname="userName"]') # fill은 채우기만 해서 이벤트가 트리거가 안됨
    username_input.type(def_front_username)
    password_input = page.locator('input[formcontrolname="password"]')
    password_input.type(dev_front_password)
    
    # Sign In 버튼(button.nclick 같은 요소가 밑에도 있어 first 추가하여 첫 번째 버튼 클릭)
    page.locator('button.button.nclick').first.click()

    # 페이지 로딩 상태를 기다림(로그인 후 로딩 딜레이 있어 조건 추가)
    page.wait_for_load_state('networkidle')

    # 또는 특정 URL을 기다릴 수도 있습니다
    # page.wait_for_url('https://dev-mobile.fashiongo.net/login?returnUrl=%2Faccount')
    
    # Needs Attention 팝업 24시간 안보이기( # 'for="personal-2"' 속성으로 label을 클릭)
    page.locator('label[for="personal-2"]').last.click()
