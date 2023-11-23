# 1.	Calculare pret discount
# Dacă un client are peste 65 de ani, atunci i se va oferi o reducere de 15%.
# În caz contrar, dacă clientul nu are peste 65 de ani, dacă persoana călătorește cu cel puțin un copil va avea o reducere de 10%
# Atat pentru seniori cat si pentru non- seniori se va aplica o reducere suplimentara de 10% daca vor calatori in timpul iernii.
# De asemenea, atât pentru seniori, cât și pentru non seniori se va aplica o taxă de lux de 3% dacă vor călători în clasa I (în orice sezon) sau 1% taxă de gestiune în caz contrar.
###

age = 72

if ((age >= 65)):
    print("Celor cu varsta de minim 65 de ani li se va oferi o reducere de 15% ")
else:
    print("Nu se acorda reducere")
decizie_discount = "Celor cu varsta de minim 65 de ani li se va oferi o reducere de 15% "
VALOARE_DISCOUNT = print(decizie_discount[64:68])

discount = 15
Discount_oferit = discount
print("Discount-ul oferit este de {:.2f}%".format(Discount_oferit))

age < 65
insotit = "De un copil"
if age < 65 :
    print("Nu se va acorda reducerea de 10%")
elif insotit == "De un copil" :
    print("Atat seniorilor cat si non-seniorilor li se va oferi o reducere de 10% daca sunt insotiti de un copil")
else:
    print("Nu se acorda reducere ")
decizie_discount = "Atat seniorilor cat si non-seniorilor li se va oferi o reducere de 10% daca sunt insotiti de un copil"
print(decizie_discount[67:70])

discount = 10
Discount_oferit = discount
print("Discount-ul oferit este de {:.2f}%".format(Discount_oferit))
#
age < 65
anotimp = "iarna"
if age < 65 :
    print("Nu se va acorda reducerea de 10%")
elif anotimp == "toamna" :
    print("Atat seniorilor cat si non-seniorilor li se va oferi o reducere de 10% daca calatoresc iarna")
else:
    print("Nu se acorda reducere ")
decizie_discount = "Atat seniorilor cat si non-seniorilor li se va oferi o reducere de 10% daca calatoresc iarna"
print(decizie_discount[67:70])
Discount = decizie_discount[67:70]
discount = 10
Discount_oferit = discount
print("Discount-ul oferit este de {:.2f}%".format(Discount_oferit))

age < 65
clasa_tren  = "Clasa I"

if age < 65 :
    print("Nu se va acorda reducerea de 10%")
elif clasa_tren == "Clasa I" :
    print("Atat seniorilor cat si non-seniorilor li se va calcula o taxa de lux de 3% daca circula la Clasa I")
else:
    print("Nu se calculeaza taxa de lux ")

taxa_de_lux = 3
Taxa_de_incasat = taxa_de_lux
print("Taxa de lux pe care trebuie sa o plateasca este de {:.2f}%".format(Taxa_de_incasat))