import random


# We run this simulation 1,000,000 times and estimate the probability of either player winning
simulations = 1000000
lebron_wins = 0
davis_wins = 0

for i in range(0,simulations):
    game_over = False
    possession = ""
    winner = ""
    p = 0.3333

    # first we flip a coin
    coin = random.randint(1,2)
    if coin == 1:
        possession = "lebron"
    else:
        possession = "davis"

    while not game_over:
        if possession == "lebron":
            # now Lebron shoots with a 50/50 of win versus turnover to Davis
            lebron_shot = random.randint(1,2)
            if lebron_shot == 1:
                winner = "Lebron"
                game_over = True
            else:
                possession = "davis"
        else:
            # now Davis has a "p" chance of Lebron stealing the ball
            steal_attempt = random.random()
            if steal_attempt <= p:
                possession = "lebron"
            else:
                # lebron's steal failed, now Davis shoots with 50/50 odds
                davis_shot = random.randint(1,2)
                if davis_shot == 1:
                    winner = "Davis"
                    game_over = True
                else:
                    pass # (Davis is assumed to win all rebounds)
    
    # now we add our game results to the tracker
    if winner == "Davis":
        davis_wins += 1
    elif winner == "Lebron":
        lebron_wins += 1
    else:
        print("ERROR: winner var not set correctly in simulation.")

# after running all the simulations we output the results

# (first an error check)
if davis_wins + lebron_wins != simulations:
    print("ERROR: win count does not add up to simulation count.")

# now print out the results
print("Lebron win count: " + str(lebron_wins))
print("Davis win count: " + str(davis_wins))
print("Lebron odds: " + str(lebron_wins/simulations))
print("Davis odds: " + str(davis_wins/simulations))


