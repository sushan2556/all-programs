def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "   this is the text that will replace word save and spaces  "
n = remove_and_split(this, "save")
print(n)



