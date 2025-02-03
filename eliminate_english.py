import re

def is_telugu(word):
    # Regular expression to match Telugu Unicode range
    telugu_pattern = re.compile("[\u0C00-\u0C7F]+")
    return bool(re.fullmatch(telugu_pattern, word))

def filter_telugu_words(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split the content into words
    words = content.split()

    # Filter out English words and keep only Telugu words
    telugu_words = [word for word in words if is_telugu(word)]

    # Write each Telugu word on a new line in the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(telugu_words))

# Example usage
input_filename = 'tel.txt'
output_filename = 'tel_final.txt'

filter_telugu_words(input_filename, output_filename)
