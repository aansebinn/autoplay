import random # 랜덤함수 추가
from Lib.browser_utils import HighlightPageWrapper
from Lib.common_utils import MO_checkout
from Lib.common_pages import dev_mobile_openpack1_url

# Pages/front openpack order
def mobile_order_openpack(page):

    # openpack item url 이동
    page.goto(dev_mobile_openpack1_url)

    # 옵션 선택
    page.locator('.btn_openPack').first.click()
    
    # 1번째칸 수량 
    item_input1 = page.locator('input.num_input.ng-untouched.ng-pristine.ng-valid')
    random_quantity = random.randint(1,3) # 1 ~ 3사이 랜덤값
    item_input1.first.type(str(random_quantity)) # type 랜덤값 입력
    
    # Add 버튼
    page.locator('button.btn-base.black').click() 

    # Add To Shopping BAG 버튼 클릭
    page.locator('button.btn_add_bag.nclick', has_text="Add to shopping bag").click(force = True) # App banner가 있어서 로그인 후 닫기하고, 강제클릭하여 해결

     # 3초 대기
    page.wait_for_timeout(3000)

    # 페이지 로딩 상태를 기다림
    page.wait_for_load_state('networkidle')

    # Footer Bag 아이콘 선택
    page.locator('ion-tab-button span.icon.bag').click()

    # checkout_process 호출
    MO_checkout(page)