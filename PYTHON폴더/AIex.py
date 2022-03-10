hp=100
attack=10
slim_hp=100
slim_at=10
frist_at=int(input("1=공격,2=도망"))
def sp_attack():
    SP=attack*0.1
    if sp_attack ==True:
        attack=slim_hp-(attack+SP)
if frist_at==1:
    HP=slim_hp-sp_attack
    print("슬라임 피가 {}남았다.".format(HP))
elif frist_at==2:
    print("도망쳤다")