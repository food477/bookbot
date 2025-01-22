def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)
        # ...

def count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    counter = 0
    for word in file_contents.split():
        counter += 1
    # print(counter)
    return counter
    # ...

def chr_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    lc_words = file_contents.lower()
    letter_dic = {}

    for letter in lc_words:    
        letter_dic[letter] = letter_dic.get(letter, 0) + 1
    return letter_dic
    
def sort_on(letter_dic):
    return letter_dic["num"] 
  
def sort_report(letter_dic):
    char_list= []
    for char, num in letter_dic.items():
        if char.isalpha():
            char_dic = {"char": char, "num": num}
            char_list.append(char_dic)
    char_list.sort(reverse=True, key=sort_on)
    return char_list

if __name__ == "__main__":
    main()
    wordcount = count()
    char_counts = chr_count()
    sorted_chars = sort_report(char_counts)
    print("--- Begin report of books/frankenstein.txt ---")
    print(wordcount, "words found in the document")

    for x in sorted_chars:
        print("The '"+x["char"]+"' character was found", x["num"],"times")
            


    