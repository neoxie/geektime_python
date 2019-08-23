import pprint
import re


def main():
    with open('in.txt', 'r') as f:
        text = f.read()
    text = re.sub(r'[^\w ]', ' ', text)
    text = text.lower()
    words = text.split()
    words = filter(None, words)

    word_count = dict()
    for word in words:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1

    d_sorted_by_key = sorted(
        word_count.items(), key=lambda x: x[0])
    d_sorted_by_value = sorted(
        d_sorted_by_key, key=lambda x: x[1], reverse=True)  # 根据字典值的升序排序

    pprint.pprint(d_sorted_by_value)

    with open('out.txt', 'w') as f:
        for word, count in d_sorted_by_value:
            f.write(f'{word} {count}\n')


if __name__ == "__main__":
    main()
