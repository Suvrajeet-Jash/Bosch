def count(str):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in str:
        if char.isalpha(): #First checking here whether the character is a letter or not, VERY IMPORTANT STEP
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

string = str(input("Enter a String: "))

v,c = count(string)

print(f"Number of Vowels and Consonants in {string} are {v} , {c} respectively")
