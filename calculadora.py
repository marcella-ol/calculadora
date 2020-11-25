# -*- coding: utf-8 -*-
"""
Calculadora
Autor: Marcella Oliverio
Função: fazer contas: soma, divisão, multiplicação, subtração, exponenciação e módulo.
""" 

print("----- CALCULADORA v2.0 -----")

sair = False

while sair == False:

	num1 = input("Digite o primeiro número: ")
	num1 = int(num1)
	operador = input("Digite o operador: ")
	num2 = input("Digite o segundo numero: ")
	num2 = int(num2)

	# + soma
	if operador == "+":
		operacao = num2 + num2

	# - subtração
	if operador == "-":
		operacao = num1 - num2

	# / divisão
	if operador == "/":
		operacao = num1 / num2

	# * multiplicação
	if operador == "*":
		operacao = num1 * num2

	# ** exponenciação 
	if operador == "**":
		operacao = num1 ** num2

	# % módulo
	if operador == "%":
		operacao = num1 % num2

	print("Resultado:")
	print(operacao)

	teste = input("Deseja sair (n/s): ")
	if teste == "s":
		sair = True