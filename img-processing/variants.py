from PIL import Image, ImageDraw, ImageFont
from IPython.display import display

# image = Image.open('msi_recruitment.png')
image = Image.open('test.jpg')

contact_sheet = Image.new(image.mode, (image.width*3, image.height*3))
images = []

draw = ImageDraw.Draw(image)
draw.rectangle([0, image.height-20, image.width, image.height], fill='black')

font = ImageFont.truetype('AkaashNormal.ttf', 20)

x, y, z = 1, 1, 1
Scales = [0.1, 0.5, 0.9]

for x in Scales:
    Conversion = ( x, 0,  0, 0, 
               0,   y,  0, 0, 
               0,   0,  z, 0) 
    text = 'channel 0 intensity {}'.format(x)
    draw.text((0, image.height-20), text, font=font, align='left')
    images.append(image.convert('RGB', Conversion))
    draw.text((0, image.height-20), text,
              fill='black', font=font, align='left')

x = 1
for y in Scales:
    Conversion = ( x, 0,  0, 0, 
               0,   y,  0, 0, 
               0,   0,  z, 0) 
    text = 'channel 1 intensity {}'.format(y)
    draw.text((0, image.height-20), text, font=font, align='left')
    images.append(image.convert('RGB', Conversion))
    draw.text((0, image.height-20), text,
              fill='black', font=font, align='left')

y = 1
for z in Scales:
    Conversion = ( x, 0,  0, 0, 
               0,   y,  0, 0, 
               0,   0,  z, 0)
    text = 'channel 2 intensity {}'.format(x)
    draw.text((0, image.height-20), text, font=font, align='left')
    images.append(image.convert('RGB', Conversion))
    draw.text((0, image.height-20), text,
              fill='black', font=font, align='left')
x = 0
y = 0

for image in images:
    contact_sheet.paste(image, (x, y))

    if image.width + x == contact_sheet.width:
        x = 0
        y += image.height
    else:
        x += image.width

contact_sheet = contact_sheet.resize(
    (int(contact_sheet.width / 2), int(contact_sheet.height / 2)))
display(contact_sheet)
# contact_sheet.save('out2.png')
