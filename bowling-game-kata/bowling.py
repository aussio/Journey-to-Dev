class Game():
    
    def __init__(self):
        self.current_score = 0
        self.rolls = []
        self.NUMBER_OF_FRAMES = 10

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):  
        score = 0
        frame_index = 0

        for _ in range(self.NUMBER_OF_FRAMES):
            current_frame = self.rolls[frame_index] + self.rolls[frame_index + 1]
            if self.is_spare(current_frame):
                current_frame += self.rolls[frame_index + 2]
            score += current_frame
            frame_index += 2
        return score

    def is_spare(self, current_frame):
        return current_frame == 10
