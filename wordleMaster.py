# code to enhance wordle guessing abilities
# note to self: start with CRANE


def find_answers(letters, absent, misplaced):

    """
    :param letters: 5 char string of word with known letters, 0 representing unknown slots
    :param absent: array of strings representing letters not in word
    :param misplaced: array of strings representing letters in word
    :return: array of possible words (strings)
    """

    # open wordle answers file to read
    answers = open("wordle_answers.txt", "r")

    possible_ans = []

    # code executes in O(N^2) time <-- not ideal
    for word in answers:
        cur_index = 0
        count = 0
        for letter in letters:
            if letter == word[cur_index] or letter == '\n':
                count += 1
            cur_index += 1
        if count == 5:
            absent_count = 0
            misplaced_count = 0
            # append word to possible ans only if it doesn't contain a letter from absent letters
            for letter in word:
                if letter in absent:
                    absent_count += 1
                if letter in misplaced:
                    misplaced_count += 1
            if absent_count == 0 and misplaced_count == len(misplaced):
                # appending all chars in word string expect last char ('\n')
                possible_ans.append(word[0:-1])

    print(possible_ans)


# '\n' represents null --> unknown slot
find_answers("r\n\n\n\n", ["c", "n", "e", "p", "i", "d"], ["a"])


# code can definitely be improved, but will be used for now

