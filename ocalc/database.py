from .models import BirthSign, Race, Class, Item, Character

# Character
CHARACTERS = []

CHARACTERS.append(Character(name='Default'))
CHARACTERS.append(Character(name='Current'))
CHARACTERS.append(Character(name='Add Skills'))

#--------------------------------------------------------------
# BIRTHSIGNS
BIRTHSIGNS = []

BIRTHSIGNS.append(BirthSign(name="Lady", willpower=10, endurance=10))
BIRTHSIGNS.append(BirthSign(name="Steed", speed=20))
BIRTHSIGNS.append(BirthSign(name="Thief", agility=10, luck=10, speed=10))
BIRTHSIGNS.append(BirthSign(name="Warrior", strength=10, endurance=10))

    
RACES = []

RACES.append(Race(name="Altmer", gender="Male", strength=30, intelligence=50, speed=30,
                alchemy=5,alteration=10, conjuration=5, destruction=10, illusion=5, mysticism=10,
                magicka=100, fire_res=-25, cold_res=-25, shock_res=-25,
                disease_res=75))

RACES.append(Race(name="Altmer", gender="Female", strength=30, intelligence=50, endurance=30,
                alchemy=5, alteration=10, conjuration=5, destruction=10, illusion=5, mysticism=10,
                magicka=100, fire_res=-25, cold_res=-25, shock_res=-25, disease_res=75))

RACES.append(Race(name="Argonian", gender="Male", willpower=30, agility=50, speed=50, endurance=30, personality=30,
                  alchemy=5, athletics=10, blade=5, hand_to_hand=5, illusion=5, mysticism=5, security=10,
                  poison_res=100, disease_res=75))

RACES.append(Race(name="Argonian", gender="Female", intelligence=50, endurance=30, personality=30,
                alchemy=5, athletics=10, blade=5, hand_to_hand=5, illusion=5, mysticism=5, security=10,
                poison_res=100, disease_res=75))

RACES.append(Race(name="Bosmer", gender="Male", strength=30, willpower=30, agility=50, speed=50, personality=30,
                acrobatics=5, alchemy=10, alteration=5, light_armor=5, marksman=10, sneak=10,
                disease_res=75))

RACES.append(Race(name="Bosmer", gender="Female", strength=30, willpower=30, agility=50, speed=50, endurance=30,
                acrobatics=5, alchemy=10, alteration=5, light_armor=5, marksman=10, sneak=10,
                disease_res=75))

RACES.append(Race(name="Breton", gender="Male", intelligence=50, willpower=50, agility=30, speed=30, endurance=30,
                alchemy=5, alteration=5, conjuration=10, illusion=5, mysticism=10, restoration=10,
                magicka=50, magic_res=50))

RACES.append(Race(name="Breton", gender="Female", strength=30, intelligence=50, willpower=50, agility=30, endurance=30,
                alchemy=5, alteration=5, conjuration=10, illusion=5, mysticism=10, restoration=10,
                magicka=50, magic_res=50))

RACES.append(Race(name="Dunmer", gender="Male", willpower=30, speed=50, personality=30,
                athletics=5, blade=10, blunt=5, destruction=10, light_armor=5, marksman=5, mysticism=5,
                fire_res=50))

RACES.append(Race(name="Dunmer", gender="Female", willpower=30, speed=50, endurance=30,
                athletics=5, blade=10, blunt=5, destruction=10, light_armor=5, marksman=5, mysticism=5,
                fire_res=50))

RACES.append(Race(name="Imperial", gender="Male", willpower=30, agility=30, personality=50,
                blade=10, blunt=5, hand_to_hand=5, heavy_armor=10, mercantile=10, speechcraft=10))

RACES.append(Race(name="Imperial", gender="Female", agility=30, speed=30, personality=50,
                blade=10, blunt=5, hand_to_hand=5, heavy_armor=10, mercantile=10, speechcraft=10))

RACES.append(Race(name="Khajiit", gender="Male", willpower=30, agility=50, endurance=30,
                acrobatics=10, athletics=5, blade=5, hand_to_hand=10, light_armor=5, security=5, sneak=5))

RACES.append(Race(name="Khajiit", gender="Female", strength=30, willpower=30, agility=50,
                acrobatics=10, athletics=5, blade=5, hand_to_hand=10, light_armor=5, security=5, sneak=5))

RACES.append(Race(name="Nord", gender="Male", strength=50, intelligence=30, willpower=30, endurance=50, personality=30,
                armorer=5, blade=10, block=10, blunt=10, heavy_armor=10, restoration=5,
                cold_res=50))

RACES.append(Race(name="Nord", gender="Female", strength=50, intelligence=30, personality=30,
                armorer=5, blade=10, block=10, blunt=10, heavy_armor=10, restoration=5,
                cold_res=50))

RACES.append(Race(name="Orc", gender="Male", strength=45, intelligence=30, willpower=50, agility=35, speed=30, endurance=50, personality=30,
                armorer=10, block=10, blunt=10, hand_to_hand=5, heavy_armor=10,
                magic_res=25))

RACES.append(Race(name="Orc", gender="Female", strength=45, willpower=45, agility=35, speed=30, endurance=50, personality=25,
                armorer=10, block=10, blunt=10, hand_to_hand=5, heavy_armor=10,
                magic_res=25))

RACES.append(Race(name="Redguard", gender="Male", strength=50, intelligence=30, willpower=30, endurance=50, personality=30,
                athletics=10, blade=10, blunt=10, heavy_armor=5, light_armor=5, mercantile=5,
                poison_res=75, disease_res=75))

RACES.append(Race(name="Redguard", gender="Female", intelligence=30, willpower=30, endurance=50,
                athletics=10, blade=10, blunt=10, heavy_armor=5, light_armor=5, mercantile=5,
                poison_res=75, disease_res=75))

    
CLASSES = []

CLASSES.append(Class(name="Acrobat", agility=5, endurance=5, blade=25, block=25,
                acrobatics=25, marksman=25, security=25, sneak=25, speechcraft=25,))

CLASSES.append(Class(name="Agent", agility=5, personality=5, illusion=25, acrobatics=25,
                marksman=25, mercantile=25, security=25, sneak=25, speechcraft=25,))

CLASSES.append(Class(name="Archer", agility=5, strength=5, armorer=25, blade=25,
                blunt=25, hand_to_hand=25, light_armor=25, marksman=25, sneak=25,))

CLASSES.append(Class(name="Assassin", intelligence=5, speed=5, blade=25, alchemy=25,
                acrobatics=25, light_armor=25, marksman=25, security=25, sneak=25,))

CLASSES.append(Class(name="Barbarian", speed=5, strength=5, armorer=25, athletics=25,
                blade=25, block=25, blunt=25, hand_to_hand=25, light_armor=25,))

CLASSES.append(Class(name="Bard", intelligence=5, personality=5, blade=25, block=25,
                alchemy=25, illusion=25, light_armor=25, mercantile=25, speechcraft=25))

CLASSES.append(Class(name="Battlemage", intelligence=5, strength=5, blade=25, blunt=25,alchemy=25, alteration=25, conjuration=25, destruction=25, mysticism=25))

CLASSES.append(Class(name="Crusader", strength=5, willpower=5, athletics=25, blade=25,
                blunt=25, hand_to_hand=25, heavy_armor=25, destruction=25, restoration=25))

CLASSES.append(Class(name="Healer", personality=5, willpower=5, alchemy=25, alteration=25,
                destruction=25, illusion=25, restoration=25, mercantile=25, speechcraft=25))

CLASSES.append(Class(name="Knight", personality=5, strength=5, blade=25, block=25,
                blunt=25, hand_to_hand=25, heavy_armor=25, illusion=25, speechcraft=25))

CLASSES.append(Class(name="Mage", intelligence=5, willpower=5, alchemy=25, alteration=25,
                conjuration=25, destruction=25, illusion=25, mysticism=25, restoration=25))

CLASSES.append(Class(name="Monk", agility=5, willpower=5, athletics=25, hand_to_hand=25,
                alteration=25, acrobatics=25, marksman=25, security=25, sneak=25,
                ))

CLASSES.append(Class(name="Nightblade", speed=5, willpower=5, athletics=25, blade=25,
                alteration=25, destruction=25, restoration=25, acrobatics=25, light_armor=25,
                ))

CLASSES.append(Class(name="Pilgrim", endurance=5, personality=5, armorer=25, block=25,
                blunt=25, light_armor=25, mercantile=25, security=25, sneak=25,
                ))

CLASSES.append(Class(name="Rogue", personality=5, speed=5, athletics=25, blade=25,
                block=25, alchemy=25, illusion=25, light_armor=25, mercantile=25,
                ))

CLASSES.append(Class(name="Scout", endurance=5, speed=5, armorer=25, athletics=25,
                blade=25, block=25, alchemy=25, acrobatics=25, light_armor=25,
                ))

CLASSES.append(Class(name="Sorcerer", endurance=5, intelligence=5, heavy_armor=25, alchemy=25,
                alteration=25, conjuration=25, destruction=25, mysticism=25, restoration=25,
                ))

CLASSES.append(Class(name="Spellsword", endurance=5, willpower=5, blade=25, block=25,
                heavy_armor=25, alteration=25, destruction=25, illusion=25, restoration=25,
                ))

CLASSES.append(Class(name="Thief", agility=5, speed=5, acrobatics=25, light_armor=25,
                marksman=25, mercantile=25, security=25, sneak=25, speechcraft=25,
                ))

CLASSES.append(Class(name="Warrior", endurance=5, strength=5, armorer=25, athletics=25,
                blade=25, block=25, blunt=25, hand_to_hand=25, heavy_armor=25,
                ))

CLASSES.append(Class(name="Witchhunter", agility=5, intelligence=5, athletics=25, alchemy=25,
                conjuration=25, destruction=25, mysticism=25, marksman=25, security=25,
                ))

#--------------------------------------------------------------
# ITEMS / ARMOR
ITEMS = []

# Rough Leather
ITEMS.append(Item(name="Rough Leather Boots", skill="Light Armor", wear="boot", rating=2.5))
ITEMS.append(Item(name="Rough Leather Cuirass", skill="Light Armor", wear="full-cuirass", rating=6.25))
ITEMS.append(Item(name="Rough Leather Gauntlets", skill="Light Armor", wear="gauntlet", rating=2.5))
ITEMS.append(Item(name="Rough Leather Helmet", skill="Light Armor", wear="helmet", rating=2.5))
ITEMS.append(Item(name="Rough Leather Shield", skill="Light Armor", wear="offhand", rating=7))

# Fur Armor
ITEMS.append(Item(name="Fur Boots", skill="Light Armor", wear="boots", rating=2))
ITEMS.append(Item(name="Fur Cuirass", skill="Light Armor", wear="cuirass", rating=5))
ITEMS.append(Item(name="Fur Gauntlets", skill="Light Armor", wear="gauntlets", rating=2))
ITEMS.append(Item(name="Fur Greaves", skill="Light Armor", wear="greaves", rating=3))
ITEMS.append(Item(name="Fur Helmet", skill="Light Armor", wear="helmet", rating=2))
ITEMS.append(Item(name="Fur Shield", skill="Light Armor", wear="offhand", rating=2))

# Leather Armor
ITEMS.append(Item(name="Leather Boots", skill="Light Armor", wear="boots", rating=2.5))
ITEMS.append(Item(name="Leather Cuirass", skill="Light Armor", wear="cuirass", rating=6.25))
ITEMS.append(Item(name="Leather Gauntlets", skill="Light Armor", wear="gauntlets", rating=2.5))
ITEMS.append(Item(name="Leather Greaves", skill="Light Armor", wear="greaves", rating=3.75))
ITEMS.append(Item(name="Leather Helmet", skill="Light Armor", wear="helmet", rating=2.5))
ITEMS.append(Item(name="Leather Shield", skill="Light Armor", wear="offhand", rating=7.5))
ITEMS.append(Item(name="Leather Bracer", skill="Light Armor", wear="gauntlets", rating=1))

# Chainmail Armor
ITEMS.append(Item(name="Chainmail Boots", skill="Light Armor", wear="boots", rating=3))
ITEMS.append(Item(name="Chainmail Cuirass", skill="Light Armor", wear="cuirass", rating=8))
ITEMS.append(Item(name="Chainmail Gauntlets", skill="Light Armor", wear="gauntlets", rating=3))
ITEMS.append(Item(name="Chainmail Greaves", skill="Light Armor", wear="greaves", rating=4))
ITEMS.append(Item(name="Chainmail Helmet", skill="Light Armor", wear="helmet", rating=3))
ITEMS.append(Item(name="Chainmail Shield", skill="Light Armor", wear="offhand", rating=9))

# Mithril Armor
ITEMS.append(Item(name="Mithril Boots", skill="Light Armor", wear="boots", rating=3.5))
ITEMS.append(Item(name="Mithril Cuirass", skill="Light Armor", wear="cuirass", rating=8.75))
ITEMS.append(Item(name="Mithril Gauntlets", skill="Light Armor", wear="gauntlets", rating=3.5))
ITEMS.append(Item(name="Mithril Greaves", skill="Light Armor", wear="greaves", rating=5.25))
ITEMS.append(Item(name="Mithril Helmet", skill="Light Armor", wear="helmet", rating=3.5))
ITEMS.append(Item(name="Mithril Shield", skill="Light Armor", wear="offhand", rating=10.5))

# Elven Armor
ITEMS.append(Item(name="Elven Boots", skill="Light Armor", wear="boots", rating=4))
ITEMS.append(Item(name="Elven Cuirass", skill="Light Armor", wear="cuirass", rating=10))
ITEMS.append(Item(name="Elven Gauntlets", skill="Light Armor", wear="gauntlets", rating=4))
ITEMS.append(Item(name="Elven Greaves", skill="Light Armor", wear="greaves", rating=6))
ITEMS.append(Item(name="Elven Helmet", skill="Light Armor", wear="helmet", rating=4))
ITEMS.append(Item(name="Elven Shield", skill="Light Armor", wear="offhand", rating=12))

# Glass Armor
ITEMS.append(Item(name="Glass Boots", skill="Light Armor", wear="boots", rating=5))
ITEMS.append(Item(name="Glass Cuirass", skill="Light Armor", wear="cuirass", rating=12.5))
ITEMS.append(Item(name="Glass Gauntlets", skill="Light Armor", wear="gauntlets", rating=5))
ITEMS.append(Item(name="Glass Greaves", skill="Light Armor", wear="greaves", rating=7.5))
ITEMS.append(Item(name="Glass Helmet", skill="Light Armor", wear="helmet", rating=5))
ITEMS.append(Item(name="Glass Shield", skill="Light Armor", wear="offhand", rating=15))

# Rusty Iron Armor
ITEMS.append(Item(name="Rusty Iron Cuirass", skill="Light Armor", wear="cuirass", rating=9))
ITEMS.append(Item(name="Rusty Iron Gauntlets", skill="Light Armor", wear="gauntlets", rating=3.5))
ITEMS.append(Item(name="Rusty Iron Greaves", skill="Light Armor", wear="greaves", rating=5.5))
ITEMS.append(Item(name="Rusty Iron Helmet", skill="Light Armor", wear="helmet", rating=3.5))
ITEMS.append(Item(name="Rusty Iron Shield", skill="Light Armor", wear="offhand", rating=11))

# Iron Armor
ITEMS.append(Item(name="Iron Boots", skill="Light Armor", wear="boots", rating=4))
ITEMS.append(Item(name="Iron Cuirass", skill="Light Armor", wear="cuirass", rating=10))
ITEMS.append(Item(name="Iron Gauntlets", skill="Light Armor", wear="gauntlets", rating=4))
ITEMS.append(Item(name="Iron Greaves", skill="Light Armor", wear="greaves", rating=6))
ITEMS.append(Item(name="Iron Helmet", skill="Light Armor", wear="helmet", rating=4))
ITEMS.append(Item(name="Iron Shield", skill="Light Armor", wear="offhand", rating=12))

# Steel Armor
ITEMS.append(Item(name="Steel Boots", skill="Light Armor", wear="boots", rating=4.5))
ITEMS.append(Item(name="Steel Cuirass", skill="Light Armor", wear="cuirass", rating=11.25))
ITEMS.append(Item(name="Steel Gauntlets", skill="Light Armor", wear="gauntlets", rating=4.5))
ITEMS.append(Item(name="Steel Greaves", skill="Light Armor", wear="greaves", rating=6.75))
ITEMS.append(Item(name="Steel Helmet", skill="Light Armor", wear="helmet", rating=4.5))
ITEMS.append(Item(name="Steel Shield", skill="Light Armor", wear="offhand", rating=13.5))

# Dwarwen Armor
ITEMS.append(Item(name="Dwarwen Boots", skill="Light Armor", wear="boots", rating=5))
ITEMS.append(Item(name="Dwarwen Cuirass", skill="Light Armor", wear="cuirass", rating=12.5))
ITEMS.append(Item(name="Dwarwen Gauntlets", skill="Light Armor", wear="gauntlets", rating=5))
ITEMS.append(Item(name="Dwarwen Greaves", skill="Light Armor", wear="greaves", rating=7.5))
ITEMS.append(Item(name="Dwarwen Helmet", skill="Light Armor", wear="helmet", rating=5))
ITEMS.append(Item(name="Dwarwen Shield", skill="Light Armor", wear="offhand", rating=15))

# Orcish Armor
ITEMS.append(Item(name="Orcish Boots", skill="Light Armor", wear="boots", rating=5.5))
ITEMS.append(Item(name="Orcish Cuirass", skill="Light Armor", wear="cuirass", rating=13.75))
ITEMS.append(Item(name="Orcish Gauntlets", skill="Light Armor", wear="gauntlets", rating=5.5))
ITEMS.append(Item(name="Orcish Greaves", skill="Light Armor", wear="greaves", rating=8.25))
ITEMS.append(Item(name="Orcish Helmet", skill="Light Armor", wear="helmet", rating=5.5))
ITEMS.append(Item(name="Orcish Shield", skill="Light Armor", wear="offhand", rating=16.5))

# Ebony Armor
ITEMS.append(Item(name="Ebony Boots", skill="Light Armor", wear="boots", rating=6))
ITEMS.append(Item(name="Ebony Cuirass", skill="Light Armor", wear="cuirass", rating=15))
ITEMS.append(Item(name="Ebony Gauntlets", skill="Light Armor", wear="gauntlets", rating=6))
ITEMS.append(Item(name="Ebony Greaves", skill="Light Armor", wear="greaves", rating=9))
ITEMS.append(Item(name="Ebony Helmet", skill="Light Armor", wear="helmet", rating=6))
ITEMS.append(Item(name="Ebony Shield", skill="Light Armor", wear="offhand", rating=18))

# Daedric Armor
ITEMS.append(Item(name="Daedric Boots", skill="Light Armor", wear="boots", rating=7.5))
ITEMS.append(Item(name="Daedric Cuirass", skill="Light Armor", wear="cuirass", rating=18.75))
ITEMS.append(Item(name="Daedric Gauntlets", skill="Light Armor", wear="gauntlets", rating=7.5))
ITEMS.append(Item(name="Daedric Greaves", skill="Light Armor", wear="greaves", rating=11.25))
ITEMS.append(Item(name="Daedric Helmet", skill="Light Armor", wear="helmet", rating=7.5))
ITEMS.append(Item(name="Daedric Shield", skill="Light Armor", wear="offhand", rating=22.5))

# Magic Boots
ITEMS.append(Item(name="Boots of the Atronach", skill="Heavy Armor", wear="boots", rating=5,
                    fire_res=50, cold_res=50, shock_res=50))
ITEMS.append(Item(name="Boots of the Olympian", skill="Light Armor", wear="boots", rating=2.5,
                    agility=8, speed=8, acrobatics=8, athletics=8))
ITEMS.append(Item(name="Grounded Boots", skill="Light Armor", wear="boots", rating=5,
                    shock_res=50, poison_weak=50))

# Magic Cuirass
ITEMS.append(Item(name="Ice Cuirass", skill="Heavy Armor", wear="cuirass", rating=13.75,
                    cold_res=50, fire_weak=25))

# Magic Gauntlets
ITEMS.append(Item(name="Gauntlets of Blinding Speed", skill="Light Armor", wear="gauntlets",rating=3.5,
                    agility=8, luck=8, speed=8))
ITEMS.append(Item(name="Gauntlets of the Battlemage", skill="Light Armor", wear="gauntlets",rating=2.5,
                    alteration=8, conjuration=8, destruction=8))
ITEMS.append(Item(name="Gauntlets of the Pugilist", skill="Heavy Armor", wear="gauntlets",rating=4,
                    strength=8, agility=8, hand_to_hand=8))
ITEMS.append(Item(name="Gauntlets of the Weaponmaster", skill="Heavy Armor", wear="gauntlets",rating=4.5,
                    blade=8, block=8, blunt=8))
ITEMS.append(Item(name="Gloves of the Caster", skill="Light Armor", wear="gauntlets",rating=2.5,
                    illusion=8, mysticism=8, restoration=8))

# Magic Greaves
ITEMS.append(Item(name="Greaves of Resilient Flesh", skill="Light Armor", wear="greaves",rating=3,
                    disease_res=50, normal_weapon_res=11, poison_res=50))
ITEMS.append(Item(name="Greaves of the Sun", skill="Heavy Armor", wear="greaves",rating=9,
                    fire_res=50, cold_weak=50))
ITEMS.append(Item(name="Greaves of Well-Being", skill="Light Armor", wear="greaves",rating=5.25,
                    endurance=8, luck=8, strength=8))

# Magic Helmet
ITEMS.append(Item(name="Helmet of the Mage", skill="Heavy Armor", wear="helmet",rating=6,
                    magicka=20, spell_absorption=14))
ITEMS.append(Item(name="Helmet of the Mind", skill="Light Armor", wear="helmet",rating=3.5,
                    disease_res=50, normal_weapon_res=11, poison_res=50))

# Magic Robe
ITEMS.append(Item(name="Robe of Glib Tongues", wear="robe",rating=3.5,
                    disease_res=50, normal_weapon_res=11, poison_res=50))

# Magic Shield
ITEMS.append(Item(name="Mirror Shield", wear="offhand",rating=15,
                    reflect_dmg=8, reflect_spell=14))
ITEMS.append(Item(name="Shield of the Elements", wear="offhand",rating=12,
                    fire_res=20, cold_res=20, shock_res=20))

# ************************************
# ITEMS / WEAPON
# Daggers
ITEMS.append(Item(name="Rusty Iron Dagger", skill="Blade", damage=3, wear='1h'))
ITEMS.append(Item(name="Iron Dagger", skill="Blade", damage=5, wear='1h'))
ITEMS.append(Item(name="Fine Iron Dagger", skill="Blade", damage=6, wear='1h'))
ITEMS.append(Item(name="Steel Dagger", skill="Blade", damage=7, wear='1h'))
ITEMS.append(Item(name="Fine Steel Dagger", skill="Blade", damage=8, wear='1h'))
ITEMS.append(Item(name="Silver Dagger", skill="Blade", damage=9, wear='1h'))
ITEMS.append(Item(name="Dwarven Dagger", skill="Blade", damage=11, wear='1h'))
ITEMS.append(Item(name="Elven Dagger", skill="Blade", damage=13, wear='1h'))
ITEMS.append(Item(name="Glass Dagger", skill="Blade", damage=15, wear='1h'))
ITEMS.append(Item(name="Ebony Dagger", skill="Blade", damage=17, wear='1h'))
ITEMS.append(Item(name="Daedric Dagger", skill="Blade", damage=19, wear='1h'))

# Shortswords
ITEMS.append(Item(name="Rusty Iron Shortsword", skill="Blade", damage=5, wear='1h'))
ITEMS.append(Item(name="Iron Shortsword", skill="Blade", damage=7, wear='1h'))
ITEMS.append(Item(name="Fine Iron Shortsword", skill="Blade", damage=8, wear='1h'))
ITEMS.append(Item(name="Steel Shortsword", skill="Blade", damage=9, wear='1h'))
ITEMS.append(Item(name="Fine Steel Shortsword", skill="Blade", damage=10, wear='1h'))
ITEMS.append(Item(name="Silver Shortsword", skill="Blade", damage=11, wear='1h'))
ITEMS.append(Item(name="Dwarven Shortsword", skill="Blade", damage=13, wear='1h'))
ITEMS.append(Item(name="Elven Shortsword", skill="Blade", damage=15, wear='1h'))
ITEMS.append(Item(name="Glass Shortsword", skill="Blade", damage=17, wear='1h'))
ITEMS.append(Item(name="Ebony Shortsword", skill="Blade", damage=19, wear='1h'))
ITEMS.append(Item(name="Daedric Shortsword", skill="Blade", damage=21, wear='1h'))

# Longswords
ITEMS.append(Item(name="Iron Longsword", skill="Blade", damage=10, wear='1h'))
ITEMS.append(Item(name="Fine Iron Longsword", skill="Blade", damage=11, wear='1h'))
ITEMS.append(Item(name="Steel Longsword", skill="Blade", damage=12, wear='1h'))
ITEMS.append(Item(name="Fine Steel Longsword", skill="Blade", damage=13, wear='1h'))
ITEMS.append(Item(name="Silver Longsword", skill="Blade", damage=14, wear='1h'))
ITEMS.append(Item(name="Dwarven Longsword", skill="Blade", damage=16, wear='1h'))
ITEMS.append(Item(name="Elven Longsword", skill="Blade", damage=18, wear='1h'))
ITEMS.append(Item(name="Glass Longsword", skill="Blade", damage=20, wear='1h'))
ITEMS.append(Item(name="Ebony Longsword", skill="Blade", damage=22, wear='1h'))
ITEMS.append(Item(name="Daedric Longsword", skill="Blade", damage=24, wear='1h'))

# Other 1h Blade
ITEMS.append(Item(name="Akaviri Katana", skill="Blade", damage=14, wear='1h'))
ITEMS.append(Item(name="Ancient Akaviri Katana", skill="Blade", damage=15, wear='1h'))
ITEMS.append(Item(name="Ruined Akaviri Katana", skill="Blade", damage=8, wear='1h'))
ITEMS.append(Item(name="Steel Cutlass", skill="Blade", damage=11, wear='1h'))
ITEMS.append(Item(name="Sharpened Cutlass", skill="Blade", damage=11, wear='1h'))

# 2h Blades
ITEMS.append(Item(name="Iron Claymore", skill="Blade", damage=12, wear='2h'))
ITEMS.append(Item(name="Fine Iron Claymore", skill="Blade", damage=13, wear='2h'))
ITEMS.append(Item(name="Steel Claymore", skill="Blade", damage=14, wear='2h'))
ITEMS.append(Item(name="Fine Steel Claymore", skill="Blade", damage=15, wear='2h'))
ITEMS.append(Item(name="Silver Claymore", skill="Blade", damage=16, wear='2h'))
ITEMS.append(Item(name="Dwarven Claymore", skill="Blade", damage=18, wear='2h'))
ITEMS.append(Item(name="Elven Claymore", skill="Blade", damage=20, wear='2h'))
ITEMS.append(Item(name="Glass Claymore", skill="Blade", damage=22, wear='2h'))
ITEMS.append(Item(name="Ebony Claymore", skill="Blade", damage=24, wear='2h'))
ITEMS.append(Item(name="Daedric Claymore", skill="Blade", damage=26, wear='2h'))

# Other 2h Blade
ITEMS.append(Item(name="Akaviri Dai-Katana", skill="Blade", damage=16, wear='2h'))

# 1h Blunt
ITEMS.append(Item(name="Rusty Iron Mace", skill="Blunt", damage=7, wear='1h'))
ITEMS.append(Item(name="Iron Mace", skill="Blunt", damage=10, wear='1h'))
ITEMS.append(Item(name="Fine Iron Mace", skill="Blunt", damage=11, wear='1h'))
ITEMS.append(Item(name="Steel Mace", skill="Blunt", damage=12, wear='1h'))
ITEMS.append(Item(name="Fine Steel Mace", skill="Blunt", damage=13, wear='1h'))
ITEMS.append(Item(name="Silver Mace", skill="Blunt", damage=14, wear='1h'))
ITEMS.append(Item(name="Dwarven Mace", skill="Blunt", damage=16, wear='1h'))
ITEMS.append(Item(name="Elven Mace", skill="Blunt", damage=18, wear='1h'))
ITEMS.append(Item(name="Glass Mace", skill="Blunt", damage=20, wear='1h'))
ITEMS.append(Item(name="Ebony Mace", skill="Blunt", damage=22, wear='1h'))
ITEMS.append(Item(name="Daedric Mace", skill="Blunt", damage=24, wear='1h'))

# War Axe
ITEMS.append(Item(name="Rusty Iron War Axe", skill="Blunt", damage=5, wear='1h'))
ITEMS.append(Item(name="Iron War Axe", skill="Blunt", damage=8, wear='1h'))
ITEMS.append(Item(name="Fine Iron War Axe", skill="Blunt", damage=9, wear='1h'))
ITEMS.append(Item(name="Steel War Axe", skill="Blunt", damage=10, wear='1h'))
ITEMS.append(Item(name="Fine Steel War Axe", skill="Blunt", damage=11, wear='1h'))
ITEMS.append(Item(name="Silver War Axe", skill="Blunt", damage=12, wear='1h'))
ITEMS.append(Item(name="Dwarven War Axe", skill="Blunt", damage=14, wear='1h'))
ITEMS.append(Item(name="Elven War Axe", skill="Blunt", damage=16, wear='1h'))
ITEMS.append(Item(name="Glass War Axe", skill="Blunt", damage=18, wear='1h'))
ITEMS.append(Item(name="Ebony War Axe", skill="Blunt", damage=20, wear='1h'))
ITEMS.append(Item(name="Daedric War Axe", skill="Blunt", damage=22, wear='1h'))

# Other Blunt
#UNDER CONSTRUCTON!

# 2h Battle Axe
ITEMS.append(Item(name="Iron Battle Axe", skill="Blunt", damage=12, wear='2h'))
ITEMS.append(Item(name="Fine Iron Battle Axe", skill="Blunt", damage=13, wear='2h'))
ITEMS.append(Item(name="Steel Battle Axe", skill="Blunt", damage=14, wear='2h'))
ITEMS.append(Item(name="Fine Steel Battle Axe", skill="Blunt", damage=15, wear='2h'))
ITEMS.append(Item(name="Silver Battle Axe", skill="Blunt", damage=16, wear='2h'))
ITEMS.append(Item(name="Dwarven Battle Axe", skill="Blunt", damage=18, wear='2h'))
ITEMS.append(Item(name="Elven Battle Axe", skill="Blunt", damage=20, wear='2h'))
ITEMS.append(Item(name="Glass Battle Axe", skill="Blunt", damage=22, wear='2h'))
ITEMS.append(Item(name="Ebony Battle Axe", skill="Blunt", damage=24, wear='2h'))
ITEMS.append(Item(name="Daedric Battle Axe", skill="Blunt", damage=26, wear='2h'))

#2h Warhammer
ITEMS.append(Item(name="Iron Warhammer", skill="Blunt", damage=14, wear='2h'))
ITEMS.append(Item(name="Fine Iron Warhammer", skill="Blunt", damage=15, wear='2h'))
ITEMS.append(Item(name="Steel Warhammer", skill="Blunt", damage=16, wear='2h'))
ITEMS.append(Item(name="Fine Steel Warhammer", skill="Blunt", damage=17, wear='2h'))
ITEMS.append(Item(name="Silver Warhammer", skill="Blunt", damage=18, wear='2h'))
ITEMS.append(Item(name="Dwarven Warhammer", skill="Blunt", damage=20, wear='2h'))
ITEMS.append(Item(name="Elven Warhammer", skill="Blunt", damage=22, wear='2h'))
ITEMS.append(Item(name="Glass Warhammer", skill="Blunt", damage=24, wear='2h'))
ITEMS.append(Item(name="Ebony Warhammer", skill="Blunt", damage=26, wear='2h'))
ITEMS.append(Item(name="Daedric Warhammer", skill="Blunt", damage=28, wear='2h'))

# Bow
ITEMS.append(Item(name="Rusty Iron Bow", skill="Marksman", damage=8, wear='1h'))
ITEMS.append(Item(name="Iron Bow", skill="Marksman", damage=8, wear='1h'))
ITEMS.append(Item(name="Fine Iron Bow", skill="Marksman", damage=9, wear='1h'))
ITEMS.append(Item(name="Steel Bow", skill="Marksman", damage=9, wear='1h'))
ITEMS.append(Item(name="Fine Steel Bow", skill="Marksman", damage=10, wear='1h'))
ITEMS.append(Item(name="Silver Bow", skill="Marksman", damage=10, wear='1h'))
ITEMS.append(Item(name="Black Bow", skill="Marksman", damage=10, wear='1h'))
ITEMS.append(Item(name="Dwarven Bow", skill="Marksman", damage=12, wear='1h'))
ITEMS.append(Item(name="Elven Bow", skill="Marksman", damage=14, wear='1h'))
ITEMS.append(Item(name="Glass Bow", skill="Marksman", damage=16, wear='1h'))
ITEMS.append(Item(name="Ebony Bow", skill="Marksman", damage=18, wear='1h'))
ITEMS.append(Item(name="Daedric Bow", skill="Marksman", damage=20, wear='1h'))

# Arrow
ITEMS.append(Item(name="Iron Arrow", skill="Marksman", damage=8, wear='offhand'))
ITEMS.append(Item(name="Steel Arrow", skill="Marksman", damage=9, wear='offhand'))
ITEMS.append(Item(name="Silver Arrow", skill="Marksman", damage=10, wear='offhand'))
ITEMS.append(Item(name="Dwarven Arrow", skill="Marksman", damage=11, wear='offhand'))
ITEMS.append(Item(name="Elven Arrow", skill="Marksman", damage=12, wear='offhand'))
ITEMS.append(Item(name="Glass Arrow", skill="Marksman", damage=13, wear='offhand'))
ITEMS.append(Item(name="Ebony Arrow", skill="Marksman", damage=14, wear='offhand'))
ITEMS.append(Item(name="Daedric Arrow", skill="Marksman", damage=15, wear='offhand'))

# Magic Amulet
ITEMS.append(Item(name="Acrobat's Amulet", speed=20, athletics=20, acrobatics=20, wear='necklace'))
ITEMS.append(Item(name="Amulet of Axes", reflect_dmg=33, blunt=25, wear='necklace'))
ITEMS.append(Item(name="Necklace of Swords", reflect_dmg=33, blade=25, wear='necklace'))

# Magic Ring
ITEMS.append(Item(name="Elemental Ring", fire_res=20, cold_res=20, shock_res=20, wear='ring'))
ITEMS.append(Item(name="Mundane Ring", reflect_spell=35, magic_res=50, wear='ring'))
ITEMS.append(Item(name="Ring of Perfection", strength=10, endurance=10, agility=10, speed=10,
                  personality=10, willpower=10, intelligence=10, wear='ring'))
ITEMS.append(Item(name="Ring of Skimming", speed=20, athletics=20, water_walking=True, wear='ring'))
ITEMS.append(Item(name="Ring of Stamina", fatigue=25, health=25, wear='ring'))
ITEMS.append(Item(name="Ring of the Iron Fist", hand_to_hand=25, reflect_dmg=33, wear='ring'))
ITEMS.append(Item(name="Ring of Thieves", detect_life=25, sneak=15, security=10, wear='ring'))
ITEMS.append(Item(name="Ring of Treachery", acrobatics=10, mercantile=10, light_armor=10,
                  security=10, sneak=10, speechcraft=10, wear='ring'))
ITEMS.append(Item(name="Ring of Vitality", disease_res=100, paralysis_res=10, poison_res=100, wear='ring'))
ITEMS.append(Item(name="Ring of War", armorer=10, athletics=10, blade=10, block=10, blunt=10,
                  hand_to_hand=10, heavy_armor=10, wear='ring'))
ITEMS.append(Item(name="Ring of Wizardry", alchemy=10, alteration=10, conjuration=10,
                  destruction=10, mysticism=10, restoration=10, wear='ring'))

ITEMS.append(Item(name="Sorcerer's Ring", spell_absorption=25, magicka=25, wear='ring'))

# Null value items
ITEMS.append(Item(name="-", wear='ring'))
ITEMS.append(Item(name="-", wear='necklace'))
ITEMS.append(Item(name="-", wear='helmet'))
ITEMS.append(Item(name="-", wear='gauntlets'))
ITEMS.append(Item(name="-", wear='boot'))
ITEMS.append(Item(name="-", wear='cuirass'))
ITEMS.append(Item(name="-", wear='graves'))
ITEMS.append(Item(name="-", wear='mainhand'))
ITEMS.append(Item(name="-", wear='offhand'))
