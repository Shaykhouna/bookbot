def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	words = text.split()
	#print(text)
	#print(len(words))
	letters_dict = {}
	for letter in range(ord('a'),ord('z')+1):
		letters_dict[chr(letter)] = get_letter_count(text.lower(), chr(letter))
	#print(letters_dict)
	letters_list = list(letters_dict.items())
	letters_list.sort(reverse=True,key=reference_key)
	print("---> Your selected Book Report <---")
	print()
	print(f"number of words: {len(words)}")
	print()
	for element in range(0, len(letters_list)):
		print(f"The number of letter \"{letters_list[element][0]}\" in the Book is: {letters_list[element][1]}")
	print()
	print("Report Completed successfully.")
def reference_key(element):
	return element[1]


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_letter_count(text, letter):
	count = 0
	for index in range(0,len(text)):
		if text[index] == letter:
			count = count + 1
	return count

main()
