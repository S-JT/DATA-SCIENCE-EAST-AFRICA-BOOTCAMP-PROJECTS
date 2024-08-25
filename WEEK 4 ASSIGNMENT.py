                   #QUESTION 1
#1'A PALINDROME IS A STRING OR A NUMBER THAT ARE SIMILAR WHEN THEY ARE REVERSED
#2'let us use these strings and numbers to test out how to do this. ( RADAR, 12321, QUEUE)
#3'.string_1 is RADAR, String_2 is 12321 and string_3 is queue
#4'Reversed function can be used to check if the string is a palindrome as shown below
#5' The reverse function creates different types of data for these two inputs therefore this has to be changed to a list in order to itemize each character in the strings before running the code.

text_1 = "RADAR"
text_2 = "12321"
text_3 = "QUEUE"

string_1 = reversed(text_1)
string_2 = reversed(text_2)
string_3 = reversed(text_3)

print(type(text_1))
print(type(string_1))

if list(text_1) == list(string_1):
    print("True")

if list(text_2) == list(string_2):
    print("True")

if list(text_3) == list(string_3):
        print("True")
else:print("False")

                                #"QUESTION 2"
## LIST COMPREHENSION - This is a syntax construction that allows for creation of lsts within an existing list to avoid writing a for statement for each instance.
## Example 1: Seasons. If the required output is those seasons with S, the code below can be used to callout such data from the existing dataset provided.

Seasons = ["summer", "spring", "autumn", "winter"]
new_list = []

for x in Seasons:
    if "s" in x:
        new_list.append(x)

    print(new_list)

#Example 2: where the required dataset should contain all seasons except 'Summer'.

newlist = [x for x in Seasons if x != "summer"]

for x in Seasons:
    if "summer" in x:
        new_list.append(x)

    print(newlist)


#Example 3: where the required dataset should contain a range of data.

Wind_Speed = ["4", "6", "7", "9", "13", "15", "19", "20", "24", "26", "32","33", "35", "39", "43", "44"]
new_list_2 = [x for x in range(50) if x > 22]
print(new_list_2)

      #QUESTION 3
#compound datatypes: Compound data types are made up of more than one component. They are data types that are formed from the existing data tyes in python.
# default python data types include: strings,integers,float,complex,list,tuple,range, bool,bytes etc.

#EXAMPLE 1: String
df = "Weather"
print(df)
print(type(df))

#EXAMPLE 2: List and Tuple
#A list is an array of objects and can be changed/altered. Tuples are just like lists but they are immutable/cannot be altered

#LIST:Array of data is closed with square brackets
Seasons = ["summer", "spring", "autumn", "winter"]
print(type(Seasons))

#TUPLE: Array of data is closed with curved brackets
Seasons_1= ("summer", "spring", "autumn", "winter")
print(type(Seasons_1))


#EXAMPLE 3: SETS and DICTIONARIES
# Sets are used to categorize data into specific groups and can be used to drop duplicates in a dataset.
# Sets can be used to convert a list to a set
#Example
Wind_speed_set ={"Wind_Speed"}
print(type(Wind_speed_set))


#Dictionaries are used to store unique / data keys that may need to be stored e.g Names and other unique identifiers
#while using dictionaries, colons are used to define terms/data keys intended to be stored for future use
mydict = {"name":"Janice","National Id":"300000001", "Nationality":"Kenyan"}
print(type(mydict))

#QUESTION 4: string and bigrams.
# writing functions that takes string and returns a list of bigrams.
#Bigrams are 2 words that when used together create a distinct meaning.
#trigrams are 3 words that when used together create a distinct meaning

#The first step is to split the text to a list of words.
#secondly, bigrams will be generated to create word pairs that are adjacent to each other
#Thirdly, the bigrams will be returned
#Example:

def generate_bigrams(Text):
    Words = Text.split()
    bigrams = [(Words[i], Words[i + 1]) for i in range(len(Words) - 1)]

    return bigrams

Text = "Flooding crisis in Kenya"
bigrams = generate_bigrams(Text)
print(bigrams)

#QUESTION 5: DICTIONARY
#dictionary with keys as letters and values as lists of letters
#Dictionaries are used to create key identifiers in this case, they will be letters (alphabetical)
#In this example values will be a list of letters (Numerical)
# the zip operator is used to match up items in each list to create a tuple
#after zipping, a dictionary is created for each specific item on the list (alphabetical) to match up with the respective value(numerical)
drinks = ["water", "soda", "beer", "wine", "whiskey"]
quantity =[20,5,10,4,3]

print([item for item in zip(drinks,quantity)])

drinks_dict =dict(zip(drinks,quantity))
print(drinks_dict)

for key in drinks_dict.items():
    print(key)

#to define the closes key index, a target value can be used to check if it is in the dataset or indicates which value is closest
#Example.

drinks_dict = {'water': 20, 'soda': 5, 'beer': 10, 'wine': 4, 'whiskey': 3}

def closest_key(drinks_dict,target_value):
    closest_key = None
    closest_index = float('inf')

    for key, value_list in drinks_dict.items():
        if target_value in value_list:
            index = value_list.index(target_value)
            if index < closest_index:
                closest_index = index
                closest_key = key

    return closest_key
























