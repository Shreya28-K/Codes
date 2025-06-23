from functools import reduce
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.8), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]
def filter_max(playlist):
  return playlist[1]>5.00 
maxs=list(filter(filter_max,playlist))
print("The songs that are longer than 5 minutes is = ",maxs)

def map_dura(playlist):
  d=playlist[1]
  m=int(d)
  s=(d-m)*100
  return m*60+round(s)

time=list(map(map_dura,playlist))
print(time)

def reduce_t(x,y):
  return x+y
print(reduce(reduce_t,time))
    S