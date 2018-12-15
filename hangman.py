from typing import Any
import random


def func(file) -> Any:
    """
    generate a random word
    """

    word_list = []

    with open(file, encoding='utf8') as f:
        for line in f:
            clean = line.lower().strip()
            clean_str = ''
            for char in clean:
                if char.isalpha():
                    clean_str += char
            if len(clean_str) > 2:
                word_list.append(clean_str)

    word = word_list[random.randint(0, len(word_list) - 1)]

    return word


class Hangman:

    def __init__(self, name: str)-> None:
        """
        initialize game with a player name
        """
        self.name = name

    def game(self, guesses: int) -> Any:
        """
        games main loop
        """
        word = func('words.txt')
        cover = '*'*len(word)
        letters_guessed = []
        print(cover)
        while guesses != 0:
            if cover == word:
                return f'{self.name} guessed the word: {word}'
            else:
                guess = input('guess a letter').lower()
                while guess in letters_guessed:
                    print('you already guessed that letter')
                    guess = input('guess a letter').lower()
                letters_guessed.append(guess)

                index = []
                if guess in word:
                    for i in range(len(word)):
                        if word[i] == guess:
                            index.append(i)

                    new = ''
                    for i in range(len(cover)):
                        if i in index:
                            new += guess
                        else:
                            new += cover[i]
                    cover = new
                else:
                    guesses -= 1
                print(cover)
        return f'{self.name} lost, the word was: {word}'
