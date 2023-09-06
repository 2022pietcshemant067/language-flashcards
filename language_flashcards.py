import random

# Dictionary of flashcards (words and their meanings)
flashcards = {
    "apple": "a fruit",
    "book": "a written or printed work",
    "computer": "an electronic device for processing data",
    "dog": "a domesticated mammal",
    # Add more flashcards as needed
}

# Function to practice flashcards
def practice_flashcards():
    print("Welcome to the Language Flashcards program!")
    print("Enter 'exit' to quit the program.")
    
    while True:
        word = random.choice(list(flashcards.keys()))
        meaning = flashcards[word]
        
        print(f"What does '{word}' mean?")
        user_input = input("Your answer: ").strip().lower()
        
        if user_input == "exit":
            print("Goodbye! Thanks for practicing.")
            break
        elif user_input == meaning.lower():
            print("Correct! Great job!")
        else:
            print(f"Oops! That's not quite right. The correct answer is: '{meaning}'")

if _name_ == "_main_":
    practice_flashcards()