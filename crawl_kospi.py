import pandas as pd
import requests
from bs4 import BeautifulSoup

df = pd.read_csv('kospi_list.csv')
for index, row in df.iterrows():
    if row['회사명'] != '삼성전자':
        continue
    print(row['회사명'], row['종목코드'])
    kospi_code = str(row['종목코드'])
    kospi_code = '0'*(6-len(kospi_code)) + kospi_code

    url = 'https://finance.naver.com/item/main.nhn?code=' + kospi_code

    #print(url)
    #1) 당기순이익을 본다! 당기순손실 나면 안 사면 됨. 2000개 종목 중 살 종목이 많다. 3년, 5년 기록을 찾아서 적자난 기업은 다 탈락. 분기는 1년 정도 기간을 본다. 분기 한, 두번 적자는 괜찮다. 유상증자는 조심! 유상증자는 회사에 돈이 없어서 하는 것. 유상증자는 100이던 주가가 50이 될 수 있음. 유상증자로 주식이 반토막 나면 100%되야 본전. 그런 리스크를 원하지 않는다. 계속 수익을 내는 기업을 찾는다.
    url = 'https://finance.naver.com/item/coinfo.nhn?code=' + kospi_code
    url = f'https://navercomp.wisereport.co.kr/v2/company/cF3002.aspx?cmp_cd={kospi_code}&frq=0&rpt=0&finGubun=MAIN&frqTyp=0&cn=&encparam=UDdRTnhjaHZlRkZHTkZaY0dxTVRKdz09'
    res = requests.get(url)
    #print(res.text)
    print(res.text)

    #soup = BeautifulSoup(res.text, 'html.parser')
    #div_id = '#fabG05RlB6cn'
    #data = soup.find("div", {"id": div_id})
    #print(data)

    

    #pd.read_html()



    break
    