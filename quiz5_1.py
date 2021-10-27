import matplotlib.pyplot
import math



get_data("quiz5_1.csv")         # You need to modify this line of code!!
matplotlib.pyplot.title("Magnitude vs. Depth")
matplotlib.pyplot.scatter(mags, depths)
matplotlib.pyplot.ylabel("Depth (km)")
matplotlib.pyplot.xlabel("Magnitude")
for i in range(len(loc)):
    print("{}: {}".format(mags[i], loc[i]))

rms = rootmeansquare(mags)
print("Root Mean Square of Magnitude (>=6.0): {:.2f}".format(rms))

matplotlib.pyplot.show()

# Expected Output:
#6.0: "7 km NNW of Thrapsann
#6.1: "241 km NNW of Nanao
#7.3: Vanuatu region
#6.0: Mid-Indian Ridge
#6.3: South Sandwich Islands region
#6.9: Vanuatu region
#6.21: "Hawaii region
#6.9: "114 km E of Chignik
#6.4: "0 km SSE of Palekastro
#6.4: Solomon Islands
#6.1: "67 km WNW of Sola
#6.0: south of the Fiji Islands
#6.2: "21 km SSE of Yilan
#Root Mean Square of Magnitude (>=6.0): 6.38