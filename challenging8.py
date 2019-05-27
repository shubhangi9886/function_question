string=raw_input("Enter string:")
count1=0
count2=0
for i in string:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
print(count1)
print(count2)

# string1 = raw_input("Enter string:")
# count1 = 0
# count2 = 0
# i = 0
# while i < len(string1):
#       if string1[i] == "A" to "Z":
#             count1=count1+1
#       elif string1[i] == "a" to "z":
#             count2=count2+1
# print(count1)
# print(count2)
