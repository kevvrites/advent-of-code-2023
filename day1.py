f = open("day1input.txt", 'r')
# f = open("day1sample1.txt", 'r')
# f = open("day1sample2.txt", 'r')
lines = f.readlines()

# Part 1
sum = 0
nums = []

for line in lines:
	for idx in range(len(line)):
		if line[idx] in '1234567890':
			nums.append(int(line[idx]))
	sum += nums[0]*10
	sum += nums[-1]
	nums = []

print(sum)

# Part 2
def replace_number_words(string):
    number_words = {
        "one": "1", "two": "2", "three": "3",
        "four": "4", "five": "5", "six": "6", "seven": "7",
        "eight": "8", "nine": "9"
    }

    result = ""
    temp = ""
    
    for char in string:
        temp += char
        for word, digit in number_words.items():
            if temp.endswith(word):

                temp = temp[:-len(word)] + digit + word[-1]
                print(temp)
    result += temp
    return result
				
sum2 = 0
for line in lines:	
	cleaned = replace_number_words(line)
	print(cleaned)
	for idx in range(len(cleaned)):
		if cleaned[idx] in '1234567890':
			nums.append(int(cleaned[idx]))
	sum2 += nums[0]*10
	sum2 += nums[-1]
	nums = []

print(sum2)