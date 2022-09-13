import pandas

alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_frame = pandas.DataFrame(alphabet_data)

nato_dict = {row.letter: row.code for (index, row) in data_frame.iterrows()}

user_input = (input("Type your word: ")).upper()

code_word = [nato_dict[letter] for letter in user_input]

print(code_word)

