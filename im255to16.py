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
    strOut = ["{", ""]
    count = 0
    idx = 1
    for data in colorOut:
        strOut[idx] += data + ", "

        if count == 50:
            count = 0
            idx += 1
            strOut.append("")
        else:
            count += 1

    strOut.append("};")

    print("Writing to file")
    file.write("\n".join(strOut))
    print("Done writing")
    file.close()