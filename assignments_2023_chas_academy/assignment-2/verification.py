import solution

test_data = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
expected = ["0.1", "1.1.1", "1.2", "1.2.1", "1.11", "2", "2.0", "2.0.0"]
assert solution.solution(test_data) == expected

test_data = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
expected_result = ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]
assert solution.solution(test_data) == expected_result
