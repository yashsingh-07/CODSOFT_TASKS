from datetime import datetime

# ============================================================
# ALEX - SPORTS EXPERT CHATBOT
# CodSoft Internship - Task 1
# Rule-Based Chatbot using Python
# ============================================================

BOT_NAME = "Alex"


# ============================================================
# WELCOME MESSAGE
# ============================================================

def show_welcome():
    print("=" * 65)
    print("              🏆 ALEX - SPORTS EXPERT")
    print("=" * 65)
    print("Hello! I am Alex, your sports knowledge chatbot.")
    print("I can answer questions about sports, players, rules,")
    print("tournaments, scoring and sports terminology.")
    print()
    print("Type 'help' to see what I know.")
    print("Type 'bye' to end the conversation.")
    print("=" * 65)


# ============================================================
# HELP
# ============================================================

def show_help():
    print("\nAlex: Here are the topics I can discuss:\n")

    print("🏏 Cricket")
    print("⚽ Football / Soccer")
    print("🏀 Basketball")
    print("🎾 Tennis")
    print("🏸 Badminton")
    print("🏑 Hockey")
    print("🏐 Volleyball")
    print("🏓 Table Tennis")
    print("🥊 Boxing")
    print("🥋 Karate")
    print("🏃 Athletics")
    print("🏊 Swimming")
    print("🏎️ Formula 1")
    print("⛳ Golf")
    print("🏅 Olympics")

    print("\nI can also tell you about:")
    print("• Famous players")
    print("• Basic rules")
    print("• Scoring systems")
    print("• Major tournaments")
    print("• Sports positions")
    print("• Sports benefits")
    print("• Date and time")


# ============================================================
# CRICKET
# ============================================================

def cricket_response(user):

    # Famous players
    if ("famous player" in user or
        "famous players" in user or
        "famous cricketer" in user or
        "famous cricketers" in user or
        "best player" in user or
        "best players" in user or
        "top player" in user or
        "top players" in user):

        print("Alex: Some famous cricket players include:")
        print("Alex: Virat Kohli, Sachin Tendulkar, MS Dhoni,")
        print("Alex: Rohit Sharma, Brian Lara and AB de Villiers.")

    elif "virat" in user or "kohli" in user:
        print("Alex: Virat Kohli is an Indian international cricketer.")
        print("Alex: He is widely regarded as one of the leading batters")
        print("Alex: of his generation.")

    elif "sachin" in user or "tendulkar" in user:
        print("Alex: Sachin Tendulkar is an Indian cricket legend.")
        print("Alex: He is widely regarded as one of the greatest batters")
        print("Alex: in cricket history.")

    elif "dhoni" in user:
        print("Alex: MS Dhoni is a former Indian captain and wicketkeeper-batter.")
        print("Alex: He is known for his leadership and finishing ability.")

    elif "rohit" in user or "sharma" in user:
        print("Alex: Rohit Sharma is an Indian international cricketer.")
        print("Alex: He is known for his batting and leadership.")

    elif "babar" in user:
        print("Alex: Babar Azam is a Pakistani international cricketer")
        print("Alex: known for his batting.")

    elif "abd" in user or "ab de villiers" in user:
        print("Alex: AB de Villiers is a former South African cricketer.")
        print("Alex: He was known for his innovative and aggressive batting.")

    elif "brian lara" in user or "lara" in user:
        print("Alex: Brian Lara is a legendary former West Indian cricketer.")
        print("Alex: He was famous for his outstanding batting performances.")

    # Formats
    elif "format" in user or "formats" in user:
        print("Alex: The three major international cricket formats are:")
        print("Alex: Test, ODI and T20.")

    elif "test" in user:
        print("Alex: Test cricket is the longest international format.")
        print("Alex: A Test match can last up to five days.")

    elif "odi" in user:
        print("Alex: ODI stands for One Day International.")
        print("Alex: Each team normally gets 50 overs.")

    elif "t20" in user:
        print("Alex: T20 is a short format of cricket.")
        print("Alex: Each team normally gets 20 overs.")

    # Tournaments
    elif "ipl" in user:
        print("Alex: IPL stands for Indian Premier League.")
        print("Alex: It is a major professional T20 cricket league in India.")

    elif "world cup" in user:
        print("Alex: The Cricket World Cup is a major international cricket tournament.")

    # Rules and scoring
    elif "wicket" in user:
        print("Alex: A wicket can refer to the dismissal of a batter,")
        print("Alex: the three stumps, or the pitch area depending on context.")

    elif "run" in user or "score" in user:
        print("Alex: Runs are scored by the batting team.")
        print("Alex: A boundary normally scores 4 runs and a six scores 6 runs.")

    elif "bowler" in user:
        print("Alex: Bowlers attempt to dismiss batters and restrict")
        print("Alex: the batting team's score.")

    elif "rules" in user:
        print("Alex: Cricket is played between two teams.")
        print("Alex: Teams take turns batting and bowling.")
        print("Alex: The team with more runs generally wins.")

    else:
        print("Alex: Cricket is a bat-and-ball sport played between two teams.")
        print("Alex: Ask me about formats, famous players, IPL, World Cups")
        print("Alex: rules or scoring.")


# ============================================================
# FOOTBALL
# ============================================================

def football_response(user):

    if ("famous player" in user or
        "famous players" in user or
        "best player" in user or
        "best players" in user or
        "top player" in user or
        "top players" in user):

        print("Alex: Some famous football players include Lionel Messi,")
        print("Alex: Cristiano Ronaldo, Neymar, Pelé and Diego Maradona.")

    elif "messi" in user:
        print("Alex: Lionel Messi is an Argentine footballer.")
        print("Alex: He is widely regarded as one of the greatest football")
        print("Alex: players in history.")

    elif "ronaldo" in user:
        print("Alex: Cristiano Ronaldo is a Portuguese footballer.")
        print("Alex: He is known for his goal scoring, athleticism and")
        print("Alex: long and successful career.")

    elif "neymar" in user:
        print("Alex: Neymar is a Brazilian footballer known for his")
        print("Alex: technical skill and creativity.")

    elif "pele" in user or "pelé" in user:
        print("Alex: Pelé was a legendary Brazilian footballer.")
        print("Alex: He is regarded as one of the greatest players in football history.")

    elif "maradona" in user:
        print("Alex: Diego Maradona was an Argentine football legend.")
        print("Alex: He is remembered as one of football's greatest players.")

    elif "offside" in user:
        print("Alex: The offside rule prevents attackers from gaining")
        print("Alex: an unfair advantage near the opponent's goal.")

    elif "world cup" in user:
        print("Alex: The FIFA World Cup is the major international")
        print("Alex: football tournament.")

    elif "champions league" in user:
        print("Alex: The UEFA Champions League is a major European")
        print("Alex: club football competition.")

    elif "goalkeeper" in user:
        print("Alex: The goalkeeper protects the team's goal.")
        print("Alex: They can use their hands inside their own penalty area.")

    elif "position" in user or "positions" in user:
        print("Alex: Common positions include goalkeeper, defender,")
        print("Alex: midfielder and forward.")

    elif "goal" in user:
        print("Alex: A goal is scored when the entire ball crosses")
        print("Alex: the goal line between the posts and under the crossbar.")

    else:
        print("Alex: Football is played between two teams trying to score goals.")
        print("Alex: Ask me about players, positions, rules or tournaments.")


# ============================================================
# BASKETBALL
# ============================================================

def basketball_response(user):

    if ("famous player" in user or
        "famous players" in user or
        "best player" in user or
        "best players" in user):

        print("Alex: Some famous basketball players include:")
        print("Alex: Michael Jordan, LeBron James, Stephen Curry and Kobe Bryant.")

    elif "lebron" in user:
        print("Alex: LeBron James is an American professional basketball player.")
        print("Alex: He is widely regarded as one of the greatest basketball players.")

    elif "jordan" in user:
        print("Alex: Michael Jordan is a basketball legend.")
        print("Alex: He is widely regarded as one of the greatest basketball players.")

    elif "curry" in user:
        print("Alex: Stephen Curry is an American basketball player.")
        print("Alex: He is famous for his exceptional three-point shooting.")

    elif "kobe" in user:
        print("Alex: Kobe Bryant was an American basketball legend.")
        print("Alex: He was known for his scoring ability and competitive mindset.")

    elif "nba" in user:
        print("Alex: NBA stands for National Basketball Association.")
        print("Alex: It is a major professional basketball league.")

    elif "score" in user or "points" in user:
        print("Alex: A free throw is worth 1 point.")
        print("Alex: A normal field goal is worth 2 points.")
        print("Alex: A three-pointer is worth 3 points.")

    elif "position" in user:
        print("Alex: Common positions include point guard, shooting guard,")
        print("Alex: small forward, power forward and center.")

    else:
        print("Alex: Basketball is a team sport where players try to score")
        print("Alex: by putting the ball through the opponent's hoop.")


# ============================================================
# TENNIS
# ============================================================

def tennis_response(user):

    if ("famous player" in user or
        "famous players" in user or
        "best player" in user or
        "best players" in user):

        print("Alex: Some famous tennis players include:")
        print("Alex: Roger Federer, Rafael Nadal, Novak Djokovic and Serena Williams.")

    elif "federer" in user:
        print("Alex: Roger Federer is a Swiss tennis legend.")
        print("Alex: He was known for his elegant playing style and exceptional career.")

    elif "nadal" in user:
        print("Alex: Rafael Nadal is a Spanish tennis legend.")
        print("Alex: He is particularly famous for his success on clay courts.")

    elif "djokovic" in user:
        print("Alex: Novak Djokovic is a Serbian tennis player.")
        print("Alex: He is one of the most successful players in tennis history.")

    elif "serena" in user:
        print("Alex: Serena Williams is an American tennis legend.")
        print("Alex: She is one of the most successful players in tennis history.")

    elif "grand slam" in user or "grand slams" in user:
        print("Alex: The four Grand Slam tournaments are:")
        print("Alex: Australian Open, French Open, Wimbledon and US Open.")

    elif "scoring" in user or "score" in user:
        print("Alex: Tennis scoring uses points, games and sets.")

    elif "surface" in user or "court" in user:
        print("Alex: Major tennis surfaces are hard court, clay and grass.")

    elif "singles" in user or "doubles" in user:
        print("Alex: Tennis can be played as singles or doubles.")

    else:
        print("Alex: Tennis is a racket sport played across a net.")


# ============================================================
# BADMINTON
# ============================================================

def badminton_response(user):

    if ("famous player" in user or
        "famous players" in user or
        "best player" in user or
        "best players" in user):

        print("Alex: Some famous badminton players include:")
        print("Alex: P. V. Sindhu, Saina Nehwal, Lin Dan and Viktor Axelsen.")

    elif "sindhu" in user:
        print("Alex: P. V. Sindhu is one of India's most successful badminton players.")

    elif "saina" in user:
        print("Alex: Saina Nehwal is a highly successful Indian badminton player.")

    elif "lin dan" in user:
        print("Alex: Lin Dan is a legendary former Chinese badminton player.")

    elif "axelsen" in user:
        print("Alex: Viktor Axelsen is a Danish badminton player.")

    elif "score" in user or "scoring" in user:
        print("Alex: Modern badminton uses rally scoring.")
        print("Alex: Games are generally played to 21 points.")

    elif "singles" in user or "doubles" in user:
        print("Alex: Badminton can be played in singles or doubles.")

    else:
        print("Alex: Badminton is a racket sport played using a shuttlecock.")


# ============================================================
# HOCKEY
# ============================================================

def hockey_response(user):

    if "famous player" in user or "famous players" in user:
        print("Alex: Famous hockey players include Dhyan Chand,")
        print("Alex: Wayne Gretzky and Sidney Crosby.")

    elif "dhyan chand" in user:
        print("Alex: Major Dhyan Chand was an Indian field hockey legend.")

    elif "gretzky" in user:
        print("Alex: Wayne Gretzky is a Canadian ice hockey legend.")

    elif "rules" in user:
        print("Alex: In field hockey, players use sticks to control the ball")
        print("Alex: and attempt to score in the opponent's goal.")

    else:
        print("Alex: Hockey is a team sport played using sticks and a ball or puck.")


# ============================================================
# VOLLEYBALL
# ============================================================

def volleyball_response(user):

    if "famous player" in user or "famous players" in user:
        print("Alex: Famous volleyball players include Karch Kiraly")
        print("Alex: and Giba.")

    elif "score" in user or "scoring" in user:
        print("Alex: Volleyball commonly uses rally scoring.")
        print("Alex: A team generally needs 25 points to win a set,")
        print("Alex: with exceptions for the deciding set.")

    elif "position" in user or "positions" in user:
        print("Alex: Volleyball positions include setter, outside hitter,")
        print("Alex: opposite hitter, middle blocker and libero.")

    else:
        print("Alex: Volleyball is played by two teams separated by a net.")


# ============================================================
# TABLE TENNIS
# ============================================================

def table_tennis_response(user):

    if "famous player" in user or "famous players" in user:
        print("Alex: Famous table tennis players include Ma Long,")
        print("Alex: Fan Zhendong and Jan-Ove Waldner.")

    elif "score" in user or "scoring" in user:
        print("Alex: A standard table tennis game is generally played to 11 points.")

    elif "singles" in user or "doubles" in user:
        print("Alex: Table tennis can be played as singles or doubles.")

    elif "equipment" in user:
        print("Alex: Basic equipment includes a table, net, racket and ball.")

    else:
        print("Alex: Table tennis is a racket sport played on a table divided by a net.")


# ============================================================
# BOXING
# ============================================================

def boxing_response(user):

    if "famous player" in user or "famous boxer" in user:
        print("Alex: Famous boxers include Muhammad Ali, Mike Tyson,")
        print("Alex: Manny Pacquiao and Floyd Mayweather Jr.")

    elif "muhammad ali" in user or user == "ali":
        print("Alex: Muhammad Ali was one of the most famous heavyweight boxers in history.")

    elif "mike tyson" in user or "tyson" in user:
        print("Alex: Mike Tyson is a former heavyweight boxing champion.")

    elif "weight" in user:
        print("Alex: Boxing is divided into different weight classes.")

    elif "round" in user:
        print("Alex: Boxing matches are divided into rounds.")

    else:
        print("Alex: Boxing is a combat sport involving regulated punching,")
        print("Alex: defense, movement and strategy.")


# ============================================================
# KARATE
# ============================================================

def karate_response(user):

    if "famous player" in user or "famous karate" in user:
        print("Alex: Famous karate athletes include Rika Usami,")
        print("Alex: Rafael Aghayev and Sandra Sánchez.")

    elif "kata" in user:
        print("Alex: Kata is a structured sequence of karate techniques and movements.")

    elif "kumite" in user:
        print("Alex: Kumite refers to sparring or combat practice in karate.")

    elif "belt" in user:
        print("Alex: Karate uses belt ranks to represent a practitioner's level and progress.")

    else:
        print("Alex: Karate is a martial art involving striking techniques,")
        print("Alex: defensive movements and kata.")


# ============================================================
# ATHLETICS
# ============================================================

def athletics_response(user):

    if "famous player" in user or "famous athlete" in user:
        print("Alex: Famous athletes include Usain Bolt, Carl Lewis,")
        print("Alex: Eliud Kipchoge and Michael Johnson.")

    elif "usain bolt" in user or user == "bolt":
        print("Alex: Usain Bolt is a Jamaican sprinting legend.")

    elif "kipchoge" in user:
        print("Alex: Eliud Kipchoge is a Kenyan long-distance running legend.")

    elif "sprint" in user:
        print("Alex: Sprinting includes races such as 100m, 200m and 400m.")

    elif "marathon" in user:
        print("Alex: A marathon covers 42.195 kilometres.")

    elif "long jump" in user:
        print("Alex: Long jump is an athletics event where athletes")
        print("Alex: attempt to jump as far as possible.")

    elif "high jump" in user:
        print("Alex: High jump requires athletes to clear a horizontal bar.")

    else:
        print("Alex: Athletics includes running, jumping and throwing events.")


# ============================================================
# SWIMMING
# ============================================================

def swimming_response(user):

    if "famous player" in user or "famous swimmer" in user:
        print("Alex: Famous swimmers include Michael Phelps,")
        print("Alex: Katie Ledecky and Ian Thorpe.")

    elif "phelps" in user:
        print("Alex: Michael Phelps is an American swimming legend.")
        print("Alex: He is one of the most decorated Olympians.")

    elif "ledecky" in user:
        print("Alex: Katie Ledecky is an American competitive swimmer.")

    elif "stroke" in user:
        print("Alex: The main competitive strokes are freestyle, backstroke,")
        print("Alex: breaststroke and butterfly.")

    elif "freestyle" in user:
        print("Alex: Freestyle is a swimming category where competitors")
        print("Alex: commonly use the front crawl.")

    else:
        print("Alex: Swimming is both a recreational and competitive sport.")


# ============================================================
# FORMULA 1
# ============================================================

def formula1_response(user):

    if "famous player" in user or "famous driver" in user:
        print("Alex: Famous Formula 1 drivers include Lewis Hamilton,")
        print("Alex: Michael Schumacher, Max Verstappen and Ayrton Senna.")

    elif "verstappen" in user:
        print("Alex: Max Verstappen is a Formula 1 driver from the Netherlands.")

    elif "hamilton" in user:
        print("Alex: Lewis Hamilton is a British Formula 1 driver")
        print("Alex: and multiple-time world champion.")

    elif "schumacher" in user:
        print("Alex: Michael Schumacher is a legendary German Formula 1 driver.")

    elif "senna" in user:
        print("Alex: Ayrton Senna was a legendary Brazilian Formula 1 driver.")

    elif "race" in user or "grand prix" in user:
        print("Alex: Formula 1 races are called Grands Prix.")

    elif "qualifying" in user:
        print("Alex: F1 qualifying determines the starting order for the race.")

    elif "pit stop" in user:
        print("Alex: A pit stop allows a team to perform tasks such as changing tyres.")

    else:
        print("Alex: Formula 1 is the highest class of international")
        print("Alex: single-seater motor racing.")


# ============================================================
# GOLF
# ============================================================

def golf_response(user):

    if "famous player" in user or "famous golfer" in user:
        print("Alex: Famous golfers include Tiger Woods, Jack Nicklaus")
        print("Alex: and Arnold Palmer.")

    elif "tiger woods" in user:
        print("Alex: Tiger Woods is one of the most famous and successful golfers in history.")

    elif "jack nicklaus" in user:
        print("Alex: Jack Nicklaus is a legendary American professional golfer.")

    elif "score" in user:
        print("Alex: Golf aims to complete the course using as few strokes as possible.")

    elif "hole" in user:
        print("Alex: A standard golf course generally has 18 holes.")

    else:
        print("Alex: Golf is played by hitting a ball toward a series of holes")
        print("Alex: using as few strokes as possible.")


# ============================================================
# OLYMPICS
# ============================================================

def olympics_response(user):

    if "famous player" in user or "famous athlete" in user:
        print("Alex: Famous Olympic athletes include Usain Bolt,")
        print("Alex: Michael Phelps and Simone Biles.")

    elif "medal" in user:
        print("Alex: Olympic medals are awarded as gold, silver and bronze.")

    elif "summer" in user:
        print("Alex: The Summer Olympics feature a large variety of sports.")

    elif "winter" in user:
        print("Alex: The Winter Olympics feature sports associated with snow and ice.")

    else:
        print("Alex: The Olympic Games are a major international multi-sport event.")
        print("Alex: Athletes from around the world compete across many sports.")


# ============================================================
# GENERAL SPORTS
# ============================================================

def general_sports_response(user):

    if "benefit" in user or "benefits" in user:
        print("Alex: Sports can improve physical fitness, coordination,")
        print("Alex: teamwork, discipline and overall well-being.")

    elif "team sport" in user:
        print("Alex: Examples include football, cricket, basketball,")
        print("Alex: volleyball and hockey.")

    elif "individual sport" in user:
        print("Alex: Examples include tennis, swimming, athletics,")
        print("Alex: golf and boxing.")

    elif "best sport" in user:
        print("Alex: There is no single best sport.")
        print("Alex: It depends on your interests and goals.")

    else:
        print("Alex: Sports develop physical skills, discipline,")
        print("Alex: teamwork, strategy and coordination.")


# ============================================================
# MAIN CHATBOT
# ============================================================

def alex_chatbot():

    show_welcome()

    while True:

        user = input("\nYou: ").lower().strip()

        # Empty input
        if user == "":
            print("Alex: Please type something so I can help you.")

        # Greetings
        elif user in [
            "hi",
            "hello",
            "hey",
            "hii",
            "hola",
            "good morning",
            "good afternoon",
            "good evening"
        ]:
            print("Alex: Hello! 👋 I'm Alex, your sports expert.")
            print("Alex: Which sport would you like to discuss?")

        # About Alex
        elif "your name" in user or "who are you" in user:
            print("Alex: My name is Alex.")
            print("Alex: I am a Python-based rule-based sports chatbot.")
            print("Alex: I use predefined if-elif rules to generate responses.")

        # Help
        elif user == "help" or "what can you do" in user:
            show_help()

        # Time
        elif "time" in user:
            current_time = datetime.now().strftime("%I:%M %p")
            print("Alex: The current time is", current_time)

        # Date
        elif "date" in user or "today" in user:
            current_date = datetime.now().strftime("%d-%m-%Y")
            print("Alex: Today's date is", current_date)

        # Thank you
        elif "thank" in user or "thanks" in user:
            print("Alex: You're welcome! 🏆")
            print("Alex: Keep playing, keep learning and keep improving!")

        # Cricket
        elif "cricket" in user:
            cricket_response(user)

        # Football
        elif "football" in user or "soccer" in user:
            football_response(user)

        # Basketball
        elif "basketball" in user:
            basketball_response(user)

        # Tennis
        elif "tennis" in user:
            tennis_response(user)

        # Badminton
        elif "badminton" in user:
            badminton_response(user)

        # Hockey
        elif "hockey" in user:
            hockey_response(user)

        # Volleyball
        elif "volleyball" in user:
            volleyball_response(user)

        # Table Tennis
        elif "table tennis" in user or "ping pong" in user:
            table_tennis_response(user)

        # Boxing
        elif "boxing" in user:
            boxing_response(user)

        # Karate
        elif "karate" in user:
            karate_response(user)

        # Athletics
        elif "athletics" in user or "running" in user:
            athletics_response(user)

        # Swimming
        elif "swimming" in user:
            swimming_response(user)

        # Formula 1
        elif "formula 1" in user or user == "f1":
            formula1_response(user)

        # Golf
        elif "golf" in user:
            golf_response(user)

        # Olympics
        elif "olympics" in user or "olympic" in user:
            olympics_response(user)

        # General sports
        elif "sport" in user or "sports" in user:
            general_sports_response(user)

        # Exit
        elif user in ["bye", "exit", "quit", "goodbye"]:
            print("Alex: Goodbye! 👋")
            print("Alex: Keep playing, keep learning and keep improving! 🏆")
            break

        # Unknown input
        else:
            print("Alex: Sorry, I don't have a predefined response for that.")
            print("Alex: Try asking about a sport, famous players,")
            print("Alex: rules, scoring, tournaments or terminology.")

    print("\n" + "=" * 65)
    print("           🏆 ALEX CHATBOT SESSION ENDED")
    print("=" * 65)


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":
    alex_chatbot()