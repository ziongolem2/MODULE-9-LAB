Saul 
Resendiz


			WEEK MODULE 9 LAB

	QUESTION #1:

# DICTIONARIES:
room_numbers = {'CS101': '3004', 'CS102': '4501', 'CS103': '6755', 'NT110': '1244', 'CM241': '1411'}

professors = {'CS101': 'Haynes', 'CS102': 'Alvarado', 'CS103': 'Rich', 'NT110': 'Burke', 'CM241': 'Lee'}

meeting_times = {
    "CS101": '8:00 a.m.',
    "CS102": '9:00 a.m.',
    "CS103": '10:00 a.m.',
    "NT110": '11:00 a.m.',
    "CM241": '1:00 p.m.'
		}

# getting user input for course number to seaarch dictionaries
course_number = input("Please enter a course number: ")

# Search input in dictionaries and print info if available
if course_number in room_numbers:
    user_room = room_numbers[course_number]
    user_professor = professors[course_number]
    user_meeting_time = meeting_times[course_number]

    print("COURSE INFORMATION DETAILS:")
    print("-------------------------------")
    print(f" Course Room Number: {user_room}")
    print(f" Course Professor: {user_professor}")
    print(f" Course Meeting Time: {user_meeting_time}")
else:
    print("Course number was not found in our list of available courses.")


	QUESTION #2:

NUM_STATES = 5

def main():
    state_caps = state_cap_dictionary()
    
    correct = 0
    incorrect = 0
    
    # Quzzing User
    for count in range(NUM_STATES):
        state, capital = state_caps.popitem()
        
        print('What is the capital of ', state, '?', end ='')
        response = input()
        
        if response.lower() == capital.lower(): 
            correct += 1 
            print('Correct!')
        else: 
            incorrect += 1
            print('Incorrect.')
            
    print('Correct Responses:', correct)
    print('Incorrect Responses:', incorrect)
            
def state_cap_dictionary():
    
    sc = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'}
    
    return sc
    
main()


	QUESTION #3:

codes = {
 'A': '%', 'a': '9', 'B': '@', 'b': '#'
 }
 
 #file encryption
 def encrypt_file(input_file, output_file):
    with open(input_file, 'r') as infile:
        data = file.read()
    encrypted_data = ''.join(codes.get(char, char) for char in data)
    with open(output_file, 'w') as outfile:
        outfile.write(encrypted_data)

# decrypting now
def decrypt_file(input_file):
    with open(input_file, 'r') as infile:
        encrypted_data = file.read()
    decrypted_data = ''.join([codes.get(char, char) for char in encrypted_data])
    print(decrypted_data)

	
	QUESTION #4:

def unique_words_found(filename):
    unique_words = set()
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    # adding format validation to our word
                    if word.isalnum():  # if alphanumeric
                        word = word.lower()  
                        # adding the finalized word to our set
                        unique_words.add(word) 
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

    # printing all unique words from set
    print(unique_words)

# Get filename from user input
filename = input('Enter txt file name: ')
# run our function
unique_words_found(filename)

	
	QUESTION #5:

def store_word_frequency(file_name):
    word_frequency = {}   #creating frequency dictionary
    with open(file_name, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.isalnum():
                    word = word.lower()  
                else: # if it is not a proper word, skip
                    continue
                if word not in word_frequency:
                    word_frequency[word] = 1
                else:
                    word_frequency[word] += 1
    return word_frequency    #returning word frequency dictionary

# displaying how much time the word appeared
def display_word_frequency(word_frequency):
    for word, frequency in word_frequency.items():
        print(f"'{word}': {frequency}")
# creating the file
def create_word_frequency_file(word_frequency):
    with open('word_frequency.txt', 'w') as output_file:
        for word, frequency in word_frequency.items():
            output_file.write(f"'{word}': {frequency}\n")

def main():
    file_name = input('Enter txt file name: ')
    word_frequency = store_word_frequency(file_name)
    print("WORD FREQUENCIES:")
    display_word_frequency(word_frequency)
    create_word_frequency_file(word_frequency)


	QUESTION 6:

def file_words_to_set(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
        return set(words)  # returns a set of the words list

def main():
    user_file1 = input("Enter 1st file name: ")
    user_file2 = input("Enter 2nd file name: ")

    # reading the data of the given files into sets
    set1_words = file_words_to_set(user_file1)
    set2_words = file_words_to_set(user_file2)

    # implementing set methods
    unique_words = set1_words.union(set2_words)
    alike_words = set1_words.intersection(set2_words)
    in_first_not_second = set1_words.difference(set2_words)
    in_second_not_first = set2_words.difference(set1_words)
    in_either_not_both = set1_words.symmetric_difference(set2_words)

    # printing the methods of the files:
    print("\nUNIQUE WORDS:")
    print(unique_words)

    print("\nWORDS IN BOTH FILES:")
    print(alike_words)

    print("\nWORDS IN 1ST BUT NOT 2ND FILE:")
    print(in_first_not_second)

    print("\nWORDS IN 2ND BUT NOT 1ST FILE:")
    print(in_second_not_first)

    print("\nWORDS IN EITHER FILE, NOT BOTH:")
    print(in_either_not_both)

main()

