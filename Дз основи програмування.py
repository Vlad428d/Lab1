helloEng = "Hello, World!"
helloUkr = "Привіт світ!"
b = 2026
print(helloEng, end=' '); print(helloUkr)
name = input("Як тебе звати? :")
print(f"Привіт, {name}!")
print(f"Рік {b} був чудовим роком!")
print(f"типи данних: {type(helloEng)}, {type(helloUkr)}, {type(b)}")

print("калькулятор")
n1 = int(input("Введіть перше число: "))
o = input("Введіть операцію (+, -, *, /, %, **): ")
n2 = int(input("Введіть друге число: "))
if o == "+":
    r = n1 + n2
elif o == "-":
    r = n1 - n2 
elif o == "*":
    r = n1 * n2
elif o == "%":
    r = n1 % n2
elif o == "**":
    r = n1 ** n2    
elif o == "/":     
    if n2 != 0:
        r = n1 / n2
    else:
        r = "Ділення на нуль неможливе!"
else:
    r = "Невідома операція!"
print(f"Результат: {r}") 
print(f"типи данних: {type(n1)}, {type(o)}, {type(n2)}, {type(r)}")                           