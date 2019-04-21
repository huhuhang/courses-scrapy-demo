# -*- coding: utf-8 -*-
import scrapy
from shiyanlou_course.items import ShiyanlouCourseItem

class CoursesSpider(scrapy.Spider):
    name = 'courses'
    allowed_domains = ['shiyanlou.com']
    start_urls = ['https://www.shiyanlou.com/courses/?fee=free']

    def parse(self, response):
        # 解析当前页面各课程所在的 div, 将返回全部课程 Selector 列表
        courses = response.xpath('//div[@class="col-sm-12 col-md-3"]')
        # 遍历每个课程, 解析名称, 描述, 图片
        for course in courses:
            # 按定义好的 Item 结构返回数据
            item = ShiyanlouCourseItem()
            item['name'] = course.xpath('.//h6[@class="course-name"]/text()').extract_first().strip()
            item['description'] = course.xpath('.//div[@class="course-description"]/text()').extract_first().strip()
            item['image'] = course.xpath('.//img[@class="cover-image"]/@src').extract_first()

            yield item