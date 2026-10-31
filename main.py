# TODO: keep only letters, digits and spaces, lowercase them,
# and join the words with single hyphens.

title = input()

temp = ""
for ch in title:
    if not(ch.isalpha() or ch.isdigit() or ch == ' '):
        continue
    temp += ch.lower()

l = temp.split(" ")
temp_ = []
for parts in l:
    if parts == '':
        continue
    temp_.append(parts)

title = "-".join(temp_)
slug = title

print(slug)
