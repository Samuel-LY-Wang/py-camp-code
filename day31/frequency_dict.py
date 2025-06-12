def is_chinese_char(ch):
    """Check if a character is a Chinese character."""
    return '\u4e00' <= ch <= '\u9fff'

with open("day31/zh_cn_50k.txt", "r") as file:
    text = file.read()
    words=text.split()
    word_list = []
    for word in words:
        try:
            int(word)
            continue #skip frequency num
        except ValueError:
            if len(word) >= 1 and not is_chinese_char(word[0]):
                # Skip words that are not Chinese characters or are too short
                continue
            word_list.append(word.strip())
with open("day31/word_list.txt", "w") as output_file:
    for word in word_list:
        output_file.write(word + "\n")