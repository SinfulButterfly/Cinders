def get_input():
    inpt = input("> ").split()
    word = inpt[0]
    if word in dicti:
        verb = dicti[word]
    else:
        print("Verb {} is not recognized". format(word))
        return
    if len(inpt) >= 2:
        phrase = inpt[1]
        print(verb(phrase))
    else:
        print(verb("nothing"))

def say(noun):
    return 'You said "{}"'.format(noun)

def examine(noun):
    if noun in GameObjects.objects or noun == "self" or noun == hero_name:
        if noun != "self" and noun != hero_name:
            obj = GameObjects.objects[noun]
        else: obj = GameObjects.objects[hero_race]
        return obj.comments + "{} {} has {} Hp left \n".format(obj.class_name, obj.name, obj.hp) + obj.description
    else:
        return "There is no {} here.".format(noun)

def hit(noun):
    if noun in GameObjects.objects or noun == "self" or noun == hero_name or noun == hero_race:
        if noun != "self" and noun != hero_name and noun != hero_race:
            game_object = GameObjects.objects[noun]
            game_object.hp -= 1                                                             # attack power
            msg = ("your blade takes a tour to the nearest {}s' body \n".format(noun))
            if game_object.hp <= 0:
                msg += ("\nYou have viciously murdered a {}\n".format(noun))
        else:
            game_object = GameObjects.objects[hero_race]
            game_object.hp -= 2
            msg = "Your blade sinks under your skin \n"
            if game_object.hp <= 0:
                msg += "\n You've just commited suicide! \n"
                raise ValueError("You cannot be that dead. \n\n\n Game over")
        return msg+game_object.description
    else:
        msg = "Poor {} just got a slap from you".format(noun)
        return msg

def heal(noun):
    if noun in GameObjects.objects or noun == "self" or noun == hero_name or noun == hero_race:
        if noun != "self" and noun != hero_name and noun != hero_race:
            game_object = GameObjects.objects[noun]
            if game_object.hp > 0 and game_object.hp < game_object.default_hp:
                game_object.hp += 1                                                         # heal_power
            msg = ("You've tried to heal {}'s wounds\n".format(noun))                       # +you have healed ...
            if game_object.hp == 0:
                game_object.hp += 0.1
                msg += ("{} is at death's door. "
                        "Healing of such injuries may require some stronger spells\n".format(noun))
            if game_object.hp < 0:
                msg += ("{} is dead. Seeing it healed would be a miracle\n".format(noun))
        else:
            game_object = GameObjects.objects[hero_race]
            if game_object.hp >= 0 and game_object.hp < game_object.default_hp:
                game_object.hp += 1                                                         # healpower
            msg = ("You've tried to heal your wounds\n".format(noun))                       # +you have healed ...
            if game_object.hp == 0:
                msg += ("You are teetering on the brink. It will take more then healing to lift you up\n".format(noun))
        return msg + game_object.description
    else:
        return "You've thrown some spells at what you considered to be a {}".format(noun)


dicti = {"say": say, "examine": examine, "hit": hit, "heal": heal}


class GameObjects:
    class_name = ""
    name = ""
    description = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObjects.objects[self.class_name] = self

    def get_description(self):
        return self.class_name + "\n" + self.description

class Self(GameObjects):
    def __init__(self, name, race):
        self.default_hp = 10
        self.hp = 10
        self.attack_power = 3
        self.heal_power = 2
        self.class_name = race
        self.comments = "What a pity, there anin't no mirror around\n"
        self._description = ""
        super().__init__(name)

    @property
    def description(self):
        if self.hp >= 10:
            return self._description + "You're fine"
        elif self.hp > 7:
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
        self.description = value

class Goblin(GameObjects):
    def __init__(self, name=""):
        self.default_hp = 3
        self.attack_power = 3
        self.heal_power = 1
        self.hp = 3
        self.class_name = "goblin"
        self.comments = "(A foul creature) \n"
        self._description = ""
        super().__init__(name)

    @property
    def description(self):
        if self.hp >= 3:
            return self._description + "It is fine"
        elif self.hp >= 2:
            return self._description + "It is wounded"
        elif self.hp >= 1:
            return self._description + "It is heavily injured"
        elif self.hp >= 0:
            return self._description + "It is at death's door"
        else:
            return self._description + "It is dead as death"

    @description.setter
    def description(self, value):
        self._description = value

class Wolf(GameObjects):
    def __init__(self, name=""):
        self.default_hp = 2
        self.attack_power = 2
        self.heal_power = 0
        self.hp = 2
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
    def __init__(self, name=""):
        self.default_hp = 5
        self.attack_power = 2
        self.heal_power = 3
        self.hp = 5
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

if __name__ == "__main__":
    print("Attention! You are entering textRPG zone and now are hitting the point of no return. "
          "Use say/examine/hit [word] commands to venture through \n\n")
    print("You wake up hearing a harpy shriek from above finding thineself in a bed among the ruins. "
          "A goblin hunter with his faithful wolf companion are starring at you silently \n "
          "My name is Jakem,- the goblin pronounces meekly ")
    g1 = Goblin("jakem")
    w1 = Wolf()
    h1 = Harpy()
    hero_name = input("What is your name? \n")
    hero_race = input("What's your race? \n")
    hero = Self(hero_name, hero_race)
    while True:
        get_input()
    # ToDo: (task pinned forever)Add some more creatures
    # ToDo: Add "hit trading algorithm"
    # ToDo: Add heal/damage power DONE; Invent usage
    # ToDo: Add resources: manna (maybe, stamina too)
    # ToDo: Add friend-or-foe system and reputations
    # ToDo: Invent evasion, dodge-text
    # ToDo: godot engine, Unreal Engine 4, Blender, Learn about graph interface for this rpg,
    # ToDo: Think about that or any other unusual concept for a game
        # constants (variables that never change value) should be CAPS_WITH_UNDERSCORES;
        # For 3D games, the library Panda3D can be used. For 2D games, you can use pygame.
