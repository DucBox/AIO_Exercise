def create_word_list(string):
    word_list = []
    word_list.append(string[0])
    for i in range(1, len(string)):
        if string[i] in word_list:
            continue
        else:
            word_list.append(string[i])
    return word_list
 
def create_word_count_dict(string, word_list):
    word_count = {}
    for word in word_list:
        count = 0
        for j in range(len(string)):
            if word == string[j]:
                count += 1
        word_count[f'{word}'] = count
    return word_count

if __name__ == '__main__':
    string = 'Happiness'
    word_list = create_word_list(string)
    word_count_dict = create_word_count_dict(string, word_list)
    print(word_count_dict)

