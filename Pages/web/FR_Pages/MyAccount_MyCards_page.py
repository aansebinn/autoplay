import random # 랜덤함수 추가
from Lib.browser_utils import HighlightPageWrapper
from Lib.common_utils import checkout_process
from Lib.common_pages import dev_openpack1_url

# Pages/front openpack order
def MyCards(page):

    # My Account > My Cards 이동
    # playwright 내장함수 goto로 이동
    page.goto('https://dev-www.fashiongo.net/MyAccount/CreditCard')

    # Add New Card 버튼
    page.locator('button.btn.btn_m_blue.cls_add_card.add-new-card-btn.nclick')

    item_input1 = page.locator('#openPackEachSizePc00')
    random_quantity = random.randint(1,3) # 1 ~ 3사이 랜덤값
    item_input1.type(str(random_quantity)) # type 랜덤값 입력

    # Add To Shopping BAG 버튼 클릭
    page.locator('.btn.btn_black_v01.addCart.nclick').click()

    # 페이지 로딩 상태를 기다림
    page.wait_for_load_state('networkidle')

    # 헤더 /cart 아이콘 클릭
    page.locator('#miniCount').click()

    # checkout_process 호출
    checkout_process(page)