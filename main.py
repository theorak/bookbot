# A function that takes a dictionary and returns the value of the "count" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["count"]

# This function prints the actual book report
def print_report(book_path, words_count, characters):
    print(f"--- Begin report of {book_path} ---")
    print(f"{words_count} words found in the cocument")
    print()

    characters.sort(reverse=True, key=sort_on)
    for dict in characters:
        print(f"The '{dict['char']}' character was found {dict['count']} times")
    
    print("--- End report ---")

# Main function
def main():
    words_count = 0
    characters = []
    char_collection = {}
    book_path = "books/frankenstein.txt"

    with open(book_path) as f:
        file_contents = f.read()

    words = file_contents.split()
    words_count = len(words)

    for word in words:   
        lower_word = word.lower()    
        for char in lower_word:
            if char.isalpha():
                if char in char_collection:
                    char_collection[char] += 1
                else:
                    char_collection[char] = 1
    
    for char, count in char_collection.items():
        char_dict = {
            'char': char,
            'count': count
        }
        characters.append(char_dict)


    print_report(book_path, words_count, characters)

main()