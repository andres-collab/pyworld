class Joke:
  
    counter =0

    def __init__(self):
        Joke.counter += 1
        self.counter = 1

    def upone(self):
        self.counter += 1
