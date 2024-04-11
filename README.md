
# Convert HTML to Text in Python

This Python script, `convert_html_to_text.py`, is designed to convert HTML files into plain text files.
It uses the BeautifulSoup library to parse and extract the text content from HTML documents.

'pip install html2text` must be completed before code activation
'pip install beautifulsoup4'pip install beautifulsoup4 must be completed prior to code activation
The code assumes that the HTML files are well-formed and can be parsed by BeautifulSoup. If your HTML files are not standard, you may need to adjust the parsing logic accordingly.

## How it works

The script starts by importing necessary libraries, including `logging` for logging messages,
`subprocess` is for using external commands, and `BeautifulSoup` is for parsing HTML.

It then sets up basic logging with a specified format and level to provide information and error messages
during the conversion process.

The core of the script is the `convert_html_to_text` function, which takes two arguments: `html_file` (the input HTML file)
and `txt_file` (the output text file).

The function opens the HTML file for reading, uses BeautifulSoup to parse its content, extracts the text content
using `soup.get_text()`, then writes the extracted text to the specified output text file (txt_file) in UTF-8 encoding.

After successful conversion, the script logs a message indicating the conversion from the HTML file to the text file.

If any exception occurs during the conversion process, the script logs an error message and attempts to use the
`html2text` command-line tool as a fallback.

If BeautifulSoup fails to convert the HTML file, the script uses the `html2text` command-line tool, a
dedicated tool for converting HTML to text. It captures the output and error messages from `html2text` and logs them
accordingly.

If `html2text` also fails, the script logs an exception message indicating the failure.

In summary, this script provides a convenient way to convert HTML files to text files using `BeautifulSoup` and
handles potential errors by attempting to use the `html2text` command-line tool as a fallback.
It logs informative messages throughout the process to update you on the conversion status.
