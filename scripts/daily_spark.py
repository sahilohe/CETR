import random

def get_daily_spark():
    """
    Returns a random curiosity-sparking problem or question.
    In future iterations, this could pull from a curated offline library.
    """
    sparks = [
        "Why do some plants have thorns?",
        "How can we count to 100 in a different way?",
        "Design the tallest stable tower you can build.",
        "Create an algorithm that sorts a list of numbers.",
        "Why do cats have whiskers?",
        "Invent a new way to represent fractions.",
        "What would happen if the Earth stopped spinning?",
        "How do birds fly without an engine?",
        "If you could invent a new color, what would it look like and what would you call it?",
        "How does a light bulb work?",
    ]
    return random.choice(sparks)

def main():
    print("✨ Your Daily Spark of Curiosity! ✨\n")
    print(get_daily_spark())
    print("\n-------------------------------------\n")
    print("Think, conjecture, explain, test, refine!")

if __name__ == "__main__":
    main()

