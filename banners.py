""" This funtion takes 3 arguments to print a banner.
The firsr paramater (x) represents the character you want repeated on the top.
 The text argument represents the text you want displayed on the banner ,text must be entered between doubble quotes("").
The (y) argument represents the character that will be repeated on the bottom of the banner."""

def banner(x,text,y):
    print(x * 32)
    print("       ",text,"        ")
    print(y * 32)

