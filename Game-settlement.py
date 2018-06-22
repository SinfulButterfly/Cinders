def get_input():
  inpt = input(": ").split()
  word = inpt[0]
  if word in dicti:
    verb = dicti[word]
  else:
    print("Verb {} is not recognized". format(word))
    return
  if len(inpt) >= 2:
      phrase=inpt[1]
      print (verb(phrase))
  else:
      print(verb("nothing"))
def say(noun):
  return 'You said "{}"'.format(noun)
def examine(noun):
  if noun in GameObjects.objects:
    return GameObjects.objects[noun].get_description()
  else:
    return "There is no {} here.".format(noun)
def hit(noun):
    if noun in GameObjects.objects:
        object = GameObjects.objects[noun]
        if type(object)==Goblin or Wolf:
            object.hp-=1
            if object.hp<=0:
                print("You have viciously murdered a {} type(object)".format(type(object)))
        else:
            print("{} got a slap from you".format(type(object)))

dicti = {"say": say, "examine":examine, "hit":hit}
class GameObjects:
  class_name = ""
  description = ""
  objects = {}
  def __init__(self, name):
    self.name = name
    GameObjects.objects[self.class_name] = self
  def get_description(self):
    return self.class_name + "\n" + self.description

class Goblin(GameObjects):
  def __init__(self,name):
    self.hp=3
    self.class_name = "goblin"
    self.description = "A foul creature"
    super.__init__(self)
  @property
  def health(self):
      if self.hp>=3:
          return self.description, "it is fine"
      if self.hp==2:
          return self.description, "It is wounded"
      if self.hp==1:
          return self.description, "It is heavily injured"
      if self.hp==0:
          return self.description, "It is at death's door"

class Wolf(GameObjects):
  class_name = "wolf"
  description = "Wolves hunt in packs!"
goblin = Goblin(input("What's this goblins name? "))
wolf=Wolf(input("Guess this wolf is nameless,  how would you prefer to refer to it?" ))

while True:
  get_input()