rows = int(input("enter how many rows:"))
cols = int(input("enter how many colomns:"))
matrix1 = []
matrix2 = []
summatrix = []
submatrix = []

def fninput():
    for i in range(0,rows):
      row = []
      for j in range(0,cols):
          user_input = int(input("enter row:"+str(i+1)+"colomn:"+str(j+1)+"\n"))
          row.append(user_input)
          matrix1.append(row)

    for i in range(0,rows):
      row = []
      for j in range(0,cols):
          user_input = int(input("enter row:"+str(i+1)+"colomn:"+str(j+1)+"\n"))
          row.append(user_input)
          matrix2.append(row)
def fnsum():
    for i in range(0,rows):
          row = []
          for j in range(0,cols):
              sum = matrix1[i][j] + matrix2[i][j]
              row.append(sum)
              summatrix.append(row)
    for i in range(0,rows):
        for j in range(0,cols):
            print(summatrix[i][j], end=" ")
        print()
def fnsub():
    for i in range(0,rows):
          row = []
          for j in range(0,cols):
              sum = matrix1[i][j] - matrix2[i][j]
              row.append(sum)
              submatrix.append(row)
    for i in range(0,rows):
        for j in range(0,cols):
            print(submatrix[i][j], end=" ")
        print()
want_to_do = int(input("for addition enter:1      for subtraction enter:2\n"))
while True:
    if want_to_do == 1:
        fninput()
        fnsum()
        break
    elif want_to_do == 2:
        fninput()
        fnsub()
        break
    else:
        print("invalid input!!! enter again")
        want_to_do = int(input("for addition enter:1      for subtraction enter:2\n"))
