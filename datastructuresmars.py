intro = """Anton Voyl n’arrivant plus à dormir, poursuivi par la vision d’un motif inconnu sur son tapis, rumina moult
solutions, pour finir par l’ablation du sinus.
Il aurait fallu plus, car il voyait sa fin pas trop loin. Il aurait voulu, auparavant, savoir si l’Omission qu’il
soupçonnait (rapport au cinq), virait ou non à l’hallucination.
Il nota dans son journal faits, soupçons, divagations, jusqu’à un synopsis d’un roman où Aignan, un garçon
ayant vaincu un sphinx, grandissait pour finir baisant sa maman, puis pourrissait sur un îlot, par mortification
pour son forfait.
Soudain Anton Voyl disparut, laissant un mot confus."""

intro= intro.lower()


for char in intro:
    if char.isalpha() == True:
        
        intro = intro.replace(char, "")