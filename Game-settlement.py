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
            msg = ("your blade takes a tour to the nearest {}s' body".format(noun))
            if object.hp<=0:
                msg+=("\nYou have viciously murdered a {}".format(noun))
    else:
        msg = "Poor {} just got a slap from you".format(noun)
    return msg
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
    self._description = "(A foul creature) \n"
    super().__init__(name)
  @property
  def description(self):
      if self.hp>=3:
          return self._description + "It is fine"
      if self.hp==2:
          return self._description + "It is wounded"
      if self.hp==1:
          return self._description + "It is heavily injured"
      if self.hp==0:
          return self._description + "It is at death's door"
      if self.hp < 0:
          return self._description + "It is dead as death"
  @description.setter
  def description(self,value):
     self._description=value
class Wolf(GameObjects):
   def __init__(self,name):
      self.hp=2
      self.class_name = "wolf"
      self.description = "(Wolves hunt in packs!) \n"
      super().__init__(name)
   @property
   def description(self):
       if self.hp >= 2:
           return self._description + "It is gazing on you with a bit of hope"
       if self.hp == 1:
           return self._description + "It is heavily injured"
       if self.hp == 0:
           return self._description + "It is at death's door, you are a monster"
       if self.hp < 0:
           return self._description + "It is dead as death"
   @description.setter
   def description(self, value):
       self._description = value
print("Attention! You are entering textRPG zone and now are hitting the point of no return. Use say/examine/hit [word] commands to venture through \n\n")
print("You wake up in a bed among the ruins. A goblin hunter with his faithful wolf companion are starring at you silently \n My name is Jakem,- the goblin says unsurely ")
goblin = Goblin("Jakem")
wolf=Wolf(input("Guess this wolf is nameless.. How would you prefer to refer to it? " ))
while True:
  get_input()
