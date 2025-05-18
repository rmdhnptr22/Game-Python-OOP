import random

class Game:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.guesses = []
        self.max_attempts = 5

    def make_guess(self, guess):
        if guess < 1 or guess > 100:
            return "Tebakan harus antara 1 dan 100."
        
        self.guesses.append(guess)
        
        if guess < self.secret_number:
            return "Tebakan terlalu rendah."
        elif guess > self.secret_number:
            return "Tebakan terlalu tinggi."
        else:
            return "Selamat! Anda telah menebak angka yang benar."

    def get_remaining_attempts(self):
        return self.max_attempts - len(self.guesses)

    def is_game_over(self):
        return (len(self.guesses) >= self.max_attempts) or (self.guesses and self.guesses[0] == self.secret_number)

    def get_secret_number(self):
        return self.secret_number

def main():
    game = Game()
    print("Selamat datang di permainan tebak angka!")
    print("Saya telah memilih angka antara 1 dan 100.")
    print(f"Anda memiliki {game.max_attempts} kesempatan untuk menebak.")

    while not game.is_game_over():
        guess = int(input("Masukkan tebakan Anda: "))
        result = game.make_guess(guess)
        print(result)
        print(f"Sisa kesempatan: {game.get_remaining_attempts()}")

        if game.is_game_over():
            if game.guesses[-1] != game.secret_number:
                print(f"Permainan selesai! Angka yang benar adalah {game.get_secret_number()}.")

if __name__ == "__main__":
    main()