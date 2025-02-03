from googletrans import Translator

# Initialize translator
translator = Translator()
i=0
# Read input lines from the file
with open('./en1.txt', 'r', encoding='utf-8') as file:
    input_lines = file.readlines()

# Open output file in write mode
with open('./tel1.txt', 'w', encoding='utf-8') as file:
    # Iterate through each line and translate
    for line in input_lines:
        # Translate text into Telugu
        telugu_translation = translator.translate(line.strip(), src='en', dest='te').text

        # Write Telugu translations to the output file
        file.write(f'{telugu_translation}\n')
        i = i+1
        print(i)

# Print success message
print('Translations appended to tel_basic.txt file.')
