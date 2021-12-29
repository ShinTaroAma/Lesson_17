text_for_write = input("""Enter your message """)
file = open('text.txt', 'a')
file.write(text_for_write + " ")
file.close()

with open('text.txt', 'r') as my_file:
    wirsh = my_file.read()
print(wirsh)


