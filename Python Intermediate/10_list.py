import csv
data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]
try:
    with open('testnew.csv','r')as file:
        f=file.read()
        for i in f:
            print(i)

except:
    print("File not found.Creating a new one.")
    with open('testnew.csv','w')as file:
        wri_obj=csv.writer(file)
        wri_obj.writerows(data)

finally:
    print("Exceuted Successfully!!!")
        
    
