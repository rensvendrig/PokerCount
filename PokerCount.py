import streamlit as st
def calculate_winners(players_info, chip_values):
    winners = {}
    sum_buy_in = 0
    
    for player in players_info:
        name = player["name"]
        buy_in = player["buy_in"]
        sum_buy_in += buy_in
        end_score = sum([a*b for a,b in zip(player["end_score"], chip_values)])
        winnings = end_score - buy_in
        winners[name] = round(winnings, 2)
        
    if sum(winners.values()) != 0:
        print('Het totale win/loss getal komt niet uit op 0!')
        dif_per_player = sum(winners.values())/len(players_info)        
        winners  = {k: round(v - dif_per_player,2) for k, v in winners.items()}
    
    return winners

def distribute_losses(players):
    total_winnings = sum(players.values())
        
    losers = {k: v for k, v in players.items() if v < 0}
    winners = {k: v for k, v in players.items() if v > 0}
    total_losses = sum(losers.values()) * -1

    payments = {}
    for loser, loss in losers.items():
        for winner in sorted(winners, key=lambda x: players[x], reverse=True):
            if total_losses == 0:
                break

            payment = min(players[winner], loss * -1)
            players[winner] -= payment
            key_pay = loser +' betaalt ' + winner
            payments[key_pay] = round(payment, 2)
            total_losses -= payment
            loss += payment

            if players[winner] == 0:
                del winners[winner]
    
    pay_wout_zeros = {k: v for k, v in payments.items() if v != 0.0 or v != -0.0 }
    
    return pay_wout_zeros


# chip_values = [0.05, 0.1, 0.2, 0.4, 1.0]

# players = [{"name": "Bram", "buy_in": 10, "end_score": [21,3,4,3,4]},
#            {"name": "Lukas", "buy_in": 10, "end_score": [21,22,12,15,4]},
#            {"name": "Rens", "buy_in": 10, "end_score": [8, 20, 11, 6, 5]},
#             {"name": "Brandt", "buy_in": 10, "end_score": [16, 4, 17, 9, 3]},
#            {"name": "Mojet", "buy_in": 10, "end_score": [2, 7, 10, 0, 1]}]

# winnings_losses = calculate_winners(players, chip_values)
# print(winnings_losses)
# distribute_losses(winnings_losses)