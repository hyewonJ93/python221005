# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(1,11):
        #오늘의 유머 베스트오브베스트
        data ='http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        # 한글이 깨지는 경우 디코딩
        page = data.decode('utf-8', 'ignore') # 디폴트 ignore 글씨 깨져도 상관없음
        soup = BeautifulSoup(page, 'html.parser')
        # attrs는 속성들
        list = soup.find_all('td', attrs={'class':'subject'})
        # <td class="subject">
        # <a href="/board/view.php?>미군의 저격수 처리 방법</a>
        # f = open("c:\\work\\aaaaaa.txt", "wt", encoding="utf-8")
        for item in list:
                try:
                        title = item.find("a").text.strip()
                        # print(title)
                        # f.write(title+ "\n")
                        if(re.search('한국',title)):
                            print(title.strip())
                except:
                        pass
        
