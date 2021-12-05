decks = open('input/day22input.txt', 'r').readlines()
p = 0
player_one_deck = []
player_two_deck = []
for card in decks:
    c = card.replace('\n', '')
    if c.isdigit():
        if p == 1:
            player_one_deck.append(int(c))
        else:
            player_two_deck.append(int(c))
    else:
        p += 1


def score(winner_deck):
    points = 0
    i = 1
    # print('winners deck: %s' %(winners_deck))
    while len(winner_deck) > 0:
        card = winner_deck.pop()
        points += i * card
        # print('card(%s): %s, score: %s' %(i, card, points))
        i += 1
    return points

def play_round(player_one, player_two):
    i = 0
    while min(len(player_one), len(player_two)) > 0:
        # print('Round: %s \ndeck a: %s\ndeck b: %s' %(i+1,  player_one, player_two))
        da = player_one.pop(0)
        db = player_two.pop(0)
        # print('a: %s vs b: %s' %(da, db))
        if da > db:
            player_one.append(da)
            player_one.append(db)
            if len(player_two) == 0 :
                # print('deck a is winner!')
                winning_deck = player_one
                # print(score(player_one))
        else: 
            player_two.append(db)
            player_two.append(da)
            if len(player_one) == 0:
                # print('deck b is winner!')
                winning_deck = player_two
                # print(score(player_two))
        # print('results\ndeck a: %s deck b: %s\n----' %(player_one, player_two))
        i += 1
    
    return winning_deck

player_one_deck_series = {}
player_two_deck_series = {}
player_deck_series = {}
game_count = 1
def play_recursive_combat(player_one, player_two, g):
    i = 1
    # print('\n=== Game %s ===\n' %(g)) ## sample output
    global game_count
    global player_one_deck_series
    global player_two_deck_series

    while min(len(player_one), len(player_two)) > 0:
        keya = tuple(player_one)
        keyb = tuple(player_two)
        if g not in player_deck_series:
            player_deck_series[g] = set()
        if keya in player_deck_series[g] or keyb in player_deck_series[g]:
            return 'a', player_one
        else:
            player_deck_series[g].add(keya)
            player_deck_series[g].add(keyb)
#         print('''
# -- Round %s (Game %s) --
# Player 1\'s deck: %s
# Player 2\'s deck: %s''' % (i, g, ', '.join(str(x) for x in player_one), ', '.join(str(x) for x in player_two)))  # sample output
        da = player_one.pop(0)
        db = player_two.pop(0)
#         print('''Player 1 plays: %s
# Player 2 plays: %s''' %(da, db)) ## sample output
        if db <= len(player_two) and da <= len(player_one):
            game_count += 1
            # print('Playing a sub-game to determine the winner...') ## sample output
            # print('i is %s when calling self with args: %s, %s, %s' % (
                # i, list(player_one[:da]), list(player_two[:db]), max(g, game_count))) ## DEBUG
            recurse_game = play_recursive_combat(list(player_one[:da]), list(player_two[:db]), max(g, game_count))
            winner = recurse_game[0]
            # print('\n...anyway, back to game %s.' %(g)) ## sample output
            if winner == 'a':
                # print('Player 1 wins round %s of game %s!' %(i, g)) ## sample output
                player_one.append(da)
                player_one.append(db)
                if len(player_two) == 0:
                    winner = 'a'
                    winning_deck = player_one
                    # print('The winner of game %s is player 1!' % (g)) ## sample output
            else:
                # print('Player 2 wins round %s of game %s!' % (i, g)) ## sample output
                player_two.append(db)
                player_two.append(da)
                if len(player_one) == 0:
                    winner = 'b'
                    winning_deck = player_two
                    # print('The winner of game %s is player 2!' %(g)) ## sample output
            

        elif da > db:
            # print('Player 1 wins round %s of game %s!' %(i, g)) ## sample output
            player_one.append(da)
            player_one.append(db)
            if len(player_two) == 0:
                winner = 'a'
                winning_deck = player_one
                # print('The winner of game %s is player 1!' % (g))## sample output
        else:
            # print('Player 2 wins round %s of game %s!' %(i, g)) ## sample output
            player_two.append(db)
            player_two.append(da)
            if len(player_one) == 0:
                winner = 'b'
                winning_deck = player_two
                # print('The winner of game %s is player 2!' % (g)) ## sample output
        i += 1

    return winner, winning_deck


game_one = play_round(list(player_one_deck), list(player_two_deck))
recursive_game = play_recursive_combat(list(player_one_deck), list(player_two_deck), int(1))
print('-----part one-----\nscore: %s\n-----part two-----\nscore: %s' %(score(game_one), score(recursive_game[1])))
