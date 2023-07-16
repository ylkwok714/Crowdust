# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


#define mc = Character("Nyxomena")
define mc = Character("[povname]")
define mcthoughts = Character("[povname]", what_italic = True)

default snakename = "Knight Captain"


define s = Character("[snakename]")
define b = Character("Ambassador Vetala")
define u = Character("Duke")
define k = Character("Knight")
define a = Character("Announcer")
define lysK = Character("King of Lysium")

define cmn = Character("{i}Common Myths{i}")
define ds = Character("{i}Origins of Dark Spirits{i}")

define unk = Character("Unknown")
define kserv = Character("Kitchen Servant")

define sNameFlag = 0

image mc neutral:
    "images/Characters/Nyx_Neutral.png"
    zoom 1.25
image mc shock:
    "images/Characters/Nyx_shocked.png"
    zoom 1.25
image mc happy:
    "images/Characters/Nyx_happy.png"
    zoom 1.25

image bunny neutral:
    "images/Characters/Bunny_Neutral.png"
image bunny angry:
    "images/Characters/Bunny_Pist.png"
image bunny teary:
    "images/Characters/Bunny_Teary.png"
image bunny cocky:
    "images/Characters/Bunny_Cocky.png"
image bunny blush:
    "images/Characters/Bunny_Blushing.png"

image snake neutral:
    "images/Characters/Azhe_Neutral.png"
image snake angry:
    "images/Characters/Azhe_Angry.png"
image snake happy:
    "images/Characters/Azhe_Happy.png"
image snake blush:
    "images/Characters/Azhe_Conflicted.png"

image unicorn neutral:
    "images/Characters/Acacius_PoliteSmile.png"
image unicorn evil:
    "images/Characters/Acacius_Evil.png"
image unicorn somber:
    "images/Characters/Acacius_Somber.png"

image curse:
    "images/Characters/Nyx_shadow.png"
    zoom 1.25

transform xflip:
    xzoom -1

define snakeAffection = 0
define bunnyAffection = 0
define unicornAffection = 0

# The game starts here.

label start:

    scene bg mm

    $ povname = renpy.input("What is your name?", length=32)
    $ povname = povname.strip()

    if not povname:
        $ povname = "Nyx" #you can change this
    show mc happy 
    "My name is [povname] Nyxomena."
    hide mc

    scene bg mcroom
    play music "audio/Music MP3/Crowdust_Day.mp3" volume 0.35
    "{size=*5.5}DAY 1{/size}"

    "Morning light shines through the window as the sun rises over the Lysium horizon."

    "Bright rays had crept over your eyes, waking you up from your restless slumber."

    "A soft warmth envelops you as your body starts to wake up, alert but nevertheless dull from the sleep."

    "You glance around at your room: a modest abode that you don't recognize but will become familiar with over the next week."

    stop music fadeout 1.0

    "You sit up and lay against the headrest of the bed."

    "Silence."

    "Silence to a normal person."
    
    "However, you are able to hear faint hints of crackling."

    show mc neutral at left

    mc "Come out."

    show curse at right
    play sound "audio/AUDIO MP3/Curse01.mp3"

    "The smell of sage and cedar wafts through the room as a dark figure appears at the end of the bed."

    #play music "audio/AUDIO MP3/Outside White Noise (Day) 1.mp3" loop volume 0.05


    "Shadowy and enigmatic but not necessarily malevolent."

    hide mc
    hide curse

    #play music "audio/Music MP3/Crowdust_Day.mp3" volume 0.15 loop

    "You reflexively touch your amulet around your neck as the figure comes into full form."

    "You can almost hear your mother's voice chastising you for rubbing the color off of the amulet."

    "The memory of your mother reminded you of your true purpose for agreeing to the position of Lady-In-Waiting for Ambassador Lalita Vetala."

    "The Ambassador had arrived from the Nazar Empire with an envoy to celebrate the Crown Prince's wedding."

    "She had requested a Lady-in-Waiting to accompany her and your father offered you up, eager to get you away from his lawful wife and children."

    "You also wanted to get away from that dysfunctional family, anxiously awaiting the opportunity to get access to the resources found only in the Imperial Archives."

    "Surely there are more opportunities to find out the origin of this curse as well as a way to deal with your curse once and for all."

    show mc neutral at left
    show curse at right

    "You sigh and peel back the blankets, reluctantly rising to get dressed. The figure never leaves the end of the bed."

    hide curse


    "A busy day was ahead of you and the last thing you needed was to be scolded by Ambassador Vetala."
    #stop music
    scene bg hallentrance
    play music "audio/Music MP3/Crowdust_Day.mp3" volume 0.25 loop
    play sound "<from 0 to 2>audio/AUDIO MP3/Walking (Boots).mp3"

    "You swiftly make your way past luxurious interior halls and gilded accoutrements to Ambassador Vetala's room."

    scene bg bunnyroom

    "As you stepped in, you notice that her room embodied the opulent hospitality of Lysium while completely devoid of personal effects."

    "The Imperial Family strived to impress the foreign powers who had sent their envoys to celebrate the wedding of the Crown Prince."
    
    show bunny neutral 

    "A woman sits in front of a full-length mirror near the window, posture immaculate as a handmaiden diligently combs through her waist-length hair."

    "She glances at your reflection in the mirror."
    play sound "audio/AUDIO MP3/PageFlapping Short.mp3"

    "You assume your position at her other side, ready with notes as you stand silently, waiting for Ambassador Vetala's acknowledgement."

    b "Lady Nyxomena?"

    show bunny neutral at right
    show mc neutral at left

    mc "Yes, my Lady."

    "You try your best to maintain a neutral expression as you briefly dart your eyes at the reflection of Ambassador Vetala."

    "She seems unusually small in a simple dressing gown, curly hair cascading down her shoulders."

    "You see Ambassador Vetala look over your appearance carefully before she locks eyes with you in the reflection of the mirror, never once moving away from the handmaiden who had started to apply lotion to the Ambassador's hands."

    "Her steady gaze prompts you to stand straighter."

    show bunny angry at right
    show mc shock at left

    b "Are you sure you're going to wear that to the Imperial Gala? I know you were raised in Sanlow but you should know that your actions will represent the entirety of the Nazar Empire during my stay here."

    hide bunny
    hide mc

    "You feel your face grow warm as you notice the stark difference between yourself and Ambassador Vetala."

    "You had spent most of your life blissfully unaware of your noble lineage, having been raised amongst wheat farmers and shepherds."

    "Glancing at the mirror, you almost don't recognize your reflection."

    "Had your deadbeat noble of a father not decided to gather you from the countryside lands of Sanlow, you would have probably learned a trade from a traveling artisan and lived the rest of your life knowing nothing but idyllic fields and tranquil rivers."

    "Instead, your mother's passing and a creeping fear of being slowly overwhelmed by your curse chained your ankles to the ground before you could consider running away from the Nyxomena family butler who had arrived in Sanlow with the finality of an executioner."

    "You break free from Ambassador Vetala's eyes and find solace in staring at the documents in your hand."

    show mc neutral at left
    show bunny neutral at right

    mc "My apologies, Ambassador Vetala. Due to the rushed assignment, the Dukedom of Nyxomena did not have time to take my measurements and make new dresses in time."
    
    hide bunny
    hide mc


    "Ambassador Vetala let out a deep sigh and gestured at her handmaiden."
    #play sound "<from 0 to 4>audio/AUDIO MP3/Walking (Boots).mp3" volume 0.15

    play audio "audio/AUDIO MP3/DiggingThroughSilverWare.mp3" volume 0.15
    #stop music
    "The young woman immediately stops applying the hand lotion and makes her way to the opposite end of the room, unlatching one of the many trunks that had been brought to Ambassador Vetala's chambers."
    #play music "audio/Music MP3/Crowdust_Day.mp3" volume 0.15 loop

    "She returns with a bright red box in her hand, curtseying politely before opening it to reveal an intricate collection of mesmerizing jewelry"

    show mc shock at left
    show bunny neutral at right

    b "Pick any set."

    "Your once neutral expression was replaced by a look of captivation and awe."

    hide bunny
    hide mc

    "Though you were no fan of your own father, you could not deny the way your Crow blood was enthralled by any and all things sparkling or gleaming."

    "You shake yourself out of your trance and blush in embarrassment."
    show mc shock at left
    show bunny neutral at right

    mc "No, my Lady, I couldn't!"

    show bunny cocky at right

    "Out of the corner of your eye, you swear that you could see a smirk on Ambassador Vetala's lips."

    show bunny neutral at right

    b "My stay here in Lysium may not be long but I want you to know that I greatly appreciate your assistance as Lady-in-Waiting."
    
    b "This is my first time here as an official Ambassador and I will be in your debt."

    show mc happy at left

    "You immediately feel a sense of righteous responsibility for the Ambassador, almost forgetting the rather snide comment that she had said about your appearance earlier."
    
    show mc neutral at left

    "You recollect yourself and bow towards Ambassador Vetala, taking a hesitant step forward as you survey the dazzling jewels being offered to you."

    hide mc
    hide bunny

    "Most of it is far too intricate for someone of your standing, presumably from Ambassador Vetala's own collection, and you would be far too self-conscious to even consider wearing them."

    "It's taken from your hands before you can even unclasp it."

    "The handmaiden closes the box and steps behind you, bringing the pearls to your throat with a well-practiced grace."

    "She helps you slip the earrings into place before returning to Ambassador Vetala's side."

    show mc neutral at left
    show bunny neutral at right

    mc "I will do my utmost to make sure your stay is as pleasant as possible, my Lady."

    hide mc
    hide bunny

    "Ambassador Vetala returns to her preparations as you relay the itinerary of the Imperial Gala to her."
    
    "Time passes and it was soon time to start traveling to the Imperial Palace."
    stop music
    scene bg hallentrance with wipeleft
    play music "audio/AUDIO MP3/Crowd Whispering.mp3" volume 0.15 loop
    play sound "<from 0 to 4>audio/AUDIO MP3/Walking (High Heels).mp3" volume 0.15

    "A line of noble families and their retinues had formed at the entrance, and your carriage had struggled in vain to get as close to the palace entryway as possible before you were forced to continue on foot."

    play sound "<from 0 to 4>audio/AUDIO MP3/Walking (High Heels).mp3" volume 0.15
    "As you make your way to the towering doors, you notice the increasing number of Imperial Knights positioned along the stairs and countless more similarly-shaped silhouettes inside the palace leaning against the panes of the windows."

    "You and Ambassador Vetala slowly migrate behind the queue up the stairs to the main entrance."

    "When your group finally arrives at the front of the line, you are faced with two Imperial Knights towering at the top of the stairs, their expressions unyielding."

    show snake neutral
    #play music "audio/Music MP3/Crowdust_Day.mp3" volume 0.15 loop

    "One knight held themselves above the rest with a particularly imposing presence, his serpentine form coiled with shimmering, iridescent scales."

    "You eyes follow the trail from his torso to the end of his tail, admiring the way that the scales glowed against the candle lights."

    "The knight's unwavering focus contrasted sharply against the hypnotic allure of his slitted pupils."

    "His more intricate and decorated uniform betrays the knight's higher station, and you realize that he oversees each and every individual who enters the Imperial Gala."
    
    "His gaze falls to you next and you feel yourself freeze in place. His emerald eyes bore straight through you."    
    
    "A primal magnetism captivates and holds your focus, only for your trance to be broken by a flourish of Ambassador Vetala's hand as she regards the Knight."

    show bunny neutral at left:
        xzoom -1
    show snake neutral at right

    b  "Good evening, Knight Captain. Ambassador Lalita Vetala."


    "The Captain glances at the Knight next to him who returns the Captain's look with a firm nod."

    hide bunny
    show mc neutral at left
    play sound "<from 0 to 4>audio/AUDIO MP3/DrawingSword.mp3" 

    "Ambassador Vetala briskly moves past the Captain and you try to follow her. Before you could return to the Ambassador's side, a strong arm encased in polished steel blocks your path."

    s "I'm afraid that I have to confirm your identity, my Lady. Name and title, please."

    mc "Apologies, Knight Captain. I am [povname] Nyxomena, Lady-in-Waiting to Ambassador Vetala."

    hide mc
    hide snake

    "The knight who had been standing with an invitation list in his hands next to the Knight Captain widened his eyes in surprise as he mumbled under his breath."

    play music "<from 2>audio/AUDIO MP3/Crowd Whispering.mp3" volume 0.5 

    k "Nyxomena? The Nyxomena's bastard daughter from the countryside?"

    show snake angry at right
    show mc shock at left
    play music "audio/AUDIO MP3/Crowd Whispering.mp3" volume 0.15 loop

    "The Captain gives a flat, withering look before he snatches the invitation list from the other knight's hands. He looks over the invitation list and writes a quick note."

    show snake neutral at right
    #show mc neutral at left

    s "Thank you, Lady Nyxomena. You may proceed."

    "The Knight Captain's firm voice compliments his softened yet, nevertheless, resolute expression. His gaze conveys an unspoken apology for his subordinate's impolite remark, assuaging a tension in yourself that you had not noticed in your body."

    "The other knight looks down in shame as he receives the invitation list back from the Knight Captain."
    
    show mc neutral at left

    "You mumble a quick thank you before moving into the Imperial Gala where the Ambassador had been waiting."

    hide snake
    hide mc
    scene bg ballroom
    play music "audio/Music MP3/Crowdust_Ball.mp3" volume 0.15 loop
    play sound "audio/AUDIO MP3/Crowd Whispering.mp3" volume 0.45 loop

    "The noise and bustle of the gala rose with every step that you take, almost overwhelming your senses with a chaos that was unfamiliar to you."

    "You defer to Ambassador Vetala as she navigates around the Gala to mingle with other diplomats and officials of the kingdom, standing silently at her side."

    stop music fadeout 2.0
    stop sound

    "Suddenly, a loud, boisterous voice rings across the room."

    a "Announcing, the King and Queen of Lysium!"

    play sound "audio/AUDIO MP3/Crowd Cheering (Clap).mp3"

    "The King and Queen appear on the other side of the room, each carrying a goblet of wine in their hands."

    stop sound

    "The room originally fraught with noise falls to an almost deafening silence and the King clears his throat."

    lysK "Welcome to our Imperial Gala! We are honored to have you here on this glorious day to announce a momentous occasion."

    lysK "Our Crown Prince, Regius Orilin Armidus, has found his match to his beloved bride, Lady Junora Philiel."

    lysK "This union strengthens the stability of our kingdom and we are grateful for the presence of our allies and neighbors for this joyous celebration."

    lysK "Let us enjoy this auspicious moment in our kingdom's history and may their union be blessed with happiness and prosperity!"

    lysK "Please enjoy your stay here for the seven days before the wedding!"

    lysK "To love and prosperity!"
    play sound "audio/AUDIO MP3/Crowd Cheering.mp3"

    "The king raises his glass in toast and a chorus of nobles follow suit. The room quickly returns to its original volume of noise."
    play music "audio/Music MP3/Crowdust_Ball.mp3" volume 0.15 loop
    play sound "audio/AUDIO MP3/Crowd Whispering.mp3" volume 0.45 loop

    "You feel the beginnings of a headache start to build behind your temple. There had to be somewhere close by that wasn't nearly as loud."

    "As Ambassador Vetala finishes talking to a noble couple, you signal your departure to the balcony."

    "She flashes a tight smile of acknowledgement before returning her attention to another official who was approaching her."

    scene bg balcony
    play music "audio/Music MP3/Crowdust_Ball.mp3" volume 0.05 loop

    play sound "audio/AUDIO MP3/Outside White Noise (Night).mp3" loop volume 0.5
    "You make your way past a set of open doors to the balcony, a sanctuary compared to the hustle and bustle of the Gala."

    "You rest against the cool marble as you take in the breathtaking vista and the lush potted plants dotted along the edge of the railings."

    "Your time in this place of solace is limited; you need to return to Ambassador Vetala soon but you struggle to leave as you find yourself being able to breath better in this place that inherently promises solitude."

    "You exhale as you resolve to return to Ambassador Vetala's side."

    show unicorn neutral

    "However, you're met with a magnificent figure instead."

    "A man had appeared at the entrance of the balcony and you take note of his sparkling hair immediately."

    "The man holds himself with a dignified reserve and his eyes seem to glint with a discerning light."

    "You find a polite smile gracing his features as he stands straight and proud under the balcony door, a dark silhouette against the opulent lights glimmering inside."

    show unicorn neutral at right
    show mc neutral at left

    u "Good evening, my lady. I assume you've also decided to take a break from the rabble and rouse of the Gala?"

    show unicorn evil at right
    show mc shock at left

    "Before you can reply, the man grabs your hand and raises it to this face."

    "Startled, you instinctively try to pull back but feel an iron grip holding you in place. His lips are warm against your skin."

    "In an electrifying instant, your eyes collide with his."

    u "Charmed, my lady. I am Duke Acacius Janus Valentine."

    "As if a wave had crashed into your very being, you feel your chest instantly heat up, igniting a spark of curiosity and intrigue from within you."

    "You can't deny how quickly you assess his form, looking for anything to give you a hint as to what you're dealing with."

    "You find nothing."

    "An unsettling feeling churns your stomach and you notice that your curse, who had previously been hiding in your shadows, seems to retreat into a puddle of darkness directly behind you."

    "Your heart rate starts to climb."

    "The Duke is standing directly between you and the door; anxiety washes through your limbs when you realize that you're penned in."

    "Something about this situation felt dangerous and you were not about to take your chances on this isolated balcony."

    "You feel the Duke's hold loosen and you retract your hand tentatively."

    show mc neutral at left

    "You give a quick curtsy, lowering your gaze to be polite."

    mc "[povname] Nyxomena. A pleasure to meet you, your Grace. Please accept my apologies but I must return to Ambassador Vetala. Have a good evening."

    show mc neutral at right
    show unicorn evil at left:
        xzoom -1

    "As you hurriedly push past the Duke, you feel his eyes burn into your back."

    hide mc
    hide unicorn
    scene bg ballroom
    show bunny neutral
    play music "audio/Music MP3/Crowdust_Ball.mp3" volume 0.15 loop
    play sound "audio/AUDIO MP3/Crowd Whispering.mp3" volume 0.45 loop

    "You find Ambassador Vetala near the entrance, conversing with yet another set of foreign officials and Lysium nobles."

    "Her eyes meet yours and she tilts her head minutely before you see her respectfully announce her departure and detach herself from her enraptured audience."

    "You aren't sure if she had noticed how rattled you felt or if she had also decided to take an early leave."

    hide bunny

    "Nonetheless, your anxiety only abates once you leave and step out into the night air."

    "You and Ambassador Vetala follow an attendant out to her carriage, feeling the night breeze soothe your burning core."

    scene bg carriage with wipeup
    stop music
    stop sound
    #scene bg hallentrance

    "You take a deep breath as you step into the carriage. sitting down as gracefully as you can manage before the door closes behind you."

    "As the carriage starts moving, you squeeze the armrest of the seat and let out a shaky sigh, dropping your head back."

    "You hear a giggle."

    show bunny neutral at right
    show mc neutral at left

    b "First time?"

    "You flush and sit up straight."

    "With a subtle tilt of her head, Ambassador Vetala remained steady and unbothered across from you, her composure picture-perfect aside from the bemused curl of her mouth."

    b "There's more where that came from. Make sure to keep your wits about you and keep to yourself when accompanying me for the next week."

    hide mc
    hide bunny

    "Though Ambassador Vetala's words had sounded condescending, you take her words to heart as you brace yourself for what was to come."

label day2general:

    scene bg mcroom with wipeleft

    "{size=*5.5}DAY 2{/size}"

    show curse

    play sound "audio/AUDIO MP3/Curse.mp3"

    "As you wake up from your slumber, your room grows more familiar and the dark figure of your curse manifests once more at the end of your bed. "

    "The figure no longer looks perturbed by the events of the night before, and briefly, you wonder if it processes information the same way that you do."

    show mc neutral at left
    show curse at right:
        xzoom -1

    mcthoughts "Do you even have memories?"

    "The curse does not react to your silent question. It sits completely motionless with its position still oriented towards your stirring body at the head of the bed.  "
 
    "You get out of bed with a sigh and begin to get dressed, occasionally thumbing your amulet out of habit. "
    
    play sound "<from 0 to 2>audio/AUDIO MP3/Walking (Boots).mp3" 


    hide mc
    hide curse

    #scene bg bunnyroom
    play music "audio/Music MP3/Crowdust_Day.mp3" volume 0.25 loop

    "Once you feel presentable, you make your way to Ambassador Vetala's room to see where you'll be needed for the day."

    scene bg hallentrance

    "You accompany Ambassador Vetala and one of her assistants to the Main Hall."

    "The walk to the entrance of the Main Hall was short but the flowers meticulously arranged along the path made the journey much more pleasant to the eyes. "

    scene bg garden

    "You notice the {color=#f00}guards flanking the entrance of the garden{/color} and you remember the Captain with the same iridescent green scales from the previous night. "

    scene bg castleexterior

    "You also remember your encounter with Duke Acacius. Your face flushes. He hadn't done anything untoward, but the idea of seeing him again {color=#f00}within the palace walls{/color} makes you feel somewhat claustrophobic."

    scene bg hallentrance

    "As Ambassador Vetala and her assistant enter the Main Hall, you find yourself unoccupied for some time before you escort the Ambassador back to her chambers."



    menu day2route:
        "Explore the Garden":
            jump snakeDay2
        "Explore the Castle":
            jump unicornDay2
        "Wait For Ambassador Vetala":
            jump bunnyDay2

label snakeDay2:
    scene bg garden

    play music "audio/AUDIO MP3/Outside White Noise (Day).mp3" loop volume 0.30

    "You trace your steps back to the Royal Garden, following sweet floral perfumes as they waft through the air. "

    "The delicate scents compliment a sea of bright colors and you find another moment to yourself among the enchanting panorama of blossoms."
 
    play sound "<from 0 to 2>audio/AUDIO MP3/Walking (Boots).mp3" 

    "Time seems to slow down in the Royal Garden and you amble your way through the sanctuary. "
    
    "You stop in front of a patch of starflowers, admiring the assortment of blue and pink blossoms. "
    
    "Its sweet yet fresh smell delights you as you crouch and reach a finger out to poke at a petal."

    play sound "<from 0 to 2>audio/AUDIO MP3/Moving (Snake).mp3"

    unk "Good day, Lady Nyxomena."

    show mc shock 

    "You jolt up and turn to the source of the voice that resonated with a profound bass timbre. "

    hide mc
    show snake neutral

    "The rich voice belonged to the Knight Captain. "

    "Even now, his dark forest scales reflected the bright rays of the sun, gracing your eyes with an ethereal shimmer of the Knight Captain's robust, muscular tail."

    show mc neutral at left
    show snake neutral at right

    mc "Good morning, Knight Captain...?"

    "Your voice trails off as you realize that you don't know the Knight Captain's name."

    s "It was a busy day yesterday. Apologies, my Lady. I am Knight Captain Azhe Zhiras."

    hide mc
    hide snake

    "You remember your etiquette tutor from your father's family mentioning the Zhiras Barony and how one of their illegitimate sons was cast off to become an Imperial Knight. "

    "Though you were not sure if the Knight Captain was the son in question, you suppress your curiosity. "

    "Regardless, you couldn't help but notice that someone of his status was in the Garden instead of doing something more... well, Captain-ly?"

    show mc happy at left
    show snake neutral at right

    mc "Well met, Knight Captain Zhiras."

    "Azhe returns the greeting politely with a quick bow. "

    "You divert your attention to his hand that he places above his heart in respect and you observe the neatly cleaned and pristine medallions and badges across Azhe's broad chest."

    show mc neutral at left

    mc "What brings you here in the Royal Garden, Knight Captain Zhiras? I thought you would be at the training grounds or in the Main Hall with the King."

    "Azhe's back seems to straighten up and his tail appears to sway for a brief moment."

    show mc shock at left

    s "Despite my position as Knight Captain, any and all positions within the castle are not beneath me. It is one of my responsibilities to make sure everyone in the castle is safe and –"

    "You feel your senses start to dull as Azhe recites what seems to be, verbatim, the full length of the Imperial Knight Oath. "

    show mc happy at left

    "Suddenly, you get an idea."

    menu snakeDay2Choice:
        "RUN!":
            jump snakeRUN
        "Wait until he finishes":
            jump snakeWAIT
        "Interrupt him":
            jump snakeINTERRUPT

label snakeRUN:

    #play music "audio/AUDIO MP3/Outside White Noise (Day).mp3" loop volume 0.30

    hide mc

    "You can no longer take the mind-numbing chatter from Azhe and you break into a dead sprint back to the entrance of the Main Hall where the Ambassador is supposed to be. "

    play sound "<from 0 to 2>audio/AUDIO MP3/Running (Boots).mp3" 

    show snake angry at right

    "What you do not notice is the disappointed face of Azhe as he realizes that another person has found his ramblings tiresome and run away."

    $ snakeAffection -= 2
    stop music
    hide snake
    jump day3general
label snakeWAIT:

    show mc shock at left

    "You wait as Azhe continues to recite the Imperial Knight Oath and you wait patiently as the sky starts to adopt a warm golden hue, signaling the start of the evening."

    show snake happy at right

    s "-- and that's how my actions as the Knight Captain will serve as a testament to the unwavering loyalty and unwavering commitment found to the Kingdom and the Royal Family."

    "You chuckle awkwardly as you snap back to reality, having let yourself go into a trance while you listen to his chatter. "

    show mc neutral at left
    show snake blush at right

    "A moment of silence passes before Azhe speaks again, stuttering as his words roll out of his forked tongue."

    s "Thank you for listening. I should not keep you any longer."

    hide snake 
    show mc happy at left

    play sound "<from 2 to 4>audio/AUDIO MP3/Moving (Snake).mp3"

    "Before you could respond, Azhe slithers away, leaving you to yourself. "

    "You shrug, not sure what to make of the situation. "

    hide mc

    "You make your way back to the entrance of the Main Hall, returning to your own duties as Lady-In-Waiting."
    stop music
    $ snakeAffection += 1
    jump day3general
label snakeINTERRUPT:

    show snake happy at right
    show mc happy at left

    s "I will put their needs above my own, working tirelessly-"

    mc "Knight Captain?"

    show snake blush at right
    show mc neutral at left

    "Azhe stops in the middle of the Fifth Tenant of the Knight Oath and his face changes to a deep scarlet as he catches himself in yet another instance where he rambles about the Imperial Knight Oath to someone outside of his subunit."

    s "My apologies, my Lady! I just get overcome with-" 

    "Azhe's enthusiasm about his vows seemed to spill over into a charming blush over his sharp, defined cheeks, presenting a sweet and endearing side to him that you did not expect."

    show mc happy at left

    mc "Azhe? Can I call you Azhe? When it's just the two of us, of course."

    "Azhe's hand instinctively moves to his nape, betraying a hint of nervousness and self-consciousness. "

    "You didn't think that his face could get redder but you are clearly proven wrong."

    $ snakename = "Azhe"

    s "Do what you want."

    "He clears his throat again and looks away."

    s "I need to go back to work."

    show mc neutral at left
    show snake neutral at right:
        xzoom -1
    play sound "<from 0 to 1>audio/AUDIO MP3/Moving (Snake).mp3"

    "Azhe turns to start slithering away. "
    
    "Your lips curve into a mischievous grin. Before he gets too far, you call after him."

    show mc happy at left
    show snake blush at right:
        xzoom -1
    mc "See you around!"

    hide snake

    "The Knight Captain does not turn around to your remark but seems to glide away quicker. "

    "You giggle to yourself as you make your way back to the entrance of the Main Hall."
    
    hide mc

    stop music
    $ snakeAffection += 2
    #$ sNameFlag = 1
    jump day3general

label unicornDay2:

    play music "audio/Music MP3/Crowdust_Ball.mp3" volume 0.25 loop
    "Despite her many promises, you know that Lady Vetala's meetings tend to run longer than she anticipates. "

    "You have hours to kill if not the rest of the evening - the idea of sitting in the hall for the entire time sounds like an agonizing death by boredom. "

    "You stand and stretch, tilting your head back and forth to relieve the tension in your neck. "

    "Why not explore?"

    #scene bg castleexterior

    "The areas that are off-limits to guests are clearly marked and you've certainly never seen opulence done like in Lysium."

    scene bg hallentrance
    play sound "<from 0 to 2>audio/AUDIO MP3/Walking (Boots).mp3" 

    "You stroll at a leisurely pace to a hallway that yawns into one of the many antechambers with high vaulted ceilings and glimmering chandeliers; you take care not to gawk as you steal appraising glances at the architecture."

    "As you continue, you begin to pick up on the distant sound of laughter coming from one of the ballrooms. "

    "It's not THE ballroom- you're in the eastern wing of the castle- but the doors are left ajar to prevent the air from becoming too stuffy."

    "You consider lingering to eavesdrop, but the idea of being caught sends a jolt of panic through you. "

    "There wouldn't be a convenient excuse if someone happened to open the door and hit you with it. "

    scene bg ballroom:
        xzoom -1

    "Your shoes click off of the polished floor and you slow to a brief stop. "
    stop music fadeout 0.5

    play music "audio/AUDIO MP3/Crowd Whispering.mp3"  loop volume 0.45

    "The quiet murmur of overlapping voices meets your ears, slowly growing closer. "

    "You renew your stride and turn the corner to find one of the doors propped open and a small scattering of nobles milling about."

    "There is no clear distinction of class or hierarchy of the way people are mingling, so you decide that it's safe enough to approach. "

    "Upturned chairs are stacked against the wall and the tables are piled at least three deep. You wonder if this room was meant to be opened in the first place. "

    "Perhaps they were in the process of setting up and a few people decided to be nosy?"

    "You're broken from your wondering by a cold jolt of alarm crackling through your nerves.  "

    show unicorn neutral

    "A heartbeat later, you see the ominous Duke from the previous night standing with a small group of similar nobility. "

    "He's looking directly at you with an intensity that immediately sets you on edge. "

    "You falter mid-step and force yourself to look past him even as the nape of your neck prickles with anxiety. "

    hide unicorn

    "He wouldn't abandon his peers to single you out, right?"

    show unicorn neutral at right
    show mc shock at left

    u "Lady Nyxomena. How fortuitous to see you here."

    show mc neutral at left

    "Damn it all."

    menu unicornd2Choice:
        "Force a smile":
            $ unicornAffection += 2
            jump unicd2ForceSmile
        "Stand your ground":
            $ unicornAffection += 1
            jump unicd2StandGround
        "Escape":
            $ unicornAffection -= 1
            jump unicd2Escape
    
label unicd2ForceSmile:

    show mc neutral at left

    "You swallow your discomfort and force a smile onto your face. "

    hide mc
    hide unicorn

    "If your deadbeat father had given you a single useful trait, it was the confidence to bluff your way out of a sticky situation. "

    "You only have to hope that it holds."

    show mc neutral at left
    show unicorn neutral at right

    mc "Of course. I was just... getting some air."

    show unicorn evil at right

    u "I would expect nothing less from a woman of your breeding."

    "The Duke smiles politely as your stomach drops. "

    hide mc
    hide unicorn

    "How fast did word spread around here? Were you really that recognizable?"

    show unicorn evil at right
    show mc neutral at left

    "He steps into your personal space and rests one hand on your elbow, pressing lightly to steer you away from the rest of the nobles. "

    "The proximity makes your skin crawl, but more importantly, the mention of your breeding makes your blood boil. "

    "The other shoe is going to drop any second. "

    "You briefly entertain the idea of slapping him across the face when it does."
    
    "Unfortunately, an outburst of that sort would almost certainly make it back to Ambassador Vetala before you have a chance to explain yourself."

    hide mc
    hide unicorn

    "Except... "

    "It never comes. "
    scene bg garden2

    show unicorn neutral at right
    show mc neutral at left
    play sound "<from 0 to 2>audio/AUDIO MP3/Walking (Boots).mp3" 
    play music "audio/AUDIO MP3/Outside White Noise (Night).mp3" loop volume 0.25

    "Duke Acacius walks you toward one of the arched windows, releasing your arm and folding his hands behind his back. "


    "You step deliberately to the side and resist the urge to cross your arms, giving him a sidelong glance as he gazes out at the tops of the topiary. "

    show unicorn somber at right

    "Either the snide remark was a brief lapse in judgment or he truly has no idea who you are. Some of your hostility fades, though that doesn't make him any more welcome."

    u "I've always found the landscape to be particularly rejuvenating." 

    u "While these gardens are a bit much for my taste, they serve their purpose well enough, don't you think?"

    show unicorn neutral at right

    "He glances at you with a polite smile before returning his attention to the gardens outside. "

    "Despite your reservations, you take your eyes off of him to look out the window. "

    "The gardens sprawl below in a carefully manicured collection of green and white."

    show mc happy at left

    mc "They're lovely."

    jump unicd2End
label unicd2StandGround:

    show mc neutral at left

    mc "It seems my fortunes fall short today. What do you want?"

    "Rather than recoil at the flatness in your tone, the Duke's smile widens with a flicker of genuine amusement. "

    show unicorn evil at right

    "He reaches for your hand again and you take a deliberate step away, expression cool and unamused. "

    "The bastard seems to take your aloofness as an invitation, though thankfully he doesn't attempt to touch you again."

    show unicorn neutral at right

    u "My sincerest apologies, my Lady, if I've caught you at a bad time. I had wanted to apologize for the brevity of our first meeting."

    hide mc
    hide unicorn

    "Something about his tone rubs you the wrong way. There's something woven into his words, hidden between the lines and left unsaid, for you to pick up. "

    "You can't recall if unicorns were considered one of the fair folk, but either way, wordplay and nuance has never been your strongest suit. "

    "Try as you might, you can't put a finger on what he isn't saying. "

    show mc neutral at left
    show unicorn neutral at right

    mc "No apology necessary. Is that all?"

    jump unicd2End
label unicd2Escape:

    show mc neutral at left

    "You take a step back. "

    "Another. "

    "The Duke touches your arm and offers you a thin smile, his hair glinting like spun silver. "

    hide mc
    hide unicorn

    "A crackle of white-hot adrenaline runs through your limbs. "

    "You're pushing him away before you even register that you're moving, putting distance between the two of you. "

    "You do not want to be touched. "

    "You become conscious of every place that your dress clothing is constricting you, rubbing against your skin and making your teeth itch. "

    "Your amulet feels cold against the flush creeping up your throat. "

    show unicorn somber 

    "Duke Acacius' smile fades as you back away, posture straightening to something more serious. "

    "He takes another step closer with one arm extended, reaching for you before clearly thinking better of it. "

    "His hand wavers in the air before his arm falls back to his side and he glances over your shoulder at the nobles who are no doubt taking notice."

    u "Is something the matter?"

    show unicorn somber at right
    show mc neutral at left

    "You need air. "

    "Actual air, not the perfume-drenched and dusty air within the castle walls. "

    "You need to get your head on straight before you lose control. "

    "Your hand flies to your collar where your amulet burns like a chip of ice. "

    "Forcing a steady breath, you give the Duke your most passable smile and the shortest curtesy you can manage."

    mc "Excuse me."

    hide mc

    "You brush past him and keep your chin raised even as you feel everyone's eyes on you. "

    hide unicorn
    play sound "<from 0 to 2>audio/AUDIO MP3/Walking (Boots).mp3" 

    "Your shoes click evenly against the ground. "

    "Once you make it back into the hallway and turn the corner, you swiftly take both shoes off, clutching them to your chest and fleeing to your chambers with silent footfalls."

    "This is going to be the longest week of your life."
    stop music

    jump day3general
label unicd2End:

    show mc neutral at left
    show unicorn neutral at right

    "To your relief, the conversation is cut short as one of the Duke's previous partners waves him over. "

    "You manage to hide your smile as he sighs dramatically, dipping his head in acknowledgement."

    u "It seems time to take my absence. I hope to see you again, my Lady. May I?"

    "This time he {i}asks{/i} before taking your hand, and finding no valid reason to scorn him, you permit it. "

    "He kisses your knuckles and then bows, careful not to snag his horn on any of your finery. "

    "He hesitates for just long enough that you wonder if you're imagining it, but the way his gaze lingers is confirmation enough."

    u "Give the Ambassador my regards."

    hide unicorn

    "Another thin smile and he finally takes his leave, sparing you no backward glance."
    stop music
    jump day3general

label bunnyDay2:

    #scene bg hallentrance

    "While briefly tempted to find something to do, your sense of duty ultimately wins out. "

    "You sigh and take a seat at the nearest bench. "

    "Ambassador Vetala hadn't mentioned how long the meeting was supposed to take, and while you don't need to be here, it was a silent expectation of being her Lady-in-Waiting."

    play sound "audio/AUDIO MP3/PageFlapping Short.mp3"

    "You set your documents on the bench and glance up and down the hallway. No errant nobles or statuesque guards to be seen; for once, luck is in your favor. "

    "You slip two fingers underneath the paneling of your corset and carefully extract a tailor's pencil in soft blue. The Ambassador had shown you this particular trick; she was an expert at stashing all sorts of odds and ends in her expansive wardrobe. "

    "You never had nearly enough layers to pull off anything of her caliber."

    play sound "audio/AUDIO MP3/PageFlapping Short.mp3"

    "Humming to yourself, you open your booklet and navigate to its center, flipping through a collection of blank pages in between the Ambassador's itinerary and a simplified map of the castle."

    "Though originally meant for annotations and personal specifications, Ambassador Vetala wrote her own notes and you weren't allowed into the majority of her meetings so you filled the space with doodles."

    "There are already a few disembodied flowers scattered across the page, most drawn in profile from your previous walks through the garden. "

    "They aren't exactly lifelike, but for your purposes, they're good enough. "

    "A few more blossoms join the rest and then your memories are picked clean; what else can you draw? "

    "You tap the pencil on the page as you think. "

    "What about a crow?"

    "The shape is etched into the back of your amulet, but you've seen it enough times to draw the figure without reference. "

    "A round body, beady eyes, a triangular beak. A crescent forms the wings and a small wedge becomes the tail. "

    "You look down at the drawn bird and smile, pleased with its simple shape, only to startle when the door cracks open to your right."

    show bunny angry
    play sound "<from 0 to 2>audio/AUDIO MP3/Walking (High Heels).mp3" 

    "Ambassador Vetala steps out of the room, veil pulled low over her face. "

    play sound "<from 0 to 2>audio/AUDIO MP3/Running (Boots).mp3" volume 0.15

    "Her handmaiden scurries to close the door behind them and then disappears, clearly on some sort of mission, as the Ambassador crosses the foyer. "

    "Caught off guard, you jam the tailor's pencil between the pages and move to stand."

    show bunny angry at right
    show mc neutral at left

    mc "Ambassador Vetala-?"

    show bunny cocky at right

    "She holds up a single hand, expression pinched, before she takes a seat beside you."

    b "Don't."

    menu bunnyd2Choice:
        "Ask if something happened":
            $ bunnyAffection -= 2
            jump bunnyd2AskHappened
        "Say nothing and straighten her veil":
            $ bunnyAffection += 2
            jump bunnyd2Veil
        "Ask if she's alright":
            $ bunnyAffection += 1
            jump bunnyd2Alright

label bunnyd2AskHappened:

    show bunny angry at right
    
    "The Ambassador's expression hardens and she presses her lips into a thin, brittle line."

    b "Nothing that concerns you."

    show mc shock at left

    "Your face heats and you avert your eyes, taking a sudden interest in the ornate mosaic on the floor. "

    "Ambassador Vetala says nothing else, staring resolutely across the foyer. "

    "You can feel the tension in her posture but can only guess at what might have upset her so badly. "

    show mc neutral at left

    "The handmaiden's reappearance is a subtle lifeline. "

    "Ambassador Vetala stands and takes something from her hands, though all you are able to see is a flash of white parchment and a red-leather binding. "

    "She hardly spares you a glance as she drifts back to the door."

    show bunny cocky at right

    b "There's no need to wait for me."

    hide bunny
    hide mc

    jump bunnyd2End
label bunnyd2Alright:

    show bunny cocky at right

    "Ambassador Vetala studies you with an unreadable expression before she sighs, adjusting her veil and gazing across the foyer. "

    "Her silence drags. "

    "For a moment, you aren't sure that she will answer you, but her voice is low when she finally speaks."

    show bunny neutral at right

    b "I will be fine. Just a bit of petty squabbling."

    "She turns her head to face you directly, the jewels along her throat glittering in the rich afternoon light. "

    "You are suddenly aware of how artificial everything is- her posture is a balancing act between too casual and too stiff, and the smile she offers does not reach her eyes. "

    hide mc
    hide bunny

    "Her lie is fairly obvious but you aren't confident enough to call her on it. "

    "Instead, you nod, determined to offer a short respite before she's ultimately whisked away again. "

    "The two of you sit in companionable silence."

    "Her handmaiden reappears, scarcely seeming to move as she hurries across the foyer. "

    "She carries a red leather booklet and a scroll sealed with wax that Ambassador Vetala accepts with a single nod. "

    show bunny neutral

    "She stands in one fluid motion and dismisses her assistant with the wave of one manicured hand, tucking her newly-fetched documents against her body. "

    "Ambassador Vetala gestures to the room; duty calls."

    "She pauses and glances back at you before she pulls the door open, lips curved into a real smile, highlighting her sharp teeth."

    "She winks at you."

    show bunny neutral:
        xzoom -1

    b "You wouldn't believe how some people act behind closed doors."

    hide bunny

    jump bunnyd2End
label bunnyd2Veil:

    show bunny neutral

    "Ambassador Vetala lifts an eyebrow as you lean into her space, but she doesn't move as you reach out and carefully straighten her veil. "

    "You aren't sure how much is too much, so you hesitate before untucking a coil of hair from beneath her sash. "

    "She regards you with a steady expression before her eyes soften."

    b "That was unneccessary."

    "Her tone is more contemplative than accusatory, and the instinctive apology withers before you can open your mouth. She nods once."

    show bunny neutral:
        xzoom -1


    b "...Thank you."

    "Ambassador Vetala gestures to the room; duty calls."

    "She pauses and glances back at you before she pulls the door open, lips curved into a real smile, highlighting her sharp teeth."


    hide bunny

    jump bunnyd2End
label bunnyd2End:

    hide mc

    "Once again, you find yourself alone. "

    play sound "audio/AUDIO MP3/PageTurn.mp3"

    "You hesitate before unfolding the documents yet again and pick up the tailor's pencil. "

    "You can sit here for a bit longer to see if the Ambassador will reappear any time soon; the rest of the day is spent wondering what could have set her off."

    jump day3general


label day3general:
    scene bg mcroom with wipeleft

    "{size=*5.5}DAY 3{/size}"

    "You emerge from the depths of slumber. "

    "Despite the weather being as sunny as the day before, you take longer to get out of bed, feeling like your blankets have conspired to keep you captive for another hour or so. "

    "Alas, you have work to do. "

    "Your mind is drowsier and more sluggish today as you get ready for the day ahead."

    "Ambassador Vetala had allotted time in her schedule today for a visit to the Imperial Archives. "

    "She had previously expressed an interest in learning more about the Kingdom's history and etiquette before the Prince's wedding. "

    "{i}You{/i} remember your true purpose for accompanying Ambassador Vetala to the Imperial Archives: to find any clue about your curse from the archives on the Nyxomena family history."

    play sound "<from 0 to 3>audio/AUDIO MP3/Walking (Boots).mp3"

    "You take long, quick strides to Ambassador Vetala's room, deliberately trying to give yourself a semblance of wakefulness."

    scene bg bunnyroom

    "Upon reaching her room, you spot a cup of chai next to a significant stack of paperwork. You take note of the Ambassador's sluggishness and feel a sense of camaraderie with the Ambassador of the Nazar Empire."

    "Together with Ambassador Vetala, you make your way to the solemn halls of the Imperial Archives." 

    scene bg libraryentrance
    
    "The towering bookshelves fraught with academic journals and official documents intimidates you, having not seen such a huge collection of information in one setting. "

    "Compared to the town library that was the size of your current room, the Imperial Archives was a grand labyrinth of faded grandeur and literary wonders."

    show bunny neutral at right
    show mc neutral at left

    b "This shouldn't take more than thirty minutes."

    mc "Yes, my Lady."

    hide bunny

    "A library assistant approached the Ambassador and helped her with her find, leaving you in solitude as you try to navigate through the scent of weathering parchment and aging leather. "

    hide mc

    "Though there were other library assistants scattered in and around the shelves, you didn't want to disturb them, feeling a slowly-growing apprehension about potentially needing to explain your reasons for finding more on the Nyxomena family history."

    scene bg libraryshelves

    "You arrive at the Noble Family shelves and reach the intersection of N and M documents. An academic journal titled Common Myths of the Nyxomena is tucked behind a crooked tome."
    
    "You pull both the journal and the tome from the shelves with a frown. "

    "The tome is heavy and the words Origins of Dark Spirits are embossed against the leather.  "

    "That... doesn't belong here. At all. Someone must have been browsing an aisle over and set it down before their attention was called elsewhere. "

    "You roll your eyes and consider putting it back, but that would just leave the problem unaddressed. Hm. You'll try to remember to flag down one of the archivists on your way out."

    play sound "audio/AUDIO MP3/HeavyBookDrop.mp3"

    "You seat yourself at a nearby mahogany table and start to skim through the journal's contents."
 
    "The academic journal was written by what seemed to be a fervent fan of the family. "

    "This \"fan\" also happened to be a scholar of noble genealogy, though your lip curls at the idea of an updated edition including your bastard blood. "

    "You scoff at the grandiose praise and blatant bias towards your father's noble line. "

    "Thankfully they seemed to be a generation or two short of reaching your sire."

    show mc neutral

    mcthoughts "Did this scholar get paid to write this?"

    hide mc

    "You continue to read."

    #would be cool if we had pic of book here

    cmn "The Nyxomena Family has been blessed with many generations of sons and celebrates each noble birth accordingly. "

    cmn "Much rarer are the instances of a daughter, typically found every few generations, and their births have been viewed as heralds of unrest. "

    cmn "When a daughter is born, the child does not normally live for much longer than two decades. "

    cmn "Causes of death are inconclusive and range from consumption to asphyxiation; in the few instances that the young woman survives long enough to become a bride, no viable heirs have ever been produced. "

    cmn "The longest-surviving daughter to date had not seen her twenty-third birthday before her death-Endove Cinna Quinwan (née Nyxomena) passed away before she was able to deliver her child. "

    cmn "Such children have intermittently shown signs of hysteria from adolescence onward; chief complaints include frequent claims of a dark figure following them and a persistent feeling of being watched. "

    cmn "Attempts to safeguard their health have been unsuccessful. There have been no responses from the family about the origins of the dark figure or any explanations of what could have been plaguing the female descendants of the Nyxomenas. "

    cmn "The current Count, Hadrian Markus Nyxomena has said that \"their deaths prove only weakness and a minute defect in our noble bloodline\". It has been speculated that-"
    play sound "audio/AUDIO MP3/HeavyBookDrop.mp3"

    "You snap the journal closed."

    show mc neutral

    mcthoughts "What a prick."

    hide mc

    "You had known about your rumored fate from the half-brothers who had taunted you, calling you a major flaw of the family bound for death in a couple years' time. "

    "You put the journal down to resist the urge to throw it across the room. You had come here for answers, damn it all, not idle speculation. "

    "The tome sits innocently on the edge of the table and you pick it up to avoid losing your temper entirely. You run a single fingertip over the spine, tracing the unadorned title. "

    "You could easily clock the more somber and serious nature of this book. "

    play sound "audio/AUDIO MP3/PageFlapping Short.mp3"

    "The tome seemed to be a compendium of essays that speculated on the various reasons that \"dark spirits\" may appear. Begrudgingly, you decide that you might as well skim a few pages."

    ds "Many hast questioned how dark spirits are formed. "

    ds "The most common explanation for the presence of dark spirits is that they are created as the issue of individuals whom committed outstanding evils, normally from the envious concentration of feelings by a betrayed party. "

    ds "Dark spirits shall not properly pass on from the material orb and shall persist betwixt multiple generations of their bloodline unless the root of the scorn has been addressed. "

    ds "'Tis currently unknown how to release dark spirits from their curse-like form. Dark spirits can normally be summoned by mana users who ..."

    "You stop reading as a chill runs along your spine. "

    "Is that what your curse is? An ancient grudge?"

    "You go back to the middle of the page, studying the words \"individuals whom committed outstanding evils\" as you try to commit them to memory. You have no allegiance to your bloodline, but it's still chilling to wonder what one of your ancestors could have possibly done."

    "You try to skim through the {i}\"Common Myths of the Nyxomena\"{/i} again but find no evidence of any possible \"outstanding evils\" that could have been committed. "

    "The author made no attempt to hide his favoritism- you'll need an unbiased account to find anything else of note. You drag one hand across your face and try to chase away the gritty feeling behind your eyes."

    "Glancing up, you realize that the evening has started to set in, painting the library in long shadows and golden sunlight. What should have been thirty minutes from waiting for Ambassador Vetala had become several hours. "

    "Your stomach drops. "

    "Did she leave without you?   Or did she wander further into the stacks?"

    scene bg libraryentrance

    "You abandon your research on the table as you brush yourself off and walk briskly to the main aisle. You pass some bookshelves and find the Ambassador curled up in a wide leather chair, veil obscuring her expression. "

    "A stack of books sits on the table to her right, a few more scattered at her feet. The knot of anxiety loosens. "

    "You approach the Ambassador, reminding her to feed herself lest she get dizzy once again."

    show mc neutral at left
    play music "audio/Music MP3/Crowdust_Day.mp3" volume 0.25 loop

    mc "Ambassador Vetala, it is time for dinner!"

    show bunny teary at right

    "Ambassador Vetala glances up and pushes her hair out of her face, giving you a bleary look. "

    "She must not have moved since sitting down- you see that she's more than three-fourths of the way through a book titled {i}Typical Faux Pas in Lysium.{/i}"

    "She glances at the window and her eyes widen as she looks back, clearing her throat and straightening her dress."

    show bunny neutral at right

    b "... My apologies for the wait. I am normally good with my time management."

    hide bunny
    hide mc

    scene bg bunnyroom
    play sound "audio/AUDIO MP3/Silverware.mp3"

    "You and Ambassador Vetala make your way to a smaller dining room adjacent to her bedroom and indulge in a fulfilling supper of roast chicken and vegetables."

    if snakeAffection > 0:
        jump snaked3Night
    if unicornAffection > 0:
        jump unicornd3Night
    else:
        jump bunnyd3Night


label snaked3Night:
    "After dinner, you are in Ambassador Vetala's room for some of your final tasks of the day."

    b "Could you make a visit to the kitchen and get me a slice of the strawberry cake that was at dinner earlier?" 
    
    b "The maids are busy preparing some of my items for the wedding in a few days."

    mc "Yes, my Lady."

    "You leave Ambassador Vetala in her room as she focuses on some paperwork from her home country."
 
    scene bg kitchennight
    stop music fadeout 1.0

    "You walk briskly to the kitchen, making sure not to dawdle or get distracted from your mission. "

    "You had heard from one of the maids that Ambassador Vetala needed some type of sweet to make sure that she could focus on her official papers and workload. "

    "Apparently, the last maid who could only get a cake after Ambassador Vetala finished her work was reprimanded and let go from her service."

    "You open the door and do not see any of the chefs in the kitchen."

    show mc neutral

    mcthoughts "Huh, they must be off work by now."

    hide mc
    play sound "audio/AUDIO MP3/Silverware(Drop).mp3"

    "Choosing not to light any of the candles in the kitchen, you decide to start searching around the oven and ice box to see if there are any remnants of the strawberry cake that the chefs might have saved for themselves. "

    "As you dip to search one of the lower cabinets, you hear the kitchen door opening and a subtle swishing sound."

    "You remain still, for fear of being caught by someone for being in the kitchen when you shouldn't have. "

    "You hear the slithering noise move to the far right as well as a chorus of cabinets and jar lids opening and closing. "

    "The noise started to slowly move closer to you and, before the noise could get too close, you decide to peel off the bandage, praying that Ambassador Vetala could vouch for you. "

    "You pop up from your hunched over position in the corner of the kitchen."

    show mc shock at left

    mc "I'm just trying to find the strawberry cake!"

    "You hear a resounding gasp of astonishment and you notice a tall figure holding a flickering candle about five paces away from you."

    unk "Lady Nyxomena! What are {i}you{/i} doing here?!"

    show snake neutral at right

    "You recognize the voice to be [snakename]!"
    
    mc "What are {i}you{/i} doing here?!"

    show snake blush at right

    "Azhe's demeanor wavered. He started to stammer."

    s "I'm only trying to make sure the kitchen doesn't have any intruders! Nothing else!"

    show mc neutral at left

    "You raise your eyebrow in disbelief."

    show mc happy at left


    mc "Ah yes, the intruders hidden in the cabinets and jars. Of course!"

    "You remark sarcastically as you gesture towards the open cabinet next to Azhe. Azhe quickly closes the cabinet."
 
    show mc happy at left

    "A subtle smirk tugs at the corners of your mouth."

    mc "The Knight Captain wouldn't be stealing from the kitchen, would he? What would his subordinates {i}think{/i}??"

    show snake angry at right
    play sound "<from 0 to 2>audio/AUDIO MP3/Moving (Snake).mp3"

    "Before you could react, Azhe slithered closer to you and put his finger on your lips to shush you."

    s "Keep your voice down! I'll tell you where the rest of the sweets are but you have to keep quiet about me being here!"

    menu snaked3Choice:
        "* Nod your head *":
            $ snakeAffection += 2
            jump snaked3Yes
        "Do not agree":
            $ snakeAffection -= 2
            jump snaked3No

label snaked3Yes:
    show mc neutral at left
    show snake neutral at right:
        xzoom -1

    "You slowly nod, agreeing to an unspoken truce as you quietly follow Azhe. "

    "As he starts to move in the darkness, you grab his hand in the dark. You feel Azhe stop in his tracks."

    mc "I don't have a candle with me."

    show snake blush at right:
        xzoom -1
 
    "A moment passed before he silently let your hand stay in his. "

    "You feel your heart flutter in your chest as his hand intertwines with yours. "

    "The kitchen around you fades into insignificance and, for a brief moment, you forget why you were here in the first place as Azhe leads you into another area of the kitchen."

    "You feel Azhe stop moving and place his candle at a nearby table."

    show snake neutral at right:
        xzoom -1

    s "Just a second-"

    show mc shock at left
    hide snake

    "You let go of his hand and you can barely see Azhe extend his serpentine body to reach the top of a stack of crates." 
    
    "He grabs a small sack and opens a cabinet near the same level. A few seconds pass as you hear some shuffling of boxes and jars and Azhe returns to his regular height." 
    
    "He places a plate with two slices of cake and a small sack filled to the brim with cookies on the table next to the candle."
    
    show mc happy at left
    show snake neutral at right

    mc "Thank you, [snakename]! You're a lifesaver!"

    show snake blush at right

    "You wrap your arms quickly around his torso, holding for a brief moment."

    "You can't tell what Azhe's face looks like at this moment but you quickly remember your mission for the Ambassador."

    "You grab the plate and start to return to Ambassador Vetala's room."

    hide mc 
    hide snake

    "On your way back, you think of different recipes for sweets that you could make for your newfound friend."

    jump tbcEnding
label snaked3No:

    show mc happy at left

    mc "No can do."

    show snake angry at right:
        xzoom -1

    "You barely notice Azhe's face twist into a scowl as he moves away across the kitchen, leaving you in the darkness. "

    hide snake
    hide mc

    "You return to your search in the kitchen, unable to find the cake that the Ambassador asked for. "

    "You leave the kitchen with a small box of crackers as a consolation prize."

    scene bg bunnyroom

    "When you return to the Ambassador's room, you notice an empty plate with remnants of cream." 
    
    "One of the maids tells you that an official visited while you were gone and treated her to a slice of their share of strawberry cake."

    jump tbcEnding

label unicornd3Night:
    "Ambassador Vetala remains immersed in her work for the rest of the evening. "

    "You help her carry her many books back to her chambers; thankfully, a lifetime of living among farmers has made the chore a breeze. "
    play sound "audio/AUDIO MP3/PageTurn.mp3" 

    "You sat in comfortable silence and skimmed through some of the least dry sections of her books. "

    "{i}History of the Lysium Royal Ancestry{/i}? {i}Most Devilish Scandals of the Past Century{/i}?"

    "Only once the candles were beginning to burn low did Ambassador Vetala stir from her studies, tapping her quill against the paper she had been writing on."

    show bunny neutral

    b "Lady Nyxomena, could you please fetch another pot of ink from the library? "

    hide bunny

    "You resist the urge to sigh. "

    "At least it was something to do aside from reading about the scandals of the 56th Lysium Queen and her dozen mistresses. "

    "A brisk walk would stave off some of your boredom."
    show bunny neutral at right
    show mc neutral at left

    mc "Of course, my Lady."

    scene bg hallentrance

    hide bunny 
    hide mc
    play music "audio/AUDIO MP3/Outside White Noise (Night) 1.mp3" loop volume 0.5
    "The castle is well-lit enough that you don't need a candle to walk the halls at night, nodding politely at the few guards you pass. "

    "It's almost eerie to see these grand halls devoid of life; the soldiers are so still they may as well be statues."

    "You aren't sure when the silence grew more unsettling than peaceful. "

    "The hair on the back of your neck raises in warning. "

    show unicorn somber 

    "You look up just as the Duke appears from one of the dining halls, pulling the door closed with a soft click. "

    "He stands there for a moment and runs one hand through his hair, letting out a sigh before abruptly looking up. "
    play sound "<from 0 to 2>audio/AUDIO MP3/Walking (Boots).mp3" 

    "His expression is blank before recognition flickers across his face; he smiles and crosses the hall to join you, dipping into a full bow."

    show unicorn neutral at right
    show mc neutral at left

    u "Good evening, my Lady. What keeps you out at this hour?"

    mc "A brisk walk before bed has always helped my nerves."

    "You smile in return. A white lie never hurt anyone."

    show unicorn evil at right

    u "Of course, of course." 

    u "My social visit with Count Stotern had concluded a mere quarter-hour ago; it seems many visiting parties aren't eager to stay out after dark."

    "His smile is borderline condescending, eyes glinting with some unspoken joke. "

    u "I suppose some superstitions persist even away from home."

    menu unicd3Choice:
        "Be polite":
            $ unicornAffection += 2
            jump unicd3Polite
        "Claim busy":
            $ unicornAffection += 1
            jump unicd3Busy
        "Get skeptical":
            $ unicornAffection -= 1
            jump unicd3Skeptical

label unicd3Polite:
    mc "Old habits die hard, I would imagine."

    show unicorn neutral at right

    "The Duke hums thoughtfully before giving you a particularly intrigued look. "

    "Without warning, he steps closer and you aren't fast enough to back up before his hand grazes your upper arm. "

    "He traces his fingers up and along your shoulder, touch lingering before he tucks an errant lock of hair back behind your ear. "

    "You feel a sudden spark of relief that you had stopped for a shawl-the idea of his hand on your bare skin sends a shiver up your spine. "

    show unicorn evil at right

    "His gaze drops lower, but not quite low enough to constitute an insult. "

    "The Duke's thumb brushes the edge of your choker before he removes his hand entirely, offering you a contemplative look."
    
    show unicorn neutral at right

    u "A lovely color. I hadn't realized such beauty could be found in Lysium."

    "You don't react to the careful barb against your upbringing, having heard worse from others already."

    mc "It was my mother's."

    show unicorn somber at right

    "His eyebrows raise before the meaning seems to register. His expression falls to something much more somber."

    u "I hadn't realized. My condolences."

    "A hollow platitude that you're almost tempted to laugh. "

    "You've heard it a thousand times and you were likely to hear it a thousand more. "

    "It seems like no one really knew how to confront the unpleasant realities of life."

    jump unicd3End
label unicd3Busy:
    mc "I suppose, but I'm sure other parties have their own plans as well."

    mcthoughts "{i}Like yourself.{i}"

    "Unfortunately, your subtle hint seems to fall on deaf ears. "

    show unicorn neutral at right

    "The Duke simply hums in agreement, clasping his arms behind his back. "

    "The motion pulls the deep cut of his shirt further open; it seems too convenient to be wholly accidental. "

    "By sheer force of will, you keep your expression politely neutral and your gaze fixed firmly above his collarbones, though the Duke seems too lost in thought to notice."

    u "It seems everyone has an agenda of their own these days."

    "His tone is light and carefree; the comment seems to be no more than idle chatter. "

    "Yet it still gives you a moment of pause. Your curse never materializes around other people. "

    "Logically, you know there isn't anything that could have informed him of your condition, but the more emotional part of your mind whispers that he {i}knows{/i}."

    mc "It comes with the title, I'm sure."

    "He glances at you, seeming somewhat surprised before his gaze shifts away. You have the vague impression that he hadn't meant to speak that part aloud."

    u "Naturally."

    jump unicd3End
label unicd3Skeptical:
    mc "Or perhaps they have plans elsewhere. It isn't unreasonable to think that other dignitaries are meeting off-record."

    "Your words are especially pointed as you raise one eyebrow and glance at the door that the Duke had come from." 
    
    show unicorn somber at right

    "His smile fades, eyes narrowed minutely."

    u "Of course not, my Lady."

    jump unicd3End
label unicd3End:
    "You shift your weight and barely resist the urge to cross your arms, glancing impatiently down the hall. "

    "Finally, the Duke seems to take the hint, clearing his throat and offering a half-bow. "

    show unicorn neutral at right

    u "I would hate to keep you much longer, though I must thank Lady Fortune for allowing our paths to cross yet again. I only hope to be as lucky in the coming days. "

    "His smile is indulgent; the bastard doesn't even have the sincerity to seem bashful with such blatant flirting. "

    "You only dip your head in response to his bow and allow the Duke to step out of the way, giving you one last polite smile before departing. "

    #scene bg 

    "You resume your walk at a deliberately carefree pace, listening to the departing clicks of the Duke's steps upon the floor as they slowly grow fainter. "

    "Only then are you able to relax. "

    "You pass the door that the Duke had originally come from, noticing that it sat somewhat ajar. "

    "He hadn't even bothered to make sure it had closed. No wonder the castle was so drafty. "

    "You roll your eyes and push the door open to close it properly, though the lack of candlelight is enough to give you pause. "

    "You hesitate before looking into the dining hall, noticing that it's completely empty. "

    "All of the tables have been set for the morning; not a single utensil was out of place. "

    "Was the Duke even meeting with anyone? Or was he just sitting in an empty room? More importantly- why?"

    #scene bg hallentrance

    "A prickle of unease has you closing the door and walking just a bit faster, retreating to the certainty of your chambers. "

    "You only remember when you pass the hall to the Ambassador's chamber:"

    "The pot of ink. "

    "You'll just have to tell her that none of the studies were open."

    jump tbcEnding

label bunnyd3Night:
    "The rest of the day is relatively peaceful. "

    "Ambassador Vetala remains immersed in her studies and dismisses you for the majority of the evening. "

    "You knock politely at the door to see if there's anything else you need to do tonight."

    show bunny neutral 

    b "Come in!"

    hide bunny

    "Pushing the door open, you find the Ambassador sitting at her desk with several candles scattered around the room. "

    "Books are piled neatly against the wall and several letters sit unfolded in front of her. "

    "She glances up at your entry and breaks into a tired smile."

    show bunny neutral at right
    show mc neutral at left

    b "Lady Nyxomena! I was hoping that would be you. I was wondering if I could ask a favor."

    "Her tone is light enough, yet something tells you that her ask is going to be nonnegotiable."

    mc "Of course."

    b "Could you please visit the kitchen? I believe I'll be awake for a few more hours and I would love something sweet while I read."

    show bunny teary at right

    "She pouts just a little bit until you laugh, shaking your head."

    show mc happy at left

    mc "Sure. Strawberry?"

    show bunny neutral at right

    b "Please!"

    "You curtsy once and leave the door ajar, heading back to your chambers for something lightweight to put over your shoulders."

    scene bg hallentrance
    hide mc
    hide bunny

    "The climate in Lysium is cooler than you're used to, and at night, the halls feel especially drafty."

    "The late-evening stillness is refreshing compared to the constant bustle of the day. "

    "You wonder if this is what it would be like to have grown up as a member of nobility. "

    "It seems strangely lonely."

    "Your thoughts are company enough, it seems, because your journey goes by in an instant. "

    scene bg kitchen

    "Soon enough, you're standing in one of the several serving halls, watching firelight dance along the smooth stone walls. "

    "Thankfully the kitchen is still staffed even at this hour. One of the servants meets you at the door."

    kserv "Does my Lady have a request?"

    show mc neutral

    mc "I've been asked to fetch, ah, a slice of cake? For Ambassador Vetala. Strawberry, if you have it."

    hide mc

    "Whether through sheer professionalism or because they had been informed of the Ambassador's sweet tooth in advance, the servant hardly blinks. "

    "They nod and ask you to wait a moment, disappearing into the quiet bustle of the kitchen. "

    "You see dough being covered with stiff cloth; someone is coring apples before slicing them into picturesque crescents. "

    "Getting ready for the morning, you presume."

    "It isn't long before the servant returns with a covered platter. "

    "They open it briefly so you can see the requested cake, as well as a handful of cookies and cut fruit arranged artfully beside it, though they pause before handing it to you."

    kserv "Will my Lady require an escort?"

    show mc neutral 

    mcthoughts "To carry a slice of cake? Yeah, no."

    show mc happy

    mc "I couldn't possibly impose."

    hide mc
    play sound "audio/AUDIO MP3/Silverware01.mp3" volume 0.3

    "The servant nods once and presses the platter into your hands, making sure your grip is secure before relinquishing it. "

    "The platter is undoubtedly heavier than the plate itself. "

    "Satisfied, you're given a shallow bow before the servant vanishes into the kitchen once more. "

    "As the door closes, you see a glimpse of them returning to a pot held above an open flame, plucking a wooden spoon from one of the cluttered countertops."

    scene bg bunnyroom
    play sound "<from 0 to 2>audio/AUDIO MP3/Running (Boots).mp3" volume 0.15

    "You bring your prize back to the Ambassador's chambers. The door, thankfully, is still left ajar; you're able to push it open with your shoulder. "

    show bunny neutral
    play sound "audio/AUDIO MP3/UnrollingScroll02.mp3" volume 0.15

    "The Ambassador holds up one finger before you can say anything and makes a hardly-visible line on one of the scrolls before she carefully re-rolls it and clasps her hands together."

    show bunny blush at right
    show mc neutral at left

    b "Delightful! I hope it wasn't too much trouble."

    mc "Not at all."

    menu bunnyd3Choice:
        "Ask how her work is going":
            $ bunnyAffection += 1
            jump bunnyd3HowWork
        "Ask if she needs anything else":
            $ bunnyAffection -= 1
            jump bunnyd3AnythingElse
        "Ask how the cake is":
            $ bunnyAffection += 2
            jump bunnyd3Cake

label bunnyd3HowWork:
    show bunny angry at right
    play sound "audio/AUDIO MP3/PageFlapping Short.mp3" 

    "The Ambassador gives a particularly long sigh, closing one of the many books that lay open across the desk. "

    show bunny neutral at right

    "She pushes her hair away from her face and gives you a thin smile."

    show bunny blush at right

    b "Good enough, all things considered, though progress is slow. This is a welcome distraction."

    show mc happy at left

    "You smile at her greatly improved mood, feeling a bit more relieved to see just how much she's perked up. "

    hide mc
    hide bunny

    "It's already been quite the day; the wedding is still several nights away and you know Ambassador Vetala well enough to know she'll work diligently the entire time."

    show bunny neutral at right
    show mc neutral at left

    "She makes a vague gesture with one hand, indicating the vanity near the window."

    b "Your company is always appreciated. Unless you have plans, you're welcome to join me."

    mc "Of course, my Lady."

    b "No need for the formalities. I've invited you as a friend."

    hide mc
    hide bunny

    "You spend the rest of the evening in her chambers, your conversation drifting from recent affairs to the shreds of gossip she's picked up from the other dignitaries."

    jump tbcEnding
label bunnyd3AnythingElse:

    show bunny angry 

    "Ambassador Vetala looks up at you with a furrow between her brows, lips curved into a small frown. "
    play sound "audio/AUDIO MP3/Silverware.mp3" 

    "She looks almost hurt in the moment it takes for her to turn away, pushing some of her books away to make space for the plate of sweets. "

    "Rather than immediately digging in, she picks at a bit of cream with a single tine of her fork."

    b "No, thank you. You're dismissed."

    "You stand there for a long moment before realizing she has nothing else to say. "

    hide bunny
    hide mc
    
    "The air feels heavy and awkward. Uncertain, you bow and begin to back away, turning to open the door as quietly as possible. "
    
    "You presume she is exhausted as she continues to pick at her slice of cake, unaffected by your departure."
    
    "As you slip into the hallway, you hope tomorrow will be a better day. "
    
    jump tbcEnding
label bunnyd3Cake:
    show bunny blush at right

    "Her smile is bright and somewhat mischievous as she gestures for you to come closer. "

    hide bunny
    #hide mc

    "She scoops some of her various books off of a side chair and pulls it in for you to sit on before she picks up the plate."

    show bunny blush at right
    show mc neutral at left

    b "It's delightful. Here- try a piece."

    show mc shock at left

    "You lean in to accept the fork from her, but rather than handing it to you, Ambassador Vetala feeds it to you directly. "

    show mc happy at left

    "It takes a moment to overcome the awkwardness of being scrutinized but the cake itself is a wonderful distraction. "

    "It's shockingly complex in its simplicity. "

    "The cream is rich and light, offset by the tart sweetness of ripe strawberries and the deeply sweet ruby syrup. "

    "The cake itself is airy enough that it seems to melt in your mouth. "

    show bunny neutral at right

    "You must have been making some kind of face because Ambassador Vetala suddenly laughs, bright and carefree as she asks if you'd like another piece. "

    show mc shock at left

    "Your face burns and you stutter something vaguely apologetic. You scoot back in your chair to make a hasty escape- the Ambassador doesn't let you get very far."

    show mc happy at left

    b "No need to be so bashful. There's certainly enough to share."

    "She grins at you, her eyes sparkling. "

    "In this moment, she seems much less like a princess and much more like a peer. "

    hide mc
    hide bunny

    "You spend the rest of the evening together, polishing off the plate of sweets and half a bottle of red wine. "

    "You talk until Ambassador Vetala can hardly keep her eyes open and take your leave with a muffled giggle, bidding her a good evening before you escape to your own room. "

    "You undress and drop gracelessly into bed, nestling into the plush covers. It takes sleep mere moments to catch up with you."
    
    jump tbcEnding

label tbcEnding:

    scene bg tbc
    play music "audio/Music MP3/Crowdust_Day.mp3"  loop

    #""
    $ renpy.pause()

    return
