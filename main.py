
# Basic Rock Paper Scissors Game
# Name: Austin Aspenwall
# Date: 02/20/2026

import random

"""
main.py
---------
Rock Paper Scissors game for CS101 Fall 2025 Lab 02.
This script allows a user to play a 3-round game of Rock, Paper, Scissors against the computer.
It uses the 'rich' library for colorful output.
"""

import random
from rich.console import Console
from rich.text import Text

# Create a Console object for rich output
console = Console()
"""
main.py (Starter Template)
-------------------------
Rock Paper Scissors game for CS101 Fall 2025 Lab 02.

Complete the TO-DOs to finish the game!
"""

import random
from rich.console import Console

console = Console()

choices = ['rock', 'paper', 'scissors']
num_to_choice = {'1': 'rock', '2': 'paper', '3': 'scissors'}

# : Implement this function to get and validate the user's choice.
def get_user_choice(num_to_choice):
	"""Prompt the user for their choice and return 'rock', 'paper', or 'scissors'."""
	while True:
		choice = console.input("Enter your choice (1 for Rock, 2 for Paper, 3 for Scissors): ")
		if choice in num_to_choice:
			return num_to_choice[choice]
		
		else:
			console.print("[bold red]Invalid input. Please enter 1, 2, or 3.[/bold red]")
			pass
		break
	# : Use console.input and validate input (accept 1/2/3 or words)
	

#: Implement this function to randomly select the computer's choice.
def get_computer_choice(choices):
	"""Randomly return 'rock', 'paper', or 'scissors'."""
	return random.choice(choices)

# : Implement this function to determine the winner of a round.
def determine_winner(user_choice, computer_choice):
	"""Return 'user', 'computer', or 'tie' based on the choices."""
	if user_choice == computer_choice:
		winner = 'tie'
		return winner
	elif (user_choice == 'rock' and computer_choice == 'paper'):
		winner = 'lose'
		return winner
	elif (user_choice == 'rock' and computer_choice == 'scissors'):
		winner = 'win'
		return winner
	elif (user_choice == 'paper' and computer_choice == 'scissors'):
		winner = 'lose'
		return winner
	elif (user_choice == 'paper' and computer_choice == 'rock'):
		winner = 'win'
		return winner
	elif (user_choice == 'scissors' and computer_choice == 'rock'):
		winner = 'lose'
		return winner
	elif (user_choice == 'scissors' and computer_choice == 'paper'):
		winner = 'win'
		return winner

# : Implement this function to print the round result with color.
def print_round_result(user_choice, computer_choice, winner):
	"""Print the choices and the winner of the round using rich colors."""
	console.print(f"You chose: [bold cyan]{user_choice}[/bold cyan]")
	console.print(f"Computer chose: [bold magenta]{computer_choice}[/bold magenta]")
	if winner == 'tie':
		console.print("[blue]It's a tie![/blue]")
	elif winner == 'win':
		console.print("[bold green]You win this round![/bold green]")
	elif winner == 'lose':
		console.print("[bold red]Computer wins this round![/bold red]")
	

# : Implement the main game loop.
def main():
	"""Main function to run the game for 3 rounds and print the final result."""
	user_score = 0
	computer_score = 0
	rounds = 3
	for round_num in range(1, rounds + 1):
		# : Get user and computer choices
		user_choice = get_user_choice(num_to_choice)
		computer_choice = get_computer_choice(choices)
		# : Determine winner
		winner = determine_winner(user_choice, computer_choice)
		# : Print round result
		round = f"Round {round_num} of {rounds}"
		console.print(f"\n[bold yellow]{round}[/bold yellow]")
		print(print_round_result(user_choice, computer_choice, winner))
		# : Update scores
		if winner == 'win':
			user_score += 1
		elif winner == 'lose':
			computer_score += 1
	console.print(f"\nFinal Score - You: {user_score} | Computer: {computer_score}")	
	if user_score > computer_score:

		console.print("[bold green]Congratulations, you win the game![/bold green]")
	else:
		console.print("[bold red]Computer wins the game! Better luck next time![/bold red]")
	
	# : Print final scores and announce the overall winner
	

if __name__ == "__main__": 
    main()
