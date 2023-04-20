for i in range (1, 100):

    a = i // 10;
    b = i % 10;

    if (a == 3 or a == 6 or a == 9 or b == 3 or b == 6 or b ==9):

        if ((b == 3 or b == 6 or b == 9) and (a == 3 or a == 6 or a == 9)):

            print("짝짝", end="\t");
    
        else:

            print("짝", end="\t");
    
    else:

        print(f"{i}", end="\t");

    if (i % 10 == 0):

        print("");