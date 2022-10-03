__author__ = 'miserylab'

from time import sleep
# curl 'https://demowebshop.tricentis.com/addproducttocart/catalog/31/1/1' \
#   -X 'POST' \
#   -H 'Accept: */*' \
#   -H 'Accept-Language: en-US,en;q=0.9,pt;q=0.8' \
#   -H 'Connection: keep-alive' \
#   -H 'Content-Length: 0' \
#   -H 'Cookie: Nop.customer=864a7c1b-e110-48a5-a1dd-fa09e25cc6ce; ARRAffinity=d6c82487af1ea910e6463ed8508be095561f2dc09520dd60ef6e65e0a2105a9f; ARRAffinitySameSite=d6c82487af1ea910e6463ed8508be095561f2dc09520dd60ef6e65e0a2105a9f' \
#   -H 'DNT: 1' \
#   -H 'Origin: https://demowebshop.tricentis.com' \
#   -H 'Referer: https://demowebshop.tricentis.com/' \
#   -H 'Sec-Fetch-Dest: empty' \
#   -H 'Sec-Fetch-Mode: cors' \
#   -H 'Sec-Fetch-Site: same-origin' \
#   -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36' \
#   -H 'X-Requested-With: XMLHttpRequest' \
#   -H 'sec-ch-ua: "Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "Windows"' \
#   --compressed

from uuid import uuid4
import requests

def test():
    print(uuid4())


def test_add_to_cart_unauthorized():
    response = requests.post('https://demowebshop.tricentis.com/addproducttocart/catalog/31/1/1',
                             cookies={'Nop.customer': '864a7c1b-e110-48a5-a1dd-fa09e25cc6ce;'})
    assert response.status_code == 200
    assert response.json()['success'] is True
    assert response.json()['message'] == 'The product has been added to your <a href=\"/cart\">shopping cart</a>'


def test_add_to_cart_unauthorized_one_product():
    response = requests.post('https://demowebshop.tricentis.com/addproducttocart/catalog/31/1/1',
                             cookies={'Nop.customer': str(uuid4())})
    assert response.status_code == 200
    assert response.json()['success'] is True
    assert response.json()['message'] == 'The product has been added to your <a href=\"/cart\">shopping cart</a>'
    assert response.json()['updatetopcartsectionhtml'] == '(1)'

'''добавить два товара (не работает)'''
def test_add_to_cart_unauthorized_two_product():
    uid = str(uuid4()) + ';'
    requests.post('https://demowebshop.tricentis.com/addproducttocart/catalog/31/1/1',
                             cookies={'Nop.customer': uid})
    sleep(1)
    response = requests.post('https://demowebshop.tricentis.com/addproducttocart/catalog/31/1/1',
                             cookies={'Nop.customer': uid})
    assert response.status_code == 200
    assert response.json()['success'] is True
    assert response.json()['message'] == 'The product has been added to your <a href=\"/cart\">shopping cart</a>'
    assert response.json()['updatetopcartsectionhtml'] == '(2)'


def test_add_to_cart_authorized():
    from dotenv import load_dotenv
    import os
    load_dotenv()
    login = os.getenv('user_login')
    password = os.getenv('user_password')

    curl
    'https://demowebshop.tricentis.com/login' \
    - H
    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
    - H
    'Accept-Language: en-US,en;q=0.9,pt;q=0.8' \
    - H
    'Cache-Control: no-cache' \
    - H
    'Connection: keep-alive' \
    - H
    'Content-Type: application/x-www-form-urlencoded' \
    - H
    'Cookie: ARRAffinity=d6c82487af1ea910e6463ed8508be095561f2dc09520dd60ef6e65e0a2105a9f; ARRAffinitySameSite=d6c82487af1ea910e6463ed8508be095561f2dc09520dd60ef6e65e0a2105a9f; __RequestVerificationToken=ZcRtklYYKVHhwp6PBpG9dknajjjeHHeqRVfadOzX1tLCIMoeVn6UArTnWJ3f0PgN67KSn8Vebe5OpUC3aduW3Jr9fJSHGuoQWvRXU4bZVWg1; NopCommerce.RecentlyViewedProducts=RecentlyViewedProductIds=72; ASP.NET_SessionId=4k1nturkhyrlrvintaqjue4l; Nop.customer=6869e29e-d13a-4a9b-b34b-5342b630ff63' \
    - H
    'DNT: 1' \
    - H
    'Origin: https://demowebshop.tricentis.com' \
    - H
    'Pragma: no-cache' \
    - H
    'Referer: https://demowebshop.tricentis.com/login' \
    - H
    'Sec-Fetch-Dest: document' \
    - H
    'Sec-Fetch-Mode: navigate' \
    - H
    'Sec-Fetch-Site: same-origin' \
    - H
    'Sec-Fetch-User: ?1' \
    - H
    'Upgrade-Insecure-Requests: 1' \
    - H
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36' \
    - H
    'sec-ch-ua: "Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"' \
    - H
    'sec-ch-ua-mobile: ?0' \
    - H
    'sec-ch-ua-platform: "Windows"' \
    - -data - raw
    'Email=emailtest%40example.com&Password=123456&RememberMe=false' \
    - -compressed
    
    response = requests.post(/login)
