from collections import defaultdict
def longestStrChain(words):
    if not words:
        return 0

    words.sort(key=lambda a: len(a))
    tracker = {}
    curr_chain = 1
    max_chain = 1

    for word in words:
        for i in range(len(word)):
            # check if you have seen the word if you remove one letter
            cut_word = word[:i] + word[i + 1:]

            # if it was found before then update the current chain
            if cut_word in tracker.keys():
                curr_chain = max(curr_chain, tracker[cut_word] + 1)

        # see if you have reached a new maximum chain and reset the current one
        max_chain = max(max_chain, curr_chain)
        tracker[word] = curr_chain  # remember each word's chain
        curr_chain = 1

    return max_chain


print longestStrChain(["a","b","ba","bca","bda","bdca"])