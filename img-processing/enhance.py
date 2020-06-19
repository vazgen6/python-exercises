from PIL import Image, ImageEnhance
from IPython.display import display

img = Image.open('img.png').convert('RGB')

enhancer = ImageEnhance.Brightness(img)

images = []

for i in range(0, 10):
    images.append(enhancer.enhance(i/10))

first_img = images[0]

contact_sheet = Image.new(first_img.mode, (first_img.width * 3, first_img.height * 3))

current_location_x = 0
current_location_y = 0

for img in images[1:]:
    contact_sheet.paste(img, (current_location_x, current_location_y))
    if current_location_x + first_img.width == contact_sheet.width:
        current_location_x = 0
        current_location_y += first_img.height
    else:
        current_location_x += first_img.width

contact_sheet = contact_sheet.resize((int(contact_sheet.width / 2),  int(contact_sheet.height / 2)))

contact_sheet.save('all.png')