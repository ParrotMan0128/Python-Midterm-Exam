meatQuality = input("고기의 등급이 무엇입니까?: ");
meatPrice = int(input("고기의 가격이 얼마입니까?: "));

if (meatQuality == "S"):

    if (meatPrice <= 10000):

        print("지금 당장 구매한다.");

    else:

        print("구매하지 않는다.");

elif (meatQuality == "C"):

    print("구매하지 않는다.");

else:

    print("나중에 구매한다.");

