import random

ACE_PROB = 0.01
KING_PROB = 0.1
WORST_PROB = 0.89

ACE_REWARD = "Ace"
MODERATE_REWARDS = ["Kingo", "Kinger", "Kingin"]
WORST_REWARDS = ["W1", "W2", "W3", "W4", "W5"]

def draw_reward():
    reward = None
    reward_prob = random.random()
    
    if reward_prob <= ACE_PROB:
        reward = ACE_REWARD
    elif reward_prob <= ACE_PROB + KING_PROB:
        reward = random.choice(MODERATE_REWARDS)
    else:
        reward = random.choice(WORST_REWARDS)
    
    return reward

def main():
    draw_coins = int(input("Enter the number of draw coins: "))
    guaranteed_ace = False
    
    while True:
        if draw_coins <= 0:
            print("No more draw coins.")
            break
            
        if guaranteed_ace:
            print("Ace is guaranteed in the next draw!")
            guaranteed_ace = False
        
        user_input = input("Press 'D' or 'd' to draw a reward: ")
        if user_input.lower() == 'd':
            draw_coins -= 1
            reward = draw_reward()
            print("You got:", reward)
            if reward == ACE_REWARD:
                guaranteed_ace = True
        
        print("Remaining draw coins:", draw_coins)
    
if __name__ == '__main__':
    main()
