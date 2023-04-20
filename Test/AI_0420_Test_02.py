import random as r;

ph = r.randint(1, 14);

if ( ph >= 1 and ph <= 6 ):

    print(f"ph={ph}, 산성입니다");

elif (ph == 7):

    print(f"ph={ph}, 중성입니다");

else:

    print(f"ph={ph}, 알칼리입니다");