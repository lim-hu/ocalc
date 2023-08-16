from . import app
from .models import db, Race, Character, Class, Item, BirthSign
from flask import render_template, redirect, request
from .database import CLASSES, RACES, BIRTHSIGNS, ITEMS, CHARACTERS

# Defines Datas

A_SKILL = ["Blade", "Blunt", "Hand To Hand", "Armorer", "Block", "Heavy Armor", "Athletics", "Arcobatics",
          "Light_armor", "Security", "Sneak", "Marksman", "Mercantile", "Speechcraft", "Illusion", "Alchemy",
          "Conjuration", "Mysticism", "Alteration", "Destruction", "Restoration",
          "STR", "END", "AGI", "SPD", "PER", "WIL", "INT", "LCK"]


def check_inputs(input_dict, A_SKILL, add_data):
    for skill in input_dict:
        if skill in A_SKILL:
            if int(input_dict[skill]) >= 100:
                input_dict[skill] = 100;
            elif int(input_dict[skill]) <= 0:
                input_dict[skill] = 0;
                
    add_data.strength = int(input_dict["STR"])
    add_data.endurance = int(input_dict["END"])
    add_data.agility = int(input_dict["AGI"])
    add_data.speed = int(input_dict["SPD"])
    add_data.personality = int(input_dict["PER"])
    add_data.willpower = int(input_dict["WIL"])
    add_data.intelligence = int(input_dict["INT"])
    add_data.luck = int(input_dict["LCK"])    
                                    
    add_data.blade = int(input_dict["Blade"])
    add_data.blunt = int(input_dict["Blunt"])
    add_data.hand_to_hand = int(input_dict["Hand To Hand"])
    add_data.armorer = int(input_dict["Armorer"])
    add_data.block = int(input_dict["Block"])
    add_data.heavy_armor = int(input_dict["Heavy Armor"])
    add_data.athletics = int(input_dict["Athletics"])
    add_data.acrobatics = int(input_dict["Acrobatics"])
    add_data.light_armor = int(input_dict["Light Armor"])
    add_data.security = int(input_dict["Security"])
    add_data.sneak = int(input_dict["Sneak"])
    add_data.marksman = int(input_dict["Marksman"])
    add_data.mercantile = int(input_dict["Mercantile"])
    add_data.speechcraft = int(input_dict["Speechcraft"])
    add_data.illusion = int(input_dict["Illusion"])
    add_data.alchemy = int(input_dict["Alchemy"])
    add_data.conjuration = int(input_dict["Conjuration"])
    add_data.mysticism = int(input_dict["Mysticism"])
    add_data.alteration = int(input_dict["Alteration"])
    add_data.destruction = int(input_dict["Destruction"])
    add_data.restoration = int(input_dict["Restoration"])
    
    db.session.commit()
    
    return input_dict


def update_character(character, race, class_, weared_item_stat, birthsign, add_data, weared_items):
    
    # Generals
    character.race = race.name
    character.gender = race.gender
    character.class_ = class_.name
    character.birthsign = birthsign.name
    # Attributes
    character.strength = race.strength + weared_item_stat["strength"] + birthsign.strength + add_data.strength
    character.endurance = race.endurance + weared_item_stat["endurance"] + birthsign.endurance + add_data.endurance
    character.speed = race.speed + weared_item_stat["speed"] + birthsign.speed + add_data.speed
    character.agility = race.agility + weared_item_stat["agility"] + birthsign.agility + add_data.agility
    character.personality = race.personality + weared_item_stat["personality"] + birthsign.personality + add_data.personality
    character.intelligence = race.intelligence + weared_item_stat["intelligence"] + birthsign.intelligence + add_data.intelligence
    character.willpower = race.willpower + weared_item_stat["willpower"] + birthsign.willpower + add_data.willpower
    character.luck = race.willpower + weared_item_stat["luck"] + birthsign.luck + add_data.luck
    # Skills
    character.blade = race.blade + class_.blade + weared_item_stat["blade"] + add_data.blade
    character.blunt = race.blunt + class_.blunt + weared_item_stat["blunt"] + add_data.blunt
    character.hand_to_hand = race.hand_to_hand  + class_.hand_to_hand + weared_item_stat["hand_to_hand"] + add_data.hand_to_hand
    character.armorer = race.armorer + class_.armorer + weared_item_stat["armorer"] + add_data.armorer
    character.block = race.block + class_.block + weared_item_stat["block"] + add_data.block
    character.heavy_armor = race.heavy_armor + class_.heavy_armor + weared_item_stat["heavy_armor"] + add_data.heavy_armor
    character.athletics = race.athletics + class_.athletics + weared_item_stat["athletics"] + add_data.athletics
    character.acrobatics = race.acrobatics + class_.acrobatics + weared_item_stat["acrobatics"] + add_data.acrobatics
    character.light_armor = race.light_armor + class_.light_armor + weared_item_stat["light_armor"] + add_data.light_armor
    character.security = race.security + class_.security + weared_item_stat["security"] + add_data.security
    character.sneak = race.sneak + class_.sneak + weared_item_stat["sneak"] + add_data.sneak
    character.marksman = race.marksman + class_.marksman + weared_item_stat["marksman"] + add_data.marksman
    character.mercantile = race.mercantile + class_.mercantile + weared_item_stat["mercantile"] + add_data.mercantile
    character.speechcraft = race.speechcraft + class_.speechcraft + weared_item_stat["speechcraft"] + add_data.speechcraft
    character.illusion = race.illusion + class_.illusion + weared_item_stat["illusion"] + add_data.illusion
    character.alchemy = race.alchemy + class_.alchemy + weared_item_stat["alchemy"] + add_data.alchemy
    character.conjuration = race.conjuration + class_.conjuration + weared_item_stat["conjuration"] + add_data.conjuration
    character.mysticism = race.mysticism + class_.mysticism + weared_item_stat["mysticism"] + add_data.mysticism
    character.alteration = race.alteration + class_.alteration + weared_item_stat["alteration"] + add_data.alteration
    character.destruction = race.destruction + class_.destruction + weared_item_stat["destruction"] + add_data.destruction
    character.restoration = race.restoration + class_.restoration + weared_item_stat["restoration"] + add_data.restoration
        
    character.fire_res = weared_item_stat["fire_res"]
    character.cold_res = weared_item_stat["cold_res"]
    character.shock_res = weared_item_stat["shock_res"]
    character.magic_res = weared_item_stat["magic_res"]
    character.poison_res = weared_item_stat["poison_res"]
    character.disease_res = weared_item_stat["disease_res"]
    character.paralysis_res = weared_item_stat["paralysis_res"]
    character.normal_weapon_res = weared_item_stat["normal_weapon_res"]
    character.fire_weak = weared_item_stat["fire_weak"]
    character.cold_weak = weared_item_stat["cold_weak"]
    character.shock_weak = weared_item_stat["shock_weak"]
    character.poison_weak = weared_item_stat["poison_weak"]
    character.reflect_dmg = weared_item_stat["reflect_dmg"]
    character.reflect_spell = weared_item_stat["reflect_spell"]
    character.fire_dmg = weared_item_stat["fire_dmg"]
    character.cold_dmg = weared_item_stat["cold_dmg"]
    character.shock_dmg = weared_item_stat["shock_dmg"]
    character.poison_dmg = weared_item_stat["poison_dmg"]
    character.absorb_life = weared_item_stat["absorb_life"]
    character.health = (character.endurance * 2) + weared_item_stat["health"]
    character.magicka = (character.intelligence * 2) + race.magicka + weared_item_stat["magicka"]
    character.fatigue = (character.endurance + character.strength + character.agility + character.willpower) + weared_item_stat["fatigue"]
    character.spell_absorption = weared_item_stat["spell_absorption"]
    # character.water_walking = weared_item_stat["water_walking"]
    character.detect_life = weared_item_stat["detect_life"]
        
    for weared_item in weared_items:
        match weared_item.skill:
            case "Light Armor":
                weared_item_stat["rating"] += weared_item.rating * (0.35 + (0.0065 * character.light_armor))
            case "Heavy Armor":
                weared_item_stat["rating"] += weared_item.rating * (0.35 + (0.0065 * character.heavy_armor))
            case "Blade":
                weared_item_stat["damage"] += weared_item.damage * 0.5 * (0.75 + character.strength * 0.005) * (0.2 + (character.blade + 0.4 * (character.luck - 50)) * 0.015)
            case "Blunt":
                 weared_item_stat["damage"] += weared_item.damage * 0.5 * (0.75 + character.strength * 0.005) * (0.2 + (character.blunt + 0.4 * (character.luck - 50)) * 0.015)
            case "Bow":
                 weared_item_stat["damage"] += weared_item.damage * 0.5 * (0.75 + character.agility * 0.005) * (0.2 + (character.marksman + 0.4 * (character.luck - 50)) * 0.015)
    
    character.damage = round(weared_item_stat["damage"])
    character.rating = round(weared_item_stat["rating"])
    db.session.commit()
    
    
def calc_items_stat(character, input_dict):
    
    character.helmet = input_dict["helmet"]
    character.necklace = input_dict["necklace"]
    character.mainhand = input_dict["mainhand"]
    character.cuirass = input_dict["cuirass"]
    character.offhand = input_dict["offhand"]
    character.ring1 = input_dict["ring1"]
    character.boot = input_dict["boot"]
    character.ring2 = input_dict["ring2"]
    
    # ----------- ADD ITEMS ------------
    weared_items = []
    weared_item_stat = default_weared_item_stat.copy()
    weared_items.append(Item.query.filter_by(name=character.helmet).first())
    weared_items.append(Item.query.filter_by(name=character.gauntlet).first())
    weared_items.append(Item.query.filter_by(name=character.cuirass).first())
    weared_items.append(Item.query.filter_by(name=character.greaves).first())
    weared_items.append(Item.query.filter_by(name=character.boot).first())
    weared_items.append(Item.query.filter_by(name=character.offhand).first())
    weared_items.append(Item.query.filter_by(name=character.mainhand).first())
    weared_items.append(Item.query.filter_by(name=character.ring1).first())
    weared_items.append(Item.query.filter_by(name=character.ring2).first())
    weared_items.append(Item.query.filter_by(name=character.necklace).first())
     
    for weared_item in weared_items:
                
        weared_item_stat["strength"] += weared_item.strength
        weared_item_stat["endurance"] += weared_item.endurance
        weared_item_stat["speed"] += weared_item.speed
        weared_item_stat["agility"] += weared_item.agility
        weared_item_stat["willpower"] += weared_item.willpower
        weared_item_stat["intelligence"] += weared_item.intelligence
        weared_item_stat["personality"] += weared_item.personality
        weared_item_stat["luck"] += weared_item.luck
        
        weared_item_stat["blade"] += weared_item.blade
        weared_item_stat["blunt"] += weared_item.blunt
        weared_item_stat["hand_to_hand"] += weared_item.hand_to_hand
        weared_item_stat["armorer"] += weared_item.armorer
        weared_item_stat["block"] += weared_item.block
        weared_item_stat["heavy_armor"] += weared_item.heavy_armor
        weared_item_stat["athletics"] += weared_item.athletics
        weared_item_stat["acrobatics"] += weared_item.acrobatics
        weared_item_stat["light_armor"] += weared_item.light_armor
        weared_item_stat["security"] += weared_item.security
        weared_item_stat["sneak"] += weared_item.sneak
        weared_item_stat["marksman"] += weared_item.marksman
        weared_item_stat["mercantile"] += weared_item.mercantile
        weared_item_stat["speechcraft"] += weared_item.speechcraft
        weared_item_stat["illusion"] += weared_item.illusion
        weared_item_stat["alchemy"] += weared_item.alchemy
        weared_item_stat["conjuration"] += weared_item.conjuration
        weared_item_stat["mysticism"] += weared_item.mysticism
        weared_item_stat["alteration"] += weared_item.alteration
        weared_item_stat["destruction"] += weared_item.destruction
        weared_item_stat["restoration"] += weared_item.restoration
        
        weared_item_stat["fire_res"] += weared_item.fire_res
        weared_item_stat["cold_res"] += weared_item.cold_res
        weared_item_stat["shock_res"] += weared_item.shock_res
        weared_item_stat["magic_res"] += weared_item.magic_res
        weared_item_stat["poison_res"] += weared_item.poison_res
        weared_item_stat["disease_res"] += weared_item.disease_res
        weared_item_stat["paralysis_res"] += weared_item.paralysis_res
        weared_item_stat["normal_weapon_res"] += weared_item.normal_weapon_res
        
        weared_item_stat["fire_weak"] += weared_item.fire_weak
        weared_item_stat["cold_weak"] += weared_item.cold_weak
        weared_item_stat["shock_weak"] += weared_item.shock_weak
        weared_item_stat["poison_weak"] += weared_item.poison_weak
        weared_item_stat["fire_dmg"] += weared_item.fire_dmg
        weared_item_stat["cold_dmg"] += weared_item.cold_dmg
        weared_item_stat["shock_dmg"] += weared_item.shock_dmg
        weared_item_stat["poison_dmg"] += weared_item.poison_dmg
        weared_item_stat["absorb_life"] += weared_item.absorb_life
        
        weared_item_stat["reflect_dmg"] += weared_item.reflect_dmg
        weared_item_stat["reflect_spell"] += weared_item.reflect_spell
        weared_item_stat["health"] += weared_item.health
        weared_item_stat["magicka"] += weared_item.magicka
        weared_item_stat["fatigue"] += weared_item.fatigue
        weared_item_stat["spell_absorption"] += weared_item.spell_absorption
        weared_item_stat["detect_life"] += weared_item.detect_life
           
    return weared_item_stat, weared_items


# -------------- START DATAS --------------
with app.app_context():
    default_weared_item_stat = {"rating": 0, "damage": 0, "strength": 0, "endurance": 0, "speed": 0, "agility": 0, "willpower": 0, 
                            "intelligence": 0, "personality": 0, "luck": 0, "strength": 0, "blade": 0, "blunt": 0, 
                            "hand_to_hand": 0, "armorer": 0, "block": 0, "heavy_armor": 0, "athletics": 0, "acrobatics": 0, 
                            "light_armor": 0, "security": 0, "sneak": 0, "marksman": 0, "mercantile": 0, "speechcraft": 0, 
                            "illusion": 0, "alchemy": 0, "conjuration": 0, "mysticism": 0, "alteration": 0, "destruction": 0, 
                            "restoration": 0, "fire_res": 0, "cold_res": 0, "shock_res": 0, "magic_res": 0, "poison_res": 0, 
                            "disease_res": 0, "paralysis_res": 0, "normal_weapon_res": 0, "fire_weak": 0, "cold_weak": 0,
                            "shock_weak": 0, "poison_weak": 0, "fire_dmg": 0, "cold_dmg": 0, "shock_dmg": 0, "poison_dmg": 0,
                            "absorb_life": 0, "reflect_dmg": 0, "reflect_spell": 0, "health": 0, "magicka": 0, "fatigue": 0,
                            "spell_absorption": 0, "detect_life": 0
                            }
    race_selection = []
    main_hands = []
    A_CLASS = [class_.name for class_ in Class.query.all()]
    A_RACE = list({race.name for race in Race.query.all()})
    race = Race.query.filter_by(name="Altmer", gender="Male").first()
    old_race = race
    class_ = Class.query.filter_by(name="Acrobat").first()
    old_class_ = class_
    add_data = Character.query.filter_by(name="Add Skill").first()
    def_character = Character.query.filter_by(name="Default").first()
    character = Character.query.filter_by(name="Current").first()
    classes = Class.query.all()
    races = Race.query.all()
    for race in races:
        race_selection.append(race.name)
    race_selection = list(set(race_selection))
    birthsigns = BirthSign.query.all()
    mainhands = Item.query.filter_by(wear='1h').all()
    two_hands = Item.query.filter_by(wear='2h').all()
    for two_hand in two_hands:
        mainhands.append(two_hand)
    offhands = Item.query.filter_by(wear='offhand')
    boots = Item.query.filter_by(wear='boots')
    cuirasses = Item.query.filter_by(wear='cuirass')
    greavess = Item.query.filter_by(wear='greaves')
    gauntlets = Item.query.filter_by(wear='gauntlet')
    helmets = Item.query.filter_by(wear='helmet')
    rings = Item.query.filter_by(wear='ring')
    necklaces = Item.query.filter_by(wear='necklace')
  

@app.route("/", methods=["GET", "POST"])
def home():
    class_ = old_class_
    if request.method == 'POST':
        # Curret input Values
        input_dict = request.form.to_dict()
        input_dict = check_inputs(input_dict, A_SKILL, add_data)
        race = Race.query.filter_by(name=input_dict["race"], gender=input_dict["gender"]).first()
        class_ = Class.query.filter_by(name=input_dict["class"]).first()
        birthsign = BirthSign.query.filter_by(name=input_dict["birthsign"]).first()
        weared_item_stat, weared_items = calc_items_stat(character, input_dict)
        
        update_character(character, race, class_, weared_item_stat, birthsign, add_data, weared_items)
                    
    return render_template('calculator.html',character=character, classes=classes, class_=class_, birthsigns=birthsigns, races=races,
                           helmets=helmets, cuirasses=cuirasses, gauntlets=gauntlets, boots=boots, greavess=greavess, race_selection=race_selection,
                           offhands=offhands, mainhands=mainhands, rings=rings, necklaces=necklaces, add_data=add_data)
    

@app.route("/create_db")
def create_db():
    db.create_all()
    return redirect("/fill_db")

@app.route("/fill_db")
def fill_db():
    db.session.add_all(CLASSES)
    db.session.add_all(RACES)
    db.session.add_all(BIRTHSIGNS)
    db.session.add_all(ITEMS)
    db.session.add_all(CHARACTERS)
    db.session.commit()
    return redirect("/")