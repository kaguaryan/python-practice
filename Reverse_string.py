originalString = "ryan"  # string we want to reverse

def reverse_a_string(string):
    Reversedstring = []  # space to store characters
    for i in range((len(string)-1), -1, -1):  # Go from the last character to the first
        Reversedstring.append(string[i])  # Add the character to the list
    return "".join(Reversedstring)  # Join the list into a string and return it

print(reverse_a_string(originalString))  # Reverse the string and print it
