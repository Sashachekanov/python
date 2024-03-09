from PIL import Image
image = Image.open('C://Users//Ученик//PycharmProjects//sasha//ryh//sadic.jpg')


print('Ширина:', image.width)
print('Высота:', image.height)


new = image.resize((150,150), Image.LANCZOS)
new.save('icon_sadic.jpg')
new.close()
image = Image.open('C://Users//Ученик//PycharmProjects//sasha//ryh//popa.jpg')

print('Ширина:', image.width)
print('Высота:', image.height)


new = image.resize((150,150), Image.LANCZOS)
new.save('icon_popa.jpg')
new.close()