# 📘 Assignment: Python Text Processing

## 🎯 Objective

Practice string manipulation, file I/O, and basic text-processing techniques by building small utilities that analyze and transform text files.

## 📝 Tasks

### 🛠️ Build text-processing utilities

#### Description
Implement a Python program that reads a text file and provides multiple text-processing features such as word counts, most common words, search-and-replace, and line trimming. The program should be runnable from the command line and accept the input filename as an argument.

#### Requirements
Completed program should:

- Read a UTF-8 text file specified by the user.
- Provide a function to count total words and unique words.
- Report the top N most frequent words (N configurable).
- Support a search-and-replace operation that outputs the transformed text to a new file.
- Handle basic punctuation and case normalization when counting words.
- Gracefully handle missing files with a clear error message.

#### Example usage
```
# Count words
python starter_text_processing.py sample.txt --count

# Show top 10 words
python starter_text_processing.py sample.txt --top 10

# Replace 'foo' with 'bar' and write to out.txt
python starter_text_processing.py sample.txt --replace foo bar --out out.txt
```

**Skills practiced:** File I/O, string methods, regular expressions, dictionaries, CLI argument parsing

**Starter files:** `starter_text_processing.py`, `sample.txt`
