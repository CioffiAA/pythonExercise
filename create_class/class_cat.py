# -*- coding: utf-8 -*-
"""
@File  : class_Animal.py
@Author: AFei
@Date  : 2020/10/25 22:27
@Desc  : 用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），
数量为5个。
"""
from create_class.class_animal import Animal


# 定义猫类
class Cat(Animal):
    def __init__(self, name, animal_type, feet_num, live_place, fur_color):
        """
        构造函数：继承父类中的实例变量，并定义自己的实例变量
        :param name: 姓名
        :param animal_type: 类型
        :param feet_num: 脚的个数
        :param live_place: 生活地点
        :param fur_color: 毛发颜色
        """
        super().__init__(name, animal_type, feet_num, live_place)
        self.fur_color = fur_color

    def play(self, toy):
        """
        定义玩的方法
        :param toy: 玩具
        :return: None
        """
        print(f"猫咪爱玩{toy}。")
