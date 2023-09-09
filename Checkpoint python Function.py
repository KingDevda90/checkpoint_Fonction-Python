#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Creatuion des fonctions
def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num,num2):
    if num2 == 0:
        print("Error, le numero 2 doit etre different de zero")
    else:
        return num1/num2
#Fonction qui invite l'utilisateur d'entrer le premier numero
def calculator():
    num1 = int(input("Enter le premier numero : "))
    return num1
num1 = calculator()
#Creation du dictionnaire
operation ={"+":add,
            "-":subtract,
            "*":multiply,
            "/":divide}

#Boucle while qui permet l'execution automatique
while True :
    
#Boucle for pour impriemer les symboles
    for op in operation:
        print(f"{op} sont les operations qui existent")
#À l'intérieur de la boucle while, invitez l'utilisateur à sélectionner un symbole d'opération.
    op = input("Choisir l'operateur : ")
#Inviter l'utilisateur à entrer le deuxieme numero 
    num2 = int(input("Choisir un deuxieme numero : ")) 
#Utilisez le dictionnaire pour récupérer la fonction qui correspond 
#au symbole d'opération sélectionné et stockez-la dans une variable 'calculation_function'
    if op in operation:
        calculation_function = operation[op]
#Effectuez le calcul en appelant la « calculation_function » sur les deux nombres d'entrée et
#stockez le résultat dans une variable « réponse ».
        resultat = calculation_function(num1, num2)
#Imprimez l'équation et le résultat du calcul.        
        print(f"Résultat : {num1} {op} {num2} = {resultat}")
#Demandez à l'utilisateur s'il souhaite continuer à utiliser le résultat comme premier nombre pour d'autres calculs.
    should_continue = input("Voulez vous utiliser le dernier resulat pour continuer le calcul (O/N): ")
    if should_continue.upper() == "O":
        num1 = resultat
    else : 
        num1 = calculator()
    continuer = input("Voulez-vous continuer (O/N) ? ")
    if continuer.upper() != "O" :
        break


# In[ ]:




