# -*- coding: utf-8 -*-
"""
@File  : main.py
@Author: AFei
@Date  : 2020/10/26 0:00
@Desc  : 
"""
import random

from wuxia.tonglao import TongLao
from wuxia.xuzhu import XuZhu

if __name__ == '__main__':
    # 1.创建天山童姥的实例，传入血量和武力值
    tian_shan = TongLao(980, 221)

    # 调用see_people方法
    tian_shan.see_people("丁春秋")

    # 随机生成敌方的血量和武力值
    enemy_hp = random.randint(999, 1100)
    enemy_power = random.randint(188, 220)

    # 双方交战并输出战况结果
    tian_shan.battle(enemy_hp, enemy_power)

    # 2.创建虚竹的实例:
    print("************分隔符************")
    xu_zhu = XuZhu(898, 180)
    #  调用念经的方法
    xu_zhu.read()

    # 调用的继承的see_people方法
    xu_zhu.see_people("WYZ")
