class noodle:
    def __init__(self, name, price):
        self.name = name
        self.price = price
#系統開始
print("歡迎使用拉麵點餐機!")
noodle1 = noodle("鹽味拉麵", 200)
noodle2 = noodle("醬油拉麵", 240)
noodle3 = noodle("豚骨拉麵", 280)

print(noodle1.name, "$", noodle1.price)
print(noodle2.name, "$", noodle2.price)
print(noodle3.name, "$", noodle3.price)
count = 0
choice = int(input("請選擇拉麵口味 (輸入: 1 or 2 or 3) "))
if choice == 1:
    count = 200
elif choice == 2:
    count = 240
else: 
    count = 280
#print(type(choice))
#print(count)
size = input("是否加大(Y/N): 豚骨口味+$58, 其他口味+$38 ")
if size == "Y" and choice == 3:
    count = count + 58
elif size == "Y" and choice != 3:
    count = count + 38
else:
    count = count
#print(count)
egg = input("是否加糖心蛋?(Y/N) ")
if egg == "Y":
    count = count + 30
meat = input("是否加叉燒?(Y/N) ")
if meat == "Y":
    count = count + 60

print(count)