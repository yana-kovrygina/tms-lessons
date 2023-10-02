def get_most_frequent_word(text: str) -> str:
    counts: dict[str, int] = {}
    for word in text.split():
        counts.setdefault(word, 0)
        counts[word] += 1

    max_count = 0
    result = ''
    for word,count in counts.items():
        if max_count < count:
            max_count = count
            result = word
    return result


assert get_most_frequent_word('aa a a a a ewfweg egeg') == 'a'