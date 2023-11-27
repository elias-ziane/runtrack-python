def draw_rectangle(width, height) :
    largeur = "-" * (width - 2)
    esspace = " " * (width - 2)
    print(f"|{la}|")
    for k in range((height - 2)):
        print(f"|{space}|")
    print(f"|{la}|")

draw_rectangle(10, 3)