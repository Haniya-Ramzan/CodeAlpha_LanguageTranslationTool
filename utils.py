import os
from datetime import datetime


def save_history(original_text, translated_text):
    """
    Saves every translation into history/history.txt
    """

    # Create history folder if it doesn't exist
    os.makedirs("history", exist_ok=True)

    history_file = os.path.join("history", "history.txt")

    with open(history_file, "a", encoding="utf-8") as file:

        file.write("\n")
        file.write("=" * 70 + "\n")
        file.write(f"Date & Time : {datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}\n")
        file.write("=" * 70 + "\n\n")

        file.write("Original Text:\n")
        file.write(original_text + "\n\n")

        file.write("Translated Text:\n")
        file.write(translated_text + "\n\n")

        file.write("-" * 70 + "\n")