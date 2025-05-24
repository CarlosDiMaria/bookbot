from stats import get_word_count, get_chars_count, get_sorted_char_count_report
import sys

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  text = get_book_text(sys.argv[1])
  num_words = get_word_count(text)
  chars_count = get_chars_count(text)
  char_count_report = get_sorted_char_count_report(chars_count)
  print_char_report(num_words, char_count_report)


def get_book_text(file_path):
  with open(file_path) as f:
    return f.read()


def print_char_report(num_words, char_count_report):
  print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------")
  for c in char_count_report:
    print(f"{c["char"]}: {c["num"]}")
  print("============= END ===============")
main()