with open ("rosalind_ini6.txt", "r") as file:
    word_dict = {}
    for word in str.split(' '):
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
        

for key, value in word_dict.items():
    print key
    print value

print word_dict
