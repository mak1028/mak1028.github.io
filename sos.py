# -*- coding: cp1252 -*-


message = raw_input("WHat message would you like converted to Morse Code? ").upper()

print message

morse = {"A":".-", "N":"-.", "0":"-----","B":"-...", "O":"---", "1":".----","C":"-.-.", "P":".--.","2":"..---", 
	"D":"-..", "Q":"--.-", "3":"...--", "E":".", "R":".-.", "4":"....-", "F":"..-.", "S":"...", "5":".....", 
	"G":"--.", "T":"-", "6":"-....", "H":"....", "U":"..-", "7":"--...", "I":"..", "V":"...-", "8":"---..",
	"J":".---", "W":".--", "9":"----.", "K":"-.-", "X":"-..-", "L":".-..", "Y":"-.--", "M":"--", "Z":"--.."}
newMessage = ""
n=0
print 

for i in message:
    for x in morse:
        if i == x:
            newMessage += morse[x] + "   "
            
print newMessage
