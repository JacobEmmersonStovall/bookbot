def report_book(path):
    with open(path) as f:
        content = f.read()
        words = content.split()
        letter_count = {}
        list_of_letter_counts = []
        print(f"--- Begin report of {path} ---")
        print(f"{len(words)} words found in the document")
        for word in words:
            for char in word.lower():
                if char.isalpha() and char in letter_count:
                    letter_count[char] += 1
                elif char.isalpha():
                    letter_count[char] = 1
        for key in letter_count:
            list_of_letter_counts.append((key, letter_count[key]))
        list_of_letter_counts.sort(key=lambda x: x[1], reverse=True)

        print("")
        for item in list_of_letter_counts:
            print(f"The '{item[0]}' character was found {item[1]} times")
        print("--- End report ---")

def main():
    book_paths = ["./books/frankenstein.txt"]
    for path in book_paths:
        report_book(path)

main()