n = int(input())

for row in range(1, n + 1):
    for col_multiflier in range(1,n + 1):
        whole_result = row * col_multiflier
        letter_result = str(whole_result)[-1]
        print(f"{letter_result}", end="")

    # TODO: add an inner loop over the columns 1..n.
    # Print each cell's digit without ending the line,
    # and let the print() below close the row.
    
    print()
