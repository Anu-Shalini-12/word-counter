def word_count(text):
    """Count the number of words in the given text."""
    words = text.split()
    return len(words)

# Get multiple lines of user input
print("Enter paragraphs or sentences (press Enter twice to finish):")
user_input_lines = []

try:
    while True:
        line = input()
        if not line:
            break
        user_input_lines.append(line)

    # Combine lines into a single string
    user_input = " ".join(user_input_lines)

    # Check for empty input
    if not user_input.strip():
        raise ValueError("Error: No input provided.")

    # Count words
    count = word_count(user_input)

    # Display the result
    print(f"\nTotal word count: {count}")

except Exception as e:
    print(f"An error occurred: {e}")
