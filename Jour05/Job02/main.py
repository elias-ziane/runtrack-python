def draw_rectangle(width, height) :
    largeur = "-" * (width - 2)
    espace = " " * (width - 2)
    print(f"|{largeur}|")
    for k in range((height - 2)):
        print(f"|{espace}|")
    print(f"|{largeur}|")

draw_rectangle(10, 3)