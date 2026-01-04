from random import choice

cards: list[int] = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card() -> int:
    return choice(cards)

def check_sum(card_list: list[int]) -> int:
    total = sum(card_list)
    # Handle Aces: convert 11 to 1 if busting
    num_aces = card_list.count(11)
    while total > 21 and num_aces > 0:
        total -= 10  # Convert one Ace from 11 to 1
        num_aces -= 1
    return total

def is_blackjack(card_list: list[int]) -> bool:
    """Check if hand is a natural blackjack (21 with 2 cards)"""
    return len(card_list) == 2 and check_sum(card_list) == 21

def print_hands(user_cards: list[int], cp_cards: list[int]) -> None:
    card_sum = check_sum(user_cards)
    print(f"Your cards: {user_cards}, current score: {card_sum}")
    print(f"Computer's first card: {cp_cards[0]}")


def main() -> None:
    should_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    while should_play=='y':
        # Initial deal
        user_cards: list[int] = [draw_card(), draw_card()]
        cp_cards: list[int] = [draw_card(), draw_card()]

        print_hands(user_cards, cp_cards)

        # Check for natural blackjack
        user_has_blackjack = is_blackjack(user_cards)
        dealer_has_blackjack = is_blackjack(cp_cards)

        if user_has_blackjack or dealer_has_blackjack:
            print(f"Your final hand: {user_cards}, final score: {check_sum(user_cards)}")
            print(f"Computer's final hand: {cp_cards}, final score: {check_sum(cp_cards)}")
            if user_has_blackjack and dealer_has_blackjack:
                print("Both have Blackjack! It's a tie! 🤝")
            elif user_has_blackjack:
                print("Blackjack! You win! 🎉")
            else:
                print("Dealer has Blackjack! You lose 😭")
        else:
            # Player's turn
            card_sum = check_sum(user_cards)
            draw_another = input("Type 'y' to get another card, type 'n' to pass: ")
            while draw_another=='y' and card_sum < 21:
                user_cards.append(draw_card())
                card_sum = check_sum(user_cards)
                print_hands(user_cards, cp_cards)
                if card_sum < 21:
                    draw_another = input("Type 'y' to get another card, type 'n' to pass: ")
                else:
                    break

            # Check player bust
            if card_sum > 21:
                print(f"Your final hand: {user_cards}, final score: {card_sum}")
                print(f"Computer's final hand: {cp_cards}, final score: {check_sum(cp_cards)}")
                print("You went over. You lose 😭")
            else:
                # Dealer's turn (draws to 17, standard blackjack rules)
                cp_sum = check_sum(cp_cards)
                while cp_sum < 17:
                    cp_cards.append(draw_card())
                    cp_sum = check_sum(cp_cards)

                # Final scoring
                print(f"Your final hand: {user_cards}, final score: {card_sum}")
                print(f"Computer's final hand: {cp_cards}, final score: {cp_sum}")

                if cp_sum > 21:
                    print("Dealer busts! You win 😃")
                elif card_sum > cp_sum:
                    print("You win 😃")
                elif card_sum == cp_sum:
                    print("It's a tie! 🤝")
                else:
                    print("You lose 😭")


        should_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        print('\n'*20)


if __name__ == "__main__":
    main()