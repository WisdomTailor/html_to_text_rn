"""
This script recursively traverses through a given root directory, 
identifies all 'index.htm' files within subdirectories,
converts them to plain text using BeautifulSoup, 
and saves the output text files with corresponding subdirectory names
in a specified output directory.
"""
import os
import logging
from bs4 import BeautifulSoup

# Configure logging to include time, logging level, and message
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def convert_html_to_text(html_file, txt_file):
    """
    Converts the content of an HTML file to plain text and saves it in a text file.

    :param html_file: Path to the input HTML file.
    :param txt_file: Path to the output text file where plain text will be saved.
    """
    try:
        with open(html_file, 'r', encoding='utf-8') as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, 'html.parser')
        text = soup.get_text()

        with open(txt_file, 'w', encoding='utf-8') as file:
            file.write(text)

        logging.info("Converted %s to %s", html_file, txt_file)

    except FileNotFoundError:
        logging.error(f"File not found {html_file}")
    except Exception as e:
        logging.error("Failed to convert HTML to text: %s", e)

def process_directory(root_dir, output_dir):
    """
    Walks through all subdirectories of the given root directory, looking for 'index.htm' files to convert.

    :param root_dir: Root directory to start processing from.
    :param output_dir: Output directory to save the converted text files.
    """
    for subdir, _, files in os.walk(root_dir):
        for filename in files:
            if filename.lower() == 'index.htm':
                file_path = os.path.join(subdir, filename)
                subfolder_name = os.path.basename(subdir)
                output_txt_file_path = os.path.join(output_dir, f"{subfolder_name}.txt")
                convert_html_to_text(file_path, output_txt_file_path)

if __name__ == "__main__":
    # Define the root directory containing subfolders with 'index.htm' files
    root_directory = r"D:\Literotica Stories\s"
    # Define the directory where you want to save the output text files
    output_directory = r"D:\Literotica Stories\Stories text"

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    process_directory(root_directory, output_directory)
