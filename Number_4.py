import re


def Grosspay(Hours,rate):
   Pay=Hours*rate
   return Pay

Hours=int(input("Enter your Working Hours!: "))
rate=float(input("Enter your Rate of payment: "))
print("GrossPay: ", Grosspay(Hours,rate))
