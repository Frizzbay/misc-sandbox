"""
Seven Segment Display Simulator
==============================

This program simulates a seven-segment display using ASCII characters.
Each digit (0-9) is represented using a 3x5 grid pattern where:
- '#' represents an LED that is ON
- ' ' represents an LED that is OFF

The program takes a string of digits as input and displays them
side-by-side in seven-segment format.
"""

def create_digit_patterns():
    """
    Creates and returns a dictionary mapping digits (0-9) to their
    corresponding seven-segment display patterns.
    
    Each pattern is a multi-line string representing a 3x5 grid.
    """
    patterns = {
        0: """
###
# #
# #
# #
###
""",
        1: """
#
#
#
#
#
""",
        2: """
###
  #
###
#
###
""",
        3: """
###
  #
###
  #
###
""",
        4: """
# #
# #
###
  #
  #
""",
        5: """
###
#
###
  #
###
""",
        6: """
#
#
###
# #
###
""",
        7: """
###
  #
  #
  #
  #
""",
        8: """
###
# #
###
# #
###
""",
        9: """
###
# #
###
  #
  #
"""
    }
    return patterns


def display_seven_segment(input_string):
    """
    Displays the input string in seven-segment format.
    
    Args:
        input_string (str): String of digits to display
    
    The function works by:
    1. Converting each digit pattern into a list of rows
    2. Printing corresponding rows from all digits side-by-side
    """
    # Get the digit patterns
    digit_patterns = create_digit_patterns()
    
    # Store all digit patterns as lists of rows
    all_patterns = []
    
    # Process each digit in the input
    for digit_char in input_string:
        # Convert character to integer for dictionary lookup
        digit_num = int(digit_char)
        
        # Get the pattern for this digit
        pattern = digit_patterns[digit_num]
        
        # Split pattern into individual rows, removing extra whitespace
        rows = pattern.strip().split("\n")
        
        # Add this digit's rows to our collection
        all_patterns.append(rows)
    
    # Print all digits side-by-side, row by row
    for row_index in range(5):  # Each digit has 5 rows
        line = ""
        
        # Get the same row from each digit pattern
        for pattern in all_patterns:
            line += pattern[row_index] + " "  # Add space between digits
        
        print(line.rstrip())  # Remove trailing space and print


def main():
    """
    Main function to get user input and display the seven-segment output.
    """
    try:
        # Get input from user
        user_input = input("Enter values: ")
        
        # Validate input contains only digits
        if not user_input.isdigit():
            print("Error: Please enter only digits (0-9)")
            return
        
        # Display the seven-segment representation
        display_seven_segment(user_input)
        
    except KeyboardInterrupt:
        print("\nProgram terminated by user")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
