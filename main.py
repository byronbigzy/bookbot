path_to_file = "books/frankenstein.txt"

def readFile(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

        print(file_contents)

def countWords(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

        words = file_contents.split()
        return len(words)

def countCharacters(path_to_file):
    characterCount = {}
    with open(path_to_file) as f:
        file_contents = f.read()    

        for char in file_contents.lower():
            if char in characterCount:
                characterCount[char] += 1
            else:
                characterCount[char] = 1

        return characterCount

def aggregateReport(path_to_file):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{countWords(path_to_file)} words found in the document\n")

    charCount = countCharacters(path_to_file)

    for char in charCount:
        if char.isalpha():
            print(f"'{char}': {charCount[char]}")

if __name__ == "__main__":
    # readFile(path_to_file)
    # countWords(path_to_file)
    # countCharacters(path_to_file)
    aggregateReport(path_to_file)