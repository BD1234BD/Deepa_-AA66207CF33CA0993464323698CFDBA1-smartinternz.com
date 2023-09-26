class player:
  def player(self):
    print("the player is playing a cricket")

class Batsman (player):
  def play(self):
     print("the batmen is bating.")

class Bowler (player):
  def play(self):
    print("the bowler is bowling.")


batsman = Batsman()
bowler = Bowler()


batsman.play()
bowler.play()
