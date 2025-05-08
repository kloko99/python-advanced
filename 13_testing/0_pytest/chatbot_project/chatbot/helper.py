"""
Helper functions for the chatbot project.
"""


def clean_message(text):
    """Cleans the input message by stripping and converting to lowercase."""
    return text.strip().lower()


def count_words(text):
    """Zählt die Anzahl der Wörter in einem Text"""
    return len(text.strip().split())
