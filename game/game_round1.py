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


# 定义fight函数--单轮赛制
def fight():
    # 定义双方的血量和攻击力
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 200

    # 双发战斗，计算各自剩余的血量
    my_final_hp = my_hp - enemy_power
    enemy_final_hp = enemy_hp - my_power
    # 比较双方血量
    if my_final_hp > enemy_final_hp:
        print("我赢了")
    elif my_final_hp < enemy_final_hp:
        print("我输了")
    elif my_final_hp == enemy_final_hp:
        print("双方打成平手")

# 调用函数
fight()
