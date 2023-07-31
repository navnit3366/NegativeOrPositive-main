import string

def check(file_name, string_to_search):
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            #List of words (without punctuation)
            words = [word.strip(string.punctuation) for word in line.split()]
            if string_to_search in words:
                return True
    return False

while True:
  word = input('Check if word is positive | ')
  if check('positivewords.txt', word):
    print('The word is positive')
  elif check('negativewords.txt', word):
    print('Word is negative')
  else:
    print('Word is not in database')
    addWord = input('should word be added? | ')
    if addWord == 'yes':
      addNegOrPos = input('should we add it to the negative file, or the positive file? | ')
      if addNegOrPos == 'positive':
        with open("positivewords.txt", "a+") as file_object:
        # Move read cursor to the start of file.
          file_object.seek(0)
          # If file is not empty then append '\n'
          data = file_object.read(100)
          if len(data) > 0 :
              file_object.write("\n")
        with open("positivewords.txt", "a") as myfile:
          myfile.write(word)
        print('done!')
      elif addNegOrPos == 'negative':
        with open("negativewords.txt", "a+") as file_object:
        # Move read cursor to the start of file.
          file_object.seek(0)
          # If file is not empty then append '\n'
          data = file_object.read(100)
          if len(data) > 0 :
              file_object.write("\n")
        with open("negativewords.txt", "a") as myfile:
          myfile.write(word)
        print('done!')
    elif addWord == 'no':
      print('ok')
