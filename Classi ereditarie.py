from re import I, U, X


class basic:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printnome(self):
        print(self.firstname, self.lastname)

class intermediate(basic):
    def __init__(self, fname, lname, cod):
        basic.__init__(self, fname, lname)
        self.codicecliente = cod
    def printnome(self):
        print(self.firstname, self.lastname, self.codicecliente)

class premium(intermediate):
    def __init__(self, fname, lname, cod, sco):
        intermediate.__init__(self, fname, lname, cod)
        self.score = sco
    def printnome(self):
        print(self.firstname, self.lastname, self.codicecliente, self.score)

ListaBasic = []
ListaIntermediate = []
ListaPremium = []

i = 1
while i < 3:

 tipoprofilo = input("seleziona profilo")
 if tipoprofilo == "basic":
    fname = input ("inserire il nome")
    lname = input ("inserire cognome")
    x= basic(fname,lname)
    x.printnome()
    ListaBasic.append(x.firstname)
    ListaBasic.append(x.lastname)
    print (ListaBasic)
    ContBasic=len(ListaBasic)/2
    print(ContBasic)

 elif tipoprofilo == "intermediate":
    fname = input ("inserire il nome")
    lname = input ("inserire cognome")
    cod = input ("inserire codice utente")
    y = intermediate(fname,lname,cod)
    y.printnome()
    ListaIntermediate.append(y.firstname)
    ListaIntermediate.append(y.lastname)
    ListaIntermediate.append(y.codicecliente)
    print (ListaIntermediate)
    ContIntermediate=len(ListaIntermediate)/3
    print(ContIntermediate)

 elif tipoprofilo == "premium":
    fname = input ("inserire il nome")
    lname = input ("inserire cognome")
    cod = input ("inserire codice utente")
    sco = input ("inserire il proprio punteggio")
    z = premium(fname,lname,cod,sco)
    z.printnome()
    ListaPremium.append(z.firstname)
    ListaPremium.append(z.lastname)
    ListaPremium.append(z.codicecliente)
    ListaPremium.append(z.score)
    print (ListaPremium)
    ContPremium=len(ListaPremium)/4
    print(ContPremium)

i = i + 1
print(i)