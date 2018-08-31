"""
ID: michael332
LANG: PYTHON3
TASK: gift1
"""
fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')

num = int(fin.readline())
people_money = {}
people_money_list = []

for i in range(num):
    person = fin.readline().strip()
    people_money_list.append(person)    
    people_money[person] = 0    

for i in range(num):
    person = fin.readline().strip()
    amount, people_num = map(int, fin.readline().strip().split())
    if people_num != 0:
        amount -= int(amount % people_num)
    people_money[person] -= amount
    for j in range(people_num):
        receiver = fin.readline().strip()
        people_money[receiver] += int(amount/people_num)

output = ""
for i in range(len(people_money_list)):
    output += people_money_list[i] + " %d\n" % people_money.get(people_money_list[i])


fout.write(str(output))
fout.close()
