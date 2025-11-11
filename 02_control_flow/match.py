"""Python match-case is for pattern matching, allowing execution based on value patterns."""

# Example 1: Basic match-case statement

command = "start"

"""Use _ as a wildcard to match any value not explicitly handled. This is basically the default case."""

match command:
    case "start":
        print("System starting...")
    case "stop":
        print("System stopping...")
    case _:
        print("Unknown command.")


# Example 2: Match-case with multiple patterns

status = 404
"""Use | as an or operator in match-case statements"""
match status:
    case 200 | 201:
        print("Success!")
    case 400 | 404:
        print("Client error.")
    case 500 | 503:
        print("Server error.")
    case _:
        print("Unknown status code.")

# Example 3: Match-case with guards
score = 85

match score:
    case s if s >= 90:
        print("Excellent score.")
    case s if s >= 75:
        print("Good score.")
    case s if s >= 60:
        print("Passable score.")
    case _:
        print("Poor score.")
