def draw_rectangle(width, height):
    
    # Dessine la partie supérieure du rectangle
    print('-' * width)

    # Dessine les côtés du rectangle
    for _ in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')

    # Dessine la partie inférieure du rectangle
    print('-' * width)

# Exemple d'utilisation
draw_rectangle(10, 3)