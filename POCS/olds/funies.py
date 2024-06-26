from jokes import Joke 


def reverando(input):
    return input[::-1]

joke = Joke()
joke.upone()
joke.upone()

otroJoke= Joke()

masJoke= Joke()

print("Bromas count " + str(joke.counter))

print("Bromas count " + str(Joke.counter))
