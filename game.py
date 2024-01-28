import sys
import random
import pygame

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_RECT = (SCREEN_WIDTH, SCREEN_HEIGHT)

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50

PATH_SPRITE_SIZE = 16

BIOME_GRID_ROWS = 4
BIOME_GRID_COLS = 2

BIOME_WIDTH = 608
BIOME_HEIGHT = 152
BIOME_MARGIN = 20  # Margin between biomes

AI_FONT_COLOR = (255, 255, 255)  # White

# Only 48 possible combiniations, need to increast this substantially
PERSONALITIES = [
    "ANGRY",        # 00
    "JOVIAL",       # 01
    "MYSTERIOUS",   # 02
]

BG01S = [
    "CIRCUS PERFORMER", #00
    "ARTIST",           #01
    "DIPLOMAT",         #02
    "STEAMBOAT CAPTAIN",#03
]

BG02S = [
    "TURNED ADVENTURER",    #00
    "RAISED BY WOLVES",     #01 
    "TURNED REBEL LEADER",  #02
    "SEEKING VENGEANCE",    #03
]

ALL_COMMENTS = {
    (0, 0, 0): [
        "You think this is tough? Try walking a tightrope over a pit of lions while angry! Now THAT was an adventure!",
		"I used to juggle flaming torches for a living, and now I'm dealing with these ridiculous monsters? What a circus my life has become!",
		"These dungeons are like a never-ending clown car of surprises. Just when you think you've seen it all, out pops another ridiculous creature!",
		"I'll show those monsters what a real 'big top' is all about! Prepare to be amazed, you overgrown carnival rejects!",
		"I've tamed lions, tigers, and bears in the circus, but these dungeons are a whole different kind of animal!",
		"Step right up, folks! Watch me turn these foes into confetti with my trusty sword! It's all in a day's work for a circus performer turned adventurer!",
    ],
    (0, 0, 1): [
        "I may have been raised by wolves, but I'll be damned if I let anyone treat me like an animal!",

        "My circus skills might seem wild, but they're nothing compared to the instincts I learned in the wilderness!",

        "Being raised by wolves toughened me up for anything life throws at me, whether it's performing under the big top or battling monsters in the forest.",

        "I howled at the moon with my wolf family, and now I'll howl with fury at anyone who stands in my way!",

        "I may have the heart of a circus performer, but I've got the ferocity of a wolf. Together, I'm a force to be reckoned with!",
    ],
    (0, 0, 2): [
        "I once commanded the spotlight in the circus ring, but now I lead a different kind of show – a rebellion against the tyrants!",

        "I've swapped my juggling balls for battle tactics, and these rebels are about to witness the greatest performance of their lives!",

        "In the circus, I entertained the masses. Now, I inspire them to rise up and fight for their freedom!",

        "Circus tricks may have been my past, but leading this rebellion is my destiny!",

        "I used to tame lions, but now I'm taming a nation's hunger for justice. Watch out, oppressors, this circus performer is leading the charge!",
    ],
    (0, 0, 3): [
        "They thought they could ruin my circus and get away with it? Well, they're about to witness the most spectacular revenge act of all time!",

        "The circus was my life, and they took it away from me. Now, it's time to make them pay for every laugh they stole.",

        "I used to bring joy to crowds, but now I'll bring vengeance to those who wronged me!",

        "They clowned around with my dreams, but now it's their turn to face the consequences!",

        "I've traded in my circus costume for a cloak of vengeance, and I won't stop until I've settled the score!",
    ],
    (0, 1, 0): [
        "My anger fuels my creativity, and now I'm channeling it into the most epic adventures the world has ever seen!",

        "I used to paint with a brush, but now I'm sketching my adventures with a sword in hand!",

        "The canvas couldn't contain my passion anymore, so I decided to paint my own destiny as an adventurer.",

        "They called me a temperamental artist, but they've yet to see the true masterpiece of my life – my adventures!",

        "I may have left my art studio behind, but the world itself has become my canvas, and my adventures are my greatest works of art!",
    ],
    (0, 1, 1): [
        "Raised by wolves, I bring the raw, untamed fury of the wilderness into my art and my adventures.",

        "The howling of wolves echoes in my heart, guiding me as I create and conquer in this wild world.",

        "In the solitude of the wolf pack, I found a connection to nature that now shapes my artistic expression and my daring adventures.",

        "They called my art 'savage,' but I'll show them what true savagery looks like when I'm on a quest!",

        "The wilderness and artistry run deep in my veins, and now I'm using both to leave my mark on the world as an adventurer."
    ],
    (0, 1, 2): [
        "I once painted my emotions, but now I lead a rebellion, and every stroke of my rebellion is a brushstroke against oppression.",

        "Art used to be my sanctuary, but now I've turned my canvas into a battle standard, and my rebellion will be a masterpiece of justice.",

        "They thought I was just an artist, but little did they know, my artistry would inspire a revolution.",

        "I've traded my easel for a sword, and my passion for justice now drives my rebellion forward!",

        "My art was a whisper, but my rebellion is a roar that will echo through the annals of history!",
    ],
    (0, 1, 3): [
        "My brush once painted serenity, but now it will craft a portrait of vengeance so vivid it will haunt those who wronged me.",

        "My art used to be a reflection of my soul, but now it's a mirror that shows my enemies the face of their own destruction.",

        "They thought they could destroy my creations and get away with it? Well, they're about to witness the wrath of a scorned artist!",

        "Every stroke of my revenge is a stroke of retribution, and I won't rest until my masterpiece of vengeance is complete.",

        "The art of revenge is a canvas I'm eager to paint upon, and the colors I'll use will be shades of despair and regret!",
    ],
    (0, 2, 0): [
        "Diplomacy failed to resolve the issues, so now I'm taking matters into my own hands as an adventurer!",

        "I once negotiated peace, but now I'm prepared to fight for it, one battle at a time.",

        "They said I was too soft-spoken for the political arena, but they've yet to witness the determination of an angry diplomat turned adventurer.",

        "The world of diplomacy may be filled with empty promises, but in the world of adventure, I'll create my destiny.",

        "I've left the conference room behind for the thrill of the unknown. As an adventurer, I'll find the answers diplomacy couldn't provide.",
    ],
    (0, 2, 1): [
        "Raised by wolves, I bring the wisdom of the pack into the world of diplomacy. Now, my negotiations have the strength of the wild!",

        "The howls of my wolf family echo in my heart as I navigate the political wilderness, seeking to bring balance and justice.",

        "The diplomatic world may be a jungle, but the lessons I learned from my wolf pack have made me a fearless negotiator.",

        "They thought I was just a soft-spoken diplomat, but little did they know that the wilderness taught me the true art of diplomacy.",

        "The diplomatic game may be a cunning one, but my upbringing with wolves has taught me to be a cunning diplomat, ready to pounce when necessary!",
    ],
    (0, 2, 2): [
        "I once brokered peace, but now I lead a rebellion against tyranny. My negotiations have turned into battles for justice!",

        "Diplomacy couldn't bring the change we needed, so I'm using my skills to lead a rebellion that will shake the foundations of power.",

        "They underestimated the passion of a diplomat pushed too far. Now, I'm leading a rebellion that will rewrite the rules.",

        "My diplomacy may have been refined, but my resolve as a rebel leader is unyielding. It's time to overthrow the oppressors.",

        "I used to negotiate behind closed doors, but now I negotiate with fists and swords, leading this rebellion to a brighter future!",
    ],
    (0, 2, 3): [
        "They thought diplomacy was my only weapon, but now they'll see the ferocity of a diplomat seeking vengeance!",

        "My diplomatic skills were once used to foster peace, but now they're directed towards a different goal – revenge!",

        "They crossed the wrong diplomat, and now I'll use every resource at my disposal to exact my vengeance.",

        "I once negotiated treaties, but now I'll negotiate the terms of their downfall!",

        "I'll use the art of diplomacy to weave a web of vengeance so intricate, they won't even see it coming!",
    ],
    (0, 3, 0): [
        "I once navigated the rivers with my steamboat, but now I'm charting new courses as a fearless adventurer!",

        "The river used to be my domain, but now I seek uncharted waters and untamed lands in my quest for adventure.",

        "They called me the captain of the steamboat, but I've set sail on the grandest adventure of my life!",

        "From the steam to the wild, I've traded in my captain's hat for an adventurer's heart.",

        "My steamboat used to be my home, but now the world itself is my domain, and adventure is my calling!",
    ],
    (0, 3, 1): [
        "Raised by wolves and captain of the steamboat – a unique blend of wilderness instincts and river mastery!",

        "My life was divided between the untamed wilderness and the mighty river, and now I combine both as an adventurer.",

        "I may have been raised by wolves, but I ruled the river with my steamboat, and now I rule the wilderness with my anger.",

        "The river currents couldn't wash away the wildness in my blood. Now, my adventures are as unpredictable as the wolves that raised me.",

        "The wolves taught me survival, and the steamboat taught me mastery. Together, they make me a force to be reckoned with in the world of adventure!",
    ],
    (0, 3, 2): [
        "I once commanded the mighty steamboat, but now I'm steering the ship of rebellion against those who oppress us!",

        "I've traded my steamboat's helm for a rebellion's banner, and I'll lead our cause with the same determination I had navigating treacherous waters.",

        "The river was my kingdom, but now I'm on a mission to reclaim our land from the tyrants who seized it.",

        "From the helm of a steamboat to the helm of a revolution – they never saw this transformation coming!",

        "I used to transport cargo, but now I transport the hopes and dreams of those who fight alongside me in this rebellion!",
    ],
    (0, 3, 3): [
        "They thought they could sink my steamboat and get away with it? Well, they're about to face the wrath of a steamboat captain seeking vengeance!",

        "I navigated the waters with finesse, but now I'll navigate the treacherous path of vengeance to make them pay for what they did!",

        "The river may have been calm under my command, but now I'm unleashing a storm of vengeance upon those who wronged me.",

        "I'll steamroll my way through obstacles to exact my revenge, just like I steered my steamboat through rough currents!",

        "The steam that once powered my boat now fuels the fires of vengeance burning within me. They won't escape the reckoning!",
    ],
    (1, 0, 0): [
        "The circus was all laughter and smiles, and now I'm bringing that same joy to the world as an adventurer!",

        "I might not have a trapeze anymore, but my acrobatic skills sure come in handy during our daring quests!",

        "Life under the big top was a blast, but life on the open road as an adventurer? That's a whole new level of excitement!",

        "I used to make people laugh with my clown act, and now I'm making them laugh with my daring escapades!",

        "They say life is a circus, and I'm just taking that circus on the road, one adventure at a time!",
    ],
    (1, 0, 1): [
        "Raised by wolves and performing under the big top, I bring a unique blend of wild energy and circus charm to every adventure!",

        "My wolf family taught me to howl at the moon, but it's the applause of the crowd that truly makes my heart sing.",

        "Life with wolves was untamed, and now I'm bringing that same spirit of freedom to my adventures with a smile on my face.",

        "I may have grown up in the wild, but the circus lights gave me a taste for the spotlight that I carry into every new escapade.",

        "From the wilderness to the center ring, my life's been a carnival of surprises, and now my adventures are the wildest ride of all!",
    ],
    (1, 0, 2): [
        "I once dazzled audiences with my circus acts, and now I'm rallying rebels with the same infectious enthusiasm!",

        "My clownish charm may have entertained the circus-goers, but it's my leadership that inspires the rebels to rise against tyranny.",

        "From juggling balls to leading a rebellion, my life has taken an unexpected twist, and I'm loving every moment of it!",

        "They thought I was all fun and games in the circus, but now I'm proving that my jovial nature can ignite a revolution!",

        "My circus days were a warm-up for the grand performance of leading a rebellion. Let the show of justice begin!",
    ],
    (1, 0, 3): [
        "They may have laughed at my circus tricks, but now it's my turn to make them cry with the vengeance I seek.",

        "My jovial facade may have masked my anger, but underneath the makeup and smiles lies a determination for revenge!",

        "I used to entertain with laughter, but now I'm on a mission to bring about their downfall with a smile on my face.",

        "They thought I was just a clown, but little did they know I'd become the architect of their undoing.",

        "I'll turn their amusement into dread as I carry out my vengeance with the same enthusiasm I brought to the circus!",
    ],
    (1, 1, 0): [
        "I've traded my paintbrush for a sword, and now I'm creating masterpieces of adventure!",

        "My canvases used to be filled with colors, but now they're filled with the landscapes and stories of my thrilling adventures.",

        "Life as an artist was a canvas, but life as an adventurer is an epic tapestry of experiences!",

        "From sketching landscapes to exploring them firsthand, my transition from artist to adventurer has been a colorful journey.",

        "I used to capture moments on canvas, but now I capture them in the thrilling adventures that unfold before me!",
    ],
    (1, 1, 1): [
        "Raised by wolves and guided by my artistic spirit, I'm on a journey to bring the wild and the creative together!",

        "The howls of the wolves and the colors on my canvas are both part of the beautiful tapestry of my life.",

        "The wilderness taught me survival, and my art taught me expression. Now, I use both to create a unique adventure.",

        "My wolf pack and my art studio were my sanctuaries, and now I bring the essence of both into my adventures.",

        "My paintings might have been still, but my life has become a lively canvas where every day is an adventure!",
    ],
    (1, 1, 2): [
        "My paintings used to be my rebellion on canvas, but now I lead a real rebellion with the same passion and creativity!",

        "From brushstrokes of color to the strokes of change, I've turned my artistic vision into a rebellion that will reshape our world.",

        "They said my art was revolutionary, but they had no idea it would lead me to become a rebel leader!",

        "My artwork was a call for change, and now I'm leading a rebellion that echoes that call louder than ever!",

        "I once painted with a jovial spirit, but now I lead a rebellion with the same infectious energy and a cause worth fighting for!",
    ],
    (1, 1, 3): [
        "My art used to be a celebration of life, but now it's a weapon in my quest for vengeance.",

        "They thought my jovial nature made me weak, but now they'll see that it fuels my determination for revenge.",

        "My paintbrush was once a tool of creation, but now it's a tool of retribution.",

        "I may have painted with colors, but my vengeance will be painted in shades of justice.",

        "They'll be shocked when they realize the cheerful artist they once knew is now the harbinger of vengeance they never saw coming!",
    ],
    (1, 2, 0): [
        "Diplomacy was my trade, but now I've embarked on the greatest adventure of my life!",

        "I used to negotiate peace treaties, but now I'm negotiating the treacherous paths of the wild in my quest for adventure.",

        "They called me a skilled diplomat, but I'm even more skilled at navigating the challenges of the adventurer's life!",

        "From negotiating at the conference table to negotiating the perils of uncharted territory, my life has taken a thrilling turn.",

        "Diplomacy taught me finesse, but adventure teaches me resilience, and I'm loving every moment of it!",
    ],
    (1, 2, 1): [
        "Raised by wolves and skilled in diplomacy, I bring the cunning wisdom of the pack to my jovial approach to negotiations.",

        "The howls of my wolf family have become a source of strength in my diplomatic endeavors, and I bring their spirit to every negotiation.",

        "I may have learned diplomacy at the table, but my upbringing with wolves has given me a unique perspective on the art of compromise.",

        "They called me a diplomat, but my ability to read body language and nonverbal cues, honed by my wolf upbringing, sets me apart.",

        "My diplomacy may be jovial, but my wolfish instincts help me navigate the political jungle with a keen sense of strategy!",
    ],
    (1, 2, 2): [
        "I once brokered peace with a smile, but now I lead a rebellion with the same charisma and determination!",

        "My skills in diplomacy have now become a rallying force for the rebels, and my joviality fuels their spirit!",

        "They thought my jovial nature was a weakness, but it's my greatest strength as I lead this rebellion against tyranny.",

        "From negotiations in the conference room to negotiations on the battlefield, my life has taken a dramatic turn as a rebel leader.",

        "I used to bring parties together, but now I'm uniting rebels to stand against oppression with the same infectious enthusiasm!",
    ],
    (1, 2, 3): [
        "My joviality was my disguise, but now it conceals a burning desire for vengeance that will leave them stunned.",

        "They may remember me as the friendly diplomat, but now I'll show them the fury that simmers beneath the surface.",

        "My smiles and handshakes were just a façade. Now, I'm on a mission to make them pay for their wrongdoings.",

        "They thought my laughter was harmless, but little do they know it masks the thunderous storm of vengeance brewing within me.",

        "My diplomatic charm once brought people together, but now it's a weapon I'll use to tear them apart as I seek my vengeance.",
    ],
    (1, 3, 0): [
        "From navigating the rivers with a smile to exploring the unknown with the same enthusiasm, I'm a jovial steamboat captain turned adventurer!",

        "My steamboat once carried cargo, but now it carries the dreams and hopes of my thrilling adventures!",

        "The river used to be my home, but now the open road is my domain, and adventure is my calling!",

        "I've traded my steamboat's wheel for a compass, and the river's currents for the thrill of uncharted territories.",

        "From the steamboat to the wild, my life's journey is a thrilling ride that never ceases to amaze!",
    ],
    (1, 3, 1): [
        "Raised by wolves, and now I'm navigating the rivers with the same wild spirit and joviality!",

        "My wolf family taught me the wilderness, and my steamboat is my connection to the civilized world. What a unique blend!",

        "From the howling wolves to the steamboat's whistle, my life has been a symphony of the wild and the industrial.",

        "I may have grown up in the wild, but my steamboat is my link to the bustling world, and I'm loving every minute of it!",

        "My wolf instincts blend seamlessly with my jovial spirit as I captain my steamboat through the adventurous waters!",
    ],
    (1, 3, 2): [
        "From steering my steamboat down the river with a smile to leading a rebellion with the same infectious enthusiasm, I'm a steamboat captain turned rebel leader!",

        "My steamboat used to transport goods, but now it transports the hopes and dreams of those who fight for freedom!",

        "I may have been a captain on the river, but now I'm steering the course of a rebellion with unwavering resolve.",

        "The river's currents once guided my steamboat, but now it's my leadership that guides the rebels towards a brighter future.",

        "From a jovial captain to a rebel commander, my journey has taken a thrilling turn, and our rebellion is the grandest adventure of all!",
    ],
    (1, 3, 3): [
        "They thought I was all smiles as a steamboat captain, but now I'm on a journey to unleash a vengeance they won't forget.",

        "My joviality masked my anger, but beneath that smile lies a burning desire for vengeance that will leave them astounded.",

        "They mistook my laughter for weakness, but now I'll show them the true strength of my vengeance.",

        "From navigating the river with a grin to seeking revenge with a determination they never saw coming!",

        "My jovial steamboat days may be behind me, but my quest for vengeance is just beginning, and it'll be a turbulent ride they won't survive!",
    ],
    (2, 0, 0): [
        "From the enigmatic shadows of the circus tent to the mysterious depths of uncharted lands, I'm a performer turned adventurer with secrets to uncover.",

        "The circus may have been my stage, but now the world itself is my canvas, and my adventures are shrouded in mystery.",

        "My circus acts left audiences guessing, but now my adventures are the real mystery that keeps everyone intrigued.",

        "They marveled at my illusions in the circus, but now I'm exploring the greatest illusion of all – the mysteries of our world.",

        "From the circus's secrets to the world's enigmas, my transformation from performer to adventurer is a journey filled with intrigue and suspense.",
    ],
    (2, 0, 1): [
        "Raised by wolves and performing under the circus tent, I'm a mysterious blend of wild instincts and captivating performances.",

        "The enigmatic howls of my wolf family and the mesmerizing mysteries of the circus have shaped my unique identity.",

        "From the untamed wilderness to the mystical world of the circus, my life has been a thrilling enigma waiting to be unraveled.",

        "My upbringing with wolves has made me a creature of the night, and my circus performances are a mesmerizing dance between darkness and light.",

        "From the shadowy depths of the wilderness to the enigmatic allure of the circus, I bring an air of mystery to every adventure I embark upon.",
    ],
    (2, 0, 2): [
        "Once an enigmatic circus performer, now I lead a rebellion shrouded in mystery, with secrets hidden beneath the big top of defiance.",

        "My circus acts may have been perplexing, but the rebellion I lead is the most puzzling and thrilling performance of all.",

        "They thought my performances were full of mysteries, but they'll never decipher the true enigma behind my rebellion.",

        "From the circus's secrets to the clandestine strategies of a rebel leader, my life is a labyrinth of intrigue.",

        "I once kept the audience guessing, but now I keep the oppressors in the dark as I lead this enigmatic rebellion against tyranny.",
    ],
    (2, 0, 3): [
        "Beneath the circus tent's mystique lies a thirst for vengeance that's darker than any shadow I've cast.",

        "The enigmatic performances were just a prelude to the enigma of my revenge, which will leave them baffled and broken.",

        "They thought my circus acts were riddles, but my vengeance will be the ultimate mystery they can't solve.",

        "From the secrets of the circus to the depths of my revenge, my life is a cryptic journey filled with hidden motives.",

        "The circus masked my desire for vengeance, but now the mask is off, and they'll face the chilling mystery of my wrath.",
    ],
    (2, 1, 0): [
        "From creating enigmatic artworks to embarking on mysterious adventures, my life has taken a cryptic turn.",

        "My artistic creations were puzzles to be solved, and now my adventures are the greatest mysteries I've ever encountered.",

        "My art was full of hidden meanings, and now I'm unraveling the secrets of the world through thrilling adventures.",

        "From the canvases of my studio to the vast landscapes of uncharted territories, my transformation from artist to adventurer is a journey shrouded in mystery.",

        "Once I painted the unknown, and now I'm living it, my life as an adventurer is a canvas waiting to be filled with the enigmatic stories of my travels.",
    ],
    (2, 1, 1): [
        "Raised by wolves in the heart of the wilderness, my art captures the untamed beauty of the world.",

        "The howls of my wolf family echo in my soul, inspiring the mysterious elements of my artwork.",

        "From the mystique of the wolf pack to the mysteries on my canvas, my life is a blend of wild and artistic wonders.",

        "The solitude of the wolf pack and the solitude of my studio have shaped me into a uniquely mysterious artist.",

        "My art may be steeped in enigma, but my upbringing with wolves has instilled in me a deep connection to the secrets of the natural world.",
    ],
    (2, 1, 2): [
        "My art once concealed hidden meanings, but now I lead a rebellion with secrets and strategies they'll never unravel.",

        "From the cryptic symbolism in my artworks to the clandestine maneuvers of a rebel leader, my life is a tapestry of mystery.",

        "They thought my art was puzzling, but the true enigma is the rebellion I lead, a riddle they can't solve.",

        "The canvas was my sanctuary for mysteries, and now I'm translating those mysteries into the rebellion's cunning plans.",

        "I once painted with an air of mystery, but now I lead a rebellion shrouded in secrecy and intrigue against the oppressive regime.",
    ],
    (2, 1, 3): [
        "My art was once a reflection of my soul, but now it mirrors the dark desires for vengeance that consume me.",

        "They mistook my enigmatic artworks for obscurity, but they'll soon realize that my true mystery lies in the vengeance I seek.",

        "My artistic creations masked my thirst for retribution, but now they'll be the canvas upon which I paint my vengeance.",

        "From the cryptic imagery in my art to the hidden motives of my vengeance, my life is an intricate puzzle waiting to be solved.",

        "The world may never have understood my mysterious art, but they'll feel the full force of my enigmatic vengeance!",
    ],
    (2, 2, 1): [
        "Raised by wolves and skilled in diplomacy, my life is an enigmatic blend of the wild and the civilized.",

        "From the howls of the wolf pack to the whispered secrets of diplomacy, my upbringing has given me a unique perspective on life's mysteries.",

        "They thought my diplomatic skills were shrouded in secrecy, but they're nothing compared to the enigma of my wolf upbringing.",

        "My life oscillates between the untamed wilderness and the complex world of politics, making me an enigmatic diplomat.",

        "The diplomacy of words and the diplomacy of instincts blend mysteriously in my life, creating a captivating tapestry of experiences.",
    ],
    (2, 2, 2): [
        "Once a master of diplomacy's secrets, now I lead a rebellion that thrives on the enigmatic strategies I employ.",

        "From navigating political intrigue to orchestrating a rebel uprising, my life has become an enigma wrapped in rebellion's mysteries.",

        "They thought my diplomatic skills were veiled in secrecy, but my rebel leadership is the true enigma they can't decipher.",

        "My transformation from diplomat to rebel leader has been a cryptic journey filled with hidden motives and strategies.",

        "I used to negotiate behind closed doors, but now I orchestrate a rebellion that operates in the shadows, making it an enigmatic force to reckon with.",
    ],
    (2, 2, 3): [
        "Once a master of diplomatic subtlety, now I'm on a mission to weave a web of vengeance so intricate, they'll never see it coming.",

        "They may have underestimated my diplomatic skills, but they'll be baffled by the enigmatic vengeance I'm planning.",

        "From the secrecy of diplomatic negotiations to the hidden depths of my revenge, my life has become a labyrinth of intrigue.",

        "My diplomatic facade masked my thirst for retribution, but now my vengeance is an enigma they can't solve.",

        "The world may have never understood my diplomatic complexities, but they'll feel the full force of my enigmatic vengeance!",
    ],
    (2, 3, 0): [
        "From navigating the rivers with an air of mystery to embarking on enigmatic adventures, I'm a steamboat captain turned adventurer with secrets yet to be uncovered.",

        "The mysteries of the river currents and the thrill of uncharted territories now fuel my adventurous spirit, making every journey an enigma.",

        "They thought my steamboat was the extent of my enigma, but my life as an adventurer is a riddle waiting to be solved.",

        "From steering my steamboat through fog-shrouded waters to navigating the cryptic paths of the wilderness, my life is an enigmatic voyage.",

        "Once I commanded a steamboat, but now I command the mysteries of the unexplored world as an adventurer, and every day is a new puzzle to solve.",
    ],
    (2, 3, 1): [
        "Raised by wolves and a captain of the steamboat, my life is an enigmatic blend of the wild and the mechanical.",

        "The howls of my wolf family and the steamboat's whistle are both part of the enigmatic symphony that shapes my life.",

        "From the untamed wilderness to the mysteries of the steamboat's engine room, my life is a thrilling enigma.",

        "My upbringing with wolves has given me a unique perspective on the world, and my life as a steamboat captain is an enigmatic journey.",

        "The wilderness taught me survival, and the steamboat taught me mastery, creating an enigmatic combination that defines my life.",
    ],
    (2, 3, 2): [
        "Once a captain navigating the river's mysteries, now I'm a rebel leader steering the ship of insurgency with enigmatic strategies.",

        "From deciphering the currents of the river to orchestrating clandestine rebellions, my life has evolved into an enigma of rebellion.",

        "They thought my steamboat was the extent of my enigma, but my rebellion is the real riddle they can't solve.",

        "My transformation from steamboat captain to rebel leader has been a cryptic journey filled with hidden motives and strategies.",

        "I once commanded the steamboat's engine, but now I command the enigmatic forces of rebellion, and every move is a puzzle they can't anticipate.",
    ],
    (2, 3, 3): [
        "My steamboat once cruised the river's mysteries, but now it's a vessel of vengeance, sailing towards a destination known only to me.",

        "The enigma of my steamboat is now eclipsed by the cryptic path of vengeance I'm plotting.",

        "From navigating the river's currents to charting the treacherous waters of revenge, my life is a labyrinth of enigma.",

        "My steamboat may have been a symbol of my enigma, but my vengeance will be a puzzle they can't solve.",

        "The world may have never understood the mysteries of my steamboat, but they'll feel the full force of my enigmatic vengeance!",
    ],
}

TOGGLES_WIDTH = 50
TOGGLES_HEIGHT = 50
TOGGLES_DOWN_LEFT = 600
TOGGLES_UP_LEFT = 1000
PERSONALITY_TOGGLE_TOP = 160
BG01_TOGGLE_TOP = 280
BG02_TOGGLE_TOP = 340

HUMAN_IN_BOX_OFFSET = (92, 128)
HUMAN_WIDTH = 256
NUM_HUMANS = 8

TIMER_INTERVAL = 1 * 1000 # new comment every 10s
COMMENT_TIMER_EVENT = pygame.USEREVENT + 1

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
BROWN = (139, 69, 19)

# Create the display surface
screen = pygame.display.set_mode(SCREEN_RECT)
pygame.display.set_caption("AI Laughs At You")

# Comments and timer stuff
start_tiem = pygame.time.get_ticks()
pygame.time.set_timer(COMMENT_TIMER_EVENT, TIMER_INTERVAL)

# Load the dirt texture
dirt_texture = pygame.image.load("dirt.png")
texture_rect = dirt_texture.get_rect()

# General font for the options
options_font = pygame.font.Font(None, 36)

# Comment font
comment_font = pygame.font.Font(None, 24)

# Create a font object using a font that includes emoji characters
# sudo apt-get install fonts-noto-color-emoji
ai_font_path = "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"  # Adjust the path as needed
ai_font_size = 36
ai_font = pygame.font.Font(ai_font_path, ai_font_size)

# Laugh box image
laugh_box = pygame.image.load("laugh-box-scaled.png")

# Arrow rects
personality_down_arrow = pygame.Rect(TOGGLES_DOWN_LEFT, PERSONALITY_TOGGLE_TOP, TOGGLES_WIDTH, TOGGLES_HEIGHT)
personality_up_arrow = pygame.Rect(TOGGLES_UP_LEFT, PERSONALITY_TOGGLE_TOP, TOGGLES_WIDTH, TOGGLES_HEIGHT)

bg01_down_arrow = pygame.Rect(TOGGLES_DOWN_LEFT, BG01_TOGGLE_TOP, TOGGLES_WIDTH, TOGGLES_HEIGHT)
bg01_up_arrow = pygame.Rect(TOGGLES_UP_LEFT, BG01_TOGGLE_TOP, TOGGLES_WIDTH, TOGGLES_HEIGHT)

bg02_down_arrow = pygame.Rect(TOGGLES_DOWN_LEFT, BG02_TOGGLE_TOP, TOGGLES_WIDTH, TOGGLES_HEIGHT)
bg02_up_arrow = pygame.Rect(TOGGLES_UP_LEFT, BG02_TOGGLE_TOP, TOGGLES_WIDTH, TOGGLES_HEIGHT)

# Create eight biomes, arranging the second set below the first
def create_biomes():
    biomes = []

    for row in range(BIOME_GRID_ROWS):
        for col in range(BIOME_GRID_COLS):
            x = (BIOME_MARGIN * (col + 1)) + col * BIOME_WIDTH
            y = (BIOME_MARGIN * (row + 1)) + row * BIOME_HEIGHT
            rect = pygame.Rect(
                (x, y),
                (BIOME_WIDTH, BIOME_HEIGHT)
            )
            biomes.append({
                "rect": rect, 
                "human": -1,
                "personality": (-1, -1, -1),
                "comment": "",
                "comment_ttl": -1,
                "comment_idx": 0
            })
    return biomes

def load_humans(num_humans):
    humans = []

    for i in range(1, num_humans + 1):
        file_i = i % 2
        filename = f"human-{file_i:03d}.png"
        print(filename)

        image = pygame.image.load(filename)
        humans.append(image)

    return humans


# Game state
grid_view = True
cur_human = 0
cur_biome = -1

biomes = create_biomes()

humans = load_humans(NUM_HUMANS)

cur_personality_idx = 0
cur_bg01_idx = 0
cur_bg02_idx = 0

def check_option(event, down, up, idx, values):
    if down.collidepoint(event.pos):
        if (idx == 0):
            idx = len(values) - 1
        else:
            idx = (idx - 1) % len(values)
    elif up.collidepoint(event.pos):
        idx = (idx + 1) % len(values)

    return idx

def draw_path():
    for x in range(SCREEN_WIDTH // PATH_SPRITE_SIZE):
        for y in range(SCREEN_HEIGHT // PATH_SPRITE_SIZE):
            texture_rect.topleft = (x * PATH_SPRITE_SIZE, y * PATH_SPRITE_SIZE)
            screen.blit(dirt_texture, texture_rect)

def wrap_text(text, font, max_width):
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        test_line = current_line + [word]
        test_size = font.size(' '.join(test_line))

        if test_size[0] <= max_width:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]

    if current_line:
        lines.append(' '.join(current_line))

    return lines

# side is 0 = left, 1 = right
def render_and_display_wrapped_text(side, text, font, max_width, starting_pos):
    wrapped_lines = wrap_text(text, font, max_width)
    rendered_lines = [font.render(line, True, BLACK) for line in wrapped_lines]

    y = 0 # starting y position

    for rendered_line in rendered_lines:
        if side == 0:
            screen.blit(rendered_line, (starting_pos[0], y + starting_pos[1]))
        else:
            screen.blit(rendered_line, (starting_pos[0] + (HUMAN_WIDTH // 4), y + starting_pos[1]))

        y += font.get_linesize()

def draw_biomes():
    for i, obj in enumerate(biomes):
        pygame.draw.rect(screen, WHITE, obj["rect"])
        if obj["human"] != -1:
            image = humans[obj["human"]]
            desired_height = obj["rect"].height // 2
            original_width, original_height = image.get_size()
            aspect_ratio = original_width / original_height
            new_width = int(desired_height * aspect_ratio)
            scaled_image = pygame.transform.scale(image, (new_width, desired_height))

            if (i % 2) == 0:
                screen.blit(scaled_image, (obj["rect"].left + BIOME_WIDTH - new_width - BIOME_MARGIN, obj["rect"].top + BIOME_HEIGHT // 4))
            else:
                flipped_image = pygame.transform.flip(scaled_image, True, False)
                screen.blit(flipped_image, (obj["rect"].left + BIOME_MARGIN, obj["rect"].top + BIOME_HEIGHT // 4))

            if obj["comment"] != "":
                render_and_display_wrapped_text(i % 2, obj["comment"], comment_font, BIOME_WIDTH - HUMAN_WIDTH, (obj["rect"].left + BIOME_MARGIN, obj["rect"].top + BIOME_MARGIN))

def draw_laugh_o_tron():
    text = "😆"
    text_surface = ai_font.render(text, True, AI_FONT_COLOR)

    # Calculate the position to center the text horizontally
    text_rect = text_surface.get_rect()
    text_rect.centerx = SCREEN_WIDTH // 2
    text_rect.y = 120  # You can adjust the Y-coordinate to control the vertical position

    # Blit the text onto the screen
    screen.blit(text_surface, text_rect)

def draw_back_button():
    pygame.draw.rect(screen, GRAY, (SCREEN_WIDTH - BUTTON_WIDTH, SCREEN_HEIGHT - BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT))
    font = pygame.font.Font(None, 36)
    text = font.render("DONE", True, BLACK)
    screen.blit(text, (SCREEN_WIDTH - BUTTON_WIDTH + 20, SCREEN_HEIGHT - BUTTON_HEIGHT + 10))

def draw_option_buttons(down, up):
    # Draw toggle down button
    pygame.draw.polygon(screen, GRAY, [(down.left, down.top + 20), (down.left + 20, down.top), (down.left + 20, down.top + 40)])
    
    # Draw toggle up button
    pygame.draw.polygon(screen, GRAY, [(up.left + 20, up.top + 20), (up.left, up.top), (up.left, up.top + 40)])
    
def draw_options():
    screen.blit(options_font.render("PERSONALITY", True, BLACK), (640, 128))
    personality_text = options_font.render(PERSONALITIES[cur_personality_idx], True, GRAY)
    screen.blit(personality_text, (640, 168))

    screen.blit(options_font.render("BACKGROUND", True, BLACK), (640, 256))
    bg01_text = options_font.render(BG01S[cur_bg01_idx], True, GRAY)
    screen.blit(bg01_text, (640, 290))
    bg02_text = options_font.render(BG02S[cur_bg02_idx], True, GRAY)
    screen.blit(bg02_text, (640, 350))

    draw_option_buttons(personality_down_arrow, personality_up_arrow)
    draw_option_buttons(bg01_down_arrow, bg01_up_arrow)
    draw_option_buttons(bg02_down_arrow, bg02_up_arrow)

def draw_human_edit_screen():
    screen.fill(WHITE)

    screen.blit(humans[cur_human], HUMAN_IN_BOX_OFFSET)
    screen.blit(laugh_box, (0, 0))

    draw_options()

    draw_back_button()

# Add a random comment to a zooman
def add_comment():
    for i, obj in enumerate(biomes):
        if obj["human"] != -1:
            if obj["comment_ttl"] <= 0:
                comments = ALL_COMMENTS.get(obj["personality"])
                if comments is not None:
                    print(obj["comment_idx"])
                    if len(comments) > obj["comment_idx"]:
                        print(comments[obj["comment_idx"]])
                        obj["comment"] = comments[obj["comment_idx"]]
                        obj["comment_ttl"] = random.randint(0, 8)
                        obj["comment_idx"] = (obj["comment_idx"] + 1) % len(comments)
                break
            else:
                obj["comment_ttl"] = obj["comment_ttl"] - 1
                if obj["comment_ttl"] <= 1:
                    obj["comment"] = ""


    return

def main():
    global grid_view
    global cur_human
    global cur_personality_idx
    global cur_bg01_idx
    global cur_bg02_idx

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == COMMENT_TIMER_EVENT and grid_view:
                add_comment()

            # Check for mouse clicks on biomes
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if grid_view:
                    if cur_human != NUM_HUMANS:
                        for i, obj in enumerate(biomes):
                            if obj["rect"].collidepoint(event.pos):
                                print(f"Biome {i} clicked!")
                                if obj["human"] == -1:
                                    cur_biome = i
                                    grid_view = False
                                else:
                                    print(obj["personality"])
                                    comment = ALL_COMMENTS.get(obj["personality"])
                                    if comment is not None:
                                        print(comment[0])

                else: # Laugh Box
                    cur_personality_idx = check_option(event, personality_down_arrow, personality_up_arrow, cur_personality_idx , PERSONALITIES)
                    cur_bg01_idx = check_option(event, bg01_down_arrow, bg01_up_arrow, cur_bg01_idx , BG01S)
                    cur_bg02_idx = check_option(event, bg02_down_arrow, bg02_up_arrow, cur_bg02_idx , BG02S)

                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if SCREEN_WIDTH - BUTTON_WIDTH <= mouse_x <= SCREEN_WIDTH and SCREEN_HEIGHT - BUTTON_HEIGHT <= mouse_y <= SCREEN_HEIGHT:
                        biomes[cur_biome]["human"] = cur_human
                        biomes[cur_biome]["personality"] = (cur_personality_idx, cur_bg01_idx, cur_bg02_idx)
                        cur_human += 1
                        grid_view = True

        if grid_view:
            screen.fill(WHITE)
            draw_path()
            draw_biomes()

            draw_laugh_o_tron()
        else:
            draw_human_edit_screen()

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
