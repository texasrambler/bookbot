def main(args, *kwargs):
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        words = file_contents.split()
        chars = {}
        for i in range(0, len(file_contents)):
            c = file_contents[i]
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
        print('--- Begin report of books/frankenstein.txt ---')
        print(f'{len(words)} words found in the document')
        print()
        for k, v in chars.items():
            if str(k).isalpha() and not str(k).isspace():
                print(f"The '{k}' character was found {v} times")
        print("--- End report ---")
main(None)
