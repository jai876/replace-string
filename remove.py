remove_words = ['anyword', 'delete']

with open('oldfile.txt') as oldfile, open('newfile.txt', 'w') as newfile:
    for line in oldfile:
        if not any(remove_word in line for remove_word in remove_words):
            newfile.write(line)
