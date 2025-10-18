import sys
from stats import get_book_text
from stats import count 
from stats import count_character
from stats import sort_dictionary

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path=sys.argv[1]
    words = count(get_book_text(path))
    dict = count_character(get_book_text(path))
    sorted = sort_dictionary(dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print("Found",words, "total words")
    print("--------- Character Count -------")
    for item in sorted:
        ch=item["char"]
        val=item["num"]
        if ch.isalpha():
            print(f"{ch}: {val}")
    print("============= END ===============")


if __name__ == "__main__":
    main()