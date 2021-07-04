class TestShortPhrase:
    def test_short_phrase(self):
        max_lenght = 15
        phrase = input("Input a short phrase (less 15 symbols): ")
        lenght_phrase = len(phrase)

        assert lenght_phrase <= 15, f"Phrase lenght is more than {max_lenght} symbols"
