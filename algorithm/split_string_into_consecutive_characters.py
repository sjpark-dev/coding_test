def split_into_consecutive_characters(string):
    list = []
    consecutive_characters = string[0]

    for i in range(1, len(string)):
        if string[i - 1] == string[i]:
            consecutive_characters += string[i]
        else:
            list.append(consecutive_characters)
            consecutive_characters = string[i]

    list.append(consecutive_characters)

    return list


# 사용 예시
if __name__ == "__main__":
    list = split_into_consecutive_characters("aabbbcccddefffggghh")
    print(list)
