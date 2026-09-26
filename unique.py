def abv(b):
  a = []
  for i in b:
    if not(i in a):
      a.append(i)
  print(len(a))

abv("aabccd")
