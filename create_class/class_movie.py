# -*- coding: utf-8 -*-
"""
@File  : class_movie.py
@Author: AFei
@Date  : 2020/10/25 22:40
@Desc  : 用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），
数量为5个。
"""


# 定义电影类
class Movie:
    def __init__(self, name, show_time, price, style):
        """
        构造函数
        :param name: 影片名字
        :param show_time: 上映时间
        :param price: 票价
        :param style: 类型
        """
        self.name = name
        self.show_time = show_time
        self.price = price
        self.style = style

    def message(self):
        """
        定义描述电影信息的方法
        :return: None
        """
        print(f"{self.style}的{self.name}将于{self.show_time}上映，票价为{self.price}")
