import random
from datetime import datetime

class AnimalLottoTicket:
    # A tuple of valid notes (immutable, replacing the Ruby constant array)
    NOTES = ('Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G')

    def __init__(self, note1, note2, note3):
        """Creates a new ticket from three chosen notes."""
        picks_list = [note1, note2, note3]
        
        # Check for duplicates by comparing list length to set length
        if len(set(picks_list)) != 3:
            raise ValueError("The three picks must be different notes.")
            
        # Check if any pick is missing from the valid NOTES
        if any(pick not in self.NOTES for pick in picks_list):
            raise ValueError("The three picks must be notes in the chromatic scale.")
            
        # Store picks as a frozen set to protect them from being changed
        self._picks = frozenset(picks_list)
        self._purchased = datetime.now()

    @property
    def picks(self):
        """Read-only property for ticket picks."""
        return self._picks

    @property
    def purchased(self):
        """Read-only property for purchase timestamp."""
        return self._purchased

    def score(self, final):
        """Score this ticket against the final draw."""
        count = 0
        for note in final.picks:
            if note in self.picks:
                count += 1
        return count

    @classmethod
    def new_random(cls):
        """Class method constructor to create a random AnimalLottoTicket."""
        while True:
            try:
                # Pick three random choices from the NOTES tuple
                return cls(
                    random.choice(cls.NOTES),
                    random.choice(cls.NOTES),
                    random.choice(cls.NOTES)
                )
            except ValueError:
                # If duplicates are picked, the error is caught and it retries
                continue

AnimalLottoTicket.NOTES = ('TOOT', 'TWEET', 'BLAT')
