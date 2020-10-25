# -*- coding: utf-8 -*-
"""
@File  : class_Animal.py
@Author: AFei
@Date  : 2020/10/25 22:27
@Desc  : 用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），
数量为5个。
"""


# 定义人类
class Person:
    def __init__(self, name, gender, age):
        """
        构造函数
        :param name: 姓名
        :param gender: 性别
        :param age: 年龄
        """
        self.name = name
        self.gender = gender
        self.age = age

    def eat(self, place):
        """
        定义吃饭的方法
        :param place: 吃饭地点
        :return:None
        """
        print(f"{self.name}在{place}吃饭。")

    def jogging(self):
        """
        定义运动的方法
        :return: None
        """

        print(f"{self.name}喜欢慢跑。")
