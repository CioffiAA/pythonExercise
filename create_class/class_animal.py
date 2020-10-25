# -*- coding: utf-8 -*-
"""
@File  : class_Animal.py
@Author: AFei
@Date  : 2020/10/25 22:27
@Desc  : 用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），
数量为5个。
"""


#    定义动物类
class Animal:

    def __init__(self, name, animal_type, feet_num, live_place):
        """
        构造函数
        :param name: 动物名称
        :param type: 动物类型
        :param feet_num: 脚的个数
        :param liveplace: 生活地点
        """
        self.name = name
        self.animal_type = animal_type
        self.feet_num = feet_num
        self.live_place = live_place

    def run(self):
        """
        定义奔跑的方法
        :return:None
        """
        print(f"{self.animal_type}且拥有{self.feet_num}支脚的动物奔跑速度很快。")

    def search_food(self, place):
        """
        定义觅食的方法
        :param place: 觅食地点
        :return:None
        """
        print(f"{self.name}常在{place}寻找食物。")
