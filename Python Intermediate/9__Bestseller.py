import csv
def openfilecsv(file):
    with open(file,'r',encoding='utf-8') as f:
        readobj=csv.reader(f)
        l=list(readobj)

        for i in l:
            print(i)
        head=l[0]
        sales=head.index('sales in millions') # returns index of sales in millons
        print(sales)
        maxs=0
    
        for rows in l[1:]:
            if maxs<float(rows[sales]):
                maxs=float(rows[sales])

        print("Max sales book = " , maxs)

    with open('output.csv','w',newline='') as file:
        data=[
            [1 ,'Shree',3],
            [2,'Shreya',21]
             ]
        writer_obj=csv.writer(file)
        writer_obj.writerows(data)
            


openfilecsv('Bestseller.csv')
