# Programme réalisé par Voxfy (github.com/valdouz)

# Texte de bienvenue
print("\nBienvenue dans cette aventure. Cette histoire se passe dans le monde de Pokémon\n4 fins sont possibles.\nSaisissez votre nom d'utilisateur pour commencer:\n")
# Demande de nom d'utilisateur
username = input()

# Explication du contexte + réutilisation du nom d'utilisateur demandé precédemment
print("\nC'est un jour calme, Dresseur", username, "se balade dans la région de Kanto et finit par aller au Mont Sélénite toujours en compagnie de son fidèle Pokémon, Pikachu.\n\nSoudainement au milieu de la grotte, vous vous rendez compte que Pikachu n’est plus avec vous.\nVous le cherchez désespérément mais ne le trouvez pas.\nSoudain, vous entendez un mystérieux bruit aigu à l’autre extrémité ")

# Définition de choice_1 pour la boucle while
choice_1 = "0"

# Boucle fonctionnant tant que choice_1 n'est pas 1 ou 2
while not (choice_1 == "1" or choice_1 == "2"):
    # Demande de choix numéro 1, redéfinition de la variable choice_1
    choice_1 = str(input("\nChoix 1 : S'avancer prudemment vers le bruit\nChoix 2 : Appeler Pikachu à haute voix\n(Saisissez 1 ou 2): "))

# Choix 1 permettant de mener à 2 des 4 fins
if choice_1 == "1":
    # Texte indiquant que la prise de décision a bien fonctionné
    print("\nDresseur " + username + " décide de s'avancer prudemment vers le bruit mystérieux et découvre un Pokémon sauvage qui semble l'observer attentivement.")
    
    # Définition de choice_2 pour la boucle while
    choice_2 = "0"
    # Boucle fonctionnant tant que choice_2 n'est pas 1 ou 2 
    while not (choice_2 == "1" or choice_2 == "2"):
        # Demande de choix numéro 2, redéfinition de la variable choice_2
        choice_2 = str(input("Le Pokémon sauvage s'approche lentement de vous :\n\nChoix 1 : Tenter de capturer le Pokémon avec une PokéBall\nChoix 2 : Tenter de communiquer avec le Pokémon\n(Saisissez 1 ou 2): "))
    # Si choice_2 = 1 la fin 1 se déclanche
    if choice_2 == "1":
        # Texte de fin 
        print("\n[GAGNÉ (FIN 1/4)] Vous avez capturé le Pokémon sauvage avec succès ! Vous et Pikachu avez un nouveau compagnon de voyage.")
    # Si choice_2 = 2 la fin 2 se déclenche
    elif choice_2 == "2":
        # Texte de fin 
        print("\n[PERDU (FIN 2/4)] Le Pokémon sauvage ne semble pas comprendre votre langage. Il s'enfuit dans les bois, vous laissant seul et inquiet. Relancez et réessayez encore !")

# Choix 2
elif choice_1 == "2":
    # Texte indiquant que la prise de décision a bien fonctionné
    print("\nDresseur " + username + " décide d'appeler Pikachu à haute voix dans l'espoir qu'il le rejoigne.")
    # Définition de choice_2 pour la boucle while
    choice_2 = "0"
     # Boucle fonctionnant tant que choice_2 n'est pas 1 ou 2
    while not (choice_2 == "1" or choice_2 == "2"):
        # Demande de choix numéro 2, redéfinition de la variable choice_2
        choice_2 = str(input("Vous appelez Pikachu à plusieurs reprises, mais il n'y a aucune réponse :\n\nChoix 1 : Continuer à appeler Pikachu\nChoix 2 : S'aventurer plus profondément dans la forêt\n(Saisissez 1 ou 2): "))
    # Si choice_2 = 1 la fin 3 se déclenche
    if choice_2 == "1":
        # Texte de fin 
        print("\n[PERDU (FIN 3/4)] Malgré vos appels répétés, Pikachu ne répond pas. Vous décidez de poursuivre votre recherche. Peut-être qu'il vous attend quelque part dans la forêt.")
    # Si choice_2 = 2 la fin 4 se déclenche
    elif choice_2 == "2":
        # Texte de fin 
        print("\n[GAGNÉ (FIN 4/4)] Vous décidez de vous aventurer plus profondément dans la forêt à la recherche de Pikachu. Après une courte marche, vous le trouvez jouant avec d'autres Pokémon sauvages. Votre fidèle ami est sain et sauf et content de vous retrouver !")

# Signature ASCII :D
# ⠸⣷⣦⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⠀⠀⠀
# ⠀⠙⣿⡄⠈⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⠊⠉⣿⡿⠁⠀⠀⠀
# ⠀⠀⠈⠣⡀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠁⠀⠀⣰⠟⠀⠀⠀⣀⣀
# ⠀⠀⠀⠀⠈⠢⣄⠀⡈⠒⠊⠉⠁⠀⠈⠉⠑⠚⠀⠀⣀⠔⢊⣠⠤⠒⠊⠉⠀⡜
# ⠀⠀⠀⠀⠀⠀⠀⡽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠩⡔⠊⠁⠀⠀⠀⠀⠀⠀⠇
# ⠀⠀⠀⠀⠀⠀⠀⡇⢠⡤⢄⠀⠀⠀⠀⠀⡠⢤⣄⠀⡇⠀⠀⠀⠀⠀⠀⠀⢰⠀
# ⠀⠀⠀⠀⠀⠀⢀⠇⠹⠿⠟⠀⠀⠤⠀⠀⠻⠿⠟⠀⣇⠀⠀⡀⠠⠄⠒⠊⠁⠀
# ⠀⠀⠀⠀⠀⠀⢸⣿⣿⡆⠀⠰⠤⠖⠦⠴⠀⢀⣶⣿⣿⠀⠙⢄⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢻⣿⠃⠀⠀⠀⠀⠀⠀⠀⠈⠿⡿⠛⢄⠀⠀⠱⣄⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢸⠈⠓⠦⠀⣀⣀⣀⠀⡠⠴⠊⠹⡞⣁⠤⠒⠉⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣠⠃⠀⠀⠀⠀⡌⠉⠉⡤⠀⠀⠀⠀⢻⠿⠆⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠰⠁⡀⠀⠀⠀⠀⢸⠀⢰⠃⠀⠀⠀⢠⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⢶⣗⠧⡀⢳⠀⠀⠀⠀⢸⣀⣸⠀⠀⠀⢀⡜⠀⣸⢤⣶⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠈⠻⣿⣦⣈⣧⡀⠀⠀⢸⣿⣿⠀⠀⢀⣼⡀⣨⣿⡿⠁⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠈⠻⠿⠿⠓⠄⠤⠘⠉⠙⠤⢀⠾⠿⣿⠟⠋
