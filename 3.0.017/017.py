#!/usr/bin/env python
#Anagram check
import sys

def dic_compare(dic1,dic2):
    for letter in dic1:
        if (letter not in dic2):
            return False
        if (dic2[letter]!=dic1[letter]):
            return False
    return True

def text_to_dic(text):
    Line_dict={}
    for char in text.lower().strip():
        if (char in Line_dict):
            Line_dict[char]+=1
        else:
            Line_dict[char]=1
    return Line_dict  

def run(text1, text2):
    if(len(text1)!=len(text2)):
        print ('Text are not the same length!')
        return
    text1dic=text_to_dic(text1)
    text2dic=text_to_dic(text2)
    print (dic_compare(text1dic,text2dic))
    
    return

def main(args):
    if len(args)==3:
        run(args[1],args[2])
    else:
        print('Usage: 017.py text1 text2!')

if __name__ == "__main__":
    main(sys.argv)
