from NumberGame import NumberGame

game = NumberGame()

def new_game(d):
	try:
		count = int(d.get('count',[''])[0])
	except:
		return{'code':'error', 'msg':'count not given'}
	
	game.newGame(count)

	return {'code':'success'}

def guess(d):
	try:
		guess = int(d.get('guess', [''])[0])
	except:
		return {'code':'error', 'msg':'wrong guess parameter'}
	
	userGuess = game.guess(guess)
	trials = game.getGuessCount()

	return {'code':'success', 'msg': userGuess, 'trials':trials}
