import turtle as t;
import random as r;

colors=["orange", "red", "blue", "green"];

t.shape("turtle");

for i in range (0, 10):

    x = r.randint(-200, 200);
    y = r.randint(-200, 200);

    t.color(r.choice(colors));

    t.penup();
    t.goto(x, y);
    t.pendown();

    for j in range (0, 4):

        if (j % 2 == 0):

            t.forward(100);
            t.right(90);
    
        else:

            t.forward(50);
            t.right(90);

t.mainloop();
t.bye();