# -*- coding: utf-8 -*-

import random

class NumberGame:
    def __init__(self):
        self.digits = 0
        self.trials = 0


    def newGame(self, count):
        self.digits = random.randint(1, count)
        self.trials = 0
	self.limit = count

    def guess(self, userGuess):
        self.trials += 1

        if userGuess < self.digits:
            msg = "Greater"
        elif userGuess > self.digits:
            msg = "Smaller"
        else:
            msg = "Success"

	if userGuess > self.limit:
	    msg = "최대 범위 초과"

	if userGuess <= 0:
	    msg = "자연수만 입력하세요."

	return msg

    def getGuessCount(self):
        return self.trials

if __name__ == '__main__':
    game = NumberGame()
    count = int(input("범위의 최대 숫자를 지정하세요: "))
    game.newGame(count)

    while True:
        userGuess = int(input("추측한 숫자를 입력하세요: "))
        print(game.guess(userGuess))

        if userGuess == game.digits:
            break

    print("SUCCESS in %d trials" % game.getGuessCount())
