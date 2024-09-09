import random
import string

def scramble_code(code):
    # 1. Variable and function renaming
    replacements = {}
    for identifier in set(code.split()):
        if identifier.isidentifier() and not keyword.iskeyword(identifier):
            new_name = ''.join(random.choices(string.ascii_letters, k=random.randint(5, 15)))
            replacements[identifier] = new_name
    for old_name, new_name in replacements.items():
        code = code.replace(old_name, new_name)

    # 2. String encryption
    encrypted_strings = {}
    for match in re.finditer(r'"([^"]*)"', code):
        original_string = match.group(1)
        encrypted_string = ''.join(chr(ord(c) ^ 0x42) for c in original_string)  # Simple XOR encryption
        encrypted_strings[original_string] = encrypted_string
    for original_string, encrypted_string in encrypted_strings.items():
        code = code.replace(f'"{original_string}"', f'"{encrypted_string}"')

    # 3. Whitespace removal and insertion
    code = code.replace('\n', '').replace(' ', '')
    for _ in range(random.randint(10, 30)):
        insert_position = random.randint(0, len(code))
        code = code[:insert_position] + ' ' + code[insert_position:]

    # 4. Comment insertion
    for _ in range(random.randint(5, 15)):
        comment = '# ' + ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(10, 30)))
        insert_position = random.randint(0, len(code))
        code = code[:insert_position] + comment + '\n' + code[insert_position:]

    return code

# Example usage
original_code = """
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
"""

scrambled_code = scramble_code(original_code)
print(scrambled_code)
