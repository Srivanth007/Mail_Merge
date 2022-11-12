with open("E:/program/Mail Merge Project Start/Input/Letters/starting_letter.txt") as text:
    value = text.readlines()
    first_str = value[0].strip()
    # print(first_str)
    print(value)

with open("E:/program/Mail Merge Project Start/Input/Names/invited_names.txt") as user_name:
    for names in user_name.readlines():
        # first_str = value[0].strip()
        name = names.strip() 
        changed_value = value[0].replace("[name]", name)
        with open(f"E:/program/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}", mode = "w") as letters:
            value[0] = f"Dear {name},\n"
            for str1 in value:
                letters.write(str1)



# # for str1 in value:
#     print(str1.strip())