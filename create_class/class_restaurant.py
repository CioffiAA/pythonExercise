# -*- coding: utf-8 -*-
"""
@File  : class_restaurant.py
@Author: AFei
@Date  : 2020/10/25 22:42
@Desc  : 用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），
数量为5个。
"""


# 定义餐厅类
class Restaurant:
    def __init__(self, name, style, scale, score, menu):
        """
        构造函数
        :param name: 餐厅名字
        :param style: 菜系
        :param scale: 规模大小
        :param score: 评分
        :param menu: 菜单

        """
        self.name = name
        self.style = style
        self.scale = scale
        self.score = score
        self.menu = menu

    def create_dishes(self, new_dishes):
        """
        新研发菜品
        :param new_dishes: 新菜品名字
        :return:
        """
        print(f"最新研发出新菜品{new_dishes}, 欢迎新老顾客品尝。")
