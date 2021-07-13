class TestShortPhrase:
    def test_short_phrase(self):
        max_lenght = 15
        phrase = input(f"Input a short phrase (less {max_lenght} symbols): ")
        lenght_phrase = len(phrase)

        assert lenght_phrase <= max_lenght, f"Phrase lenght is more than {max_lenght} symbols"
