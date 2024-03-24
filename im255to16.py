from PIL import Image

filename = input("file name: ")

img = Image.open("./images/" + filename + ".png")

pixels = list(img.getdata())

colorOut = []
for clr in pixels:
    output = ""
    if clr[3] == 0:
        output = "0xabcd" # Ignore
    else:
        r = int((clr[0] / 255) * 31)
        g = int((clr[1] / 255) * 63)
        b = int((clr[2] / 255) * 31)

        output = hex((r<<11) + (g<<5) + b)

        if len(output) < 6:
            output = "0x" + "".join(["0" for i in range(6 - len(output))]) + output[2:]

    colorOut.append(output)

with open("./images_out/" + filename + ".txt", mode='w') as file:
    strOut = str(colorOut).replace("[", "{\n").replace("]", "\n};\n").replace("\'", "")
    listOfCommas = [i for i in range(len(strOut)) if strOut[i] == ',']
    listOfCommas = [listOfCommas[i] for i in range(len(listOfCommas)) if (i > 0 and i % 50 == 0)]
    offset = 0

    for i in listOfCommas:
        str1 = strOut[:i + offset]
        str2 = strOut[1 + i + offset:]
        offset += 1
        strOut = ",\n".join([str1, str2])

    print("Writing to file")
    file.write(strOut)
    print("Done writing")
    file.close()