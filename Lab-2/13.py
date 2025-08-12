# Prompt the user to enter some text
text = input("Enter text: ")

# Initialize an empty dictionary to store character frequencies
freq = {}

# Iterate through each character in the input text
for ch in text:
    # Check if the character is an English alphabet letter (uppercase or lowercase)
    if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        # If the character is already in the dictionary, increment its count
        if ch in freq:
            freq[ch] += 1
        # If the character is not in the dictionary, add it with count 1
        else:
            freq[ch] = 1

# Print the frequency of each character found
for char in freq:
    print(f"{char}: {freq[char]}")
