import numpy as np
class Car(object):
    def __init__(self,d,v):
        self.d=d
        self.v=v
        self.vnew=v
    def gogogo(self):
        if self.v*1.4<40:
            self.vnew=self.v*1.4
        else:
            self.vnew=40
    def nonono(self):
        self.vnew=self.v*0.6
#
# car1=Car(np.random.randint(0,90),np.random.randint(20,40))
# car2=Car(np.random.randint(0,90),np.random.randint(20,40))
# car3=Car(np.random.randint(0,90),np.random.randint(20,40))
# car4=Car(np.random.randint(0,90),np.random.randint(20,40))
#
# car1=Car(45,23)
# car2=Car(71,24)
# car3=Car(47,28)
# # car4=Car(76,28)
# print('车辆信息：')
# print(car1.d,car1.v)
# print(car2.d,car2.v,car2.vnew)
# print(car3.d,car3.v)
# print(car4.d,car4.v,car4.vnew)

def isbang4(car3,car4):
    flag4=False
    t1=(car3.d+15)/car3.vnew
    t2=(car4.d+5)/car4.vnew
    if abs(t1-t2)<1:
        flag4=True
    return flag4
def isbang3(car2,car3):
    flag3=False
    t1=(car3.d+5)/car3.vnew
    t2=(car2.d+15)/car2.vnew
    if abs(t1-t2)<1:
        flag3=True
    return flag3
def isbang2(car1,car2):
    flag2 = False
    t1 = (car1.d + 15) / car1.vnew
    t2 = (car2.d + 5) / car2.vnew
    if abs(t1 - t2) < 1:
        flag2 = True
    return flag2
def isbang1(car1,car4):
    flag1 = False
    t1 = (car1.d + 5) / car1.vnew
    t2 = (car4.d + 15) / car4.vnew
    if abs(t1 - t2) < 1:
        flag1 = True
    return flag1
#注意玩家 1控制的是 车辆 2与 4，注意玩家 2控制的是车辆 1与 3。
a=[-1,0,1]
b=[-1,0,1]
c=[-1,0,1]
d=[-1,0,1]
i=-1
result=[]
for aa in a:
    for bb in b:
        for cc in c:
            for dd in d:
                car1 = Car(27, 34)
                car2 = Car(22, 26)
                car3 = Car(85, 24)
                car4 = Car(40, 29)
                player1=(aa,bb)
                player2=(cc,dd)
                if (aa==0 and bb== 0 and cc==1 and dd==1):
                    ccccccccc=0
                if player1[0]==1.0:
                    car2.gogogo()
                else:
                    if player1[0]==-1.0:
                        car2.nonono()
                if player1[1]==1.0:
                    car4.gogogo()
                else:
                    if player1[1]==-1.0:
                        car4.nonono()

                if player2[0]==1.0:
                    car1.gogogo()
                else:
                    if player2[0]==-1.0:
                        car1.nonono()
                if player2[1]==1.0:
                    car3.gogogo()
                else:
                    if player2[1]==-1.0:
                        car3.nonono()
                time1=(90-car1.d)/car1.v+(110+car1.d)/car1.vnew
                time2=(90-car2.d)/car2.v+(110+car2.d)/car2.vnew
                time3=(90-car3.d)/car3.v+(110+car3.d)/car3.vnew
                time4=(90-car4.d)/car4.v+(110+car4.d)/car4.vnew
                if isbang1(car1,car4) or isbang2(car1,car2) or isbang3(car2,car3) or isbang4(car3,car4):
                    tbar=99999999999
                else:
                    tbar=(time1+time2+time3+time4)/4
                i=i+1
                result.append(tbar)
                print(i)
                print(player1[0],player1[1])
                print(player2[0],player2[1])
                print(tbar)
                print('-----------')
                # if (aa==0 and bb== 0 and cc==1 and dd==1):
                #     print("-----------------------------")
                #     print(time1,time2,time3,time4)
                #     print(car2.v,car2.vnew,car4.v,car4.vnew)
                #     print(player1,player2)


print('最优结果是：',min(result))
print('下标是：',result.index(min(result)))
#传统方法
chuantongt=max(200/car1.v,200/car3.v)+max(200/car2.v,200/car4.v)
print('传统方法是：',chuantongt)