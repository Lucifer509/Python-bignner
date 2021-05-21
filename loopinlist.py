list1 = [int, float, 4, "Champ", "Package", 99, 56, 0, "Prize", 6]
for item in list1:

    if str(item).isnumeric() and item >= 6:  # here we use str(item) which convert every value in list1 in str and
        # .isnumeric check if the store value in string is numeric.
        print(item)


