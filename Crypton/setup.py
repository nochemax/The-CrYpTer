import time
import sys
import os
from io import open
import threading

# Programador David soto noche
# Correo: Sotodelanoche@gmail.com
# Lenguaje Python3 scrispt 
# Fecha 19:04:2020:
# Nombre del programa : ZeUS
# Accion instalador de las paqueteria y librerias necesarias


def INstall():
	os.system('clear')
	print("\033[1;31;1m ")
	os.system('figlet -k -f usr/font/cosmike "   		Smp_A" && figlet -k -f usr/font/bulbhead " 						 		   		Zeuz"')
	print("			  		Black_Hack")                 	
	print("\033[1;37;1m ")
	while True:
		try:
			print("Actualizando Repositorios")
			os.system('apt-get update') 
			os.system('apt-get upgrade')
			os.system('clear')
			print("Procesando comprobacion de los sigientes programas: ")
			print("")
			print("python3 > v6")
			val = os.system('dpkg-query -l | grep python3.8 | wc -l') 
			if (val>6):	
				print("Espere un momento tenemos que actualizar Python3")
				os.system('apt-get install python3.8 ')
			else:
				
				print("Python3 ya Actualizado")
			print("") 
			print("Python-Tk")			
			val1 = os.system('dpkg-query -l | grep pytghon3-tk | wc -l')
			if (val1==0):
				print("Intalando modulos necesarios python3-Tk")
				os.system('apt-get install python3-tk')
			else:
				
				print("modulo instalado Python3-tK ya instalado")
			print("")			
			print("Python3-pip")			
			val2 = 	os.system('dpkg-query -l | grep pytghon3-pip | wc -l')
			if (val2==0):
				print("Intalando modulos necesarios python3-pip3")
				os.system('apt-get install python3-pip')
			else:
				
				print("modulo instalado Python3-pip3 ya instalado")
			print("")			
			print("Figlet")
			val3 = os.system('dpkg-query -l | grep figlet | wc -l')
			if (val3==0):
				print("Instalando Reposito Apt Figlet")
				os.system('apt-get install figlet')
			else:
				
				print("Reposito Apt Figlet ya instalado")
			print("")			
			print("Xclip")
			val4 = os.system('dpkg-query -l | grep xclip | wc -l')
			if (val4==0):
				print("Instalando Reposito Apt xclip")
				os.system('apt-get install xclip')
			else:
				
				print("Reposito Apt xclip ya instalado")
			print("")			
			print("Xsel")
			val5 = os.system('dpkg-query -l | grep xsel | wc -l')
			if (val5==0):
				print("Instalando Reposito Apt xsel")
				os.system('apt-get install xsel')
			else:
				
				print("Reposito Apt xsel ya instalado")		
			print("")			
			print("Zip")
			val6 = os.system('dpkg-query -l | grep zip | wc -l')
			if (val6==0):
				print("Instalando Reposito Apt Zip")
				os.system('apt-get install zip')
			else:
				
				print("Reposito Apt Zip ya instalado")
			print("")
			print("Instalando las Librerias python3")
			os.system('pip3 install -r requires.txt')

			break
		except TypeError:
			print("Ocurrio un horror durante la instalacion")			


INstall()
