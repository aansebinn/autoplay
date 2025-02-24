import random # 랜덤함수 추가
from Lib.browser_utils import HighlightPageWrapper
from Lib.common_pages import dev_openpack1_url

# Pages/front openpack order
def va_order_list_page(page):

   page.locator('div[routerlink="/order/orders"]').click() # All orders 메뉴