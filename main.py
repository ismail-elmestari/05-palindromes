#### Fonction secondaire
"""
Script contenant la fonction ispalindrome et un test de différents mots.

"""

def ispalindrome(p):
    """
    Verifie si la chaine de caractère en paramètre est un palyndrome
    """

    p=p.lower()
    p=p.replace(" ","")

    ponctu=".,!?_-:'"
    for c in ponctu :
        if c in p :
            p=p.replace(c,"")

    car_spec="àéèêëùôç"
    car_norm="aeeeeuoc"

    for c in car_spec :
        i=car_spec.index(c)
        if c in p :
            p=p.replace(c,car_norm[i])




    if p==p[::-1] :
        return True


    return False

#### Fonction principale



def main():

    """
    Test ispalindrome sur differents mots
    """

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))



if __name__ == "__main__":
    main()
