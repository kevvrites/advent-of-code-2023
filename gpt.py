def replace_number_words(string):
    number_words = {
        "zero": "0", "one": "1", "two": "2", "three": "3",
        "four": "4", "five": "5", "six": "6", "seven": "7",
        "eight": "8", "nine": "9"
    }

    result = ""
    temp = ""
    
    for char in string:
        temp += char
        for word, digit in number_words.items():
            if temp.endswith(word):
                temp = temp[:-len(word)] + digit
    result += temp
    return result

input_string = "eightwothree"
output_string = replace_number_words(input_string)
print(output_string)  # Expected output: "8wo3"