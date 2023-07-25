import scrapy

class ScrapitSpider(scrapy.Spider):
    

    name = 'hotelspider'
    #start_urls = ["https://go-fujita-kanko.reservation.jp/ja/api/SP/plans?checkin_date=20230714&checkout_date=20230715&adults=1&child1=0&child2=0&child3=0&child4=0&child5=0&children=0&rooms=1&dayuseFlg=0&sort=1&pa=&ra=&clubno=&token=&pmid=&subfacility_id=go-fkg008"]
    start_urls = ["https://go-fujita-kanko.reservation.jp/ja/hotels/fkg008/plans?checkin_date=20230714&checkout_date=20230715&adults=1&child1=0&child2=0&child3=0&child4=0&child5=0&children=0&rooms=1&dayuseFlg=0&sort=1"]

    def parse(self, response):
        yield scrapy.Request(
                url = "https://go-fujita-kanko.reservation.jp/ja/api/SP/plans?checkin_date=20230714&checkout_date=20230715&adults=1&child1=0&child2=0&child3=0&child4=0&child5=0&children=0&rooms=1&dayuseFlg=0&sort=1&pa=&ra=&clubno=&token=&pmid=&subfacility_id=go-fkg008",
                callback=self.parse_data,
            )

    

    def parse_data(self, response):
        #data = response.json()
        print("*************")
        print(response)
        print("*************")