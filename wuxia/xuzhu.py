# -*- coding: utf-8 -*-
"""
@File  : xuzhu.py
@Author: AFei
@Date  : 2020/10/25 23:57
@Desc  : 
"""
from wuxia.tonglao import TongLao


# 定义虚竹类
class XuZhu(TongLao):
    def __init__(self, my_hp, my_power):
        """
        构造函数：继承童姥类中定义的实例变量
        :param my_hp: 血量
        :param my_power: 武力值
        """
        super().__init__(my_hp, my_power)

    def read(self):
        """
        定义念经的方法
        :return: None
        """
        print("罪过罪过")
