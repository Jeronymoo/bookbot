import sys
from stats import get_num_words, count_characters, sort_dict

def get_book_text(path):
  with open(path) as f:
    file_contents = f.read()
    return file_contents

def print_report(book_path, num_words, sort_dict):
 print("============ BOOKBOT ============")
 print(f"Analyzing book found at {book_path}...")
 print("----------- Word Count ----------")
 print("Found 75767 total words")
 print("--------- Character Count -------")
 for i in sort_dict:
  if not i["char"].isalpha():
    continue
  print(f"{i['char']}: {i['amount']}")
 print("============= END ===============")

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  book_path = sys.argv[1]
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  characters = count_characters(text)
  list_sorted = sort_dict(characters)
  #print(f"{num_words} words found in the document")
  #print(characters)
  print_report(book_path, num_words, list_sorted)

main()