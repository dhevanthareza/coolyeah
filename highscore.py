# Dhevan Muhamad Anthareza - A11.2019.12293

scoreList = []
popped = []
while True:
  score = int(input("Masukan Score (input -1 untuk selesai input) = "))
  if(score < 0): 
    break
  while(len(scoreList) > 0 and scoreList[-1] < score):
    popped.append(scoreList.pop())
  if(len(scoreList) < 5):
    scoreList.append(score)
  while(len(popped) > 0):
    popVal = popped.pop()
    if(len(scoreList) < 5):
      scoreList.append(popVal)
print("5 score tertinggi = ",",".join(str(x) for x in scoreList))