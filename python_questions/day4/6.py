def reverse_str(str_ing):
    reverse_string=""

    for w in range(len(str_ing)-1,-1,-1):
        reverse_string+=str_ing[w]
    return reverse_string
print(reverse_str("sushma"))