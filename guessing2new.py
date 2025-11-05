import random

words_list = [
    "apple", "banana", "cherry", "dates", "elderberry",
    "fig", "grape", "honeydew", "kiwi", "lemon",
    "mango", "nectarine", "orange", "peach", "quince",
    "raspberry", "strawberry", "tangerine", "ugli", "vanilla",
    "watermelon", "xigua", "yam", "zucchini", "apricot",
    "blueberry", "coconut", "dragonfruit", "eggplant", "guava"
]
lives=7
word=random.choice(words_list)
hints=["_"]*len(word)
wrong=[]

def main(lives,hints,word,wrong):
    if "_" not in hints:
         print(f"You win! The word was {"".join(hints)}")
         return hints
    elif lives<=0:
         print(f"You ran out of lives! The word was {word}")
         return 
    print("".join(hints))
    answer=input("Enter a letter: ").lower()
    if len(answer)!=1 or answer.isalpha()==False:
            print("You can only enter a letter!")
            return main(lives,hints,word,wrong)

    elif answer in hints or answer in wrong:
         print("You already input",answer)
         return main(lives,hints,word,wrong)

    New_position=False
    for i in range(len(word)):
        if word[i]==answer and hints[i]=="_":
            hints[i]=answer
            New_position=True
    if not New_position:
        lives-=1
        wrong.append(answer)
        print("Wrong letter! You have",lives,"lives left")
    main(lives,hints,word,wrong)
    return hints
final=main(lives,hints,word,wrong)
