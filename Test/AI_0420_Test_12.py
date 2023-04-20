x = int(input("과자의 개수 : "));
y = int(input("한사람 당 나누어 주는 과자의 수 :  개\b\b\b"));

print(f"최대 나누어 줄수 있는 친구 : {x//y}명");
print(f"남는 과자의 수 : {x%y}개");

if x > y:
    
    print("asdf");