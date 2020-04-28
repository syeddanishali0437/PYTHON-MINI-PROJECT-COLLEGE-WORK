# PYTHON MINI PROJECT  Mad LibS STORY generator.
madlib = '''On the {} trip to {}, my {} friend and I decided to invent a game. Since 
this would be a rather {} trip, it would need to be a game with {} and {}. 
Using our {} to {}, we tried to get the {} next to us to play too, but they 
just {}ed at us and {} away. After a few rounds, we thought the game could 
use some {}, so we turned on the {} and started {} to the {} that came on. 
This lasted for {} before I got {} and decided to {}. I ll never {} that trip, 
it was the {} road trip of my {}.'''


# A list storing the blanks for the Mad Lib
blanks = [
    "adjective",
    "place",
    "adjective",
    "adjective",
    "noun, plural",
    "noun, plural",
    "noun",
    "verb",
    "noun",
    "verb",
    "action verb",
    "noun, plural",
    "noun",
    "verb that ends in ing",
    "noun",
    "measurement of time",
    "adjective",
    "action verb",
    "verb",
    "adjective",
    "noun, something you can own"
]
print("Road Trip Mad Lib\nWhen the program asks you, please enter the appropriate word.")
print("There are %i blanks in SYED DANISH ALI & AMANPREET SINGH  Mad Lib. " % (len(blanks)))
# Ask the user for each one
answers = []
for blank in blanks:
    ans = ""
    while not ans:
        ans = input(blank.capitalize() + "> ")
        if not ans:
            print("Please don't leave anything blank. It kills the experience.")
    answers.append(ans)
# The list that stores the format string


# Print the formatted Mad Lib
print(madlib.format(*answers))
feedback = input("Pretty funny, right? [y/n] ")
if feedback.lower() == "y":
    print("Thanks!")
else:
    print(":( Sorry. I'll try better next time.")
print("\n" + "="*10 + "\nMad Lib PROJECTED BY::-\nSYED DANISH ALI 2K18CSUN01043  & AMANPREET SINGH 2K18CSUN01008   CSE-4C \n CREATED ON DATE:- 28/04/2020 :: UPLOADED ON GITHUB:-28/04/2020 :: UPLOADED ON ERP:- 28/04/2020") 