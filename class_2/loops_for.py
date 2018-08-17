names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# Criando nova lista com os valores alterados
for name in names:
    usernames.append(name.lower().replace(" ", "_"))

print(usernames)

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# alterando os valores da mesma lista
for index in range(len(usernames)):
    usernames[index] = usernames[index].lower().replace(" ", "_")

print(usernames)

# Contendo tags
tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        print(token)
        count += 1

print(count)

# concatenando
items = ['first string', 'second string']

html_str = "<ul>\n"
for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)

