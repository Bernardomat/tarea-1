num1=int(input("ingrese un número: "));
num2=int(input("ingrese otro numero: "));
num3=int(input("ingrese otro numero: "));
if num1>num2 and num1>num3:
    mensaje="el numero mas grande es: ",num1;
elif num2>num1 and num2>num3:
    mensaje="el numero mas grande es: ",num2;
else:
    mensaje="el numero mas grande es: ", num3;
print(mensaje)