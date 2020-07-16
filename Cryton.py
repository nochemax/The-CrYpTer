#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ LIBRERIAS $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
import tkinter as tk
from tkinter import *
from tkinter import messagebox as MessageBox
import time
import sys
import os
#import subprocess 
from subprocess import Popen, PIPE, STDOUT
from io import open
import threading

# Programador David soto noche
# Correo: Sotodelanoche@gmail.com
# Lenguaje Python3 scrispt 
# Fecha 19:04:2020:
# Nombre del programa : ZeUS
# Accion encriptador de informacion en diversas capas o como se econoce encriptado onion

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ PRESENTACION TERMINAL $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
os.system('clear')
print("\033[1;31;1m ")
os.system('figlet -k -f usr/font/cosmike "   		Smp_A" && figlet -k -f usr/font/bulbhead " 						 		   		Zeuz"')
print("			  		Black_Hack")                 	
print("\033[1;37;1m ")
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ FUNCIONES PRINCIPALES $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ IMAGEN $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Codificacion Imagen ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def file_format_jpg():
	global JPG
	JPG=IntVar()
	JPG=(jpg.get())
	print(JPG)
	return JPG

def file_format_bmp():
	global BMP
	BMP=IntVar()
	BMP=(bmp.get())
	print(BMP)
	return BMP

def file_format_png():
	global PNG
	PNG=IntVar()
	PNG=(png.get())
	print(PNG)
	return PNG	

def Code_IMG():
	JPG=(file_format_jpg())
	BMP=(file_format_bmp())
	PNG=(file_format_png())												
	input_image=(File_IMG.get())
	i=threading.Thread(target=code, args=(input_image,JPG,BMP,PNG,))
	i.start()

def code(input_image,JPG,BMP,PNG, **datos):
	while True:
		try:
			extension=""
			if (JPG==1):
				extension="jpg"
			if (BMP==1):
				extension="bmp"
			if (PNG==1):
				extension="png"
			print("procesando....")
			os.system('usr/stegolsb steglsb -a -h -i Input_IMG/'+input_image+' -s Output/file.zip -o Output/IMG/final.'+extension+' -n 2 -c 9')
			time.sleep(1)
			os.system('rm -f Output/file.zip')
			print("[#########################] 100%")
			break
		except TypeError:
			MessageBox.showerror("Error", "Ha ocurrido un error inesperado.")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Descodificacios Imagen ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def Des_Code_IMG():
	input_image=(File_IMG.get())
	i=threading.Thread(target=descode, args=(input_image,))
	i.start()

def descode(input_image, **datos):
	while True:
		try:
			print("procesando....")
			os.system('usr/stegolsb steglsb -r -i Input_IMG/'+input_image+' Output/output_file.zip -n 2')
			break
		except TypeError:
			MessageBox.showerror("Error", "Ha ocurrido un error inesperado.")

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ SOND CODE WAV $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Codificacion Sound ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def Code_WAV():
	input_sound=(File_wav.get())
	input_text=(File_txt.get())
	i=threading.Thread(target=codewav, args=(input_sound,input_text,))
	i.start()

def codewav(input_sound,input_text, **datos):
	while True:
		try:
			print("procesando....")
			os.system('usr/stegolsb wavsteg -h -i Input_WAV/'+input_sound+' -s Input_TXT/'+input_text+' -o Output/WAV/Sound_Code.Wav -n 2')
			print("[#########################] 100%")
			break
		except TypeError:
			MessageBox.showerror("Error", "Ha ocurrido un error inesperado.")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Descodificacios sound ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def Des_Code_WAV():
	input_sound=(File_wav.get())
	input_text=(File_txt.get())
	i=threading.Thread(target=descodewav, args=(input_sound,input_text,))
	i.start()

def descodewav(input_sound,input_text, **datos):
	while True:
		try:
			print("procesando....")
			os.system('usr/stegolsb wavsteg -r -i Input_WAV/'+input_sound+' -o Output/Mensaje.txt -n 2 -b 1000')
			break
		except TypeError:
			MessageBox.showerror("Error", "Ha ocurrido un error inesperado.")

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Creation Cifrado $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Operaciones de crifrado principal ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def generate_sha512():
	global SH1
	SH1=IntVar()
	SH1=(Sha512.get())
	print(SH1)
	return SH1

def generate_GPG():
	global G1G
	G1G=IntVar()
	G1G=(GpG.get())
	print(G1G)
	return G1G
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Operaciones de crifrado principal ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def generate_zip():
	input_text=(File_txt.get())
	input_image=(File_IMG.get())
	SH1=(generate_sha512())
	G1G=(generate_GPG())
	i=threading.Thread(target=codezip, args=(input_text,SH1,G1G,input_image,))
	i.start()

def codezip(input_text,SH1,G1G,input_image, **datos):
	while True:
		try:
			if (SH1==1):
				print("[#                             ] 1%")
				os.system('sha512sum Input_IMG/'+input_image+' ~ >> Output/Keys/key1.txt') # crea txt donde mete los sha512 para crear el de 1024
				time.sleep(1)
				os.system('sha512sum Input_TXT/'+input_text+' ~ >> Output/Keys/key1.txt')
				archivo_key=(open("Output/Keys/key1.txt","r").readline())
				key1_512=(str(archivo_key[0:129]))
				key2_512=(str(archivo_key[1:129]))
				KEY_MASTER=(key1_512+key2_512)
				KEY_MASTER=(KEY_MASTER.replace(' ', ''))
				print(" **** procesando sha1024 **** ") 									# procesa el sha1024
				print(KEY_MASTER)
				print("[#########                     ] 25%")
				KEY_MASTER_CODE=KEY_MASTER.replace('1', '8').replace('2', '6').replace('3', '4').replace('4', '2').replace('5', '1').replace('6', '0').replace('7', '3').replace('8', '9').replace('9', '5').replace('0', '7').replace('a', 'D').replace('b', 'C').replace('c', 'B').replace('d', 'A')
				time.sleep(2)
				print(":::: Combinacion de cambio de caracteres realizada ::::") 							#procesa el sha1024 combinado cambiando caracteres
				print(KEY_MASTER_CODE)
				print("[################              ] 50%")		
				time.sleep(1)
				file1 = open("Output/Keys/key2.txt","w")
				file1.write(KEY_MASTER_CODE+ '\n')
				file1.close()
				time.sleep(1)
				os.system('zip --password '+KEY_MASTER_CODE+' Output/file.zip Input_TXT/'+input_text) # crea solo el zip sin GPG
				print(":::: Compresion terminada y claves generadas ::::")
				time.sleep(1)
				if (G1G==0):
					print("[######################## ] 99%")
					print ("Danger Seguridad media key ZIP Generados")

			if (G1G==1):
				KEY_MASTER_GPG=(str(KEY_MASTER_CODE[1:168])) 		# genera key para GPG
				file2 = open("Output/Keys/key3.txt","w")
				file2.write(KEY_MASTER_GPG)
				file2.close()
				print("Clave gpg")
				print(KEY_MASTER_GPG)
				print("[#########################     ] 75%")
				os.system('cat Output/Keys/key3.txt | xsel -ib')   	# copia la clave al portapapeles
				time.sleep(1)
				print ("Introduzca key GpG = Ctrl+V") 
				os.system('gpg -c Output/file.zip')					# genera gpg 						
				os.system('rm -f Output/file.zip')
				os.system('mv -f -i Output/file.zip.gpg Output/file.zip')
				print("[######################## ] 99%")
				print ("Danger Seguridad maxima")
			
			if (SH1==0 and G1G==0):
				os.system('zip -r --encrypt file.zip '+input_text)
				print ("Danger Seguridad minima Introduzca keyuser key ZIP")
			break
		except TypeError:
			MessageBox.showerror("Error", "Ha ocurrido un error inesperado.")

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ INFO program $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def Info():
	os.system('clear')
	print("\033[1;31;1m ")
	os.system('figlet -k -f usr/font/cosmike "   		Smp_A" && figlet -k -f usr/font/bulbhead " 						 		   		Zeuz"')
	print("			  		Black_Hack")                 	
	print("\033[1;37;1m ")
	MessageBox.showinfo(title="Info Creation", message="creador Smp_A \n fecha 15/04/2020 \n name program Zeuz")
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Loggin Key $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def loggin():
	if key.get()=='c':
		interfaz()
	else:
		MessageBox.showerror("Error", "Password incorrecto.")

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ INTERFAZ PRINCIPAL $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Config Win ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def interfaz():

	global File_IMG
	global File_wav
	global File_txt
	global GpG
	global Sha512
	global jpg
	global bmp
	global png
	jpg=IntVar()
	bmp=IntVar()
	png=IntVar()
	Sha512=IntVar()
	GpG=IntVar()

	win_loggin.withdraw() 										  
	interfaz=tk.Toplevel()
	interfaz.title("Smp_A")
	ox,oy=interfaz.winfo_screenwidth()/2,interfaz.winfo_screenheight()/2
	interfaz.geometry("=500x250+%d+%d" % (ox -100 ,oy -100))
	interfaz.columnconfigure(0, weight=1)
	interfaz.rowconfigure(0, weight=1)
	pht2= PhotoImage(file="usr/fondo/nuevofondo.gif")
	lblImagen2=Label(interfaz,image=pht2).place(x=0,y=0)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CAPA INDICADORES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	menu = Menu(interfaz)
	interfaz.config(menu=menu)
	powermenu = Menu(menu, tearoff=0)
	Help = Menu(menu, tearoff=0)
	menu.add_cascade(label="Power", menu=powermenu)
	menu.add_cascade(label="Help", menu=Help)
	powermenu.add_command(label="Exit", command=cerrarventana)
	Help.add_command(label="Creation", command=Info)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ INTRODUCCION DE DATOS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	File_IMG = tk.Entry(interfaz)										
	File_IMG.place(x=180,y=50, width=120, height=25)
	
	File_wav = tk.Entry(interfaz)										
	File_wav.place(x=180,y=120, width=120, height=25)

	File_txt = tk.Entry(interfaz)										
	File_txt.place(x=180,y=185, width=120, height=25)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ BOTONERA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	bttn1 = tk.Button(interfaz, text='Code IMG', command=Code_IMG)
	bttn2 = tk.Button(interfaz, text='Des Code IMG', command=Des_Code_IMG)
	bttn3 = tk.Button(interfaz, text='Code WAV', command=Code_WAV)
	bttn4 = tk.Button(interfaz, text='Des Code WAV', command=Des_Code_WAV)
	bttn5 = tk.Button(interfaz, text='FIle Zip', command=generate_zip)

	bttn1.place(x=100,y=80, width=100, height=20)
	bttn2.place(x=270,y=80, width=100, height=20)
	bttn3.place(x=100,y=150, width=100, height=20)
	bttn4.place(x=270,y=150, width=100, height=20)
	bttn5.place(x=310,y=189, width=100, height=20)
	bttn_list=[bttn1,bttn2,bttn3,bttn4,bttn5]
	
	for i in range(len(bttn_list)):
		interfaz.columnconfigure(i, weight=1)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Marcador casilla ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	selec1=tk.Checkbutton(interfaz, text="Sha512sum", variable=Sha512, onvalue=1, offvalue=0, command=generate_sha512)
	selec1.place(x=70,y=180, width=100, height=20)
	selec2=tk.Checkbutton(interfaz, text="SimetcGPG", variable=GpG, onvalue=1, offvalue=0, command=generate_GPG)
	selec2.place(x=70,y=195, width=100, height=20)

	selec3=tk.Checkbutton(interfaz, text="JPG", variable=jpg, onvalue=1, offvalue=0, command=file_format_jpg)
	selec3.place(x=100,y=25, width=60, height=20)
	selec4=tk.Checkbutton(interfaz, text="BMP", variable=bmp, onvalue=1, offvalue=0, command=file_format_bmp)
	selec4.place(x=210,y=25, width=60, height=20)
	selec5=tk.Checkbutton(interfaz, text="PNG", variable=png, onvalue=1, offvalue=0, command=file_format_png)
	selec5.place(x=310,y=25, width=60, height=20)

	interfaz.mainloop()
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Cambio de ventana loggin principal $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def cerrarventana():												
	win_loggin.destroy()
	interfaz.destroy()
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ VENTANA LOGGIN $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

win_loggin=tk.Tk()												    	
win_loggin.title("Smp_A")
ox,oy=win_loggin.winfo_screenwidth()/2,win_loggin.winfo_screenheight()/2
win_loggin.geometry("=300x200+%d+%d" % (ox-150,oy-120))

pht1= PhotoImage(file="usr/fondo/loging.gif") 				
lblImagen1=Label(win_loggin,image=pht1).place(x=0,y=0)

key=tk.Entry(win_loggin, show="*")
key.pack(padx=5, pady=5)
win_loggin.bind('<Return>', lambda event=None: bttn.invoke())
bttn=tk.Button(win_loggin, text="validar Password", fg="snow", comman=loggin)
bttn.pack()

win_loggin.mainloop()
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&