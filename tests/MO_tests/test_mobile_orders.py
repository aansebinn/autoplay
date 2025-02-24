import pytest
from MO_Pages.mobile_order_openpack_page import mobile_order_openpack
from test_mobile_login import login_fixture

def test_order_openpack(login_fixture):
    page = login_fixture    # 로그인된 페이지 사용
    mobile_order_openpack(page)    # order_openpack 실행
    # 브라우저 닫기 (pytest fixture에서 자동으로 닫기 처리)

# def test_order_prepack(login_fixture):
#     page = login_fixture    # 로그인된 페이지 사용
#     order_prepack(page)     # order_prepack 실행

# def test_order_promotion(login_fixture):
#     page = login_fixture
#     order_promotion(page)

   
