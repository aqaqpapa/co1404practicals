word_to_count={}
Text=input()
for word in Text.split():
    try:
        word_to_count[word]+=1
    except KeyError:
        word_to_count[word]=1
sorted_words = sorted(word_to_count.items())

for word, count in sorted_words:
    print(f"{word:5} : {count}")

