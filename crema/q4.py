def subtract_word(word, words):
    length = len(word)
    for i in range(length):
        temp = word
        temp = temp.replace(word[i], '', 1)
        if temp in words:
            return temp
    return -1


def longestChain(words):
    real_chain_length = 0
    words = sorted(words)
    i = 0
    for i in range(len(words)):
        chain_length = 1
        word = words[i]
        while (word in words):
            word = subtract_word(word, words)
            if word != -1:
                chain_length += 1
            else:
                if chain_length > real_chain_length:
                    real_chain_length = chain_length

        if real_chain_length < chain_length:
            real_chain_length = chain_length

    return real_chain_length


print(longestChain(['aaaaa', 'aaaa', 'aaaaaaaa', 'aaaaaaaaa', 'a', 'aaaaaa', 'aaa', 'aa', 'aaaaaaa', 'aaaaaaaaaa']))

print(longestChain(['a', 'b', 'ba', 'bca', 'bda', 'bdca']))