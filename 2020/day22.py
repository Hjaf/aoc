decks = open('day22input.txt', 'r').readlines()
p = 0
player_one_deck = []
player_two_deck = []
for card in decks:
    c = card.replace('\n', '')
    if c.isdigit():
        if p == 1:
            player_two_deck.append(int(c))
        else:
            player_one_deck.append(int(c))
    else:
        p += 1

def score(winners_deck):
    points = 0
    i = 1
    print('winners deck: %s' %(winners_deck))
    while len(winners_deck) > 0:
        card = winners_deck.pop()
        points += i * card
        print('card(%s): %s, score: %s' %(i, card, points))
        i += 1
    return points

def play_round(deck_a, deck_b):
    i = 0
    while min(len(deck_a), len(deck_b)) > 0:
        # print('Round: %s \ndeck a: %s\ndeck b: %s' %(i+1,  deck_a, deck_b))
        da = deck_a.pop(0)
        db = deck_b.pop(0)
        # print('a: %s vs b: %s' %(da, db))
        if da > db:
            deck_a.append(da)
            deck_a.append(db)
            if len(deck_b) == 0 :
                print('deck a is winner!')
                print(score(deck_a))
        else: 
            deck_b.append(db)
            deck_b.append(da)
            if len(deck_a) == 0:
                print('deck b is winner!')
                print(score(deck_b))
        # print('results\ndeck a: %s deck b: %s\n----' %(deck_a, deck_b))
        i += 1
    
    return deck_a, deck_b

# def play_recursive_combat(deck_a, deck_b):

play_round(player_one_deck, player_two_deck)
