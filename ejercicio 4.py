num1=int(input("ingrese un número: "));
num2=int(input("ingrese otro numero: "));
num3=int(input("ingrese otro numero: "));
suma=num1+num2+num3;
promedio=suma//3
if promedio%2==0:
    mensaje=promedio,"el promedio es par"
else:
    mensaje=promedio,"el promedio es impar"
print(mensaje)
