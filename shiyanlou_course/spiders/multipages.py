# -*- coding: utf-8 -*-
import scrapy
from shiyanlou_course.items import ShiyanlouCourseItem

class CoursesSpider(scrapy.Spider):
    name = 'mutipages'
    allowed_domains = ['shiyanlou.com']
    start_urls = ['https://www.shiyanlou.com/courses/?fee=free']
    
    @property
    def start_urls(self):
        """
        start_urls 需要返回一个可迭代对象，所以，你可以把它写成一个列表、元组或者生成器，这里用的是生成器
        """
        url_temp = "https://www.shiyanlou.com/courses/?cursor={}"
        cursor_list = ['', 'bz0yMA%3D%3D', 'bz00MA%3D%3D'] # 手动复制多个 cursor 值
        return (url_temp.format(cursor) for cursor in cursor_list) # 1-3 页

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
