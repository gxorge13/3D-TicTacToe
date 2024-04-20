import soundfile as sf

filename = input("File name: ")

data, sampleRate = sf.read("./sounds/" + filename + ".wav", dtype="int16", always_2d=True)

data_out = []

for d in data:
    data_out.append(hex(d[0]))

print(len(data_out), len(data))
with open("./sounds_out/" + filename + ".txt", 'w') as file:

    strOut = str(data_out).replace("[", "{\n").replace("]", "\n};\n").replace("\'", "")
    listOfCommas = [i for i in range(len(strOut)) if strOut[i] == ',']
    listOfCommas = [listOfCommas[i] for i in range(len(listOfCommas)) if (i > 0 and i % 50 == 0)]
    offset = 0

    for i in listOfCommas:
        str1 = strOut[:i+offset]
        str2 = strOut[1+i+offset:]
        offset += 1
        strOut = ",\n".join([str1, str2])

    print("Writing to file")
    file.write(strOut)
    print("Done writing")
    file.close()
