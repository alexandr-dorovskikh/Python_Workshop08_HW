# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно
# последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число).

def read_last(lines, file):
    if type(lines) != int:
        return

    f = open(file, "r", encoding="utf-8")

    try:
        file_content = f.readlines()
        while lines > 0:
            print(file_content[-lines].strip())
            lines -= 1
    finally:
        f.close()

# Требуется реализовать функцию longest_words(file), которая записывает в файл result.txt слово, имеющее максимальную
# длину (или список слов, если таковых несколько).


def longest_words(file):

    all_words = list()

    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            all_words.extend([(len(word), word) for word in line.split()])

    max_len = max(word[0] for word in all_words)

    output_file = open("result.txt", "w", encoding="utf-8")
    output_file.write('\n'.join([word[1] for word in all_words if word[0] == max_len]))
    output_file.close()


read_last(3, "article.txt")
longest_words("article.txt")
