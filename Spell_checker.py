from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()
        
    def correct_text(self, text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected = self.spell.correction(word)
            if corrected != word:
                print(f'Correcting "{word}" to "{corrected}"')
            corrected_words.append(corrected)

        return ' '.join(corrected_words)
    
    def run(self):
        print("\n---- Spell Checker ----")

        while True:
            text = input('Enter text to check (or type "exit" to quit): ')

            if text.lower() == "exit":
                print("Closing the program....")
                break

            corrected_text = self.correct_text(text)
            print(f"Corrected Text: {corrected_text}")


if __name__ == "__main__":
    app = SpellCheckerApp()
    app.run()
