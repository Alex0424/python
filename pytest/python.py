def is_password_valid(policy, password):
    range_part, letter = policy.split()
    min_count, max_count = map(int, range_part.split('-'))
    letter_count = password.count(letter)
    return min_count <= letter_count <= max_count

def count_valid_passwords_from_file(file_path):
    valid_passwords = 0
    with open(file_path, 'r') as file:
        for line in file:
            policy_part, password = line.strip().split(': ')
            if is_password_valid(policy_part, password):
                valid_passwords += 1
        return valid_passwords

print(count_valid_passwords_from_file("data.txt"))
