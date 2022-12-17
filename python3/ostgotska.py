
phrase = input().split()

totalAE = 0
for word in phrase:
    if "ae" in word:
        totalAE += 1

percentage = 100*totalAE/len(phrase)

if percentage >= 40:
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")
