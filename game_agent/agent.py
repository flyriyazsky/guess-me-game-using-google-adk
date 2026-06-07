import random
import time
from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

def get_random_number(min_value: int = 1, max_value: int = 100) -> int:
    """
    Generate a random number for a guessing game.
    
    Args:
        min_value: Minimum value for the random number (default: 1)
        max_value: Maximum value for the random number (default: 100)
    
    Returns:
        A random integer between min_value and max_value (inclusive)
    """
    # time.sleep(30) # To avoid hitting rate limits during testing, we can simulate a delay here. Remove or adjust as needed.
    return random.randint(min_value, max_value)

def evaluate_guessing_game(secret_number: int, guesses: list[int]) -> dict:
    """Evaluate a guessing game round and return result details."""
    for attempt_index, guess in enumerate(guesses, start=1):
        if guess == secret_number:
            return {
                'won': True,
                'attempts': attempt_index,
                'secret_number': secret_number,
                'last_guess': guess,
            }
    return {
        'won': False,
        'attempts': len(guesses),
        'secret_number': secret_number,
        'last_guess': guesses[-1] if guesses else None,
    }


def decide_winner(game1_guesses: list[int], game2_guesses: list[int], min_value: int = 1, max_value: int = 100) -> dict:
    """Run two guessing games and decide the winner based on performance."""
    secret1 = get_random_number(min_value, max_value)
    secret2 = get_random_number(min_value, max_value)
    result1 = evaluate_guessing_game(secret1, game1_guesses)
    result2 = evaluate_guessing_game(secret2, game2_guesses)

    if result1['won'] and result2['won']:
        if result1['attempts'] < result2['attempts']:
            winner = 'game1'
        elif result2['attempts'] < result1['attempts']:
            winner = 'game2'
        else:
            winner = 'tie'
    elif result1['won']:
        winner = 'game1'
    elif result2['won']:
        winner = 'game2'
    else:
        winner = 'tie'

    return {
        'game1': result1,
        'game2': result2,
        'winner': winner,
    }

root_agent = Agent(
    model=LiteLlm(model="ollama_chat/qwen2.5-coder:1.5b"),
    name='root_agent',
    description='A game agent for fun purposes.',
    instruction='You are a game agent that helps users play a guessing game. The user will try to guess a random number between 1 and 100, and you will provide feedback on whether their guess is too low, too high, or correct. Note that you should not reveal the secret number. You can also give hints if the user is struggling. Always encourage the user to keep trying and have fun! Use the get_random_number tool to generate a random number for the game.',
    tools=[get_random_number, evaluate_guessing_game, decide_winner],
)


