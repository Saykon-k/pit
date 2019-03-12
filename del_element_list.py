def f(x):
      if x == 'John' or x=='Paul':
          return x
      else:
          return 1
names = ['John', 'Paul', 'George', 'Ringo']
print(list(map(f,names)))
names = (list(map(f,names)))
for i in names:
      if i == 1:
           names.remove(i)
for i in names:
      if i == 1:
           names.remove(i)
print(names)
