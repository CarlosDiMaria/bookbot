def get_word_count(string):
  words = string.split()
  return len(words)

def get_chars_count(string):
  chars_count = {}
  for char in string:
      if not char.isalpha():
         continue
      char = char.lower()
      if chars_count.get(char):
        chars_count[char] += 1
      else:
         chars_count[char] = 1
  return chars_count

def get_sorted_char_count_report(chars_count):
  report_list = []
  for char in chars_count:
    report_list.append({"char": char, "num": chars_count[char]})
  report_list.sort(reverse=True, key=lambda dict: dict["num"])
  return report_list