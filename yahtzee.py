from die import Die

class YahtzeeMainClass:
    def __init__(self):
        self.ds = [Die(), Die(), Die(), Die(), Die()]
        self.keepItGoing = True
        
        while self.keepItGoing == True:
            intTurn = 0
            
            print("Welcome to Yahtzee!")
            
            while intTurn < 3:
                print(f"Starting turn: {intTurn+1} of 3, rolling dice")
                for i, d in enumerate(self.ds):
                    d.DieRoll()
                    # d.value = 5  # Test if yahtzee works
                    print(f"{i}: {d}")
                # YAHTZEE
                flag = True
                for j in range(1, 5):
                    if self.ds[j].value != self.ds[j-1].value:
                        # Set flag to false
                        flag = False
                if flag == True:
                    print(f"You got YAHTZEE! in {self.ds[0].value}'s")
                    
                else:
                    # Here we check if there is no Yahtzee: then we check what turn we are on and ask the player if we want to continue or not
                    if intTurn != 2:
                        if input("Want to throw again? (y for yes, anything else for no) ") == "y":
                            intTurn += 1
                        else:
                            self.keepItGoing = not self.keepItGoing
                            break
                    else:
                        if input("Game over! Want to play again? ") == "y":
                            intTurn = 0
                        else:
                            self.keepItGoing = not self.keepItGoing
                            break

def main():
    YahtzeeMainClass()

if __name__ == '__main__':
    main()