ticket = input()
n1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
n2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
if n1 == n2:
  print("YES")
else:
  print("NO")