# -*- coding: utf-8 -*-
"""sheet 3 -Edit

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bq3VAmIuao158oamTZK_iyUj-34MrACv

1- Write a python program that reads a file and print the number of plandromic words that it
contains.
"""

with open("Alaa.txt","r",encoding="UTF-8") as file:
  lines= file.readlines()
  for line in lines:
    words=line.strip().split(" ")
    for word in words:
      word.strip().split(" ")
      if word==word[::-1]:
        print("this word is plandromic",word)
      else:
         pass

"""2- Write a program that prompts the user to enter a text filename and displays the number of vowels and consonants in the file.


"""

file_name= input("please enter yor file name")
with open (file_name,"r",encoding="UTF-8") as file:
  
  vowels = set("A E I O U a e i o u")
  constant = set("b c d f g h j k l m n p q r s t v w x y z B C D F G H J K L M N P Q R S T V W X Y Z")
  count_v=0
  count_constant=0
  for line in lines:
    words= line.strip().split(" ")
    no_of_words=len(word)
    for word in words:
      letters= word.strip().split(" ")
      no_of_letters=len(letters) 
      for letter in word :
         if letter in vowels:
            count_v+=1
         else:
           count_constant+=1
print("number of vowels is",count_v,"number of constant",count_constant)

import collections
vowels = set("A E I O U a e i o u")
constant = set("b c d f g h j k l m n p q r s t v w x y z B C D F G H J K L M N P Q R S T V W X Y Z")
file_name= input("please enter yor file name")
with open (file_name,"r",encoding="UTF-8") as file:
 
  c= collections.Counter(file.read())
  count_vowels= sum( c[k]for k in c if k in vowels)
  count_constant= sum( c[k]for k in c if k in constant)
  print(" the value of vowels is " ,count_vowels,"the value of constant is " ,count_constant)

""" 3- Write a program that prompts the user to enter a text file, reads words from the
file, and displays all the non-duplicate words.
"""

from ast import keyword
file_name=input("please enter name")
with open (file_name,"r",encoding="UTF-8") as file_1:
 no_of_letters =0
 occurrence={}
 lines= file_1.readlines()
 for line in lines:
    words= line.strip().split(" ")
    no_of_words=len(words)
    for word in words:
            occurrence[word]=occurrence[word]+1 if  word in occurrence else 1

for key,value in occurrence.items(): 
      if value==1:
        non_duplicates={key:value}
        print(non_duplicates)

""" 4- Write a program to remove newline characters from a file and write the result in another
file.
"""

with open( "Alaa.txt","r",encoding="UTF-8")  as file_1, open("alaa (2).txt","w",encoding="UTF-8") as file_2:
   lines= file_1.readlines()
   x= [print(line.strip())  for line in lines]
   for line in lines:
    file_2.write(line.strip() )

with open("alaa (2).txt","r",encoding="UTF-8") as file_2:
   lines= file_2.readlines()
   print(lines)

""" 5- Write a program to read the first n lines of a file. Prompt the user to enter the value
for n. 
"""

num= int(input(" please enter number of lines"))
with open("Alaa.txt","r",encoding="UTF-8") as file:
  lines= file.readlines()
  for line in range(num) :
   print(lines[line])

"""6- Write a program to read the last n lines of a file. Prompt the user to enter the
value for n.
"""

with open ('alaa (2).txt','r',encoding='utf-8') as file:
  lines = file.readlines()
  num_2= int(input(" please enter number of lines"))
  for line in range(num_2,-1,-1) :
    print(lines[line])

"""7- Write a program to combine each line from the first file with the corresponding line in the
second file in a tuple.
"""

with open( "Alaa.txt","r",encoding="UTF-8")  as file_1, open("alaa (2).txt","r",encoding="UTF-8") as file_2:
  lines1 = file_1.readlines()
  lines2 = file_2.readlines()
  for line1, line2 in zip (lines1,lines2):
    print(line1+ line2)

"""8- Write a program that reads the contents of the file and counts the occurrences of each letter. Prompt the user to enter the filename.


"""

file_name=input("please enter name")
with open (file_name,"r",encoding="UTF-8") as file_1:
 no_of_letters =0
 occurrence={}
 lines= file_1.readlines()
 for line in lines:
    words= line.strip().split(" ")
    no_of_words=len(word)
    for word in words:
      letters= word.strip().split(" ")
      no_of_letters=len(letters) 
      for letter in word : 
            occurrence[letter]=occurrence[letter]+1 if  letter in occurrence else 1
print(occurrence)
print(no_of_letters)

"""9- Write a program to read and write the contents from one csv file to another."""

import csv
with open ("employee.csv","r",newline="") as output_file , open("employy_new.csv","w",newline="")as inline_file:
 reader=csv.reader(output_file)
 csv_writer= csv.writer(inline_file)
 for each_row in reader: 
    csv_writer.writerow(each_row)

with open ("employy_new.csv","r",newline="")as inline_file:
 csv_reader = csv.reader("employy_new.csv")
 print(csv_reader)

""" 10- Write the following dataset to a csv file with name “employee.csv” emp_name, sal, dept
‘a’, 100, ‘cs’
‘b’, 200, ‘is’
‘c’, 300, ‘cs’
‘d’, 400, ‘ds’
‘e’, 500, ‘cs’
‘f’, 600, ‘cs’ 
"""

import csv
csv_header_name=["emp_name","sal","dept"]
each_row=[["a", "100", "cs"],
 ["b", "200", "is"],
["c", "300", "cs"],
["d", "400", "ds"],
["e", "500", "cs"],
["f", "600", "cs"]]
with open("employee.csv",'w',newline="") as csvfile:
  csv_writer = csv.writer(csvfile)
  csv_writer.writerow(csv_header_name)
  csv_writer.writerows(each_row)

""" 11- Using employee.csv file to find the number of employees working in cs dept"""

with open('employee.csv') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    if row['dept']=='cs': print(row['emp_name'])