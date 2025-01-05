def char_counts(book_text):
  book = list(book_text.lower())
  chars = {}
  for char in book:
    if char in chars:
      chars[char] += 1
    else:
      chars[char] = 1
  return chars

def word_count(book_text):
  return len(book_text.split())

def book_agg_report(book_name):
  with open(book_name) as f:
    book_text = f.read()
    print(f"--- Begin report of {book_name} ---")
    print(f"{word_count(book_text)} words found in the document\n")

    cc = char_counts(book_text)
    for char, count in cc.items():
      if ord(char) >= ord('a') and ord(char) <= ord('z'):
        print(f"The {char} character was found {count} times")

    print("--- End Report ---")

def main():
  with open('books/frankenstein.txt') as f:
    # print(f.read())
    # print(word_count(f.read()))
    print(char_counts(f.read()))
  book_agg_report('books/frankenstein.txt')

if __name__ == '__main__':
  main()
