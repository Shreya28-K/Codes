dictm={
'Artist':'The Starry Night',
'Peroid':'Vincent van Gogh',
'Date':'1888'
}
print("Content in Dictionary")
print(dictm.items())
print('\n')

print("Keys :")
print(dictm.keys())
print('\n')

print("Values  : ")
print(dictm.values())
print('\n')

dictm['Date']=1889

print("Content in Dictionary after the update.")
print(dictm.items())
