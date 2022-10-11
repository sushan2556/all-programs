#write a progarm to print reverse of number/string.:-home work


# using string slicing 
# str1 = 123456
# str2 = "Reverse"
# print(str(str1)[::-1])
# print(str(str2)[::-1])
# #using while loop


num = int(input("enter a no ->"))  # 237
reverse = 0
while num > 0:
    reverse = (reverse*10) + num % 10 # 0*0 + 231%10 which is 0 + 1 --> first loop
    num = num // 10 # 237 // 10 is 23.7 , // ignores the decible so num is 23 --> first loop
print(reverse)

s = "hello"
for i in range(len(s)):
    if s[i]==i and s[i]+1 == i:
        continue
    print(s)
