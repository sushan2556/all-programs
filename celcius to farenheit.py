# write a program to convert temp from celcius to farenheit
# formula for it (0°C × 9/5) + 32 = 32°F

def farh (cel): # function is defined over here 
    return (cel * (9/5)) + 32 # function defination / formula 

cel = 32
f = farh(cel)
print("the ferh temp of celcius is : " + str(f))