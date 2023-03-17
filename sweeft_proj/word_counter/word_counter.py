class WordDict:
    def __init__(self, my_dict=None):
        if my_dict is None:
            self.my_dict = dict()
        else:
            self.my_dict = my_dict

    def add_new_word(self):
        new_one = input("enter the word.... \n")
        this_word = self.lowercase_english_word(new_one)
        if this_word in self.my_dict:
            self.my_dict[this_word] += 1
        else:
            self.my_dict.update({this_word: 1})

    def lowercase_english_word(self, word):
        for letter in word:
            if ord(letter) < ord('a') or ord(letter) > ord('z'):
                word = word.replace(letter, '')
        return word

    def sum_of_length(self):
        whole_length = 0
        for word in self.my_dict.keys():
            whole_length += len(word)
        if whole_length > pow(10, 6):
            print("the length mustn't be more then 10^6")

    def print_occurrences(self):
        print(len(self.my_dict))
        for element in self.my_dict.values():
            print(element, end=" ")


if __name__ == "__main__":
    my_obj = WordDict()
    number = int(input("Enter number of words..... "))
    for i in range(number):
        my_obj.add_new_word()
    my_obj.sum_of_length()
    my_obj.print_occurrences()