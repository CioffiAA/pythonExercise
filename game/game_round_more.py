# -*- coding: utf-8 -*-
"""
@File  : __init__.py.py
@Author: AFei
@Date  : 2020/10/25 22:01
@Desc  :
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，
hp的初始值为1000，power的初始值为200。
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜

"""


# 定义fight函数--多轮赛制
def fight():
    # 定义双方的血量和攻击力
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 199

    while True:

        # 双发战斗，计算各自剩余的血量
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power
        # 打印双方剩余血量
        print(f"我方剩余血量为{my_hp}")
        print(f"敌方剩余血量为{enemy_hp}")

        # 若任意一方血量<=0则结束战斗,
        if my_hp <= 0:
            print("我输了")
            # 退出while循环
            break
        elif enemy_hp <= 0:
            print("我赢了")
            break


# 调用函数
fight()
