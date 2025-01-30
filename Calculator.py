#!/usr/bin/env python3
def add(x,y):
	return x+y

def substract(x,y):
	return x-y

def multiply(x,y):
	return x*y

def divide(x,y):
	if y==0:
		return"nie mozna dzielic przez zero"
	return x/y

def calculator():
	print("wybierz operacje:")
	print("1.dodawanie")
	print("2.odejmowanie")
	print("3.mnozenie")
	print("4.dzielenie")

choice = input("wprowadz numer operacji(od 1 do 4)")

num1 = float(input("wprowadz piersza liczbe:"))
num2 = float(input("wprowadz druga liczbe:"))

if choice == '1':
	print(f"{num1} + {num2} = {add(num1,nun2)}")
elif choice == '2':
	print(f"{num1} - {num2} = {substract(num1,num2)}")
elif choice == '3':
	print(f"{num1} * {num2} = {multiply(num1,num2)}")
elif choice == '4':
	print(f"{num1} / {num2} = {divide(num1,num2)}")
else:
	print("nieprawidłowy wybór! wybierz numer od 1 do 4.")
calculator()
