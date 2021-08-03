'''Q2. 1. Input -
                 String -xyz
                 Integer- 4
          Output - 
                String - bcd

       2. Input
               String = pdh
               integer = 6
          Output
               String = vjn
'''
import string
def Character_Shift(wrd,n): #function to accept string and shift it n characters
    alpha=string.ascii_lowercase
    new_word=''
    for char in wrd:
        indx=alpha.index(char)
        indx=(indx+n)%26
        new_word=new_word+(alpha[indx])
    return new_word

word=input("Enter a String :")
shft=int(input("Enter no. of characters to be shifted :"))
print(Character_Shift(word,shft))
