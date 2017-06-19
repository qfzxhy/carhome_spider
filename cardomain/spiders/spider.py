# -*- coding: utf-8 -*-
#
from scrapy.selector import Selector
import scrapy
from cardomain.items import CardomainItem
from scrapy import Request
class Douban(scrapy.Spider):
    name = "doubanTest"
    start_urls = ['http://www.autohome.com.cn/a/'
                  ]
    url = 'http://movie.douban.com/top250'
    def parse(self, response):

        selector = Selector(response)
        first_html = selector.xpath('//div[@class="tab-content-item"]')[0]
        letter_htmls = first_html.xpath('div[@class="uibox"]/div[@class="uibox-con rank-list rank-list-pic"]') #字母
        for letter_html in letter_htmls:#
            carbrand_htmls = letter_html.xpath('dl')
            for carbrand_html in carbrand_htmls:
                carbrand = carbrand_html.xpath('dt/div/a/text()').extract()[0]
                print 'carbrand' + carbrand
                car_subbrand_html = carbrand_html.xpath('dd')
                car_subbrand_list = car_subbrand_html.xpath('div/text()').extract()
                car_subbrand_series_htmls = car_subbrand_html.xpath('ul[@class="rank-list-ul"]')
                for i, car_subrand in enumerate(car_subbrand_list):
                    html = car_subbrand_series_htmls[i]
                    car_series_list = html.xpath('li/h4/a/text()').extract()
                    print car_subrand
                    print ";".join(car_series_list)

                #
                # for i,car_subrand in enumerate(car_subbrand_list):
                #     html = car_subbrand_series_htmls[i]
                #     car_series_list = html.xpath('li/h4/a/text()').extract()
                #     print car_subrand
                #     print car_series_list
        # /div[@class="uibox-con rank-list rank-list-pic"]/dl
            #print car_htmls.xpath('div[@class="uibox-title uibox-title-border"]/span/text()').extract()[0]
        # for eachcar_html in car_htmls:
        #
        #     carbrand = eachcar_html.xpath('dt/div/a/text()').extract()[0]
        #     print 'carbrand' + carbrand
        #     car_subbrand_list = eachcar_html.xpath('dd/div[@class="h3-hit"]/text()').extract()
        #     car_subbrand_series_htmls = eachcar_html.xpath('dd/ul[@class="rank-list-ul"]')
        #     for i,car_subrand in enumerate(car_subbrand_list):
        #         html = car_subbrand_series_htmls[i]
        #         car_series_list = html.xpath('li/h4/a/text()').extract()
        #         print car_subrand
        #         print car_series_list
        # print "00000000"