import csv
table=[]
cal=[]

with open('donnees_2008.csv', newline="") as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    for row in reader:
        table.append(row)
    #print(table)
    for row in table :
        if row[6] == 'Auxerre':
            cal.append(row[9])


with open('donnees_2016.csv', newline="") as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    for row in reader:
        table.append(row)
    #print(table)
    for row in table :
        if row[6] == 'Auxerre':
            cal.append(row[9])
print("Le nombre de population a Auxerre en 2008 et 2016 :",cal[0]+cal[1],"de population.")
'''
with open('donnees_2021.csv', newline="") as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    for row in reader:
        table.append(row)
    #print(table)
    for row in table :
        if row[6] == 'Auxerre':
            cal.append(row[9])
print(cal)
'''