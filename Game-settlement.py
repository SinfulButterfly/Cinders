def get_input():
  inpt = input("> ").split()
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
  if noun in GameObjects.objects or noun == "self" or noun == HeroName:
    if noun != "self" and noun != HeroName:
        obj=GameObjects.objects[noun]
    else: obj=GameObjects.objects[HeroRace]
    return obj.comments+"{} {} has {} Hp left \n".format(obj.class_name,obj.name,obj.hp)+obj.description
  else:
    return "There is no {} here.".format(noun)
def hit(noun):
    if noun in GameObjects.objects or noun=="self" or noun==HeroName or noun==HeroRace:
        if noun!="self" and noun!=HeroName and noun!=HeroRace:
            object = GameObjects.objects[noun]
            object.hp-=1
            msg = ("your blade takes a tour to the nearest {}s' body \n".format(noun))
            if object.hp<=0:
                msg+=("\nYou have viciously murdered a {}\n".format(noun))
        else:
            object = GameObjects.objects[HeroRace]
            object.hp-=2
            msg = ("Your blade sinks under your skin \n")
            if object.hp<=0:
                msg+=("\n You've just commited suicide! \n")
                raise ValueError("You cannot be that dead. \n\n\n Game over")
        return msg+object.description
    else:
        msg = "Poor {} just got a slap from you".format(noun)
        return msg
def heal(noun):
    if noun in GameObjects.objects or noun=="self" or noun==HeroName or noun==HeroRace:
        if noun!="self" and noun!=HeroName and noun!=HeroRace:
            object = GameObjects.objects[noun]
            if object.hp>0 and object.hp<object.default_hp:
                object.hp+=1 #healpower
            msg = ("You've tried to heal {}'s wounds\n".format(noun)) #+you have healed ...
            if object.hp==0:
                object.hp += 0.1
                msg+=("{} is at death's door. Healing of such injuries may require some stronger spells\n".format(noun))
            if object.hp<0:
                msg+=("{} is dead. Seeing it healed would be a miracle\n".format(noun))
        else:
            object = GameObjects.objects[HeroRace]
            if object.hp>=0 and object.hp<object.default_hp:
                object.hp+=1 #healpower
            msg = ("You've tried to heal your wounds\n".format(noun)) #+you have healed ...
            if object.hp==0:
                msg+=("You are teetering on the brink. It will take more then healing to lift you up\n".format(noun))
        return msg+object.description
    else:return "You've thrown some spells at what you considered to be a {}".format(noun)
dicti = {"say": say, "examine":examine, "hit":hit, "heal":heal}

class GameObjects:
  class_name = ""
  name=""
  description = ""
  objects = {}
  def __init__(self, name):
    self.name = name
    GameObjects.objects[self.class_name] = self
  def get_description(self):
    return self.class_name + "\n" + self.description
class Self(GameObjects):
    def __init__(self,name,race):
        self.default_hp=10
        self.hp=10
        self.class_name=race
        self.comments = "What a pity, there anin't no mirror around\n"
        self._description = ""
        super().__init__(name)
    @property
    def description(self):
        if self.hp >= 10:
            return self._description + "You're fine"
        elif self.hp >7:
            return self._description + "You are bleeding"
        elif self.hp > 4:
            return self._description + "You are seroiously injured"
        elif self.hp > 3:
            return self._description + "your grip on life is in act"
        elif self.hp == 1:
            return self._description + "You are about to die"
        else:
            return self._description + "Your health bar just hit zero and there is no one out there to res you"
    @description.setter
    def description(self, value):
        self.description=value
class Goblin(GameObjects):
  def __init__(self,name=""):
    self.default_hp=3
    self.hp=3
    self.class_name="goblin"
    self.comments = "(A foul creature) \n"
    self._description = ""
    super().__init__(name)
  @property
  def description(self):
      if self.hp>=3:
          return self._description + "It is fine"
      elif self.hp>=2:
          return self._description + "It is wounded"
      elif self.hp>=1:
          return self._description + "It is heavily injured"
      elif self.hp>=0:
          return self._description + "It is at death's door"
      else:
          return self._description + "It is dead as death"
  @description.setter
  def description(self,value):
     self._description=value
class Wolf(GameObjects):
   def __init__(self,name=""):
      self.default_hp=2
      self.hp=2
      self.class_name = "wolf"
      self.comments = "(Wolves hunt in packs!) \n"
      self._description = ""
      super().__init__(name)
   @property
   def description(self):
       if self.hp >= 2:
           return self._description + "It is gazing on you with a bit of hope"
       if self.hp >= 1:
           return self._description + "It is heavily injured"
       if self.hp >= 0:
           return self._description + "It is at death's door, you are a monster"
       if self.hp < 0:
           return self._description + "It is dead as death"
   @description.setter
   def description(self, value):
       self._description = value
class Harpy(GameObjects):
   def __init__(self,name=""):
      self.default_hp=5
      self.hp=5
      self.class_name = "harpy"
      self.comments = "Rancid creatures with charming voices\n"
      self._description = ""
      super().__init__(name)
   @property
   def description(self):
       if self.hp >= 5:
           return self._description + "A regular harpy with a slight grin on its face"
       if self.hp >= 4:
           return self._description + "There is a scratch on her arm"
       if self.hp >= 3:
           return self._description + "Her body bares signs of a fearsome fight"
       if self.hp >= 2:
           return self._description + "She is barely floating and is about to fall"
       if self.hp >= 1:
           return self._description + "It scrambles on the ground"
       if self.hp >= 0:
           return self._description + "It is standing at death's door"
       if self.hp < 0:
           return self._description + "It has fade away"
   @description.setter
   def description(self, value):
       self._description = value

print("Attention! You are entering textRPG zone and now are hitting the point of no return. Use say/examine/hit [word] commands to venture through \n\n")
print("You wake up hearing a harpy shriek from above finding thineself in a bed among the ruins. "
      "A goblin hunter with his  faithful wolf companion are starring at you silently \n My name is Jakem,- the goblin says unsurely ")
g1=Goblin("jakem")
w1=Wolf()
h1=Harpy()
HeroName=input("What is your name? \n")
HeroRace=input("What's your race? \n")
Hero=Self(HeroName,HeroRace)
while True:
  get_input()
  # ToDo: Learn about graph interface for this rpg, add some more creatures, add "hit trading algorithm", finish names to usage
