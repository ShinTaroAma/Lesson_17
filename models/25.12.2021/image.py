with open('img.jpg', 'rb') as my_img:
    my_img = my_img.read()
with open('img2.jpg', 'a') as my_img2:
    my_img = my_img.write()
print(my_img2)
