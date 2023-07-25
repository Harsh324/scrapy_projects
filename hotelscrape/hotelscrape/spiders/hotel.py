import scrapy
import requests
from scrapy import FormRequest

class MySpider(scrapy.Spider):
    name = 'hotel'
    start_urls = ["https://go-fujita-kanko.reservation.jp/ja/api/SP/plans?checkin_date=20230714&checkout_date=20230715&adults=1&child1=0&child2=0&child3=0&child4=0&child5=0&children=0&rooms=1&dayuseFlg=0&sort=1&pa=&ra=&clubno=&token=&pmid=&subfacility_id=go-fkg008"]
    #start_urls = ["https://go-fujita-kanko.reservation.jp/ja/api/SP/plans/"]


    def start_requests(self):
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" :"en-US,en;q=0.9",
            "Cache-Control": "no-cache",
            "Origin": "https://go-fujita-kanko.reservation.jp",
            "Pragma": "no-cache",
            "Sec-Ch-Ua": '''"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"''',
            "Sec-Ch-Ua-Mobile": "?1",
            "Sec-Ch-Ua-Platform": "Android",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Referer": "https://go-fujita-kanko.reservation.jp/ja/hotels/fkg008/plans?checkin_date=20230714&checkout_date=20230715&adults=1&child1=0&child2=0&child3=0&child4=0&child5=0&children=0&rooms=1&dayuseFlg=0&sort=1&room_id&plan_id&pa=&ra=&clubno=&token=&pmid=",
            "Cookie": "_ga=GA1.3.38687789.1689753898; _gcl_au=1.1.2055274238.1689753898; _bdck=BD.iwHhr.oBJbAQ4.2; _bdnvf=YmQ0X3Ny0css98go0st38kpyDDTRMzSzsDQ3NbawtDAyMdEzAgA=; _ga=GA1.2.38687789.1689753898; _gid=GA1.2.1042298653.1690255434; _gat_gtag_UA_108058219_1=1; _gid=GA1.3.1042298653.1690255434; _gat_UA-40135696-1=1; _bdsid=BD.iwHhr.oBJbAQ4.1690255434951.2; _dc_gtm_UA-40135696-9=1; _gat_UA-39390618-97=1; _bd_prev_page=YmQ0X12M0QqDMAxFv8ZHS2112+uG+Buj2Kq1XSNtOtjfLxOFMgghh3NzHz1bELdUyXslBpoZ6imvFlXtVHDAokkmvhVaCGzdKLAqWgug8YmOyc2c3+jYvArUMoyLGZ0NT63QVLIXXEh+bdpKXHYDGf9UR0rp7JG++2bPWa8bAn6CKEGW0JbQlRBNODACvM5urT45mcHPh0sQ8aeY+AI=; _bd_prev_page_ex=YmQ0X12M0QqDMAxFv8ZHS2112+uG+Buj2Kq1XSNtOtjfLxOFMgghh3NzHz1bELdUyXslBpoZ6imvFlXtVHDAokkmvhVaCGzdKLAqWgug8YmOyc2c3+jYvArUMoyLGZ0NT63QVLIXXEh+bdpKXHYDGf9UR0rp7JG++2bPWa8bAn6CKEGW0JbQlRBNODACvM5urT45mcHPh0sQ8aeY+AI=; XSRF-TOKEN=eyJpdiI6IlB6ckl3Tkg2ditRSXpKS1M2SE1UVHc9PSIsInZhbHVlIjoiR2YyeEVGK1dDc2gxOHIvSHJ6Ni9rTGU5WkVOM2hyMStnL3k5Y0dNSTZXYUFtVForanhxYWQ0UFBTclVqeFBKVSIsIm1hYyI6ImRjZTFiYzhkYjFiZjkzYTFjOTRlNGUwM2Q5NjM3ZDU3ZDI1MmVlY2VlNTdjOTFmN2JkMzU0N2Y3OGNhYzQ0YTQiLCJ0YWciOiIifQ%3D%3D; _ga_ZW0Q4V0VKF=GS1.1.1690255430.13.0.1690255444.46.0.0; _ga_5C3WV7PPDE=GS1.1.1690255430.14.0.1690255444.46.0.0; _ga_D5XR5X9YY1=GS1.1.1690255430.13.0.1690255444.46.0.0; _ga_S1D344WCSM=GS1.1.1690255431.13.0.1690255444.47.0.0; laravelsession=eyJpdiI6Iisya0p3UWRFbVU4d1VoRW9NUFRUZEE9PSIsInZhbHVlIjoiQ24reEJUMWVweTRJZVhWZXB1MSt5RTZTSjNKb25NWUhjbU5CQS9PTjE3dExnVUNUNStRYktRZThjNmk2bDVrcXo2M3VJUzdGYitoZ1JqMXAzQ3dFWEE0RzdHS0FtcitBYUF1UDRGalZpb3FqMUh5UThXSjAwUkFYcFFBK1J2d2QiLCJtYWMiOiI4YWVjNDhhYTBkZDg5M2QyMmM4MmRiYTJmNzZjZGI1MWUyMjNjYTdmYzE4ZTA2N2ZmMjBiNzkxNGU4MjYyYzUzIiwidGFnIjoiIn0%3D",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
            "X-Xsrf-Token": "eyJpdiI6Inl1eTQ5U1ZoQzRmUFNZS2xLb3lDS3c9PSIsInZhbHVlIjoiMHEwOFBKQk52ZCtiOFpnL3B4eGdJWk5zRE56dU43YVdldFdKRTg4Z3dDVnM4bmhkYXdmUUNOVEMwdng0QUdmaml5UHJPbDFkQ2lWUXlmTGwrU1N3T2dmMXk3Z1FBMDhKMzRuNGhEeDRlbklEaUFzcmJoWDE4bzZEbDhVRnRKWGIiLCJtYWMiOiIwMWQ5YjBkYzY0YmNlOTBjY2M5ODQ4MmE4YWFjZjMyZjE0MDk0ZjkyZmEzNWY0ZTk0Mjg0YmFmY2RiZjA3NTlkIiwidGFnIjoiIn0=",
        }

        url = "https://go-fujita-kanko.reservation.jp/ja/hotels/fkg008/plans/10048601?checkin_date=20230721&checkout_date=20230722&adults=1&child1=0&child2=0&child3=0&child4=0&child5=0&children=0&rooms=1&dayuseFlg=0&sort=1"

        # payload = {
        #     "checkin_date": "20230714",
        #     "checkout_date": "20230715",
        #     "adults": "1",
        #     "child1": "0",
        #     "child2": "0",
        #     "child3": "0",
        #     "child4": "0",
        #     "child5": "0",
        #     "children": "0",
        #     "rooms": "1",
        #     "dayuseFlg": "0",
        #     "sort": "1",
        #     "pa": "",
        #     "ra": "",
        #     "clubno": "",
        #     "token": "",
        #     "pmid": "",
        #     "subfacility_id": "go-fkg008"
        # }

        #formdata = "checkin_date=20230714&checkout_date=20230715&adults=1&child1=0&child2=0&child3=0&child4=0&child5=0&children=0&rooms=1&dayuseFlg=0&sort=1&pa=&ra=&clubno=&token=&pmid=&subfacility_id=go-fkg008"

        response = requests.post(self.start_urls[0], headers=headers)
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse, meta={'data': response.json()})
        #yield self.parse(response)


        

    def parse(self, response):
        data = response.meta['data']
        print(data['additionMode'])
        print(data['sub_facility_domain'])
        print(data['holiday'])



        
        
