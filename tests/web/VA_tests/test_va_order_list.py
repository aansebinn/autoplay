import pytest
from Pages.web.VA_Pages.va_order_list import va_order_list_page
from test_va_login import login_fixture

def test_va_login(login_fixture):
    page = login_fixture    # 로그인된 페이지 사용
    va_order_list_page(page)    # order_openpack 실행
    # 브라우저 닫기 (pytest fixture에서 자동으로 닫기 처리)

   
