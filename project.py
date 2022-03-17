
# from os import sep


# print("\n\n************Kalkulyator************\n\n")

# while True:
# 	try:
#         a=float(input("a-ni daxil edin: "))
#         op=input("operator-u daxil edin: ")
#         b=float(input("b-ni daxil edin: "))
#         if op=='+':
#             print("a+b={}".format(a+b))
#             break
#         elif op=='-':
#             print("a-b={}".format(a-b))
#             break
#         elif op=='*':
#             print("a*b={}".format(a*b))
#             break
#         elif op=='/':
#             print("a/b={}".format(a/b))
#             break
#         else:
#             print("zehmet olmasa bu emeliyyatlardan birini daxil edin: +,-,*,/ \n\n")
# 	except ValueError:
# 		print("a ve b eded olmalidir")


# print("\n\n")

# while True:
#     parol=input("Parolu daxil edin: ")
#     if len(parol)>=8 and len(parol)<=13:
#         print("Parolunuzun uzunlugu duzdur")
#         break
#     else:
#         print("Paroldaki simvollarin sayi 8-13 araliginda olmalidir!!!")



# import random
# print("3 cehdiniz var")
# eded_2 = random.randint(0, 10)
# ff=False

# for i in range(1,4):
#     eded_1 = int(input("0 ile 100 arasinda bir ede daxil edin: "))
    
#     if eded_1  == eded_2:
#         print("Siz dogru tapdiniz. Ededimiz {}-dir".format(eded_2))
#         ff=True
#     else:
#         print("Siz dogru tapmadiz..")
#     if ff==True:
#         break

# if ff==False:
#     print("Siz uduzduz.... Reqemimiz {} idi".format(eded_2))


# Sifre="Dia_K201"
# i=0
# while i<3:
#     print("\n{} haqqiniz var\n".format(3-i))
#     Sifre_1=input("Sifreni daxil edin: ")
#     if Sifre==Sifre_1:
#         print("\nSifre duzgundur\n")
#         break
#     else:
#         print("Sifre sehvdir\n")
#     i+=1


# while True:
#     try:
#         print("\n\n\nProgramdan cixmaq ucun x duymesine basin\n\n\n")
#         eded_1=input("Birinci ededi daxil edin: ")
#         if eded_1=='x':
#             break
#         eded_2=input("Ikinci ededi daxil edin: ")
#         if eded_2=='x':
#             break

#         eded_1=int(eded_1)
#         eded_2=int(eded_2)
#         print(eded_1/eded_2)

#     except ZeroDivisionError:
#         print("Sifira bolmek olmaz!!!")
#     except ValueError:
#         print("Sadece reqem daxil edin")



# try:
# 	eded_1 = int(input("1-ci ededi daxil edin:  "))
# 	eded_2 = int(input("2-ci ededi daxil edin:  "))
# 	print(eded_1 , "/", eded_2, "=", eded_1 / eded_2)
# except ValueError as xeta:
# 	print("Orginl xeta mesaji: ", xeta)

print("1","2","3",sep="-")