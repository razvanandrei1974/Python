# '''
# #1. Declarati o lista cu elemente multitype
# #2. Declarati o lista goala
# #3. Accesati orice element din lista pe baza de index
# #4. Accesati pozitia unui element din lista pe baza functiei index()
# #5. Adaugati elemente in lista atat cu functia append() cat si cu functia insert(). Observati rezultatele
# #6. Stergeti elemente din lista atat cu functia pop() cat si cu functia remove(). Observati rezultatele
# #7. Numarati elementele dintr-o lista folosind functia len()
# #8. Numarati de cate ori apare un anumit element in lista folosind functia count()
# #9. Uniti doua liste folosind functia extend()
# #10. Sortati lista folosind functia sort()
# #11. Inversati continutul listei folosind functia reverse()
# #12. Stergeti toate elementele din lista folosind functia clear()
# '''
#
# #LISTE
# #1. Declarati o lista cu elemente multitype
lista = ["Florin", 2, 3.25, "Resita", True]
print(lista)
# #2. Declarati o lista goala
list_goala = []
#3. Accesati orice element din lista pe baza de index
list[3]
print(lista[3])
# #4. Accesati pozitia unui element din lista pe baza functiei index()
lista.index(3.25)
print(lista.index(3.25))
# #5. Adaugati elemente in lista atat cu functia append() cat si cu functia insert(). Observati rezultatele
lista.append("Restaurant")
lista.append(4.5)
print (lista)
lista.insert(2,25)
print(lista)
# #6. Stergeti elemente din lista atat cu functia pop() cat si cu functia remove(). Observati rezultatele
lista.pop()
print(lista)
lista.remove("Restaurant")
print(lista)
# #7. Numarati elementele dintr-o lista folosind functia len()
len(lista)
print(len(lista))
# #8. Numarati de cate ori apare un anumit element in lista folosind functia count()
print(lista.count(2))
# #9. Uniti doua liste folosind functia extend()
lista2 = ["Mere","Ananas","Kiwi","Portocale","Banane"]
lista.extend(lista2)
print(lista)
# #10. Sortati lista folosind functia sort()
# lista.sort("Florin")
# print(lista)
# #11. Inversati continutul listei folosind functia reverse()
lista.reverse()
print(lista)
# #12. Stergeti toate elementele din lista folosind functia clear()
lista.clear()
print(lista)
#
# '''
# #1. Declarati un tuplu
# #2. Declarati un tuplu gol
# #3. Accesati orice element din tuplu pe baza de index
# #4. Accesati pozitia unui element din lista pe baza functiei index()
# #5. Folositi functia count() pentru a numara de cate ori apare un element in tuplu
# #6. Folositi functia index() pentru a verifica pozitia la care se afla un anumit element in tuplu
# #7. Incercati sa modificati un element din tuplu si observati rezultatele
#
# '''
# #1
persoana=("Customer ID", "Type Account", "Initial Deposit")
print(type(persoana))
# #2
tuplu_gol=()
print(type(tuplu_gol))
# #3
print(persoana[1])
# #4
print(persoana.index("Type Account"))
# #5
print(persoana.count("Initial Deposit"))
# #6
element_cautat= "Type Account"
pozitie=element_cautat.index("Type Account")
print(f'Campul {element_cautat} se afla la pozitia {pozitie} in tuplu')
# #7 Tuplurile sunt imutabile nu se pot modifica
#
#
# '''
# #1. Declarati un set
# #2. Declarati un set gol
# #3. Adaugati un element nou in set folosind functia add()
# #4. Stergeti un element din set folosind functia pop() si respectiv functia remove(). Observati rezultatele
# #5. Verificati daca un set este o subdiviziune a unui alt set (subset)
# #6. Verificati daca un set contine toate elementele dintr-un alt set + alte elemente (superset)
# #7. Verificati care sunt elementele comune intre doua seturi (intersection)
# #8. Verificati diferenta intre doua seturi cu functia difference()
# #9. Stergeti toate elementele dintr-un set folosind functia clear()
#
# '''
# #1
fund_transfer={"Payers account no", "Payees account no", 500, "Description"}
# #2
set_gol={}
# #3
fund_transfer.add("Account Type")
print(set)
# #4
fund_transfer.pop() #se sterge aleatoriu
print(fund_transfer)
fund_transfer.remove("Account Type") #stergem elementul 2 din set
print(fund_transfer)
fund_transfer.add("payers account no")
#5


#6


#7


#8
#Diferenta va contine toate elementele din set1_diferenta care nu sunt prezente in set2
Account_list_1={"Marius", "Alin", "Petru", 250}
Account_list_2={"Petru", "Carmen", "Alin", 285, 250}
#
diferenta=Account_list_1.difference(Account_list_2)
print(f'Diferenta dintre Account List 1 si Account List 2 este {diferenta}')
# #9
Account_list_1.clear()
print(Account_list_1)

'''
#1. Declarati un dictionar
#2. Declarati un dictionar gol
#3. Adaugati un element nou in dictionar folosind functia update() si respectiv pe baza de cheie
#4. Extrageti un element din dictionar folosind metoda get() si respectiv pe baza de cheie
#5. Stergeti un element din dictionar folosind functia pop() si respectiv functia popitem(). Observati rezultatele
#6. Extrageti pe rand toate cheile, apoi toate valorile, si apoi toate item-urile din dictionar
#7. Stergeti toate valorile din dictionar folosind metoda clear()
'''
from typing import Dict

#1
Menu={
        "New Customer": "Ungar Razvan",
        "Gender Male": True,
        "Gender Female": False,
        "Date of birth": "27.08.1974",
        "Adress": "Strada Ciocarliei, 5",
        "Mobile Number": 774903493
}
print(Menu)
# #2
# #3
Menu.update({"Email":"razvan.ungar@gmail.com"})

Menu["PIN"]=1234556
print(Menu)
# #4
x = Menu.get("Password", "123456789")
print(x)
#5
Menu.pop('Gender Female') # am sterg cu ajutorul functiei pop pe baza de key
print(Menu)
Menu.popitem() #Mi-a sters ultimul key din dicitonar
print(Menu)
# #6
# ????
# #7
Menu.clear()
print(Menu)