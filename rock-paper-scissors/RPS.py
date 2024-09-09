# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    if prev_play =='':
        opponent_history.clear()

    opponent_history.append(prev_play)

    if len(opponent_history) < 3:
        #print(opponent_history[:4], ['', 'R', 'P', 'P'])
        guess = 'S'
    else:
        #print(opponent_history[:4], ['', 'R', 'P', 'P'])
        # vs quincy
        if opponent_history[:3] == ['', 'R', 'P']:
            pattern_dict = {'RP': 'S', 'PP': 'R', 'PS': 'P', 'SR': 'P', 'RR': 'S'}
            last_two = ''.join(opponent_history[-2:])
            guess = pattern_dict[last_two]
            #print(len(opponent_history), 'quincy')
        # vs abbey
        elif opponent_history[:3] == ['', 'P', 'P']:
            ideal_response = {'P': 'R', 'R': 'S', 'S': 'P'}
            guess = ideal_response[prev_play]
            if len(opponent_history) == 3:
                guess = 'S'
            elif len(opponent_history) == 4:
                guess = 'P'
                opponent_history[-1] = [prev_play, {'RR': 0, 'RP': 0, 'RS': 1, 'PR': 0, 'PP': 0, 'PS': 0, 'SR': 0, 'SP': 0, 'SS': 2}, guess]
            elif len(opponent_history) == 5:
                guess = 'S'
                opponent_history[-1] = [prev_play, {'RR': 0, 'RP': 0, 'RS': 1, 'PR': 0, 'PP': 0, 'PS': 0, 'SR': 0, 'SP': 1, 'SS': 2}, guess]
            else:
                opponent_history[-1] = [prev_play, opponent_history[-2][1]]
                last_two = opponent_history[-3][2] + opponent_history[-2][2]
                opponent_history[-1][1][last_two] += 1
                #print(opponent_history[-1])
                # guess
                potential_plays = [
                    opponent_history[-2][2] + "R",
                    opponent_history[-2][2] + "P",
                    opponent_history[-2][2] + "S",
                ]
                sub_order = {
                    k: opponent_history[-1][1][k]
                    for k in potential_plays if k in opponent_history[-1][1]
                }
                prediction = max(sub_order, key=sub_order.get)[-1:]
                ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
                guess = ideal_response[ideal_response[prediction]]
                #print(opponent_history[-1], prediction, guess)
                opponent_history[-1].append(guess)
                #print(opponent_history[-1])
                #print(len(opponent_history), 'abbey', prev_play)
        # vs kris
        elif opponent_history[:3] == ['', 'P', 'R']:
            if len(opponent_history) == 3:
                guess = 'P'
            else:
                guess = prev_play
            #print('kris', guess)
        # vs mrugesh
        elif opponent_history[:3] == ['', 'R', 'R']:
            ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
            #last_ten = opponent_history[-10:]
            #most_frequent = max(last_ten, key=last_ten.count)
            #guess = ideal_response[most_frequent]
            guess = ideal_response[prev_play]
            #print('mugesh', guess)

    return guess