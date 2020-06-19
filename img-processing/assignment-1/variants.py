from PIL import Image, ImageEnhance, ImageDraw, ImageFont, ImageColor, ImageOps, ImageFilter
from IPython.display import display

img = Image.open('test.jpg').convert('RGB')
# TODO: change this with your font path
fnt = ImageFont.truetype('readonly/AkaashNormal.ttf', 75)

enhancer = ImageEnhance.Color(img)


images = []

for i in range(0, 10):
    current_img = enhancer.enhance(i)
    drawing_object = ImageDraw.Draw(current_img)
    drawing_object.rectangle((0, 450, 800, 325), fill='black')
    drawing_object.text((20, 350), 'Channel Intensity o 0.{}'.format(
        i), fill=(255, 255, 255), font=fnt)
    images.append(current_img)

first_img = images[0]

contact_sheet = Image.new(
    first_img.mode, (first_img.width * 3, first_img.height * 3))

x = 0
y = 0

for image in images:
    contact_sheet.paste(image, (x, y))

    if first_img.width + x == contact_sheet.width:
        x = 0
        y += first_img.height
    else:
        x += first_img.width

contact_sheet = contact_sheet.resize(
    (int(contact_sheet.width / 2), int(contact_sheet.height / 2)))
contact_sheet.save('out.png')
