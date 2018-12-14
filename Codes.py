import csv
import os

#ICD10 medical codes
Ref=[]
Data = []
index = []
alldata = []

a = 0
b = 0
c = 0
Alfred = 100

df = open('ChronicICD9Ref.csv')
reader = csv.reader(df)
for row in reader:
    Ref.append('ICD10-CM!'+(row[0]))

df.close()

print 'Batman'

df = open('problist.csv')
reader = csv.reader(df)
for row in reader:
    Data.append(row[3])
    alldata.append(row)

df.close()

print 'Robin'

a = 0
while (a<len(Ref)):
    while (b<len(Data)):
        #print Ref[a]
        #print Data[b]
        if Ref[a]==Data[b]:
            print 1
            index.append(b)
        b+=1
    b = 0
    if a==Alfred:
        print a
        Alfred=Alfred+100
    a+=1

print 'Batgirl'

with open('ChronicICD10.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    while c<len(index):
        HarleyQuinn = index[c]
        spamwriter.writerow(alldata[HarleyQuinn])
        c+=1

print 'ICD10 complete'

#ICD9 medical codes
Ref=[]
Data = []
index = []
alldata = []

a = 0
b = 0
c = 0
Alfred = 100

#opening the csv file
df = open('ChronicICD9Ref.csv')
reader = csv.reader(df)
for row in reader:
    Ref.append('ICD9CM!'+(row[0]))

df.close()

print 'Joker'

df = open('problist.csv')
reader = csv.reader(df)
for row in reader:
    Data.append(row[3])
    alldata.append(row)

df.close()

print 'Harley Quinn'

a = 0
while (a<len(Ref)):
    while (b<len(Data)):
        #print Ref[a]
        #print Data[b]
        if Ref[a]==Data[b]:
            print 1
            index.append(b)
        b+=1
    b = 0
    if a==Alfred:
        print a
        Alfred=Alfred+100
    a+=1

print 'Clayface'

with open('ChronicICD9.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    while c<len(index):
        HarleyQuinn = index[c]
        spamwriter.writerow(alldata[HarleyQuinn])
        c+=1

print 'ICD9 Complete'


#SNOMED medical codes
df = open('ChronicSNOMEDRef.csv')
reader = csv.reader(df)
for row in reader:
    Ref.append('SNOMED!'+(row[0]))

df.close()

print 'Bruce Wayne'

df = open('problist.csv')
reader = csv.reader(df)
for row in reader:
    Data.append(row[3])
    alldata.append(row)

df.close()

print 'Dick Grayson'

a = 0
while (a<len(Ref)):
    while (b<len(Data)):
        #print Ref[a]
        #print Data[b]
        if Ref[a]==Data[b]:
            print 1
            index.append(b)
        b+=1
    b = 0
    if a==Alfred:
        print a
        Alfred=Alfred+100
    a+=1

print 'Alfred Pennyworth'

with open('ChronicSNOMED.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    while c<len(index):
        HarleyQuinn = index[c]
        spamwriter.writerow(alldata[HarleyQuinn])
        c+=1
print 'SNOMED Complete'
