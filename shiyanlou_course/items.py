# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ShiyanlouCourseItem(scrapy.Item):
    """
    定义 Item 非常简单，只需要继承 scrapy.Item 类，将每个要爬取
    的数据声明为 scrapy.Field()。下面的代码是我们每个课程要爬取的 3 个数据。
    """
    name = scrapy.Field() # 课程名称
    description = scrapy.Field() # 课程介绍
    image = scrapy.Field() # 课程图片