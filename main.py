# Main function that will read a text file and print the text.
def main():
    # This will open a file from a specified path
    with open("books/frankenstein.txt") as f:
        # Reads contents from the file and sets it in a variable file_contents
        file_contents = f.read()
        return file_contents

# word_count variable stores the length of the string input removing the whitespace using the split() string method.
def word_count(data):
    word_count = len(data.split())
    return f"{word_count} words found in the document"

character = {}
dedupe = set()

def count_characters(data):

    for d in data.lower():
        dedupe.add(d)
    for c in dedupe:
        character[c] = 0
    for d in data.lower():
        if d in character:
            character[d] += 1
    return character

def word_aggragate():
    count_characters(main())

    print("--- Begin report of books/frankenstein.txt ---")
    print(word_count(main()))

    for c in character:
        print(f"The {c} character was found {character[c]} times")

    print("--- End report ---")

word_aggragate()
    