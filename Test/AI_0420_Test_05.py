import random as r;

mylist = [];
list50 = [];
count = 0;

sum = 0;

for i in range (0, 15):

    rand = r.randint(10, 100);
    sum = sum + rand;

    mylist.append(rand);

for i in mylist:

    if (i < 50):
        
        list50.append(i);
        count = count + 1;

print(f"15개 발생 난수 :{mylist}");
print(f"50보다 작은 수 :{list50}");
print(f"50보다 작은 수의 개수 {count}");
print(f"15개 정수의 합 : {sum}");
print(f"15개 정수의 평균 : {sum / 15}");
print(f"15개 중 가장 작은 수 : {min(mylist)}");
print(f"15개 중 가장 큰  수 : {max(mylist)}");
