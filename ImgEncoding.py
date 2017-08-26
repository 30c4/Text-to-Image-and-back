from PIL import Image

# Starting dictionary for conversion.
en = {
    '': '0',
    'A': '50',
    'B': '51',
    'C': '52',
    'D': '53',
    'E': '54',
    'F': '55',
    'G': '56',
    'H': '57',
    'I': '58',
    'J': '59',
    'K': '60',
    'L': '61',
    'M': '62',
    'N': '63',
    'O': '64',
    'P': '65',
    'Q': '66',
    'R': '67',
    'S': '68',
    'T': '69',
    'U': '120',
    'V': '121',
    'W': '122',
    'X': '123',
    'Y': '124',
    'Z': '125',
    '0': '150',
    '1': '151',
    '2': '152',
    '3': '153',
    '4': '154',
    '5': '155',
    '6': '156',
    '7': '157',
    '8': '158',
    '9': '159',
    'a': '71',
    'b': '72',
    'c': '73',
    'd': '74',
    'e': '75',
    'f': '76',
    'g': '77',
    'h': '78',
    'i': '79',
    'j': '110',
    'k': '111',
    'l': '112',
    'm': '113',
    'n': '114',
    'o': '115',
    'p': '116',
    'q': '117',
    'r': '118',
    's': '119',
    't': '220',
    'u': '221',
    'v': '222',
    'w': '223',
    'x': '224',
    'y': '225',
    'z': '226',
    ' ': '227',
    '.': '228',
    ',': '229',
    '!': '230',
    '?': '231',
    '@': '232',
    '#': '233',
    '$': '234',
    '%': '235',
    '^': '236',
    '&': '237',
    '*': '238',
    '(': '239',
    ')': '240',
    '<': '241',
    '>': '242',
    ';': '243',
    ':': '244',
    '/': '245',
    '-': '246',
    '_': '247',
    '=': '248',
    '+': '249',
    '{': '250',
    '[': '251',
    '}': '252',
    ']': '253',
    "'": '254',
    '"': '255'
}

def encode():
    # Initialize the rgb order
    r = []
    g = []
    b = []

    zin = input("Type something: ")

    # Put the letters in rgb order
    count = 1
    for l in zin:

        if count == 1:
            r.append(en[l])
            count += 1
        elif count == 2:
            g.append(en[l])
            count += 1
        elif count == 3:
            b.append(en[l])
            count = 1

    if len(g) < len(r):
        g.append('0')
    if len(b) < len(r):
        b.append('0')

    # Generates an image and puts the RGB values in the image
    img = Image.new("RGB", (len(r), 1))
    for x in range(len(r)):
        img.putpixel((x, 0), (int(r[x]), int(g[x]), int(b[x])))

    img.save("message.png", "PNG")
    img.show()
    print("encoding succesful")

def decode():
    # Initialize the rgb order
    r = []
    g = []
    b = []

    # opens the image and places the RGB values of the pixels in their lists
    img = Image.open("message.png")
    for x in range(img.size[0]):
        rint, gint, bint = img.getpixel((x,0))
        r.append(rint)
        g.append(gint)
        b.append(bint)

    dek = list(en.keys())
    dev = list(en.values())

    zin = ""

    # checks the values for their keys
    for l in range(len(r)):
        zin += dek[dev.index(str(r[l]))]
        zin += dek[dev.index(str(g[l]))]
        zin += dek[dev.index(str(b[l]))]

    print(zin)


while True:
    com = input("> ")
    if com == "encode":
        encode()
    elif com == "decode":
        decode()
