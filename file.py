import requests

url = "https://go-fujita-kanko.reservation.jp/ja/api/SP/plans?checkin_date=20230714&checkout_date=20230715&adults=1&child1=0&child2=0&child3=0&child4=0&child5=0&children=0&rooms=1&dayuseFlg=0&sort=1&pa=&ra=&clubno=&token=&pmid=&subfacility_id=go-fkg008"
headers = {
    "Cookie": "ga=GA1.3.38687789.1689753898; _gcl_au=1.1.2055274238.1689753898; _bdck=BD.iwHhr.oBJbAQ4.2; _bdnvf=YmQ0X3Ny0css98go0st38kpyDDTRMzSzsDQ3NbawtDAyMdEzAgA=; _ga=GA1.2.38687789.1689753898; _gid=GA1.2.1042298653.1690255434; _gat_gtag_UA_108058219_1=1; _gid=GA1.3.1042298653.1690255434; _gat_UA-40135696-1=1; _bdsid=BD.iwHhr.oBJbAQ4.1690255434951.2; _dc_gtm_UA-40135696-9=1; _gat_UA-39390618-97=1; _bd_prev_page=YmQ0X12M0QqDMAxFv8ZHS2112+uG+Buj2Kq1XSNtOtjfLxOFMgghh3NzHz1bELdUyXslBpoZ6imvFlXtVHDAokkmvhVaCGzdKLAqWgug8YmOyc2c3+jYvArUMoyLGZ0NT63QVLIXXEh+bdpKXHYDGf9UR0rp7JG++2bPWa8bAn6CKEGW0JbQlRBNODACvM5urT45mcHPh0sQ8aeY+AI=; _bd_prev_page_ex=YmQ0X12M0QqDMAxFv8ZHS2112+uG+Buj2Kq1XSNtOtjfLxOFMgghh3NzHz1bELdUyXslBpoZ6imvFlXtVHDAokkmvhVaCGzdKLAqWgug8YmOyc2c3+jYvArUMoyLGZ0NT63QVLIXXEh+bdpKXHYDGf9UR0rp7JG++2bPWa8bAn6CKEGW0JbQlRBNODACvM5urT45mcHPh0sQ8aeY+AI=; XSRF-TOKEN=eyJpdiI6IlB6ckl3Tkg2ditRSXpKS1M2SE1UVHc9PSIsInZhbHVlIjoiR2YyeEVGK1dDc2gxOHIvSHJ6Ni9rTGU5WkVOM2hyMStnL3k5Y0dNSTZXYUFtVForanhxYWQ0UFBTclVqeFBKVSIsIm1hYyI6ImRjZTFiYzhkYjFiZjkzYTFjOTRlNGUwM2Q5NjM3ZDU3ZDI1MmVlY2VlNTdjOTFmN2JkMzU0N2Y3OGNhYzQ0YTQiLCJ0YWciOiIifQ%3D%3D; _ga_ZW0Q4V0VKF=GS1.1.1690255430.13.0.1690255444.46.0.0; _ga_5C3WV7PPDE=GS1.1.1690255430.14.0.1690255444.46.0.0; _ga_D5XR5X9YY1=GS1.1.1690255430.13.0.1690255444.46.0.0; _ga_S1D344WCSM=GS1.1.1690255431.13.0.1690255444.47.0.0; laravelsession=eyJpdiI6Iisya0p3UWRFbVU4d1VoRW9NUFRUZEE9PSIsInZhbHVlIjoiQ24reEJUMWVweTRJZVhWZXB1MSt5RTZTSjNKb25NWUhjbU5CQS9PTjE3dExnVUNUNStRYktRZThjNmk2bDVrcXo2M3VJUzdGYitoZ1JqMXAzQ3dFWEE0RzdHS0FtcitBYUF1UDRGalZpb3FqMUh5UThXSjAwUkFYcFFBK1J2d2QiLCJtYWMiOiI4YWVjNDhhYTBkZDg5M2QyMmM4MmRiYTJmNzZjZGI1MWUyMjNjYTdmYzE4ZTA2N2ZmMjBiNzkxNGU4MjYyYzUzIiwidGFnIjoiIn0%3D",
    "User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
}

response = requests.post(url, headers=headers)

data = response.json()
print(data['additionMode'])
print(data['sub_facility_domain'])
print(data['holiday'])
print(data['plans'][0]['planId'])

for i in range(len(data['plans'])):
    planid = data['plans'][i]['planId']
    print(planid)
    child_url = f"https://go-fujita-kanko.reservation.jp/ja/hotels/fkg008/plans/{planid}?checkin_date=20230721&checkout_date=20230722&adults=1&child1=0&child2=0&child3=0&child4=0&child5=0&children=0&rooms=1&dayuseFlg=0&sort=1&room_id&plan_id&pa=&ra=&clubno=&token=&pmid="
    print(child_url)
    # child_headers = {
    #     "Cookie": "_ga=GA1.3.38687789.1689753898; _gcl_au=1.1.2055274238.1689753898; _bdck=BD.iwHhr.oBJbAQ4.2; _bdnvf=YmQ0X3Ny0css98go0st38kpyDDTRMzSzsDQ3NbawtDAyMdEzAgA=; _gid=GA1.2.1042298653.1690255434; _gid=GA1.3.1042298653.1690255434; _bdsid=BD.iwHhr.oBJbAQ4.1690255434951.2; _gat_UA-40135696-1=1; _dc_gtm_UA-40135696-9=1; _gat_UA-39390618-97=1; _gat_gtag_UA_108058219_1=1; _ga=GA1.1.38687789.1689753898; _bd_prev_page=YmQ0X12O3QrDIAxGn8bLitV2P5cbpa8xpNrW6kzRONjbz24tyCCE7+SEkHtHZ8Q1EnEjvM81QTWmxaCsrPQWaNBRh5dEA54ua15YZG4zoHYxh9FOjF1yWJ3026BmrLm015aIfpj1YI1/KImaiI4zLtiZ14SfvgYS/imelVTJYX6n++0Zp+oM7ABegiihKaEtIWi/YwB4HreVfKeoezftLkLATVH+AQ==; _bd_prev_page_ex=YmQ0X12O3QrDIAxGn8bLitV2P5cbpa8xpNrW6kzRONjbz24tyCCE7+SEkHtHZ8Q1EnEjvM81QTWmxaCsrPQWaNBRh5dEA54ua15YZG4zoHYxh9FOjF1yWJ3026BmrLm015aIfpj1YI1/KImaiI4zLtiZ14SfvgYS/imelVTJYX6n++0Zp+oM7ABegiihKaEtIWi/YwB4HreVfKeoezftLkLATVH+AQ==; XSRF-TOKEN=eyJpdiI6Ijl1S2hrNjJRZ3dvYkZFVUxFcWN3ZlE9PSIsInZhbHVlIjoiN0NVODR5MW5mYTQweVpDUU0wNG5idUFoQ0FIeGw5R3R3RTBGdFA5M3g3MzdXcEdpU1ZqZ1BWRjJoeUhLQUtuQSIsIm1hYyI6ImI5N2YwODY1ZjZmYjZmYjdhMTU5NzY5ODY4YThhZGZkYzAwYjQ0NTc5OWFhMDk2NTBjYWMzZWNiYjhmNmIxYTUiLCJ0YWciOiIifQ%3D%3D; _ga_5C3WV7PPDE=GS1.1.1690255430.14.1.1690256150.50.0.0; _ga_D5XR5X9YY1=GS1.1.1690255430.13.1.1690256150.50.0.0; _ga_S1D344WCSM=GS1.1.1690255431.13.1.1690256150.50.0.0; _ga_ZW0Q4V0VKF=GS1.1.1690255430.13.1.1690256150.51.0.0; laravelsession=eyJpdiI6InlqTk53ckE2MlYwZUVYYUR2YkF1SGc9PSIsInZhbHVlIjoiL0ZyL3RQdXBlYXZzblRxY0FoZ0Q4MVhYYzR1anh6RWxUSzQrcFBnQ2NJNW11UzdFZHplWm1qOHZic1VVQ2R0d1E1UzNseHZGVmN5dTJBTDRZNE1ralRON2c1Mm9QSHVYOVlvcFkxL05BcG10dWwvY0ZrK2grZytXcVRSQVg0RmgiLCJtYWMiOiJiOThmMjc2ZTNkNjRlMjVhY2VhMmY2YjJkYWY0MDYzYTIyZmFhODg2NjYyYTdiZGIwNmRkMWQyZTFiMDZlYzZlIiwidGFnIjoiIn0%3D",
    #     "User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
    # }
    # child_data = requests.post(child_url, headers=child_headers).json()
    # print(child_data['additionMode'])