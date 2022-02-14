import pandas as pd
import time

start_time = time.time()

# DataBaseMadre
dbm = pd.read_excel('InvH.xlsx', 0)

# DataBaseHija
dbh = pd.read_excel('Filtro0.xlsx', 0)

# NuevaDataBase
nDb = pd.read_excel('pruebaxl.xlsx', 0)

j = 0

'''
#Barrido Madre
for i in range(len(dbm["a"])):
    #BarridoHija
    for k in range(len(dbh["a"])):
        #ComparadorCodigoMadreCodigoHija
        if dbm["a"].values[i] == dbh["a"].values[k]:
            j = j + 1
            nDb.loc[j] = dbm.loc[i]
            dbm.loc[i] = None
'''


#Barrido Madre Existencias
for i in range(len(dbm["Clave"])):
    #Barrido Hija Existencias
    for k in range(len(dbh["Clave"])):
        #Comparador de renglones/productos
        if dbm["Clave"].values[i] == dbh["Clave"].values[k]:
            dbh.iat[k,3] = dbm.iat[i,3]


#Outputs
#nDb.to_excel("Filtro0.xlsx")
dbh.to_excel("ConExis.xlsx", index=False)
#dbm.to_excel("InvMadreV0.xlsx", index=False)

print("time elapsed: {:.2f}s".format(time.time() - start_time))

'''
#Borrar espacios vacios

# NuevaDataBaseMadre
nDbM = pd.read_excel('InvMV0.xlsx', 0)

for i in range(len(nDbM["b"])):

    if pd.isnull(nDbM.loc[i][2]):
        nDbM.drop(i, axis=0, inplace=True)

nDbM.to_excel("InvMadreF0.xlsx", index=False)


'''