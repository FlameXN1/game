import random

print("Welcome to hangman!")
WORDS_LIST = [
    "apple", "banana", "orange", "pea", "car", "jazz", "music", "cat", "math",
    "future", "rice", "shape", "sugar", "circle", "square", "triangle",
    "house", "mouse", "prisoner", "burger", "computer", "code", "train",
    "gun", "bone", "road", "study", "room", "pants", "shirt", "phone",
    "bottle", "water", "printer", "tissue", "degree"
]
word=random.choice(WORDS_LIST)
lives=7
is_running=True
hint=["_"]*len(word)
while is_running:
    print("".join(hint))
    answer=input("Enter a letter: ").lower()
    if len(answer)!=1 or not answer.isalpha():
        print("You can only input one letter")
        continue
    if answer in hint:
        print("You already input that")
        continue
    New_position=False
    for i in range(len(word)):
        if word[i]==answer and hint[i]=="_":
            hint[i]=answer
            New_position=True
    if not New_position:
        print("Incorrect input, you have",lives," lives left")
        lives-=1

    if "_" not in hint:
        print("Nice! U have won! The word was: ", word)
        is_running=False
    elif lives==0:
        print("You have ran out of lives! The word was: ", word)
        is_running=False
        