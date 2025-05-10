import solution
# This code is intentionally broken as you can design your return data as you like.
# Once you have decided how your return data will be sent back, you need to update this test to verify that your code
# will work and perform what you want.
#assert solution.solution("minion-3.txt") == {"b": 0}
#assert solution.solution("minion-2.txt") == {"!": 0}

file_1 = "minion-submissions/minion-1.txt"
expected_1 = {
    "amount_of_all_words": 529,
    "amount_of_different_short_word": 39,
    "amount_of_long_words": 58,
    "amount_of_different_characters": 47,
    "amount_of_lines": 20
    }
assert solution.solution(file_1) == expected_1

file_2 = "minion-submissions/minion-2.txt"
expected_2 = {
    "amount_of_all_words": 585,
    "amount_of_different_short_word": 22,
    "amount_of_long_words": 39,
    "amount_of_different_characters": 36,
    "amount_of_lines": 20
    }
assert solution.solution(file_2) == expected_2

file_3 = "minion-submissions/minion-3.txt"
expected_3 = {
    "amount_of_all_words": 936,
    "amount_of_different_short_word": 46,
    "amount_of_long_words": 58,
    "amount_of_different_characters": 43,
    "amount_of_lines": 30
    }
assert solution.solution(file_3) == expected_3

file_4 = "minion-submissions/minion-4.txt"
expected_4 = {
    "amount_of_all_words": 12,
    "amount_of_different_short_word": 1,
    "amount_of_long_words": 1,
    "amount_of_different_characters": 21,
    "amount_of_lines": 3
    }
assert solution.solution(file_4) == expected_4