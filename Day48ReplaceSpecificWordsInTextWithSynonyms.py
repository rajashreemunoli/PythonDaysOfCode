#Create a program that replaces specific words in a text with their synonyms
import pandas as pd
import re

def load_synonyms_from_excel(file_path):
    df = pd.read_excel(file_path)
    synonyms_dict = dict(zip(df['word'].str.lower(), df['synonym']))
    return synonyms_dict

def replace_with_synonyms_from_table(text, synonyms_table):
    def replace(match):
        word = match.group(0).lower()
        return synonyms_table.get(word, word)

    pattern = re.compile(r'\b\w+\b')  # Match whole words
    replaced_text = pattern.sub(replace, text.lower()).lower()
    return replaced_text

# Example usage
excel_file_path = 'synonyms.xlsx'
input_text = "The sky is full of bright stars"

synonyms_table = load_synonyms_from_excel(excel_file_path)

output_text = replace_with_synonyms_from_table(input_text, synonyms_table)
print("Original Text:", input_text)
print("Replaced Text:", output_text)