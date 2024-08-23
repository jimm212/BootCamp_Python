#Imprimir los números primos del 1 al 100

for i in range(2,101):
#for i in range(101):
   # if i==0 or i==1:
   #     continue
  #  elif i==2:
   #     print(i)        
  #  else:
        x=False
        for j in range(i):
            if j==0 or j==1:
                continue     
            else:
                k=i%j
                if k==0:
                    x=True
                    break
        if x==False:
            print("Aqui:",i)