'''Return the number of times that the string "code" appears anywhere in the given string, 
except we'll accept any letter for the 'd', so "cope" and "cooe" count.'''

def count_code(str):
    count = 0
    for i in range(len(str)-3):
        if str[i:i+1] == "co" and str[i+3] == "e":
            count += 1
    return count

# print (count_code("aaacodebbb"))
# print (count_code('aaacodebbb'))
# print (count_code('codexxcode'))
# print (count_code('cozexxcope'))
# print (count_code('cozfxxcope'))
# print (count_code('xxcozeyycop'))
# print (count_code('cozcop'))
# print (count_code('abcxyz'))
# print (count_code('code'))
# print (count_code('ode'))
# print (count_code('c'))
# print (count_code(''))
# print (count_code('AAcodeBBcoleCCccoreDD'))
# print (count_code('AAcodeBBcoleCCccorfDD'))
print (count_code('aaacoeebbb'))