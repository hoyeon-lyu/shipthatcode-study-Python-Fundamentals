text = input()
result = text

if len(text) > 1:
    start_letter = text[0]
    end_letter = text[-1]
    result = end_letter + text[1:len(text)-1] + start_letter
    
# TODO: build a new string whose first and last characters are swapped,
# with every character between them left where it is.
# Remember that a very short string has nothing to swap.

print(result)