f = open("datascience websites list.txt")
lines = f.readlines()

seed_words = []

for i in lines:
    str = i.split("-")[-1]
    #print(str)
    words = str.split(",")
    words = [word.strip(" \n") for word in words]
    for word in words:
        if not word in seed_words:
            seed_words.append(word)
print(seed_words)
o = open("seed words.txt","w")
for word in seed_words:
    o.write(word+"\n")