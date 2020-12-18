from collections import deque
import math
def divQueue(queue):
  antrianPertama = queue
  antrianKedua = deque([])
  for i in range(math.floor(len(antrianPertama)/2)):
    antrianKedua.append(antrianPertama.pop())
  antrianKedua.reverse()
  print(antrianPertama)
  print(antrianKedua)
divQueue(deque([4,5,6,7,8,9,10]))