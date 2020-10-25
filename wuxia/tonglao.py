# -*- coding: utf-8 -*-
"""
@File  : tonglao.py
@Author: AFei
@Date  : 2020/10/25 23:24
@Desc  :
"""


# 定义天山童姥类
class TongLao:
    def __init__(self, my_hp, my_power):
        """
        构造函数
        :param hp: 血量
        :param power:  武力值
        """
        self.my_hp = my_hp
        self.my_power = my_power

    def see_people(self, name):
        """
        定义对于看到不同人作出的不同反应
        :param name: 人名
        :return: None
        """
        if name == "WYZ":
            print("师弟！！！！")
        elif name == "李秋水":
            print("师弟是我的")
        elif name == "丁春秋":
            print("叛徒！我杀了你")
        else:
            print("敢问尊下大名！")

    def fight_zms(self):
        """
        定义天山折梅手方法
        :return: None
        """
        # 武力值提升10倍
        self.my_power = self.my_power * 10
        # 血量缩减2倍
        self.my_hp = self.my_hp - 2
        # 打印天山童姥的血量和武力值
        print(f"我方血量缩减至{self.my_hp}, 武力值提升到{self.my_power}")

    def battle(self, enemy_hp, enemy_power):
        """
        定义战斗方法
        :param enemy_hp:  敌人血量
        :param enemy_power: 敌人武力值
        :return:
        """
        print(f"敌方信息：血量为{enemy_hp}, 武力值为{enemy_power}")
        print(f"我方信息：血量为{self.my_hp}, 武力值为{self.my_power}")
        # 若敌方武力值大于等于自己则使用天山折梅手技能
        if enemy_power >= self.my_power:
            self.fight_zms()

        # 计算战斗后我方和敌方的血量
        my_final_hp = self.my_hp - enemy_power
        enemy_final_hp = enemy_hp - self.my_power
        # 比较双方血量
        if self.my_hp > enemy_hp:
            print(f"我方的剩余血量为{my_final_hp}")
            print(f"敌方的剩余血量为{enemy_final_hp}")
            print("我赢了")
        elif self.my_hp < enemy_hp:
            print(f"我方的剩余血量为{my_final_hp}")
            print(f"敌方的剩余血量为{enemy_final_hp}")
            print("我输了")
        elif self.my_hp == enemy_hp:
            print(f"我方的剩余血量为{my_final_hp}")
            print(f"敌方的剩余血量为{enemy_final_hp}")
            print("双方打成平手")
