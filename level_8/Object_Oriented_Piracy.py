# Task
# You have access to the ship "draft" and "crew". "Draft" is the total ship weight and "crew" is the number of humans on the ship.
# Each crew member adds 1.5 units to the ship draft. If after removing the weight of the crew,
# the draft is still more than 20, then the ship is worth looting. Any ship weighing that much must have a lot of booty!
# Add the method
# is_worth_it

class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        return True if self.draft - 1.5 * self.crew > 20 else False