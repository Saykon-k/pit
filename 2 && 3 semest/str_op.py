s = 'У лукоморья 123 дуб зеленый 456'
i = s.find('я')
print(i+1)
print (s.count('у'))
if s.isalpha():
     print(' ') 
else:
    print(s.upper())
if len(s)>4:
    print(s.lower())
print (s.replace(s[:1],'О'))
