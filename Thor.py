#! /usr/bin/python

print(" ______________________         _____________________                                          ")
print("|                 |    |       |             |  ___  |  + VIP password list maker          ")
print("|                 |    |       |    _____    | |___| |                                         ")
print("|_____|     |_____|    |_______|   |     |   |     __|                                         ")
print("      |     |     |            |   |     |   |     \     + script by Bishop kurd python coder  ")
print("      |     |     |            |   |_____|   |   _  \                                          ")
print("      |     |     |     _____  |             |  | |  \                                         ")
print("      |_____|     |____|     |_|_____________|__| |___\   + thanks for download                ")
#the header picture-------------------------------------------------------------------------------------
print("***********************************************************************************************")
print("")
print("select an option")
print("")
print("1) just intiger : like (123,1213232,39,1000000 etc)")
print("")
print("2) string and intiger : like (john123,jack18783,sara0910912992 etc)")
print("")
print("3) intiger and string : like (1277john,123juice,21290019029jack etc) ")
print("")
print("4) string intiger string : (12324*12*21221*21212)")
print("")
print("5) Special Charater mix : like(! @ & * john)")
print("")
 
select2 = int(input("Enter the your selected number >>>>> "))
print("") 

  
if (select2== 1):
    print("")
    print("type your max number?  example(1000,9000,100,10,10000000)")
    print("")
    f = open("pass.txt","a+")
    selected_int = int(input("Type here >>> "))
    for i in range(0,selected_int):
        f.write("%d\r\n"%(i))
    f.close()


if (select2 == 2):
    print("write you pre password text first then type the number range example(john,1000 => john1 john2 - john1000)")
    print("")
    selected_str2 = raw_input("type your pre password text >>> ")
    print("")
    selected_int2 = int(input("type your number range >>> "))
    print("")
    f = open("pass.txt","a+")            
    for n in range(0,selected_int2):
        f.write("%s%d\r\n" % (selected_str2,n))
    f.close()

if (select2 == 3):
    print("write you pre password number max first then type the after number text example : (100johny , 2000akl , 2000000abc")
    print("")
    selected_int3 = int(input("type your pre number max >>> "))
    print("")
    selected_str3 = raw_input("type your after text >>> ")
    print("")
    f = open("pass.txt","a+")        
    for x in range(0,selected_int3):
        f.write("%d%s\r\n" % (x,selected_str3))
    f.close()

if (select2 == 4):
    string4 = raw_input("type the pre text >>> ")
    intiger4 = int(input("inter the justify intiger range number >>> "))
    string5 = raw_input("enter the end text >>> ")
    f = open("pass.txt","a+")         
    for d in range(0,intiger4):
        f.write("%s%d%s\r\n" % (string4,d,string5))
    f.close()

if (select2 == 5):
    string6 = raw_input("Enter the Special character : '! @ $ % *' that appears before the text >>> ")
    string7 = raw_input("Eneter a secret String >>> ")
    string8 = raw_input("Enter the Special Charachter : '! @ $ % *' hat follows the text >>> ")
    integer5 = int(input("Enter the number of words to be generated (count should be within 10) >>> "))
    f = open("pass.txt","a+")
    for d in range(1,integer5):
        f.write("%s%s%s\r\n" % (d*string6,string7,d*string8))

print("""

      ###############################
      #  Thor password list maker   # 
      #                             #
      #        F I N I S H          #
      #                             #
      #     Code   By    E-RRORE    #
      #                             #
      ###############################
""")
