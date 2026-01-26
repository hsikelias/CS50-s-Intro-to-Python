# isdigit(), #startswith

correct_text = "BRO123"
wrong_text = "BR123TY"
wrong_text2 = "BRI012" #first number starting with 0

numbers = ["0","1","2","3","4","5","6","7","8","9"]

correct_text_list = list(correct_text)

for char in correct_text_list:
    if char == "0":
        zero_index = (correct_text_list.index(char))
        print(zero_index)
        break
    elif char in numbers:
        if char.isalpha():
    else:
        print("Number Not 0"
