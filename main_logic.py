def calculate_typing_speed(text: str, duration: (float, int)) -> (float, int):
    words = text.split()
    word_count = len(words)
    words_per_minute = word_count / duration
    return words_per_minute
