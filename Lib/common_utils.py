import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 공통 환경 변수(전역 변수로 정의)
LOGIN_CREDENTIALS = {
    "fr_username": os.getenv("env_fr_username"),
    "fr_password": os.getenv("env_fr_password"),
    "va_username": os.getenv("env_va_username"),
    "va_password": os.getenv("env_va_password"),
    "mo_username": os.getenv("env_mo_username"),
    "mo_password": os.getenv("env_mo_password"),
}

def checkout_process(page):
    """
    Cart 부터 시작
    """
    # Shopping BAG 클릭 후 URL 검증
    expected_url = 'https://dev-www.fashiongo.net/cart'
    page.wait_for_url(expected_url)

    assert page.url == expected_url, f"Fail: Expected URL {expected_url}, but got {page.url}." # assert를 사용하여 실패 시 메시지 출력
    print(f"Success: {expected_url} matched the expected value!")

    # Cart > Proceed To Checkout 버튼 클릭
    page.locator('.btn-dark_grey.btn-checkoutAll.nclick').click()

    # You Have Promotions! 팝업
    page.locator_popup('button.btn-sure', has_text="Continue To Checkout").click()

    '''
    Checkout Step1_Shipping
    '''
    # Save & Continue 버튼 클릭
    page.locator('.btn-dark_grey.btn-goToPayment').click()

    ## Verify Your Address 팝업
    page.locator_popup('.common-btn.c-black', has_text="Keep This Address").click()

    '''
    Checkout Step2_Payment
    '''
    # Save & Continue 버튼 클릭
    page.locator('.btn-dark_grey.btn-goToReview').click()

    '''
    Checkout Step3_Order Review
    '''
    # Submit Order 버튼 클릭
    page.locator('.btn-dark_grey.btn-checkout').click()

    # 주문 완료 후 Thank you for your order! 텍스트가 포함된 h2 요소 확인
    page.wait_for_load_state('networkidle')  # 페이지가 완전히 로드될 때까지 기다리기
    if page.locator('h2.order-title').count() > 0:  # h2 태그의 order-title 클래스가 1개 이상 있으면 성공
        print("Order successful! Test passed.")
    else:
        print("Order not found! Test failed.")

def checkout_promotion(page):
    """
    Cart 부터 시작
    """
    # Shopping BAG 클릭 후 URL 검증
    expected_url = 'https://dev-www.fashiongo.net/cart'
    page.wait_for_url(expected_url)

    assert page.url == expected_url, f"Fail: Expected URL {expected_url}, but got {page.url}." # assert를 사용하여 실패 시 메시지 출력
    print(f"Success: {expected_url} matched the expected value!")

    # Cart > Select Vendor Promotions 버튼 클릭(Vendor ID 16502 Allium)
    page.locator('button.btn-vendor.size-medium_blue[data-nclick-extra*="vid=16502"]').click()
    # 60% Off & Free Shipping $50.00+ Orders
    apply_button = page.locator('button.btn-apply.nclick', has_text="Apply").nth(0) # 첫 번째 버튼 클릭
    apply_button.click()

    # Cart > Proceed To Checkout 버튼 클릭
    page.locator('.btn-dark_grey.btn-checkoutAll.nclick').click()

    # You Have Promotions! 팝업
    page.locator_popup('button.btn-sure', has_text="Continue To Checkout").click()

    '''
    Checkout Step1_Shipping
    '''
    # Save & Continue 버튼 클릭
    page.locator('.btn-dark_grey.btn-goToPayment').click()

    ## Verify Your Address 팝업
    page.locator('.common-btn.c-black', has_text="Keep This Address").click()

    '''
    Checkout Step2_Payment
    '''
    # Save & Continue 버튼 클릭
    page.locator('.btn-dark_grey.btn-goToReview').click()

    '''
    Checkout Step3_Order Review
    '''
    # Submit Order 버튼 클릭
    page.locator('.btn-dark_grey.btn-checkout').click()

    # 주문 완료 후 Thank you for your order! 텍스트가 포함된 h2 요소 확인
    page.wait_for_load_state('networkidle')  # 페이지가 완전히 로드될 때까지 기다리기
    if page.getByText("Thank you for your order!").count() > 0:  # h2 태그의 order-title 클래스 1개 이상 있으면 성공
        print("Order successful! Test passed.")
    else:
        print("Order not found! Test failed.")


def MO_checkout(page):
    '''
    모바일 checkout 함수, Cart 부터 시작
    '''
    # 페이지 로딩 상태를 기다림
    page.wait_for_load_state('networkidle')

    # Shopping Bag > Checkout All Vendor 버튼
    page.locator('button.checkout-btn.nclick').click()

    '''
    Checkout Step1_Shipping
    '''
    # Save & Continue
    page.locator('button.base-btn.primary.medium.ng-star-inserted').click()

    '''
    Checkout Step2_Payment
    '''
    # Save & Continue
    page.locator('button.base-btn.primary.medium.ng-star-inserted').click()

    # Backup Card 팝업 > No thanks 선택
    page.locator_popup('button.base-btn.primary-line.nclick').click()

    '''
    Checkout Step3_Order Review
    '''
    # Submit Order
    page.locator('button.base-btn.primary.medium.ng-star-inserted').click()


    # 주문 완료 후 Thank you for your order! 텍스트가 포함된 h2 요소 확인
    page.wait_for_load_state('networkidle') # 페이지 로딩 상태를 기다림
    if page.locator('h3.ttl_h3.blue_ttl').count() > 0:  # h2 태그의 order-title 클래스가 1개 이상 있으면 성공
        print("Thank you for your order! Test passed.")
    else:
        print("Order test failed.")