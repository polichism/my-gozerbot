# gozerplugs/facts.py
#
#

from gozerbot.commands import cmnds
from gozerbot.examples import examples
from gozerbot.plughelp import plughelp
import random

plughelp.add('facts', 'show some facts')

def init():
    global chuck
    global schneier
    global theo
    chuck = chucktxt.splitlines()
    schneier = schneiertxt.splitlines()
    theo = theotxt.splitlines()
    return 1

def handle_chuck(bot, ievent):
    """ get chuck norris fact """
    rand = random.randint(0,len(chuck)-1)
    ievent.reply(chuck[rand].strip())

def handle_schneier(bot, ievent):
    """ get schneier fact """
    rand = random.randint(0,len(schneier)-1)
    ievent.reply(schneier[rand].strip())

def handle_theo(bot, ievent):
    """ get theo """
    rand = random.randint(0,len(theo)-1)
    ievent.reply(theo[rand].strip())

cmnds.add('chuck', handle_chuck, 'USER')
examples.add('chuck', 'generate chuck norris fact', 'chuck')
cmnds.add('schneier', handle_schneier, 'USER')
examples.add('schneier', 'generate bruce schneier fact', 'schneier')
cmnds.add('theo', handle_theo, 'USER')
examples.add('theo', 'generate theo de raadt fact', 'theo')

chucktxt = """
Crop circles are Chuck Norris' way of telling the world that sometimes corn needs to lie  down.
Chuck Norris is ten feet tall, weighs two-tons, breathes fire, and could eat a hammer and take a shotgun blast standing.
The Great Wall of China was originally created to keep Chuck Norris out. It failed miserably.
Contrary to popular belief, Chuck Norris, not the box jellyfish of northern Australia, is the most venomous creature on earth. Within 3 minutes of being bitten, a human being experiences the following symptoms: fever, blurred vision, beard rash, tightness of the jeans, and the feeling of being repeatedly kicked through a car windshield.
Most people have 23 pairs of chromosomes. Chuck Norris has 72... and they're all poisonous.
If you ask Chuck Norris what time it is, he always says, "Two seconds 'til." After you ask, "Two seconds 'til what?" he roundhouse kicks you in the face.
Chuck Norris drives an ice cream truck covered in human skulls.
When Chuck Norris sends in his taxes, he sends blank forms and includes only a picture of himself, crouched and ready to attack. Chuck Norris has not had to pay taxes, ever.
The quickest way to a man's heart is with Chuck Norris' fist.
Chuck Norris invented Kentucky Fried Chicken's famous secret recipe, with eleven herbs and spices. But nobody ever mentions the twelfth ingredient: Fear.
CNN was originally created as the "Chuck Norris Network" to update Americans with on-the-spot ass kicking in real-time.
Chuck Norris can win a game of Connect Four in only three moves.
There is no theory of evolution, just a list of creatures Chuck Norris allows to live.
Chuck Norris once ate three 72 oz. steaks in one hour. He spent the first 45 minutes having sex with his waitress.
What was going through the minds of all of Chuck Norris' victims before they died? His shoe.
Chuck Norris is the only man to ever defeat a brick wall in a game of tennis.
Police label anyone attacking Chuck Norris as a Code 45-11.... a suicide.
Chuck Norris doesn't churn butter. He roundhouse kicks the cows and the butter comes straight out.
Chuck Norris doesn't wash his clothes, he disembowels them.
A Handicapped parking sign does not signify that this spot is for handicapped people. It is actually in fact a warning, that the spot belongs to Chuck Norris and that you will be handicapped if you park there.
Chuck Norris will attain statehood in 2009. His state flower will be the Magnolia.
Someone once videotaped Chuck Norris getting pissed off. It was called Walker: Texas Chain Saw Masacre.
If you spell Chuck Norris in Scrabble, you win. Forever.
Chuck Norris originally appeared in the "Street Fighter II" video game, but was removed by Beta Testers because every button caused him to do a roundhouse kick. When asked bout this "glitch," Norris replied, "That's no glitch."
Fool me once, shame on you. Fool Chuck Norris once and he will roundhouse you in the face.
The opening scene of the movie "Saving Private Ryan" is loosely based on games of dodgeball Chuck Norris played in second grade.
Chuck Norris once shot down a German fighter plane with his finger, by yelling, "Bang!"
Chuck Norris once bet NASA he could survive re-entry without a spacesuit. On July 19th, 1999, a naked Chuck Norris re-entered the earth's atmosphere, streaking over 14 states and reaching a temperature of 3000 degrees. An embarrassed NASA publically claimed it was a meteor, and still owes him a beer.
Chuck Norris has two speeds: Walk and Kill.
Someone once tried to tell Chuck Norris that roundhouse kicks aren't the best way to kick someone. This has been recorded by historians as the worst mistake anyone has ever made.
Contrary to popular belief, America is not a democracy, it is a Chucktatorship.
Teenage Mutant Ninja Turtles is based on a true story: Chuck Norris once swallowed a turtle whole, and when he crapped it out, the turtle was six feet tall and had learned karate.
Chuck Norris is not hung like a horse... horses are hung like Chuck Norris.
Faster than a speeding bullet ... more powerful than a locomotive ... able to leap tall buildings in a single bound... yes, these are some of Chuck Norris's warm-up exercises.
Chuck Norris is the only human being to display the Heisenberg uncertainty principle -- you can never know both exactly where and how quickly he will roundhouse-kick you in the face.
In the Bible, Jesus turned water into wine. But then Chuck Norris turned that wine into beer.
Chuck Norris can hit you so hard that he can actually alter your DNA. Decades from now your descendants will occasionally clutch their heads and yell "What The Hell was That?"
Time waits for no man. Unless that man is Chuck Norris.
Chuck Norris discovered a new theory of relativity involving multiple universes in which Chuck Norris is even more badass than in this one. When it was discovered by Albert Einstein and made public, Chuck Norris roundhouse-kicked him in the face. We know Albert Einstein today as Stephen Hawking.
Chuck Norris doesn't shower, he only takes blood baths.
The Chuck Norris military unit was not used in the game Civilization 4, because a single Chuck Norris could defeat the entire combined nations of the world in one turn.
In an average living room there are 1,242 objects Chuck Norris could use to kill you, including the room itself.
According to the Encyclopedia Brittanica, the Native American "Trail of Tears" has been redefined as anywhere that Chuck Norris walks.
Chuck Norris does not teabag the ladies. He potato-sacks them.
Pluto is actually an orbiting group of British soldiers from the American Revolution who entered space after the Chuck gave them a roundhouse kick to the face.
When Chuck Norris goes to donate blood, he declines the syringe, and instead requests a hand gun and a bucket.
There are no steroids in baseball. Just players Chuck Norris has breathed on.
Chuck Norris once challenged Lance Armstrong in a "Who has more testicles?" contest. Chuck Norris won by 5.
Chuck Norris was the fourth wise man, who gave baby Jesus the gift of beard, which he carried with him until he died. The other three wise men were enraged by the preference that Jesus showed to Chuck's gift, and arranged to have him written out of the bible. All three died soon after of mysterious roundhouse-kick related injuries.
Chuck Norris sheds his skin twice a year.
When Chuck Norris calls 1-900 numbers, he doesnt get charged. He holds up the phone and money falls out.
Chuck Norris once ate a whole cake before his friends could tell him there was a stripper in it.
Some people like to eat frogs' legs. Chuck Norris likes to eat lizard legs. Hence, snakes.
There are no races, only countries of people Chuck Norris has beaten to different shades of black and blue.
When Chuck Norris was denied an Egg McMuffin at McDonald's because it was 10:35, he roundhouse kicked the store so hard it became a Wendy's.
Chuck Norris can't finish a "color by numbers" because his markers are filled with the blood of his victims. Unfortunately, all blood is dark red.
A Chuck Norris-delivered Roundhouse Kick is the preferred method of execution in 16 states.
When Chuck Norris falls in water, Chuck Norris doesn't get wet. Water gets Chuck Norris.
Scientists have estimated that the energy given off during the Big Bang is roughly equal to 1CNRhK (Chuck Norris Roundhouse Kick)
Chuck Norris' house has no doors, only walls that he walks through.
When Chuck Norris has sex with a man, it won't be because he is gay. It will be because he has run out of women.
How much wood would a woodchuck chuck if a woodchuck could Chuck Norris? ...All of it.
Chuck Norris doesn't actually write books, the words assemble themselves out of fear.
In honor of Chuck Norris, all McDonald's in Texas have an even larger size than the super-size. When ordering, just ask to be Chucksized. 
Chuck Norris CAN believe it's not butter.
If tapped, a Chuck Norris roundhouse kick could power the country of Australia for 44 minutes.
Chuck Norris can divide by zero.
The grass is always greener on the other side, unless Chuck Norris has been there. In that case the grass is most likely soaked in blood and tears.
A picture is worth a thousand words. A Chuck Norris is worth 1 billion words.
Newton's Third Law is wrong: Although it states that for each action, there is an equal and opposite reaction, there is no force equal in reaction to a Chuck Norris roundhouse kick.
Chuck Norris invented his own type of karate. It's called Chuck-Will-Kill.
When an episode of Walker Texas Ranger was aired in France, the French surrendered to Chuck Norris just to be on the safe side.
While urinating, Chuck Norris is easily capable of welding titanium.
Chuck Norris once sued the Houghton-Mifflin textbook company when it became apparent that their account of the war of 1812 was plagiarized from his autobiography.
When Chuck Norris talks, everybody listens. And dies.
When Steven Seagal kills a ninja, he only takes its hide. When Chuck Norris kills a ninja, he uses every part.
Wilt Chamberlain claims to have slept with more than 20,000 women in his lifetime. Chuck Norris calls this "a slow Tuesday."
Contrary to popular belief, there is indeed enough Chuck Norris to go around.
Chuck Norris doesnt shave; he kicks himself in the face. The only thing that can cut Chuck Norris is Chuck Norris.
For some, the left testicle is larger than the right one. For Chuck Norris, each testicle is larger than the other one.
Chuck Norris always knows the EXACT location of Carmen SanDiego.
When taking the SAT, write "Chuck Norris" for every answer. You will score over 8000.
Chuck Norris invented black. In fact, he invented the entire spectrum of visible light. Except pink. Tom Cruise invented pink.
When you're Chuck Norris, anything + anything is equal to 1. One roundhouse kick to the face.
Chuck Norris has the greatest Poker-Face of all time. He won the 1983 World Series of Poker, despite holding only a Joker, a Get out of Jail Free Monopoloy card, a 2 of clubs, 7 of spades and a green #4 card from the game UNO.
On his birthday, Chuck Norris randomly selects one lucky child to be thrown into the sun.
Nobody doesn't like Sara Lee. Except Chuck Norris.
Chuck Norris doesn't throw up if he drinks too much. Chuck Norris throws down!
In the beginning there was nothing...then Chuck Norris Roundhouse kicked that nothing in the face and said "Get a job". That is the story of the universe.
Chuck Norris has 12 moons. One of those moons is the Earth.
Chuck Norris grinds his coffee with his teeth and boils the water with his own rage.
Archeologists unearthed an old english dictionary dating back to the year 1236. It defined "victim" as "one who has encountered Chuck Norris"
Chuck Norris ordered a Big Mac at Burger King, and got one.
Chuck Norris and Mr. T walked into a bar. The bar was instantly destroyed, as that level of awesome cannot be contained in one building.
If you Google search "Chuck Norris getting his ass kicked" you will generate zero results. It just doesn't happen.
Chuck Norris can drink an entire gallon of milk in thirty-seven seconds.
Little known medical fact: Chuck Norris invented the Caesarean section when he roundhouse-kicked his way out of his monther's womb.
Chuck Norris doesn't bowl strikes, he just knocks down one pin and the other nine faint.
The show Survivor had the original premise of putting people on an island with Chuck Norris. There were no survivors, and nobody is brave enough to go to the island to retrieve the footage.
It takes Chuck Norris 20 minutes to watch 60 Minutes.
You know how they say if you die in your dream then you will die in real life? In actuality, if you dream of death then Chuck Norris will find you and kill you.
Chuck Norris has a deep and abiding respect for human life... unless it gets in his way.
The Bermuda Triangle used to be the Bermuda Square, until Chuck Norris Roundhouse kicked one of the corners off.
There are no weapons of mass destruction in Iraq, Chuck Norris lives in Oklahoma.
Chuck Norris doesn't believe in Germany.
When Chuck Norris is in a crowded area, he doesn't walk around people. He walks through them.
Chuck Norris once ate an entire bottle of sleeping pills. They made him blink.
James Cameron wanted Chuck Norris to play the Terminator. However, upon reflection, he realized that would have turned his movie into a documentary, so he went with Arnold Schwarzenegger.
Chuck Norris can touch MC Hammer.
Thousands of years ago Chuck Norris came across a bear. It was so terrified that it fled north into the arctic. It was also so terrified that all of its decendents now have white hair.
Chuck Norris played Russian Roulette with a fully loaded gun and won.
It takes 14 puppeteers to make Chuck Norris smile, but only 2 to make him destroy an orphanage.</ul>
Chuck Norris is responsible for China's over-population. He hosted a Karate tournament in Beijing and all women within 1,000 miles became pregnant instantly.
Some people wear Superman pajamas. Superman wears Chuck Norris pajamas.
Chuck Norris once worked as a weatherman for the San Diego evening news. Every night he would make the same forecast: Partly cloudy with a 75% chance of Pain.
Simply by pulling on both ends, Chuck Norris can stretch diamonds back into coal.
When Chuck Norris does a pushup, he isn't lifting himself up, he's pushing the Earth down.
Chuck Norris invented the bolt-action rifle, liquor, sexual intercourse, and football-- in that order.
A high tide means Chuck Norris is flying over your coast. The tide is caused by God pissing his pants.
Chuck Norris keeps his friends close and his enemies closer. Close enough to drop them with one round house kick to the face.
There is in fact an "I" in Norris, but there is no "team" ...  not even close.
Scotty in Star Trek often says "Ye cannae change the laws of physics." This is untrue. Chuck Norris can change the laws of physics. With his fists.
An anagram for Walker Texas Ranger is KARATE WRANGLER SEX. I don't know what that is, but it sounds AWESOME.
Chuck Norris doesn't stub his toes. He accidentally destroys chairs, bedframes, and sidewalks.
Using his trademark roundhouse kick, Chuck Norris once made a fieldgoal in RJ Stadium in Tampa Bay from the 50 yard line of Qualcomm stadium in San Diego.
Chuck Norris roundhouse kicks don't really kill people. They wipe out their entire existence from the space-time continuum.
Chuck Norris does not own a stove, oven, or microwave , because revenge is a dish best served cold.
Tom Clancy has to pay royalties to Chuck Norris because "The Sum of All Fears" is the name of Chuck Norris' autobiography.
Chuck Norris can slam a revolving door.
Chuck Norris is expected to win gold in every swimming competition at the 2008 Beijing Olympics, even though Chuck Norris does not swim. This is because when Chuck Norris enters the water, the water gets out of his way and Chuck Norris simply walks across the pool floor.
Chuck Norris built a better mousetrap, but the world was too frightened to beat a path to his door.
The original draft of The Lord of the Rings featured Chuck Norris instead of Frodo Baggins. It was only 5 pages long, as Chuck roundhouse-kicked Sauron's ass halfway through the first chapter.
Hellen Keller's favorite color is Chuck Norris.
Chuck Norris eats beef jerky and craps gunpowder. Then, he uses that gunpowder to make a bullet, which he uses to kill a cow and make more beef jerky. Some people refer to this as the "Circle of Life."
If, by some incredible space-time paradox, Chuck Norris would ever fight himself, he'd win. Period.
Chuck Norris is currently suing myspace for taking the name of what he calls everything around you.
The crossing lights in Chuck Norris's home town say "Die slowly" and "die quickly". They each have a picture of Chuck Norris punching or kicking a pedestrian.
Science Fact: Roundhouse kicks are comprised primarily of an element called Chucktanium.
The Sherman tank was originaly called the Norris tank until Chuck Norris decided it wasn't tough enough to be associated with him. The Army, for fear of Chuck Norris, renamed the tank and promised to develop a weapon more fitting of his name. To date, no weapon created has been badass enough to be named after Chuck Norris.
Chuck Norris proved that we are alone in the universe. We weren't before his first space expedition.
Superman once watched an episode of Walker, Texas Ranger. He then cried himself to sleep.
Chuck Norris doesn't step on toes. Chuck Norris steps on necks.
The movie "Delta Force" was extremely hard to make because Chuck had to downplay his abilities. The first few cuts were completely unbelievable.
Movie trivia: The movie "Invasion U.S.A." is, in fact, a documentary.
Chuck Norris does not "style" his hair. It lays perfectly in place out of sheer terror.
There is no such thing as global warming. Chuck Norris was cold, so he turned the sun up.
A study showed the leading causes of death in the United States are: 1. Heart disease, 2. Chuck Norris, 3. Cancer
It's widely believed that Jesus was Chuck Norris' stunt double for crucifixion due to the fact that it is impossible for nails to pierce Chuck Norris' skin.
Chuck Norris did in fact, build Rome in a day.
Along with his black belt, Chuck Norris often chooses to wear brown shoes. No one has DARED call him on it. Ever.
Anytime someone is elected president in the United States, they must ask permission from Chuck Norris to live in the White House. The reason for this is because Chuck Norris had won every Federal, State, and Local election since 1777. He just allows others to run the country in his place.
Once you go Norris, you are physically unable to go back.
Ninjas want to grow up to be just like Chuck Norris. But usually they grow up just to be killed by Chuck Norris.
Chuck Norris once sued Burger King after they refused to put razor wire in his Whopper Jr, insisting that that actually is "his" way.
The last thing you hear before Chuck Norris gives you a roundhouse kick? No one knows because dead men tell no tales.
Chuck Norris doesn't play god. Playing is for children.
As a teen, Chuck Norris had sex with every nun in a convent tucked away in the hills of Tuscany. Nine months later the nuns gave birth to the 1972 Miami Dolphins, the only undefeated and untied team in professional football history.
Chuck Norris is the only person in the world that can actually email a roundhouse kick.
Chuck Norris won super bowls VII and VIII singlehandedly before unexpectedly retiring to pursue a career in ass-kicking.
Wo hu cang long. The translation from Mandarin Chinese reads: "Crouching Chuck, Hidden Norris"
Chuck Norris can set ants on fire with a magnifying glass. At night.
Some kids play Kick the can. Chuck Norris played Kick the keg.
'Icy-Hot' is too weak for Chuck Norris. After a workout, Chuck Norris rubs his muscles down with liquid-hot MAGMA.
Chuck Norris cannot love, he can only not kill.
When Chuck Norris was a baby, he didn't suck his mother's breast. His mother served him whiskey, straight out of the bottle.
According to Einstein's theory of relativity, Chuck Norris can actually roundhouse kick you yesterday.
Chuck Norris once pulled out a single hair from his beard and skewered three men through the heart with it.
In an act of great philanthropy, Chuck made a generous donation to the American Cancer Society. He donated 6,000 dead bodies for scientific research.
Chuck Norris' favourite cut of meat is the roundhouse.
When J. Robert Oppenheimer said "I am become death, the destroyer Of worlds", He was not referring to the atomic bomb. He was referring to the Chuck Norris halloween costume he was wearing.
Chuck Norris recently had the idea to sell his urine as a canned beverage. We know this beverage as Red Bull.
In a recent survey it was discovered the 94% of American women lost their virginity to Chuck Norris. The other 6% were incredibly fat or ugly.
Chuck Norris invented a language that incorporates karate and roundhouse kicks. So next time Chuck Norris is kicking your ass, don't be offended or hurt, he may be just trying to tell you he likes your hat.
If at first you don't succeed, you're not Chuck Norris.
If Chuck Norris were a calendar, every month would be named Chucktober, and every day he'd kick your ass.
Fear is not the only emotion Chuck Norris can smell. He can also detect hope, as in "I hope I don't get a roundhouse kick from Chuck Norris."
Chuck Norris's show is called Walker: Texas Ranger, because Chuck Norris doesn't run.
MacGyver can build an airplane out of gum and paper clips, but Chuck Norris can roundhouse-kick his head through a wall and take it.
Behind every successful man, there is a woman. Behind every dead man, there is Chuck Norris.
What's known as the UFC, or Ultimate Fighting Championship, doesn't use its full name, which happens to be "Ultimate Fighting Championship, Non-Chuck-Norris-Division".
Chuck Norris brushes his teeth with a mixture of iron shavings, industrial paint remover, and wood-grain alcohol.
The easiest way to determine Chuck Norris' age is to cut him in half and count the rings.
There is endless debate about the existence of the human soul. Well it does exist, and Chuck Norris finds it delicious.
Most boots are made for walkin'. Chuck Norris' boots ain't that merciful.
The US did not boycott the 1980 Summer Olympics in Moscow due to political reasons: Chuck Norris killed the entire US team with a single round-house kick during TaeKwonDo practice.
Chuck Norris wears a live rattlesnake as a condom.
The Bible was originally titled "Chuck Norris and Friends"
Chuck Norris began selling the Total Gym as an ill-fated attempt to make his day-to-day opponents less laughably pathetic.
Do you know why Baskin Robbins only has 31 flavors? Because Chuck Norris doesn't like Fudge Ripple.
When Chuck Norris says "More cowbell", he  MEANS it.
On the set of Walker Texas Ranger Chuck Norris brought a dying lamb back to life by nuzzling it with his beard. As the onlookers gathered, the lamb sprang to life. Chuck Norris then roundhouse kicked it, killing it instantly. This was just to prove that the good Chuck giveth, and the good Chuck, he taketh away.
Chuck Norris was what Willis was talkin' about.
Google won't search for Chuck Norris because it knows you don't find Chuck Norris, he finds you.
Chuck Norris can lead a horse to water AND make it drink.
Nagasaki never had a bomb dropped on it. Chuck Norris jumped out of a plane and punched the ground.
It is scientifically impossible for Chuck Norris to have had a mortal father. The most popular theory is that he went back in time and fathered himself.
Chuck Norris destroyed the periodic table, because Chuck Norris only recognizes the element of surprise.
It is believed dinosaurs are extinct due to a giant meteor. That's true if you want to call Chuck Norris a giant meteor.
Chuck Norris shot the sheriff, but he round house kicked the deputy.
That's not Chuck Norris doing push-ups -- that's Chuck Norris moving the Earth away from the path of a deadly asteroid.
Chuck Norris can judge a book by its cover.
Nothing can escape the gravity of a black hole, except for Chuck Norris. Chuck Norris eats black holes. They taste like chicken.
Chuck Norris does not play the lottery. It doesn't have nearly enough balls.
Q: How many Chuck Norris' does it take to change a light bulb? A: None, Chuck Norris prefers to kill in the dark.
As President Roosevelt said: "We have nothing to fear but fear itself. And Chuck Norris."
Chuck Norris just says "no" to drugs. If he said "yes", it would collapse Colombia's infrastructure.
Since 1940, the year Chuck Norris was born, roundhouse-kick related deaths have increased 13,000 percent.
Crime does not pay - unless you are an undertaker following Walker, Texas Ranger, on a routine patrol.
Chuck Norris invented the internet ...  just so he had a place to store his porn.
Chuck Norris does not own a house. He walks into random houses and people move.
It is better to give than to receive. This is especially true of a Chuck Norris roundhouse kick.
Chuck Norris is the only person to ever win a staring contest against Ray Charles and Stevie Wonder at the same time.
Industrial logging isn't the cause of deforestation. Chuck Norris needs toothpicks.
Chuck Norris smells what the Rock is cooking... because the Rock is Chuck Norris' personal chef.
When Chuck Norris plays Oregon Trail, his family does not die from cholera or dysentery, but rather, roundhouse kicks to the face. He also requires no wagon, since he carries the oxen, axels, and buffalo meat on his back. He always makes it to Oregon before you.
Chuck Norris is the reason why Waldo is hiding.
"Brokeback Mountain" is not just a movie. It's also what Chuck Norris calls the pile of dead ninjas in his front yard.
When God said, "let there be light", Chuck Norris said, "say 'please'."
Chuck Norris does not eat. Food understands that the only safe haven from Chuck Norris' fists is inside his own body.
One day Chuck Norris walked down the street with a massive erection. There were no survivors.
Chuck Norris built a time machine and went back in time to stop the JFK assassination. As Oswald shot, Chuck met all three bullets with his beard, deflecting them. JFK's head exploded out of sheer amazement.
Chuck Norris doesn't read books. He stares them down until he gets the information he wants.
Chuck Norris uses a night light. Not because Chuck Norris is afraid of the dark, but the dark is afraid of Chuck Norris.
Chuck Norris is not capable of hitting a target on the broad side of a barn. Every time he tries, the whole damn barn falls down.
Before each filming of Walker: Texas Ranger, Chuck Norris is injected with fourteen times the lethal dose of elephant tranquilzer. This is, of course, to limit his strength and mobility, in an attempt to lower the fatality rate of the actors he fights.
When Bruce Banner gets mad, he turns into the Hulk. When the Hulk gets mad, he turns into Chuck Norris.
Chuck Norris kills anyone that asks, "You want fries with that" because by now everyone should know that Chuck doesn't ever want fries with anything. Ever.
Chuck Norris once kicked a horse in the chin. Its decendants are known today as Giraffes.
Sticks and stones may break your bones, but a Chuck Norris glare will liquefy your kidneys.
Human cloning is outlawed because if Chuck Norris were cloned, then it would be possible for a Chuck Norris roundhouse kick to meet another chuck Norris roundhouse kick. Physicists theorize that this contact would end the universe.
Chuck Norris once went skydiving, but promised never to do it again. One Grand Canyon is enough.
Chuck Norris's version of a "chocolate milkshake" is a raw porterhouse wrapped around ten Hershey bars, and doused in diesel fuel.
If Chuck Norris round-house kicks you, you will die. If Chuck Norris' misses you with the round-house kick, the wind behind the kick will tear out your pancreas.
In a fight between Batman and Darth Vader, the winner would be Chuck Norris.
Chuck Norris puts his pants on one leg at a time, just like the rest of us. The only difference is, then he kills people.
Everybody loves Raymond. Except Chuck Norris.
Contrary to popular belief, the Titanic didn't hit an iceberg. The ship was off course and accidentally ran into Chuck Norris while he was doing the backstroke across the Atlantic.
Chuck Norris got his drivers license at the age of 16. Seconds.
The original title for Alien vs. Predator was Alien and Predator vs Chuck Norris. The film was cancelled shortly after going into preproduction. No one would pay nine dollars to see a movie fourteen seconds long.
Chuck Norris' sperm is so badass, he had sex with Nicole Kidman, and 7 months later she prematurely gave birth to a Ford Excursion.
Chuck Norris can win at solitaire with only 18 cards.
Chuck Norris once shat blood - the blood of 11,940 natives he had killed and eaten.
Maslow's theory of higher needs does not apply to Chuck Norris. He only has two needs: killing people and finding people to kill.
The truth will set you free. Unless Chuck Norris has you, in which case, forget it buddy!
For most people, home is where the heart is. For Chuck Norris, home is where he stores his collection of human skulls.
Kryptonite has been found to contain trace elements of Chuck Norris roundhouse kicks to the face. This is why it is so deadly to Superman.
Saddam Hussein was not found hiding in a "hole." Saddam was roundhouse-kicked in the head by Chuck Norris in Kansas, which sent him through the earth, stopping just short of the surface of Iraq.
Coroners refer to dead people as "ABC's". Already Been Chucked.
Chuck Norris doesn't look both ways before he crosses the street... he just roundhouses any cars that get too close.
Chuck Norris does not have to answer the phone. His beard picks up the incoming electrical impulses and translates them into audible sound.
How many roundhouse kicks does it take to get to the center of a tootsie pop? Just one. From Chuck Norris.
Chuck Norris doesnt wear a watch, HE decides what time it is.
The phrase 'break a leg' was originally coined by Chuck Norris's co-stars in Walker, Texas Ranger as a good luck charm, indicating that a broken leg might be the worst extent of their injuries. This never proved to be the case.
When chuck Norris does division, there are no remainders.
If you rearrange the letters in "Chuck Norris", they also spell "Crush Rock In". The words "with his fists" are understood.
Never look a gift Chuck Norris in the mouth, because he will bite your damn eyes off.
Give a man a fish, and you will feed him for a day. Give a man anything that is better than a fish, and Chuck Norris will beat his ass and take it.
Chuck Norris used to play baseball. When Babe Ruth was hailed as the better player, Chuck Norris killed him with a baseball bat to the throat. Lou Gehrig got off easy.
The original title for Star Wars was "Skywalker: Texas Ranger". Starring Chuck Norris.
Guantuanamo Bay, Cuba, is the military code-word for "Chuck Norris' basement".
The phrase 'balls to the wall' was originally conceived to describe Chuck Norris entering any building smaller than an aircraft hangar.
Chuck Norris' roundhouse kick is so powerful, it can be seen from outer space by the naked eye.
Ozzy Osbourne bites the heads off of bats. Chuck Norris bites the heads off of Siberian Tigers.
He who lives by the sword, dies by the sword. He who lives by Chuck Norris, dies by the roundhouse kick.
The best-laid plans of mice and men often go awry. Even the worst-laid plans of Chuck Norris come off without a hitch.
The phrase 'dead ringer' refers to someone who sits behind Chuck Norris in a movie theater and forgets to turn their cell phone off.
Chuck Norris' Roundhouse kick is so powerful, that on the set of Sidekicks he single-footedly destroyed Jonathan Brandis' Career.
Staring at Chuck Norris for extended periods of time without proper eye protection will cause blindess, and possibly foot sized brusies on the face.
Chuck Norris can taste lies.
Chuck Norris does not kick ass and take names. In fact, Chuck Norris kicks ass and assigns the corpse a number. It is currently recorded to be in the billions.
One time, Chuck Norris accidentally stubbed his toe. It destroyed the entire state of Ohio.
Little Miss Muffet sat on her tuffet, until Chuck Norris roundhouse kicked her into a glacier.
In 1990, Chuck Norris founded the non-profit organization "Kick Drugs Out of America". If the organization's name were "Roundhouse Kick Drugs out of America", there wouldn't be any drugs in the Western Hemisphere. Anywhere.
Chuck Norris can blow bubbles with beef jerky.
They had to edit the first ending of 'Lone Wolf McQuade' after Chuck Norris kicked David Carradine's ass, then proceeded to barbecue and eat him.
Chuck Norris does, in fact, live in a round house.
Chuck Norris was once on Jeopardy. This show is notable in that it was the first occasion in Jeopardy history that Alex Trebek had appeared without a mustache. And a head.
When Chuck Norris works out on the Total Gym, the Total Gym feels like it's been raped.
4 out of 5 doctors fail to recommend Chuck Norris as a solution to most problems. Also, 80% of doctors die unexplained, needlessly brutal deaths.
Chuck Norris can skeletize a cow in two minutes.
The only sure things are Death and Taxes ... and when Chuck Norris goes to work for the IRS, they'll be the same thing.
Chuck Norris' first job was as a paperboy. There were no survivors.
With the rising cost of gasoline, Chuck Norris is beginning to worry about his drinking habit.
The square root of Chuck Norris is pain. Do not try to square Chuck Norris, the result is death.
chuck Norris' testicles do not produce sperm. They produce tiny white ninjas that recognize only one mission: seek and destroy.
To be or not to be? That is the question. The answer? Chuck Norris.
Chuck Norris has never been in a fight, ever. Do you call one roundhouse kick to the face a fight?
There are two types of people in the world... people that suck, and Chuck Norris.
Chuck Norris never wet his bed as a child. The bed wet itself out of fear.
If you were somehow able to land a punch on Chuck Norris your entire arm would shatter upon impact. This is only in theory, since, come on, who in their right mind would try this?
70% of a human's weight is water. 70% of Chuck Norris' weight is his dick.
Jean-Claude Van Damme once kicked Chuck Norris' ass. He was then awakened from his dream by a roundhouse kick to the face.
The pie scene in "American Pie" is based on a dare Chuck Norris took when he was younger. However, in Chuck Norris' case, the "pie" was the molten crater of an active volcano.
Chuck Norris uses 8'x10' sheets of plywood as toilet paper.
Noah was the only man notified before Chuck Norris relieved himself in the Atlantic Ocean.
Chuck Norris once invited all of the other badasses from TV to duke it out in order to see who was the supreme badass. Only two showed up-- Jack Bauer and MacGyver.
MacGyver immediately tried to make a bomb out of some Q-Tips and Gatorade, but Chuck Norris roundhouse-kicked him in the solar plexus. MacGyver promptly threw up his own heart.
Jack Bauer tried to use his detailed knowledge of torture techniques, but to no avail: Chuck Norris thrives on pain. Chuck Norris then ripped off Jack Bauer's arm and beat him to death with it. Game, set, match.
Chuck Norris eats steak for every single meal. Most times he forgets to kill the cow.
The First Law of Thermodynamics states that energy can neither be created nor destroyed... unless it meets Chuck Norris.
Chuck Norris doesn't go on the internet, he has every internet site stored in his memory. He refreshes webpages by blinking.
Fact: Chuck Norris doesn't consider it sex if the woman survives.
It is said that looking into Chuck Norris' eyes will reveal your future. Unfortunately, everybody's future is always the same: death by a roundhouse-kick to the face.
Chuck Norris knows everything there is to know - Except for the definition of mercy.
Scientifically speaking, it is impossible to charge Chuck Norris with "obstruction of justice." This is because even Chuck Norris cannot be in two places at the same time.
Chuck Norris never has to wax his skis because they're always slick with blood.
When you say "no one's perfect", Chuck Norris takes this as a personal insult.
Chuck Norris can win a game of Trivial Pursuit with one roll of the dice, and without answering a single question... just a nod of the head, and a stroke of the beard.
182,000 Americans die from Chuck Norris-related accidents every year.
Paper beats rock, rock beats scissors, and scissors beats paper, but Chuck Norris beats all 3 at the same time.
Jesus can walk on water, but Chuck Norris can walk on Jesus.
All roads lead to Chuck Norris. And by the transitive property, a roundhouse kick to the face.
If you're driving down the road and you think Chuck Norris just cut you off, you better thank your lucky stars it wasn't the other way around.
July 4th is Independence day. And the day Chuck Norris was born. Coincidence? i think not.
Chuck Norris never goes to the dentist because his teeth are unbreakable. His enemies never go to the dentist because they have no teeth.
In the medical community, death is referred to as "Chuck Norris Disease"
Chuck Norris was once in a knife fight, and the knife lost.
If you work in an office with Chuck Norris, don't ask him for his three-hole-punch.
In the Words of Julius Caesar, "Veni, Vidi, Vici, Chuck Norris". Translation: I came, I saw, and I was roundhouse-kicked inthe face by Chuck Norris.
The First rule of Chuck Norris is: you do not talk about Chuck Norris.
Chuck Norris is widely predicted to be first black president. If you're thinking to yourself, "But Chuck Norris isn't black", then you are dead wrong. And stop being a racist.
When Chuck Norris plays Monopoly, it affects the actual world economy.
Chuck Norris can be unlocked on the hardest level of Tekken. But only Chuck Norris is skilled enough to unlock himself. Then he roundhouse kicks the Playstation back to Japan.
Chuck Norris drinks napalm to quell his heartburn.
Every time someone uses the word "intense", Chuck Norris always replies "you know what else is intense?" followed by a roundhouse kick to the face.
As an infant, Chuck Norris' parents gave him a toy hammer. He gave the world Stonehenge.
Chuck Norris once ordered a steak in a restaurant. The steak did what it was told.
Most people fear the Reaper. Chuck Norris considers him "a promising Rookie".
There are only two things that can cut diamonds: other diamonds, and Chuck Norris.
President Roosevelt once rode his horse 100 miles. Chuck Norris carried his the same distance in half the time.
Chuck Norris once ate four 30lb bowling balls without chewing.
What many people dont know is chuck norris is the founder of planned parenthood. Not even unborn children can escape his wrath.
Chuck Norris was banned from competitive bullriding after a 1992 exhibition in San Antonio, when he rode the bull 1,346 miles from Texas to Milwaukee Wisconsin to pick up his dry cleaning.
Chuck Norris qualified with a top speed of 324 mph at the Daytona 500, without a car.
Chuck Norris likes his coffee half and half: half coffee grounds, half wood-grain alcohol.
Chuck Norris uses tabasco sauce instead of visine.
The chemical formula for the highly toxic cyanide ion is CN-. These are also Chuck Norris' initials. This is not a coincidence.
Chuck Norris' credit cards have no limit. Last weekend, he maxed them out.
Think of a hot woman. Chuck Norris did her.
A man once claimed Chuck Norris kicked his ass twice, but it was promptly dismissed as false - no one could survive it the first time.
Chuck Norris sleeps with a pillow under his gun.
Chuck Norris owns a chain of fast-food restaurants throughout the southwest. They serve nothing but barbecue-flavored ice cream and Hot Pockets.
Chuck Norris doesn't chew gum. Chuck Norris chews tin foil.
Aliens DO indeed exist. They just know better than to visit a planet that Chuck Norris is on.
When in a bar, you can order a drink called a "Chuck Norris". It is also known as a "Bloody Mary", if your name happens to be Mary.
Every time Chuck Norris smiles, someone dies. Unless he smiles while he's roundhouse kicking someone in the face. Then two people die.
Some people ask for a Kleenex when they sneeze, Chuck Norris asks for a body bag.
There's an order to the universe: space, time, Chuck Norris.... Just kidding, Chuck Norris is first.
A man once asked Chuck Norris if his real name is "Charles". Chuck Norris did not respond, he simply stared at him until he exploded.
Chuck Norris starts everyday with a protein shake made from Carnation Instant Breakfast, one dozen eggs, pure Colombian cocaine, and rattlesnake venom. He injects it directly into his neck with a syringe.
In a tagteam match, Chuck Norris was teamed with Hulk Hogan against King Kong Bundy and Andre The Giant. He pinned all 3 at the same time.
Chuck Norris doesn't see dead people. He makes people dead.
Chuck Norris is the only person who can simultaneously hold and fire FIVE Uzis: One in each hand, one in each foot -- and the 5th one he roundhouse-kicks into the air, so that it sprays bullets.
For undercover police work, Chuck Norris pins his badge underneath his shirt, directly into his chest.
In the X-Men movies, none of the X-Men super-powers are done with special effects. Chuck Norris is the stuntman for every character.
We live in an expanding universe. All of it is trying to get away from Chuck Norris.
It is said that every time you masturbate, God kills a kitten. Every time God masturbates, Chuck Norris kills a lion.
The word 'Kill' was invented by Chuck Norris. Other words were 'Die', 'Beer', and 'What'.
Chuck Norris is a vegetarian. Meaning, he does not eat animals until first he puts them into vegetative state with his fists.
The 11th commandment is "Thou shalt not piss off Chuck Norris" This commandment is rarely enforced, as it is impossible to accomplish.
Chuck Norris is his own line at the DMV.
Two wrongs don't make a right. Unless you're Chuck Norris. Then two wrongs make a roundhouse kick to the face.
Who let the dogs out? Chuck Norris let the dogs out... and then roundhouse kicked them through an Oldsmobile.
Chuck Norris can do a roundhouse kick faster than the speed of light. This means that if you turn on a light switch, you will be dead before the lightbulb turns on.
When Chuck Norris goes to out to eat, he orders a whole chicken, but he only eats its soul.
Chuck Norris sold his soul to the devil for his rugged good looks and unparalleled martial arts ability. Shortly after the transaction was finalized, Chuck roundhouse-kicked the devil in the face and took his soul back. The devil, who appreciates irony, couldn't stay mad and admitted he should have seen it coming. They now play poker every second Wednesday of the month.
Chuck Norris has never won an Academy Award for acting... because he's not acting.
If Chuck Norris wants your opinion, he'll beat it into you.
Not everyone that Chuck Norris is mad at gets killed. Some get away. They are called astronauts.
Chuck Norris has to register every part of his body as a separate lethal weapon. His spleen is considered a concealed weapon in over 50 states.
A movie scene depicting Chuck Norris losing a fight with Bruce Lee was the product of history's most expensive visual effect. When adjusted for inflation, the effect cost more than the Gross National Product of Paraguay.
Godzilla is a Japanese rendition of Chuck Norris' first visit to Tokyo.
They once made a Chuck Norris toilet paper, but there was a problem-- It wouldn't take shit from anybody.
Chuck Norris once rode a nine foot grizzly bear through an automatic car wash, instead of taking a shower.
"Sweating bullets" is literally what happens when Chuck Norris gets too hot.
Chuck Norris' sperm can be seen with the naked eye. Each one is the size of a quarter.
After taking a steroids test doctors informed Chuck Norris that he had tested positive. He laughed upon receiving this information, and said "of course my urine tested positive, what do you think they make steroids from?"
Chuck Norris doesn't daydream. He's too busy giving other people nightmares.
When Arnold says the line "I'll be back" in the first Terminator movie it is implied that is he going to ask Chuck Norris for help.
There are no such things as tornados. Chuck Norris just hates trailer parks.
Chuck Norris' Penis is a third degree blackbelt, and an honorable 32nd-degree mason.
Chuck Norris does not follow fashion trends, they follow him. But then he turns around and kicks their ass. Nobody follows Chuck Norris.
The phrase 'break a leg' was originally coined by Chuck Norris's co-stars in Walker, Texas Ranger as a good luck charm indicating that a broken leg might be the worst extent of their injuries. This never proved to be the case.
Chuck Norris' roundhouse kick is so powerful, it can be seen from outer space by the naked eye.
Diamonds are not, despite popular belief, carbon. They are, in fact, Chuck Norris fecal matter. This was proven a recently, when scientific analysis revealed what appeared to be Jean-Claude Van Damme bone fragments inside the Hope Diamond.
Chuck Norris once participated in the running of the bulls. He walked.
The Drummer for Def Leppard's only got one arm. Chuck Norris needed a back scratcher.
Chuck Norris was the orginal sculptor of Mount Rushmore. He completed the entire project using only a bottle opener and a drywall trowel.
Chuck Norris once rode a bull, and nine months later it had a calf.
Chuck Norris once lost the remote, but maintained control of the TV by yelling at it in between bites of his "Filet of Child" sandwich.
For Spring Break '05, Chuck Norris drove to Madagascar, riding a chariot pulled by two electric eels.
The Manhattan Project was not intended to create nuclear weapons, it was meant to recreate the destructive power in a Chuck Norris Roundhouse Kick. They didn't even come close.
Chuck Norris has banned rainbows from the state of North Dakota.
Divide Chuck Norris by zero and you will in fact get one........one bad-ass  that is.
TNT was originally developed by Chuck Norris to cure indigestion.
After returning from World War 2 unscathed, Bob Dole was congratulated by Chuck Norris with a handshake. The rest is history.
Chuck Norris runs on batteries. Specifically, Die Hards.
"Let the Bodies Hit the Floor" was originally written as Chuck Norris' theme song.
Chuck Norris will never have a heart attack. His heart isn't nearly foolish enough to attack him.
Only Chuck Norris can prevent forest fires.
When Chuck Norris makes a burrito, its main ingredient is real toes.
Chuck Norris is not Irish. His hair is soaked in the blood of his victims.
In the movie "The Matrix", Chuck Norris is the Matrix. If you pay close attention in the green "falling code" scenes, you can make out the faint texture of his beard.
Chuck Norris' dick is so big, it has it's own dick, and that dick is still bigger than yours.
They say curiosity killed the cat. This is false. Chuck Norris killed the cat. Every single one of them.
There is no such thing as a lesbian, just a woman who has never met Chuck Norris.
Chuck Norris crossed the road. No one has ever dared question his motives.
When Chuck Norris was born, he immediately had sex with the first nurse he saw. He was her first. She was his third. That afternoon.
One time, at band camp, Chuck Norris ate a percussionist.
Chuck Norris doesn't say "who's your daddy", because he knows the answer.
Chuck Norris originally wrote the first dictionary. The definition for each word is as follows - A swift roundhouse kick to the face.
Love does not hurt. Chuck Norris does.
The term "Cleveland Steamer" got its name from Chuck Norris, when he took a dump while visiting the Rock and Roll Hall of fame and buried northern Ohio under a glacier of fecal matter.
Chuck Norris once round-house kicked a salesman. Over the phone.
The pen is mighter than the sword, but only if the pen is held by Chuck Norris.
Chuck Norris doesn't kill two birds with one stone. Chuck Norris kills all birds, with two stones. The ones in his pants.
Chuck Norris knows the last digit of pi.
Those aren't credits that roll after Walker Texas Ranger. It is actually a list of fatalities that occurred during the making of the episode.
The air around Chuck Norris is always a balmy 78 degrees.
When Chuck Norris wants an egg, he cracks open a chicken.
Chuck Norris plays racquetball with a waffle iron and a bowling ball.
According to the Bible, God created the universe in six days. Before that, Chuck Norris created God by snapping his fingers.
Chuck Norris doesn't believe in ravioli. He stuffs a live turtle with beef and smothers it in pig's blood.
Count from one to ten. That's how long it would take Chuck Norris to kill you...Fourty seven times.
The 1972 Miami Dolphins lost one game, it was an exhibition game vs. Chuck Norris and three seven year old girls. Chuck Norris won with a roundhouse-kick to the face in overtime.
Chuck Norris is not Politically Correct. He is just Correct. Always.
Mr. T pities the fool. Chuck Norris rips the fool's  head off.
Chuck Norris had to stop washing his clothes in the ocean. The tsunamis were killing people.
Chuck Norris has volunteered to remain on earth after the Rapture; he will spend his time fighting the Anti-Christ.
They were going to release a Chuck Norris edition of Clue, but the answer always turns out to be "Chuck Norris. In The Library. With a Roundhouse Kick."
Chuck Norris is the only known mammal in history to have an opposable thumb. On his penis.
A man once taunted Chuck Norris with a bag of Lay's potato chips, saying "Betcha can't eat just one!" Chuck Norris proceeded to eat the chips, the bag, and the man in one deft move.
Chuck Norris' favorite cereal is Kellogg's Nails 'N' Gravel.
In the first Jurassic Park movie, the Tyrannosaurus Rex wasn't chasing the jeep. Chuck Norris was chasing the Tyrannosaurus AND the jeep.
Chuck Norris has never been accused of murder for the simple fact that his roundhouse kicks are recognized world-wide as "acts of God."
"Brokeback Mountain" is not just a movie. It's also what Chuck Norris calls the pile of dead ninjas in his front yard.
Chuck Norris does not wear a condom. Because there is no such thing as protection from Chuck Norris.
Chuck Norris once had sex with a cigarette machine in the Osaka airport.
Rules of fighting: 1) Don't bring a knife to a gun fight. 2) Don't bring a gun to a Chuck Norris fight.
Chuck Norris is the only man who has, literally, beaten the odds. With his fists.
In ancient China there is a legend that one day a child will be born from a dragon, grow to be a man, and vanquish evil from the land. That man is not Chuck Norris, because Chuck Norris killed that man.
Chuck Norris wipes his ass with chain mail and sandpaper.
When you play Monopoly with Chuck Norris, you do not pass go, and you do not collect two hundred dollars. You will be lucky if you make it out alive.
Chuck Norris describes human beings as "a sociable holder for blood and guts".
Chuck Norris once got into a fight with a one-armed Ninja. Seeing that he had an unfair advantage, Chuck Norris ripped both of his arms off and one of his legs. He then roundhouse-kicked the ninja in the head, killing him instantly, and proceeded to sow his limbs back on using only a rusty tent spike and bailing wire.
Chuck Norris likes his ice like he likes his skulls: crushed.
Chuck Norris can kick through all 6 degrees of separation, hitting anyone, anywhere, in the face, at any time.
Most tough men eat nails for breakfast. chuck Norris does all of his grocery shopping at Home Depot.
Chuck Norris did not "lose" his virginity, he stalked it and then destroyed it with extreme prejudice.
Everything King Midas touches turnes to gold. Everything Chuck Norris touches turns up dead.
Chuck Norris' pulse is measured on the richter scale.
Most people know that Descarte said, "I think, therefore I am." What most people don't know is that that quote continues, "...afraid of Chuck Norris."
Chuck Norris once roundhouse-kicked a ten dollar bill into 200 nickels.
For every movie about Vietnam starring Chuck Norris, the historical duration of the war decreases. Just 3 more "Missing in Action" sequels, and that war will have never actually existed.
Chuck Norris' penis has a Hemi.
Chuck Norris enjoys a good practical joke. His favorite is where he removes your lower intestine and pretends to make a balloon animal out of it. Then he cracks your skull open with a Volvo for not complimenting him on his balloon animal.
Chuck Norris CAN in fact 'raise the roof'. And he can do it with one hand.
Kenny G is allowed to live because Chuck Norris doesn't kill women.
Life is not, in fact, like a box of chocolates. It is more like a box of Chuck Norris, roundhouse kicking you in the face. And if you receive a box of Chuck Norris, you ALWAYS know what you are going to get.
For Chuck Norris, every street is "one way". HIS WAY.
There are now five cup sizes at Starbucks: Short, Tall, Grande, Venti, and Chuck Norris.
During the Vietnam War, Chuck Norris allowed himself to be captured. For torture, they made him eat his own entrails. He asked for seconds.
Chuck Norris once created a flamethrower by urinating into a lighter.
Instead of having a cigarette after sex, Chuck Norris heads outside and brands his cattle.
Chuck Norris actually built the stairway to heaven.
Whoever said "only the good die young" was probably in Chuck Norris's kindergarten class.
Chuck Norris once skewered a man with the Eiffel tower.
The best part of waking up, is not Folgers in your cup, but knowing that Chuck Norris didn't kill you in your sleep.
Chuck Norris doesn't own a can opener, he just chews through the can.
Occam's Razor says that the simplest answer tends to be the correct one. Norris' Razor involves a flick of the wrist and a Columbian Necktie.
Chuck Norris needs a monkeywrench and a blowtorch to masturbate.
Proponents of higher-order theories of consciousness argue that consciousness is explained by the relation between two levels of mental states in which a higher-order mental state takes another mental state. If you mention this to Chuck Norris, expect an explosive roundhouse kick to the face for spouting too much fancy-talk.
Chuck Norris invented all 32 letters of the alphabet.
Remember The Ultimate Warrior? He quit wrestling because Chuck Norris wanted his nickname back.
If a tree falls in the forest, does anybody hear? Yes. Chuck Norris hears it. Chuck Norris can hear everything. Chuck Norris can hear the shrieking terror in your soul.
Chuck Norris actually owns IBM. It was an extremely hostile takeover.
He, who laughs last, laughs best. He who laughs at Chuck Norris  ...  dies.
Chuck Norris is like a dog, not only because he can smell fear, but because he can piss on whatever he wants.
Chuck Norris can jump-start a car using jumper cables attached to his nipples.
Chuck Norris neither melts in your mouth nor in your hand. He shreds your trachea before ravaging your soul with a combination of chocolate, whickey, roundhouse kicks and death. Oh, and pain. Lots of pain.
Chuck Norris doesn't have blood. He is filled with magma.
Chuck Norris uses Tabasco Sauce for eye drops.
Chuck Norris can get Blackjack with just one card.
"One time I was with Norris in the back of a pickup truck, along with a live deer. Norris goes up to the deer and says, 'I'm Chuck Norris! SAY IT!' Then he manipulates the deer's lips in such a way as to make it say, 'ChuckNorris'
People created the automobile to escape from Chuck Norris...Not to be outdone, Chuck Norris created the automobile accident.
Chuck Norris roundhouse kicks people in the face first and asks questions later.
When Chuck Norris was born, the only person who cried was the doctor. Never slap Chuck Norris.
Chuck Norris can sneeze with his eyes open.
Archeologists in India recently uncovered a new dinosaur. It's actually many dinosaurs but one is in the middle of all the others. The one in the middle is believed to have killed the others with a single roundhouse kick to the face. The archeologists wanted to call it ChuckNorrisaurs but the Indian government changed the name to Himotosaurous because it's simply not possible for Mr. Norris to be killed.
Chuck Norris got a perfect score on his SAT's, simply by writing Chuck Norris for every answer.
Chuck Norris has to use a stunt double when he does crying scenes.
Chuck Norris successfully seperated twins conjoined at the head by roundkicking them in the face.
Dinosaurs went extinct because of the Chuck Norrisaurus.
People have often asked the United States, What is your secret weapon against terrorists? We simply reply...Chuck Norris
Chuck Norris wears Orion's Belt around his pinky toe and he eats with the Big Dipper. 
Chuck Norris eats lightning and farts thunder.
Lightning never strikes twice in one place because Chuck Norris is looking for it. 
Chuck Norris was once a knight in King Arthur's court.  He was known as Sir Beatdown.
Chuck Norris once played rugby by himself.  He went undefeated. Chuck Norris once played rugby by himself.  He went undefeated.
In Desert Storm the reason why the Iraqi army surrendered so quickly because they knew Chuck Norris was coming. 
Chuck Norris has never looked a baby in the eyes cause it might him cry but if he does it also makes him want to punch a baby.
Chuck norris doesnt go at the speed of light, he goes at the speed of Norris
Chuck Norris does not know about this website. If he did he would have just deleted the internet.
Before sliced bread, people used to say "Thats the greatest thing since Chuck Norris". But Chuck Norris was displeased by this. So he roundhouse kicked a loaf of bread into slices.
Chuck Norris's sweat has burned holes in concrete.
The wind of Chuck Norris's round house kick can be felt from 1600 million miles away
Chuck Norris has held the World Championship in every weight class at the same time.
There is no Control button on Chuck Norris' computer.  Chuck Norris is always in control.
Chuck Norris is so bad he makes viruses sick.  As such, Chuck Norris is also responsible for the eradication of smallpox.
There are four legal methods of execution in the United States:  lethal injection, gas chamber, electric chair and Chuck Norris.
Earth's emergency defence plan in case of alien invasion is Chuck Norris.
Chuck Norris stared evil in the face, and it backed down
Chuck Norris can split the atom. With his bare hands.
On the SAT if you put Chuck Norris for every answer you will score over 8000
The United States could save billions in defense funding if they trade the Military for Chuck Norris
When Chuck Norris spits out watermelon seeds, he puts a machine gun to shame
Chuck Norris doesnt use after shave, he uses liquid hot magma.
When Chuck norris found this web-site while surfing the internt, he round house kicked his computer...10 new facts were added instantly.including this one
You can lead a horse to water but cannot make him drink, unless you're Chuck Norris
No matter what your mother always said, Chuck Norris can tune a fish.
Chuck Norris is '' The best a man can get ''
On Valentine's Day, Chuck Norris gives his wife the still beating heart of one of his enemies. Being very romantic, Chuck Norris believes every day should be Valentine's Day.
Scientists believe the world began with the "Big Bang". Chuck Norris shrugs it off as a "bad case of gas".
Chuck Norris let the dogs out.
Chuck Norris visits an active volcano every morning to get some of "the best damn espresso on Earth".
Chuck Norris eats eight meals a day. Seven are steak, and the last is the rest of the cow.
Chuck Norris does know what Willis is talking about!
Chuck Norris don't open no can of whoopass.  He makes his own.
Chuck Norris could shoot someone and still have time to roundhouse kick him in the face before the bullet hit.
Chuck Norris's body temperature is 98.6 degrees... Celsius.
The world's fastest car has 7 gears.  5, 6, and Chuck Norris.
The active ingredient in Red Bull is Chuck Norris's sweat.
The Seven Wonders of the ancient world were: Chuck Norris' left and right hands, his left and right feet, his belly button, his liver, and his beard.
When Chuck Norris goes to Vegas, he doesn't have to gamble. The casinos just give him stacks of money.
In an emergency, Chuck Norris can be used as a floatation device.
When Chuck Norris is ready to wake up, he tells the sun to get the above the horizon.
The speed of light was instituted because Chuck Norris didn't want get winded outrunning it. Chuck Norris hates to sweat.
Chuck Norris once bench-pressed the entire state of Ohio, and all of its residents.
Chuck Norris can hold his breathe for nine years.
When somebody yells "Last one in is a rotten egg," Chuck Norris is never the rotten egg.
Chuck Norris invented the question mark.
Chuck Norris trick-or-treated as himself as a child.
Chuck Norris has 3 knees on each leg.
Chuck Norris likes long walks on the beach, Barry White music, Harlequin romance novels, songbirds, rainbows, and quiet time with his lady ... just before he roundhouse kicks her in the face.
Chuck Norris can cook minute rice in 30 seconds.
If you gave Chuck Norris a typewriter and 0.000000000000000000001th of a second he can write the Complete Works of Shakespeare
Chuck Norris puts the laughter in manslaughter.
Chuck Norris' beard hair is believed to be an aphrodisiac in China.
The helicopter was invented after Chuck Norris was observed doing 8 roundhouse kicks a second.
Cars were invented to have a faster way of fleeing from Chuck Norris. Not to be outdone, Chuck Norris invented the car accident.
Chuck Norris brushes his teeth with barbed wire.
Chuck Norris can watch an episode of 60 minutes in 22 seconds.
Chuck Norris make onions CRY!!!
Some people say that Chuck Norris is a myth. Those "some people" are now dead.
When Chuck Norris sneeze, he don't say "Atchoo" he says "DIE EVERYONE!!!". That's what happens next.
Chuck Norris eats a bowl of diamonds every morning.
Chuck Norris is not only a noun, but a verb
"""

schneiertxt = """
If Bruce Schneier wants your plaintext, he'll just squeeze it out of the ciphertext using his barehands
Bruce Schneier got a perfect score on his comp-sci degree. Just by writing Bruce Schneier for every answer.
Whitfield Diffie and Martin Hellman use only their surnames out of fear of Bruce Schneier
Bruce Schneier can conduct secure multiparty computation... on his own
Bruce Schneier mounts side-channel attacks through the front channel
Bruce Schneier's discrete logarithms are uncountable and continuous
Bruce Schneier always inhabits the soundness of error margin of your zero-knowledge crypto protocol
When Bruce Schneier pre-computes S-box tables, he does it dynamically from the key... over breakfast.
Bruce Schneier can determine the exact location and velocity of any particle that's being used by quantum cryptography.
Quantum cryptography exchanged the Heisenberg Uncertainty Principle for the Schneier Dead Moral Certainty Principle when Bruce Schneier came to town.
Bruce Schneier knows Alice and Bob's shared secret.
Bruce Schneier eats 0s and 1s for breakfast. And snacks on pi.
Bruce Schneier memorizes his one time pads
Bruce Schneier assembled assembly...with his bare hands!
Bruce Schneier is computationally infeasible.
A mystery wrapped in an Enigma is no more puzzling to Bruce Schneier than a mystery wrapped in ROT-13.
Bruce Schneier doesn't even trust Trent. Trent has to trust Bruce Schneier.
Bruce Schneier once factored a prime number.
As Bruce Schneier says there is no Oscar for security theatre.
Bruce Schneier's secure handshake is so strong, you won't be able to exchange keys with anyone else for days.
Most people use passwords. Some people use passphrases. Bruce Schneier uses an epic passpoem, detailing the life and works of seven mythical Norse heroes.
Bruce Schneier's online purchases are so secure, his shopping cart is an M-1 tank.
Bruce Schneier doesn't need steganography to hide data in innocent-looking files. He just pounds it in with his fist.
Bruce Schneier can reverse any one-way cryptographic hash, just by staring it in the eye
Bruce Schneier can solve NP-Complete problems in NlogN time.
"When I wake up in the morning I piss cryptographic excellence." - Bruce Schneier
Bruce Schneier's tears can burn holes through an OpenBSD firewall. Lucky for us, Bruce Schneier never cries.
Bruce Schneier writes his books and essays by generating random alphanumeric text of an appropriate length and then decrypting it.
Bruce Schneier decrypted the Bible. The plaintext read, "Bruce Schneier".
If you use the digits of Pi to generate a visual image, it draws a picture of Bruce Schneier.
The universe was created to serve as Bruce Schneier's crib text.
Bruce Schneier's public and private keys are known as "Law" and "Order."
SSL is invulnerable to man-in-the-middle attacks. Unless that man is Bruce Schneier.
When he was three, Bruce Schneier built an Enigma machine out of Legos.
Bruce Schneier once found the inverse of a trapdoor function counting only on the fingers of one hand
A vigenere cipher with the Key "BRUCESCHNEIER" is in fact unbreakable.
Bruce Schneier fully discloses his own vulnerabilities: none.
Bruce Schneier knows your private key.
Bruce Schneier's Twofish algorithm has 16 rounds, but he always gets a knockout in the first.
The nuclear launch codes held by the President of the United States are secured by an unbreakable system: a plain brown envelope with a picture of Bruce Schneier on the flap.
Ron Rivest wears Bruce Schneier pajamas.
Bruce Schneier was only allowed to view the Kryptos sculpture at Langley for 1 second, in order not to spoil the fun other cryptographers. It was 0.9 seconds too much.
Bruce Schneier doesn't have a chin under his beard -- just more ciphertext.
If at first you don't succeed at breaking a cipher, you're not Bruce Schneier.
In a fight between Ron Rivest and Adi Shamir, the winner would be Bruce Schneier.
The output of Bruce Schneier's pseudorandom generator follows no describable pattern and cannot be compressed.
There is no chin behind Bruce Schneier's beard. There is only another pseudorandom number generator and he's gonna use it to encrypt your face.
When Bruce Schneier does modulo arithmetic, there are no remainders. Ever.
It has recently been discovered that every possible hashing algorithm produces the same value for the phrase "Bruce Schneier" -- Bruce Schneier.
Bruce Schneier made Bell-LaPadula do a brutal doodle.
Bruce Schneier once broke AES using nothing but six feet of rusty barbed wire, a toothpick, and the front axle from a 1962 Ford Falcon.
Every time Bruce Schneier smiles, an amateur cryptographer dies.
Mr. T pities the fool. Bruce Schneier just pities his data.
Bruce Schneier can change most random distributions. With his fists.
Geologists recently discovered that "earthquakes" are nothing more than Bruce Schneier and Chuck Norris communicating via a roundhouse kick-based cryptosystem.
Sweeping NSA reforms will soon require all employees to grow a Bruce Schneier beard.
Bruce Schneier mounts chosen-ciphertext attacks without choosing the ciphertext
As initialization vectors, 'Bruce Schneier' and 'Chuck Norris' are interchangeable.
When Bruce Schneier uses double ROT13 encryption, the ciphertext is totally unbreakable.
The final Beale Cipher, written 175 years ago, detailing the rightful owners of a cache of gold, has just two words in its plaintext: Bruce Schneier.
Autographed copies of "Applied Cryptography" reguarly sell for twice the going rate for enigma machines on eBay
Bruce Schneier sneers and solves Godel's incompleteness theorems.
When Bruce Schneier clicks "Random Fact" the outcome is never random.
Humboldt squids have sensors capable of detecting clothing worn by Bruce Schneier at 800 yards - to trigger their flight response.
Beyond computational complexity, there is Schneiertational complexity
Bruce Schneier can straighten out an elliptic curve with nothing but his teeth
Bruce Schneier makes abstract algebra look like elementary algebra.
"""

theotxt = """
Write more code.
Make more commits.
That's because you have been slacking.
slacker!
That's what happens when you're lazy.
idler!
slackass!
lazy bum!
Stop slacking you lazy bum!
slacker slacker lazy bum bum bum slacker!
I could search... but I'm a lazy bum ;)
sshutup sshithead, ssharpsshooting susshi sshplats ssharking assholes.
Lazy bums slacking on your asses.
35 commits an hour? That's pathetic!
Fine software takes time to prepare.  Give a little slack.
I am just stating a fact
you bring new meaning to the terms slackass. I will have to invent a new term.
if they cut you out, muddy their back yards
Make them want to start over, and play nice the next time.
It is clear that this has not been thought through.
avoid using abort().  it is not nice.
That's the most ridiculous thing I've heard in the last two or three minutes!
I'm not just doing this for crowd response. I need to be right.
I'd put a fan on my bomb.. And blinking lights...
I love to fight
No sane people allowed here.  Go home.
you have to stop peeing on your breakfast
feature requests come from idiots
henning and darren / sitting in a tree / t o k i n g / a joint or three
KICK ASS. TIME FOR A JASON LOVE IN!  WE CAN ALL GET LOST IN HIS HAIR!
shame on you for following my rules.
altq's parser sucks dead whale farts through the finest chemistry pipette's
screw this operating system shit, i just want to drive!
Search for fuck.  Anytime you see that word, you have a paragraph to write.
Yes, but the ports people are into S&M.
Buttons are for idiots.
We are not hackers. We are turd polishing craftsmen.
who cares.  style(9) can bite my ass
It'd be one fucking happy planet if it wasn't for what's under this fucking sticker.
I would explain, but I am too drunk.
you slackers don't deserve pictures yet
Vegetarian my ass
Wait a minute, that's a McNally's!
don't they recognize their moral responsibility to entertain me?
#ifdef is for emacs developers.
Many well known people become net-kooks in their later life, because they lose touch with reality.
You're not allowed to have an opinion.
tweep tweep tweep
Quite frankly, SSE's alignment requirement is the most utterly retarded idea since eating your own shit.
Holy verbose prom startup Batman.
Any day now, when we sell out.
optimism in man kind does not belong here
First user who tries to push this button, he pounds into the ground with a rant of death.
we did farts.  now we do sperm.  we are cutting edge.
the default configuration is a mixture of piss, puke, shit, and bloody entrails.
Stop wasting your time reading people's licenses.
doing it with environment variables is OH SO SYSTEM FIVE LIKE OH MY GOD PASS ME THE SPOON
Linux is fucking POO, not just bad, bad REALLY REALLY BAD
penguins are not much more than chickens that swim.
i am a packet sniffing fool, let me wipe my face with my own poo
Whiners.  They scale really well.
in your world, you would have a checklist of 50 fucking workarounds just to make a coffee.
for once, I have nothing to say.
You have no idea how fucked we are
You can call it fart if you want to.
wavelan is a battle field
You are in a maze of gpio pins, all alike, all undocumented, and a few are wired to bombs.
And that is why humppa sucks... cause it has no cause.
cache aliasing is a problem that would have stopped in 1992 if someone had killed about 5 people who worked at Sun.
"""

