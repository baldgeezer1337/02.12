import sqlite3 as db 

with db.connect('noma.db') as con:
  cur = con.cursor()
  cur.execute(""" SELECT  Nomnieks.vards, Nomnieks.uzvards,Produkts.nomas_cena_diena, Noma.beig_datums
              FROM Nomnieks
              INNER JOIN Noma ON Noma.id_nomnieks = Nomnieks.id_nomnieks
              INNER JOIN Produkts ON  Noma.id_produkts = Produkts.id_produkts
              WHERE Nomnieks.tel_nr = '26543219' 
              """)
  nomniek = cur.fetchall()

print("Izdrukā datumus, kuros klientam ar telefona nr '26543219' jaatdot produkti un cik par tiem dienā jāmaksā:\n")
sum=0
for rinda in nomniek:
  print (rinda)
  sum = sum + int(rinda[2])
print ('\nPar iznomātām precēm dienā jāsamaksā ', sum )

