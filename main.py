n = int(input())

result_now = 1
for multiflier in range(1,11):
    result_now = n * multiflier
    print(f"{n} x {multiflier} = {result_now}")

# TODO: print the ten lines of the table for n, one line per product.
# Loop over the numbers 1 through 10 and build each line with an f-string.
# Nothing is printed yet, so every test fails until you add the loop.
