def format_string(text, formatter=None):
    """
    Format a string passed to it with a formatter function passes to it.
    if formatter isn't provided the default formatter formats the string to title case.
    """

    class DefaultFormatter:
        """Formats a string into title case"""

        def format(self, text):
            return str(text).title()

    if formatter == None:
        formatter = DefaultFormatter()

    return formatter.format(text)


def main():
    text = "Hello class with in a function!"
    print(format_string(text))


if __name__ == "__main__":
    main()
