from tkinter import Variable
from typing import List
from unicodedata import name


# Esercizio delle 10

class Anagrafica ():
     parametri = []
     nome = "x"
     cognome = "y"
     eta = 34 
     professione = "z"

Operatore = Anagrafica

Operatore.nome = input("il tuo nome?")
if[type(Operatore.nome) == str]:
 Operatore.parametri.append(Operatore.nome)

Operatore.cognome = input("cognome?")
if[type(Operatore.cognome) == str]:
 Operatore.parametri.append(Operatore.cognome)

Operatore.eta = input("eta?")
if[type(int(Operatore.eta))]:
 Operatore.parametri.append(Operatore.eta)

Operatore.professione = input("professione?")
if[type(Operatore.professione) == str]:
 Operatore.parametri.append(Operatore.professione)

print(Operatore.parametri)