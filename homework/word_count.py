"""Taller evaluable"""

import os
import glob
import re
import pandas as pd


#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run_job(input_directory, output_directory):
    """Job"""
    
    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)
    
    # Read all text files from input directory
    all_words = []
    
    # Get all txt files in the input directory
    file_pattern = os.path.join(input_directory, "*.txt")
    for file_path in glob.glob(file_pattern):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Convert to lowercase and remove punctuation
            content = content.lower()
            # Replace punctuation with spaces
            content = re.sub(r'[^\w\s]', ' ', content)
            # Split into words
            words = content.split()
            all_words.extend(words)
    
    # Count words using pandas
    word_series = pd.Series(all_words)
    word_counts = word_series.value_counts().sort_index()
    
    # Create dataframe with word and count columns
    df = pd.DataFrame({
        'word': word_counts.index,
        'count': word_counts.values
    })
    
    # Save to output file
    output_file = os.path.join(output_directory, "part-00000")
    df.to_csv(output_file, sep='\t', header=False, index=False)
    
    # Create _SUCCESS file
    success_file = os.path.join(output_directory, "_SUCCESS")
    open(success_file, 'a').close()


if __name__ == "__main__":

    run_job(
        "files/input",
        "files/output",
    )
