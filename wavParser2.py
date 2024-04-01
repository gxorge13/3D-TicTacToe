import soundfile as sf
import numpy as np
import librosa

filename = input("File name: ")

data, sampleRate = librosa.load("./sounds/" + filename, dtype=float)
data = librosa.resample(data, orig_sr=sampleRate, target_sr=8000)
data = (data * np.iinfo(np.int16).max).astype(np.int16)
data_out = []

print(data)
for d in data:
    data_out.append(hex(d))

print(len(data_out), len(data))
with open("./sounds_out/" + filename + ".txt", 'w') as file:
    strOut = ["{", ""]
    count = 0
    idx = 1
    for data in data_out:
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
