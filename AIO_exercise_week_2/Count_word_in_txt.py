def create_word_count_dict(file_path):
    word_count = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.lower().split()
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    return word_count

if __name__ == '__main__':
    file_path = '/Users/ngoquangduc/Desktop/AIO Github/AIO_exercise/P1_data.txt'
    word_count_list = create_word_count_dict(file_path)
    print(word_count_list)