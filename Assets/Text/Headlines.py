import random

# String Options
def city_or_team(team, capital=False):
    if team is None:
        return ""
    if capital:
        city_or_team_table = [team.city, f"The {team.name}", f"The {team.city} {team.name}"]
    else:
        city_or_team_table = [team.city, f"the {team.name}", f"the {team.city} {team.name}"]
        
    return random.choice(city_or_team_table)

def winner(game, capital=False):
    if game is None:
        return ""
    if game.winner == "home":
        return city_or_team(game.home_team, True) if capital else city_or_team(game.home_team)
    else:
        return city_or_team(game.away_team, True) if capital else city_or_team(game.away_team)

def winner_city(game):
    if game is None:
        return ""
    return game.home_team.city if game.winner == "home" else game.away_team.city

def loser_city(game):
    if game is None:
        return ""
    return game.home_team.city if game.winner == "away" else game.away_team.city

def winner_name(game, capital=False):
    if game is None:
        return ""
    if capital:
        return f"The {game.home_team.name}" if game.winner == "home" else f"The {game.away_team.name}"
    else:
        return f"the {game.home_team.name}" if game.winner == "home" else f"the {game.away_team.name}"

def loser_name(game, capital=False):
    if game is None:
        return ""
    if capital:
        return f"The {game.home_team.name}" if game.winner == "away" else f"The {game.away_team.name}"
    else:
        return f"the {game.home_team.name}" if game.winner == "away" else f"the {game.away_team.name}"

def loser(game, capital=False):
    if game is None:
        return ""
    if game.winner == "home":
        return city_or_team(game.away_team, capital) if capital else city_or_team(game.away_team)
    else:
        return city_or_team(game.home_team, capital) if capital else city_or_team(game.home_team)

def matchup(game, capital=False):
    if game is None:
        return ""
    cities = f"{game.home_team.city} vs {game.away_team.city}"
    if capital:
        names = f"The {game.home_team.name} vs the {game.away_team.name}"
    else:
        names = f"the {game.home_team.name} vs the {game.away_team.name}"
    return random.choice([cities, names])

def matchup_and(game, capital=False):
    if game is None:
        return ""
    cities = f"{game.home_team.city} and {game.away_team.city}"
    if capital:
        names = f"The {game.home_team.name} and the {game.away_team.name}"
    else:
        names = f"the {game.home_team.name} and the {game.away_team.name}"
    return random.choice([cities, names])

# Team Headlines
def top_team_headlines(game, headline_index):
    does_it_again = [
        f"{winner(game, True)} continued their dominance this week with another convincing victory. "
        f"The rest of the league is still searching for an answer.",
        f"Another week brought another win for {winner(game)}. At this point, "
        f"excellence has become the expectation.",
        f"{winner(game, True)} once again showed why they sit atop the standings. The championship "
        f"favorites remain firmly in control.",
        f"The winning keeps coming for {winner(game)}. Their performance against {loser(game)} "
        f"this week only strengthened their grip on the league.",
        f"{winner(game, True)} handled business once again this week. Every victory makes them look "
        f"more and more unstoppable."
    ]

    scraped_by = [
        f"{winner(game, True)} escaped with a narrow victory against {loser(game)} this "
        f"week. It wasn't pretty, but the win still counts.",
        f"{winner(game, True)} found a way to survive after {loser(game)} pushed them "
        f"to the brink this week. Championship teams often win games like these.",
        f"A major scare nearly derailed {winner_city(game)}'s momentum this week. Instead, they found a way to grind "
        f"out another win.",
        f"{winner(game, True)} looked vulnerable for perhaps the first time all season. Fortunately "
        f"for them, the final score still went their way.",
        f"The league leaders were forced to work overtime this week. In the end, {winner(game)} did just "
        f"enough to remain on top."
    ]

    surprising_loss = [
        f"The league was stunned this week as {loser(game)} suffered an unexpected defeat. Even the best "
        f"teams have bad days.",
        f"{loser(game, True)} finally came back down to earth after a shocking loss. The result has "
        f"opened the door for several challengers.",
        f"One of the season's biggest surprises occurred this week when {loser(game)} was defeated. The "
        f"race for the top suddenly looks much tighter.",
        f"{loser(game, True)} entered the week as heavy favorites but left with a loss. It was a "
        f"reminder that no victory is guaranteed.",
        f"The unthinkable happened this week as {loser(game)} fell short against "
        f"{winner(game)}. Their lead remains strong, but questions are beginning to emerge."
    ]

    options = [does_it_again, scraped_by, surprising_loss]
    weight = [80, 85, 95]

    return [random.choice(options[headline_index]), weight[headline_index], game]

def contender_headlines(game, headline_index):
    beat_top_team = [
        f"{winner(game, True)} delivered a statement victory by taking down "
        f"{loser(game)}. The title race suddenly became much more interesting.",
        f"Nobody can ignore {winner(game)} after this week's performance. Defeating "
        f"{loser(game)} has firmly established them as a legitimate threat.",
        f"{winner(game, True)} proved they belong among the league's elite with a huge victory over "
        f"{loser(game)}. The standings may never look the same.",
        f"One of the biggest games of the season lived up to the hype as {winner(game)} defeated "
        f"{loser(game)}. The championship picture just got a lot more crowded.",
        f"{winner(game, True)} walked into a difficult matchup and emerged victorious. Their win "
        f"over {loser(game)} sent a message to the entire league."
    ]

    surprising_loss = [
        f"{loser(game, True)} suffered a disappointing defeat this week against an opponent many "
        f"expected them to beat. The loss could have serious playoff implications.",
        f"Momentum came to a halt for {loser(game)} after an unexpected setback against "
        f"{winner(game)}. They will need to regroup quickly.",
        f"{loser(game, True)} entered the week with high expectations but left with plenty of "
        f"questions. Their playoff position suddenly feels less secure.",
        f"A costly loss against {winner(game)} has complicated the road ahead for "
        f"{loser(game)}. Every game matters as the season continues.",
        f"{loser(game, True)} missed an opportunity to strengthen its standing this week. Instead, "
        f"they now face increased pressure moving forward."
    ]

    winning_streak = [
        f"{winner(game, True)} continue to show they are one of the hottest teams in the league "
        f"right now. Their winning streak continues to grow with every passing week.",
        f"{winner(game, True)} keep finding ways to win. What started as a solid season is "
        f"beginning to look like something special.",
        f"Confidence is surging throughout the organization as {winner(game)} extended its winning streak "
        f"this week. Few teams want to face them right now.",
        f"{winner(game, True)} continued its remarkable run this week against "
        f"{loser(game)}. Their recent form has made them a serious championship contender.",
        f"The victories keep piling up for {winner(game)}. Momentum is firmly on their side as the "
        f"season progresses."
    ]

    close_top_team = [
        f"{loser(game, True)} came up short, but their performance against "
        f"{loser(game)} earned plenty of respect. They proved they can compete with the league's best.",
        f"Despite the loss against {winner(game)}, {loser(game)} showed that the gap between "
        f"contenders and favorites may be smaller than many thought.",
        f"{loser(game, True)} pushed {winner(game)} to the limit this week. Fans are "
        f"hoping that these teams find a way to rematch in the upcoming playoffs.",
        f"The final score favored {winner(game)}, but {loser(game)} left the field with "
        f"newfound credibility. They look capable of making noise in the postseason.",
        f"{loser(game, True)} nearly pulled off one of the biggest wins of the year. Even in "
        f"defeat, they strengthened their reputation."
    ]

    options = [beat_top_team, surprising_loss, winning_streak, close_top_team]
    weight = [95, 80, 75, 60]

    return [random.choice(options[headline_index]), weight[headline_index], game]

def middler_headlines(game, headline_index):
    beat_top_team = [
        f"{winner(game, True)} shocked the league this week with a stunning upset over "
        f"{loser(game)}. Nobody saw this result coming.",
        f"One of the season's biggest surprises occurred as {winner(game)} knocked off "
        f"{loser(game)} this week. The underdogs seized their moment.",
        f"{winner(game, True)} may have changed the playoff picture with a massive upset victory. Their "
        f"season suddenly has new life.",
        f"The standings were shaken this week as {winner(game)} defeated {loser(game)}. It "
        f"was a result that few expected.",
        f"{winner(game, True)} delivered a reminder that every team is dangerous on the right day. Their "
        f"upset of {loser(game)} will be remembered for quite some time."
    ]

    close_top_team = [
        f"{loser(game, True)} may not have won, but they showed they can compete with stronger "
        f"opponents. Their performance earned attention around the league.",
        f"A narrow defeat against {winner(game)} revealed a great deal about {loser(game)}. They "
        f"are much tougher than their record suggests.",
        f"{loser(game, True)} nearly pulled off an upset this week. Even in defeat, there are plenty "
        f"of reasons for optimism.",
        f"The final score favored the better team, but {loser(game)} made them earn every point. It was "
        f"an encouraging effort.",
        f"{loser(game, True)} exceeded expectations by hanging tough against "
        f"{winner(game)}. They may be turning a corner."
    ]

    winning_streak = [
        f"{winner_name(game, True)} are quietly becoming one of the league's hottest teams after beating "
        f"{loser(game)}. Their recent success is beginning to attract attention.",
        f"{winner(game, True)} continued its climb up the standings with another victory. A playoff "
        f"push suddenly feels realistic.",
        f"The season looked average just weeks ago, but {winner_city(game)} is building serious momentum. Opponents "
        f"are starting to take notice.",
        f"{winner(game, True)} extended their winning streak and strengthened their postseason hopes. "
        f"Confidence is growing throughout the organization.",
        f"What once looked like a middle-of-the-pack team is beginning to look much more dangerous. "
        f"{winner_city(game)} is on a roll."
    ]

    facing_elimination = [
        f"{loser(game, True)} finds themselves in a must-win situation after another difficult week. "
        f"Their playoff hopes are hanging by a thread.",
        f"The margin for error has disappeared for {loser(game)}. Every remaining game now carries "
        f"enormous importance.",
        f"{loser_city(game)} is running out of opportunities to save its season after its loss against "
        f"{winner(game)}. Another loss could end their playoff dreams.",
        f"The pressure continues to mount on {loser(game)}. Their postseason future remains uncertain.",
        f"Time is running out for {loser(game)}. The next few weeks may determine the fate of their season."
    ]

    options = [beat_top_team, close_top_team, winning_streak, facing_elimination]
    weight = [90, 55, 70, 60]

    return [random.choice(options[headline_index]), weight[headline_index], game]

def bottom_feeder_headlines(game, headline_index):
    loses_again = [
        f"{loser_city(game)}'s difficult season continued this week with another defeat, this time at the hands of "
        f"{winner(game)}. Better days cannot come soon enough.",
        f"The losses continue to pile up for {loser(game)}. Finding positives has become increasingly "
        f"difficult.",
        f"{loser_name(game, True)} remain stuck near the bottom of the standings after another disappointing "
        f"result. The search for answers continues.",
        f"Another week brought another setback for {loser(game)}. Their season has become an uphill battle.",
        f"{loser(game, True)} hoped to build momentum this week but instead suffered another loss. "
        f"The frustration is beginning to show."
    ]

    upset = [
        f"In one of the season's biggest surprises, {winner(game)} stunned the league with an incredible "
        f"upset victory. Nobody expected this result.",
        f"{winner(game, True)} shocked everyone this week by defeating a heavily favored opponent. For "
        f"one day, they looked unstoppable.",
        f"The impossible became reality as {winner(game)} earned a stunning victory. Fans will be talking "
        f"about this game for weeks.",
        f"{winner(game, True)} entered the matchup against {loser(game)} as a clear underdog but left as the "
        f"winner. It may be the upset of the season.",
        f"A struggling season produced a memorable moment this week as {winner(game)} knocked off one "
        f"of the league's best teams in {loser(game)}."
    ]

    winning_streak = [
        f"{winner(game, True)} may have waited a long time, but they are finally building momentum. "
        f"Their recent play has been impossible to ignore.",
        f"After months near the bottom of the standings, {winner(game)} is beginning to show signs of life. "
        f"A late-season run is underway.",
        f"{winner(game, True)} continued its surprising turnaround this week against "
        f"{loser(game)}. What once seemed impossible now feels within reach.",
        f"The league's former cellar-dwellers are suddenly winning games. {winner_city(game)} has become one of the "
        f"most interesting stories in the league.",
        f"{winner_name(game, True)} refuse to quit despite the odds. Their recent surge has created unexpected "
        f"excitement."
    ]

    elimination = [
        f"{loser_city(game)}'s playoff hopes officially came to an end this week against {winner(game)}. Their "
        f"focus now turns toward next season.",
        f"A difficult year reached another disappointing milestone as {loser_name(game)} were eliminated from "
        f"postseason contention this week.",
        f"The math is now official: {loser(game)} can no longer reach the playoffs. The organization "
        f"faces important questions moving forward.",
        f"{loser_city(game)}'s season will end without a playoff appearance. Attention has already begun shifting "
        f"toward the future.",
        f"After a long struggle, {loser_name(game)} were officially eliminated this week. Their remaining games will be "
        f"about pride and development."
    ]

    options = [loses_again, upset, winning_streak, elimination]
    weight = [35, 80, 60, 45]

    return [random.choice(options[headline_index]), weight[headline_index], game]

# Game Headlines
def close_game_headlines(game, headline_index):
    small_margin = [
        f"{matchup(game, True)} came down to the smallest of margins. One or two plays may have made all the "
        f"difference.",
        f"Neither side deserved to lose after such a tightly contested battle. Unfortunately, only {winner(game)} "
        f"could leave with the win.",
        f"The intensity never faded as {matchup_and(game)} traded blows throughout the matchup. Fans got their money's "
        f"worth from this one.",
        f"For every answer {winner(game)} provided, {loser(game)} had a response. The result remained in doubt "
        f"until the very end.",
        f"{matchup(game, True)} featured everything fans could hope for: momentum swings, late drama, and a "
        f"finish that came down to the wire."
    ]

    overtime = [
        f"{winner(game, True)} survived an overtime thriller against {loser(game)}. Every point mattered in "
        f"one of the week's most dramatic finishes.",
        f"{matchup_and(game, True)} needed extra time to settle the score. In the end, {winner(game)} found a "
        f"way to escape with the win.",
        f"Regulation wasn't enough in the battle between {matchup_and(game)}. {winner(game, True)} eventually "
        f"pulled ahead when it mattered most.",
        f"Fans got their money's worth as {matchup(game)} went to overtime. {winner(game, True)} "
        f"outlasted {loser(game)} in a game neither side wanted to lose.",
        f"{loser(game, True)} pushed the game beyond regulation, but {winner(game)} had the final answer. The "
        f"overtime victory could prove important later in the season."
    ]

    almost_upset = [
        f"{loser(game, True)} nearly pulled off one of the season's biggest upsets. Instead, {winner(game)} "
        f"narrowly avoided disaster.",
        f"For a moment, it looked like {loser(game)} might shock the league. {winner(game, True)} "
        f"managed to hold on and escape with the victory.",
        f"{winner(game, True)} entered as the favorite, but {loser(game)} made them earn every point. The "
        f"close call serves as a warning that no win comes easy.",
        f"The result favored {winner(game)}, but the story was how close {loser(game)} came to changing everything. "
        f"Few expected such a competitive battle.",
        f"{loser(game, True)} came within reach of a statement win before {winner(game)} slammed the door "
        f"shut. The favorites survived, but not comfortably.",
    ]

    options = [small_margin, overtime, almost_upset]
    weight = [80, 85, 70]

    return [random.choice(options[headline_index]), weight[headline_index], game]

def blowout_headlines(game, headline_index):
    large_margin = [
        f"The outcome was effectively decided long before the game ended. {winner(game, True)} controlled the "
        f"matchup from start to finish.",
        f"{winner(game, True)} put together a performance that bordered on perfection. "
        f"{loser(game, True)} never found a way back into the game.",
        f"What looked competitive on paper quickly turned into a one-sided affair. {winner(game, True)} was "
        f"simply too much to handle.",
        f"{winner(game, True)} imposed its will early and never looked back. The final result was as "
        f"decisive as they come.",
        f"Every phase of the game tilted heavily in favor of {winner(game)}. The scoreboard reflected complete domination."
    ]

    expected_blowout = [
        f"{winner(game, True)} handled business exactly as expected. The result was never seriously in doubt "
        f"against {loser(game)}.",
        f"There were few surprises in the matchup between {matchup_and(game)}. {winner(game, True)} dominated "
        f"from start to finish.",
        f"{loser(game, True)} had no answer for the league's stronger side. {winner(game)} cruised to a "
        f"comfortable victory.",
        f"{winner(game, True)} delivered the kind of performance fans expected to see. The blowout win "
        f"reinforced their status as one of the teams to beat.",
        f"From the opening whistle, {winner(game)} controlled every aspect of the game. {loser(game, True)} "
        f"never found a way back into the contest."
    ]

    surprise_blowout = [
        f"Few saw this coming. {winner(game, True)} completely overwhelmed {loser(game)} in one of the week's "
        f"most surprising results.",
        f"The final margin left plenty of jaws on the floor. {winner(game, True)} turned a seemingly "
        f"competitive matchup into a rout.",
        f"{loser(game, True)} entered with higher expectations, but {winner(game)} stole the spotlight with "
        f"a dominant performance.",
        f"What looked like an even contest quickly became a one-sided affair. {winner(game, True)} delivered "
        f"a statement win over {loser(game)}.",
        f"{winner(game, True)} shocked the league by dismantling {loser(game)}. The result could change how "
        f"both teams are viewed moving forward."
    ]

    options = [large_margin, expected_blowout, surprise_blowout]
    weight = [50, 25, 75]

    return [random.choice(options[headline_index]), weight[headline_index], game]

def rivalry_headlines(game, headline_index):
    upcoming_rivalry = [
        f"The next chapter of the rivalry between {matchup_and(game)} is almost here. Both sides will be eager to "
        f"claim bragging rights.",
        f"There may be bigger games on the schedule, but few carry the emotion of {matchup(game)}. Rivalries have a "
        f"way of bringing out the best performances.",
        f"The standings can wait for a moment. All eyes are turning toward the rivalry clash between "
        f"{matchup_and(game)}.",
        f"History will once again take center stage when {matchup(game)} meet this week. Rivalry games "
        f"rarely disappoint.",
        f"Records often go out the window when {matchup_and(game)} face one another. Another memorable chapter "
        f"could be on the way.",
        f"The rivalry between {matchup_and(game)} has produced plenty of unforgettable moments. Fans are hoping the "
        f"next one arrives this week.",
        f"There is no shortage of anticipation ahead of {matchup(game)}. Both teams know exactly what this game means "
        f"to their supporters.",
        f"Few games generate as much excitement as a rivalry matchup. {matchup(game, True)} should deliver "
        f"plenty of drama.",
        f"The schedule says it is just another game, but no fan of the sport sees it that way. "
        f"{matchup(game, True)} carries extra weight every season.",
        f"Emotions will run high when {matchup_and(game)} meet again. What stories will come out of this rivalry game "
        f"this year?"
    ]

    rivalry_close = [
        f"The latest rivalry battle between {matchup_and(game)} lived up to the hype. {winner(game, True)} "
        f"escaped with a narrow victory.",
        f"Neither side could create much separation in the rivalry showdown between {matchup_and(game)}. In the "
        f"end, {winner(game)} made just enough plays to win.",
        f"Fans were treated to another classic chapter in the rivalry between {matchup_and(game)}. "
        f"{winner(game, True)} barely held off {loser(game)}.",
        f"The rivalry remains as competitive as ever after a tightly contested battle. {winner(game)} emerged "
        f"victorious, but only by the slimmest of margins.",
        f"There was little to separate the teams in the latest rivalry matchup. {winner(game, True)} found a "
        f"way to edge out {loser(game)} when it mattered most."
    ]

    rivalry_overtime = [
        f"The rivalry between {matchup_and(game)} needed overtime to produce a winner. {winner(game, True)} "
        f"eventually came out on top.",
        f"One of the season's most anticipated rivalry games delivered extra drama. {winner(game)} survived an "
        f"overtime battle against {loser(game)}.",
        f"Regulation was not enough to settle the rivalry showdown between {matchup_and(game)}. "
        f"{winner(game, True)} finally broke through in overtime.",
        f"The latest rivalry chapter added another unforgettable moment to the history books. {winner(game)} claimed "
        f"victory after extra time was required.",
        f"Fans witnessed a rivalry game worthy of its reputation. {winner(game, True)} outlasted "
        f"{loser(game)} in a thrilling overtime finish."
    ]

    rivalry_blowout = [
        f"Rivalry games are usually close, but this one was anything but. {winner(game, True)} dominated "
        f"from start to finish.",
        f"The latest rivalry matchup quickly turned one-sided. {winner(game)} overwhelmed {loser(game)} in emphatic "
        f"fashion.",
        f"Few expected such a lopsided result between rivals. {winner(game, True)} left no doubt about who "
        f"controlled the game.",
        f"The rivalry bragging rights belong firmly to {winner(game)} after a convincing blowout victory. "
        f"{loser(game, True)} never found an answer.",
        f"Instead of a classic rivalry thriller, fans saw a statement performance. {winner(game, True)} "
        f"completely dismantled {loser(game)} this week."
    ]

    options = [upcoming_rivalry, rivalry_close, rivalry_overtime, rivalry_blowout]
    weight = [80, 90, 95, 70]

    return [random.choice(options[headline_index]), weight[headline_index], game]

def tight_race_headlines(game, headline_index):
    upcoming_tight = [
        f"A heavyweight showdown is approaching as {matchup_and(game)} prepare to meet. Few games this season carry "
        f"greater importance.",
        f"The spotlight belongs to {matchup_and(game)} this week. Both teams have established themselves among the "
        f"league's elite.",
        f"Fans won't have to wait much longer for one of the season's biggest matchups. {matchup(game, True)} "
        f"should have major implications.",
        f"When top teams collide, everyone pays attention. That is exactly what will happen when {matchup_and(game)} "
        f"take the field this upcoming week.",
        f"The upcoming battle between {matchup_and(game)} could shape the race for the top of the standings. Both "
        f"sides have plenty to prove.",
        f"Few matchups generate as much excitement as a meeting between contenders. {matchup(game, True)} this "
        f"week fits that description perfectly.",
        f"The league's attention is fixed on {matchup(game)} this week. A clash between two of the best teams is "
        f"always worth watching.",
        f"There are great games, and then there are statement games. The meeting between {matchup_and(game)} falls "
        f"firmly into the second category.",
        f"The schedule makers could not have asked for a better marquee matchup. {matchup(game, True)} has all "
        f"the ingredients of a classic.",
        f"Both teams have spent weeks establishing themselves as contenders. Now {matchup(game)} will decide which "
        f"side gains the upper hand."
    ]
    
    tight_close = [
        f"The battle between contenders lived up to expectations. {winner(game, True)} narrowly defeated "
        f"{loser(game)} in a game that could have gone either way.",
        f"There was little separating the league's top teams this week. {winner(game)} emerged with the win after "
        f"a hard-fought contest.",
        f"The showdown between {matchup_and(game)} delivered exactly the drama fans expected. "
        f"{winner(game, True)} survived by the slimmest of margins.",
        f"Top teams often produce memorable games, and this was no exception. {winner(game)} found a way to edge "
        f"past {loser(game)}.",
        f"Every possession mattered when two contenders met this week. {winner(game, True)} ultimately secured "
        f"a valuable close victory."
    ]

    tight_overtime = [
        f"The clash between contenders needed overtime to determine a winner. {winner(game, True)} finally "
        f"broke through against {loser(game)}.",
        f"When two top teams meet, drama often follows. {winner(game)} prevailed only after an overtime battle.",
        f"The league's marquee matchup delivered on every level. {winner(game, True)} outlasted {loser(game)} "
        f"in overtime.",
        f"Fans expecting a classic showdown were not disappointed. {winner(game)} secured an overtime win in one of "
        f"the season's biggest games.",
        f"Regulation could not separate two of the league's strongest teams. {winner(game, True)} eventually "
        f"claimed victory in extra time."
    ]
    
    tight_blowout = [
        f"The showdown between contenders turned surprisingly one-sided. {winner(game, True)} dominated a "
        f"team many considered an equal.",
        f"What looked like a clash of titans quickly became a statement victory. {winner(game)} overwhelmed "
        f"{loser(game)} from the opening whistle.",
        f"Few expected such a decisive result between elite teams. {winner(game, True)} left no doubt about "
        f"who was better on this day.",
        f"The matchup of contenders ended with a clear winner. {winner(game)} delivered a performance that could "
        f"reshape the championship conversation.",
        f"Instead of a close battle, fans witnessed complete control. {winner(game, True)} dismantled "
        f"{loser(game)} in convincing fashion."
    ]

    options = [upcoming_tight, tight_close, tight_overtime, tight_blowout]
    weight = [85, 90, 95, 80]

    return [random.choice(options[headline_index]), weight[headline_index], game]


# Week Headlines
def first_week_headlines(team=(None, None), headline_index=0):
    first_week = [
        f"A new season is officially underway. Every team still believes a championship is possible.",
        f"The wait is over as another season begins. Expectations are high across the league.",
        f"Opening week has arrived and the race for the championship is officially on.",
        f"Months of preparation have led to this moment. The new season is finally here.",
        f"Fresh hopes and fresh storylines define the opening week. Every contender starts with a clean slate.",
        f"Excitement, questions, and plenty of surprises. The road to the championship has officially begun.",
        f"Every contender starts the week with the same record, but that won't last for long. Opening week is about "
        f"to begin shaping the season.",
        f"The offseason is over and teams across the league are taking their first steps toward a championship.",
        f"Opening week rarely answers every question, but it always creates new storylines. We've made it.",
        f"Months of anticipation give way to meaningful competition this week. The chase for the championship "
        f"has begun."
    ]

    champ = [
        f"{team[0]} enters the new season with a target on their back. Defending a championship is never easy.",
        f"The reigning champions are back in action. The {team[1]} will attempt to prove last "
        f"season was no fluke.",
        f"A new season begins, but the {team[1]} still hold the title everyone wants. The defense for the "
        f"championship starts now.",
        f"Every contender will be chasing {team[0]} this season. The defending champions are ready for the "
        f"challenge.",
        f"The banner may belong to last season, but expectations remain sky-high. {team[0]} "
        f"begin their quest for another title."
    ]

    last_year_contenders = [
        f"{team[0]} came close to reaching the top last season. Now they begin another "
        f"attempt to finish the job.",
        f"Last season ended in disappointment, but {team[0]} enters the new year with championship "
        f"ambitions intact.",
        f"The {team[1]} spent the offseason thinking about what might have been. The opportunity "
        f"for redemption starts now.",
        f"Few teams were closer to a title than the {team[1]} last season. They now begin a new campaign "
        f"determined to go one step further.",
        f"The hunger remains strong for {team[0]} after last season's near miss. Expectations "
        f"are once again running high."
    ]

    options = [first_week, champ, last_year_contenders]
    weight = [0, 0, 80]

    return [random.choice(options[headline_index]), weight[headline_index], team]

def second_week_headlines(game=None, headline_index=0):
    second_week = [
        f"Week one provided the first glimpse of which teams may contend and which teams may struggle. The season "
        f"is officially underway.",
        f"Fans finally got their first look at this year's teams in action. Early impressions are beginning to "
        f"form around the league.",
        f"Every team entered the week full of optimism. Some strengthened those hopes, while others were given an "
        f"early wake-up call.",
        f"The standings may still be young, but opening week provided plenty of reasons for excitement. A "
        f"fascinating season appears to be ahead.",
        f"The first chapter of the season has been written. Teams now begin the long process of turning "
        f"expectations into results."
    ]

    early_winners = [
        f"{winner(game, True)} could not have asked for a better start. They open the season with a "
        f"1-0 record.",
        f"The first week is complete, and {winner_city(game)} sits undefeated. It is only one game, but it is a "
        f"promising beginning.",
        f"{winner(game, True)} started the season on the right foot with an opening-week victory. Early "
        f"momentum can be valuable.",
        f"There are plenty of games left to play, but {winner_name(game)} have already secured an important first win.",
        f"The opening week brought success for {winner(game)}. They leave with a perfect 1-0 record.",
        f"A strong start is often important, and {winner_city(game)} has one after winning their season opener.",
        f"{winner(game, True)} wasted no time making a positive impression. Week one ended with a "
        f"victory in the standings.",
        f"The road ahead remains long, but {winner_name(game)} begin it with a win. A 1-0 record is exactly what they "
        f"hoped for.",
        f"{winner(game, True)} made the most of their first opportunity. They start the season unbeaten "
        f"after one week.",
        f"The season opener went according to plan for {winner(game)}. Their first win puts them in a favorable "
        f"early position."
    ]

    early_losers = [
        f"{loser_city(game)} opens the season searching for answers after falling to 0-1. Not the ideal start, but there is "
        f"still plenty of time to recover.",
        f"The season is only one week old, but {loser(game)} already find themselves playing from behind. "
        f"Their opener ended in defeat.",
        f"{loser(game, True)} hoped for a better start to the year. Instead, they begin the season "
        f"with a loss.",
        f"Week one did not go according to plan for {loser(game)}. They now turn their attention toward "
        f"avoiding an 0-2 start.",
        f"The first result of the season landed in the wrong column for {loser(game)}. Their "
        f"record sits at 0-1.",
        f"There is no reason to panic yet, but {loser(game)} will be eager to bounce back after an opening-week "
        f"defeat.",
        f"{loser_name(game, True)} leave the first week still searching for their first victory. The season "
        f"opener proved disappointing.",
        f"The standings are young, but {loser_city(game)} already faces the challenge of recovering from a slow start.",
        f"Opening-day optimism gave way to frustration for {loser(game, True)}. Their season begins "
        f"with a loss.",
        f"{loser(game)} will have an opportunity to respond next week, but for now they sit at 0-1 after "
        f"dropping their opener."
    ]

    options = [second_week, early_winners, early_losers]
    weight = [0, 80, 60]

    return [random.choice(options[headline_index]), weight[headline_index], game]

def third_week_headlines(game=None, headline_index=0):
    third_week = [
        "With two weeks in the books, early trends are beginning to emerge. Some teams are validating expectations "
        "while others are searching for answers.",
        "The season is still young, but week two provided valuable clues about the league's true contenders. Every "
        "win is becoming more meaningful.",
        "Two weeks of action have already produced several surprises. Teams are beginning to separate themselves from "
        "the pack.",
        "The opening excitement has settled into reality as week two comes to a close. Some early success stories "
        "appear legitimate.",
        "Week two reinforced one important lesson: no team can afford to fall behind. The standings are beginning to "
        "take shape."
    ]

    early_winners = [
        f"{winner(game, True)} opened the season with back-to-back victories. Early momentum is quickly "
        f"becoming one of their greatest strengths.",
        f"Two games, two wins for {winner(game)}. Their perfect start has fans wondering how high this team "
        f"can climb.",
        f"{winner(game, True)} remained unbeaten by securing their second consecutive victory. The strong "
        f"start is impossible to ignore.",
        f"Another week brought another win for {winner(game)}. They now sit at 2-0 and look ready to "
        f"challenge anyone.",
        f"{winner(game, True)} showed early doubters this week why they shouldn't be slept on this "
        f"season. Their second win keeps the early success rolling."
    ]

    early_losers = [
        f"The season has gotten off to a difficult start for {loser(game)}. Two games have produced "
        f"two losses and plenty of questions.",
        f"{loser_city(game)} continues to search for answers after falling to 0-2. The urgency is already "
        f"beginning to build.",
        f"Another week brought another setback for {loser(game)}. Their winless start now stretches through "
        f"two games.",
        f"{loser(game, True)} hoped to bounce back, but the result only deepened their early struggles. "
        f"An 0-2 record haunts the start to their season.",
        f"The pressure continues to grow around {loser(game)}. Their second straight loss puts them in an "
        f"early hole."
    ]

    options = [third_week, early_winners, early_losers]
    weight = [0, 80, 55]

    return [random.choice(options[headline_index]), weight[headline_index], game]

def fourth_week_headlines(game=None, headline_index=0):
    fourth_week = [
        f"Three weeks into the season, the league is beginning to reveal its identity. Early contenders are "
        f"starting to establish themselves.",
        f"The season's opening phase is nearing completion, and teams can no longer rely on small sample sizes. "
        f"Every result now carries greater weight.",
        f"Week three offered a clearer picture of where teams stand. Some are building momentum while others are "
        f"already facing pressure.",
        f"The standings are becoming more meaningful with each passing week. Several teams have already begun "
        f"separating from the field.",
        f"Three weeks of action have created plenty of storylines. The race for playoff positioning is beginning "
        f"earlier than expected."
    ]

    early_winners = [
        f"{winner(game, True)} has stormed out to a 3-0 start. Few teams have looked stronger through "
        f"the opening stretch.",
        f"Three games have produced three victories for {winner(game)}. Their perfect record is becoming one of "
        f"the league's biggest stories.",
        f"{winner(game, True)} continued their unbeaten run with another impressive performance. A 3-0 "
        f"start has them sitting near the top of the standings.",
        f"The momentum keeps building for {winner(game)}. Their third straight win confirms this team is a "
        f"serious contender.",
        f"{winner_city(game)} remains flawless through three weeks of action. The rest of the league is beginning to "
        f"take notice."
    ]

    early_losers = [
        f"The hole keeps getting deeper for {loser(game)}. Three games into the season, they remain without a "
        f"victory.",
        f"{loser(game, True)} dropped to 0-3 after another disappointing result. Time is already "
        f"becoming a factor.",
        f"The search for a breakthrough win continues for {loser(game)}. Their third straight loss has created "
        f"a difficult situation.",
        f"{loser(game, True)} hoped this would be the week things changed. Instead, they remain winless "
        f"through three contests.",
        f"The season is still young, but {loser_city(game)} is already facing an uphill climb. An 0-3 start leaves "
        f"little margin for mistakes."
    ]

    options = [fourth_week, early_winners, early_losers]
    weight = [0, 75, 65]

    return [random.choice(options[headline_index]), weight[headline_index], game]

def down_the_stretch_headlines(game=None, headline_index=0):
    important_games = [
        f"With the season winding down, the upcoming matchup between {matchup_and(game)} could have major playoff "
        f"implications. Neither team can afford to give ground at this stage.",
        f"The race for postseason positioning continues when {matchup_and(game)} meet this week. A single result "
        f"could dramatically shift the standings.",
        f"Every game matters this late in the season, especially when direct competitors face off. "
        f"{matchup(game, True)} could have a lasting impact on the playoff picture.",
        f"The margin for error is shrinking as {matchup_and(game)} prepare to meet. Both teams know this matchup may "
        f"determine who gains the upper hand in the standings.",
        f"The postseason is approaching quickly, making the showdown between {matchup_and(game)} one of the most "
        f"important games of the week. The stakes are impossible to ignore."
    ]

    increasing_playoff_position = [
        f"{winner(game, True)} took a major step toward securing favorable playoff positioning. The "
        f"victory could pay dividends long after the regular season ends.",
        f"The win was worth more than just another mark in the standings for {winner(game)}. Their path toward "
        f"a strong playoff seed looks much clearer now.",
        f"{winner(game, True)} strengthened its postseason outlook with a critical victory. Every "
        f"advantage matters as the playoff race tightens.",
        f"Timing could not have been better for {winner(game)}. The win significantly improves their "
        f"chances of entering the playoffs from a position of strength.",
        f"{winner(game, True)} may have secured one of the most important wins of its season. The "
        f"result provides a valuable boost in the battle for playoff positioning."
    ]

    escaping_elimination = [
        f"{winner(game, True)} kept its season alive with a crucial victory. Elimination will have to "
        f"wait at least one more week.",
        f"Facing enormous pressure, {winner(game)} delivered exactly the result it needed. Their playoff hopes "
        f"remain alive.",
        f"{winner(game, True)} refused to see its season come to an end. The win keeps the door open "
        f"for a postseason run.",
        f"The situation was desperate, but {winner(game)} responded with one of its biggest wins of the "
        f"year. Their hopes are still breathing.",
        f"{winner(game, True)} entered the game with little room for error and emerged with a "
        f"lifeline. The fight for survival continues."
    ]

    options = [important_games, increasing_playoff_position, escaping_elimination]
    weight = [95, 85, 80]

    return [random.choice(options[headline_index]), weight[headline_index], game]

def final_week_headlines(game=None, headline_index=0):
    final_week = [
        "The regular season has reached its conclusion. Months of competition have led to this moment.",
        "One final week remains in the race for postseason glory. Every game carries enormous implications.",
        "The playoff picture is nearly complete, but several critical questions remain unanswered. The final week "
        "promises drama.",
        "There are no more second chances after this week. Teams must seize the opportunities still in front of them.",
        "Championship dreams remain alive for some, while others are simply trying to extend their season. The "
        "stakes have never been higher.",
        "The regular season's final chapter is here. Every result could reshape the playoff bracket.",
        "Months of hard work now come down to a single week. Teams across the league are feeling the pressure.",
        "For contenders, the goal is clear: enter the postseason with momentum. For everyone else, survival remains "
        "the priority.",
        "The standings may look settled, but the final week has a habit of producing surprises. Nothing is "
        "guaranteed until the final whistle.",
        "One last round of games stands between the league and the playoffs. The road to the championship is "
        "about to begin in earnest."
    ]

    important_games = [
        f"Everything comes down to this. The final matchup between {matchup_and(game)} could determine who reaches "
        f"the playoffs.",
        f"The stakes could not be higher as {matchup_and(game)} meet in the season finale. A playoff spot may hang in "
        f"the balance.",
        f"One game remains, and it carries enormous consequences. The outcome of {matchup(game)} could reshape the "
        f"postseason picture.",
        f"The regular season ends with a showdown that matters. {matchup_and(game, True)} will battle with "
        f"playoff hopes on the line.",
        f"Fans could hardly ask for a more meaningful finale. The clash between {matchup_and(game)} may decide who "
        f"keeps playing and who goes home."
    ]

    last_chance = [
        f"There is no room for error left for {loser(game)}. Their final game is effectively a playoff game "
        f"before the playoffs begin.",
        f"{loser_name(game, True)} enter the last week knowing exactly what is required. A win is necessary to "
        f"keep their postseason hopes alive.",
        f"The path is simple for {loser(game)} but far from easy. They must win in the final week or risk "
        f"seeing their season end.",
        f"Every possession will matter when {loser(game)} takes the field next week. Their playoff dreams "
        f"depend on securing a victory.",
        f"{loser_city(game)} has reached the point where only one result matters. Anything short of a win could bring "
        f"their season to a close."
    ]

    options = [final_week, important_games, last_chance]
    weight = [0, 100, 80]

    return [random.choice(options[headline_index]), weight[headline_index], game]

# Playoff Headlines
def playoff_headlines(game=None, headline_index = 0):
    close_playoff_game = [
        f"Playoff intensity was on full display as {winner(game)} narrowly defeated {loser(game)}. Every possession "
        f"carried enormous weight.",
        f"The postseason delivered another thriller. {winner(game, True)} escaped with a hard-fought victory "
        f"over {loser(game)}.",
        f"There was little separating the teams throughout the playoff battle. {winner(game, True)} made just "
        f"enough plays to survive.",
        f"The margin between victory and defeat was razor-thin. {winner(game, True)} came out on top in a "
        f"game that could have gone either way.",
        f"Fans witnessed playoff drama at its finest. {winner(game, True)} edged out {loser(game)} in a tense "
        f"contest.",
        f"Neither team was willing to give an inch during the postseason showdown. {winner(game)} eventually found the "
        f"breakthrough it needed.",
        f"The stakes were high and the game reflected it. {winner(game, True)} survived a fierce challenge "
        f"from {loser(game)}.",
        f"Every point felt critical in the playoff matchup between {matchup(game)}. {winner(game, True)} "
        f"ultimately secured the win.",
        f"The postseason often produces unforgettable finishes, and this game was no exception. {winner(game)} held "
        f"off {loser(game)} in dramatic fashion.",
        f"Late-game execution proved decisive as {winner(game)} earned a narrow playoff victory. "
        f"{loser(game, True)} pushed them to the limit.",
        f"The playoff race grew even more intense after a tightly contested battle. {winner(game, True)} "
        f"emerged victorious by the slimmest of margins.",
        f"Neither side could pull away in a game filled with tension and momentum swings. {winner(game)} eventually "
        f"claimed the result.",
        f"Championship aspirations were on the line throughout the contest. {winner(game, True)} delivered "
        f"when the pressure was greatest.",
        f"The crowd was treated to a playoff classic between {matchup(game)}. {winner(game, True)} barely "
        f"held off {loser(game)}.",
        f"A single bounce or break could have changed everything. Instead, {winner(game)} walked away with a "
        f"crucial playoff victory."
    ]

    blowout_playoff_game = [
        f"Playoff games are often competitive, but this one was anything but. {winner(game, True)} dominated "
        f"from beginning to end.",
        f"{winner(game, True)} delivered a statement performance in the postseason. {loser(game)} had no "
        f"answer for the onslaught.",
        f"The playoff matchup quickly turned one-sided as {winner(game)} seized complete control. The result was "
        f"never seriously in doubt.",
        f"{winner(game, True)} overwhelmed {loser(game)} in a performance that sent a message to the rest "
        f"of the field.",
        f"There was little drama in this postseason contest. {winner(game)} cruised to one of the most convincing "
        f"wins of the playoffs.",
        f"Championship contenders often make statements in the playoffs, and {winner(game, True)} certainly "
        f"did that here.",
        f"{loser(game, True)} entered with hopes of advancing, but {winner(game)} completely took over "
        f"the game.",
        f"The postseason spotlight belonged entirely to {winner(game, True)}. Their dominant victory left "
        f"no room for debate.",
        f"Instead of a close battle, fans witnessed a playoff rout. {winner(game)} controlled every phase of the "
        f"contest.",
        f"{winner(game, True)} looked every bit like a championship contender while dismantling {loser(game)} "
        f"in convincing fashion."
    ]

    rivalry_playoff_game = [
        f"The rivalry between {matchup_and(game)} reached the postseason stage, and {winner(game)} emerged "
        f"victorious. The win will be remembered for years.",
        f"Rivalry games carry extra emotion, especially in the playoffs. {winner(game, True)} claimed bragging "
        f"rights and a postseason victory.",
        f"The stakes were already high, but the rivalry made them even higher. {winner(game)} defeated {loser(game)} "
        f"in a memorable playoff clash.",
        f"The latest chapter in the rivalry between {matchup(game)} unfolded under playoff pressure. "
        f"{winner(game, True)} came out on top.",
        f"Few postseason matchups generate as much excitement as a rivalry game. {winner(game)} delivered when it "
        f"mattered most.",
        f"History and playoff implications collided when {matchup_and(game)} met. {winner(game, True)} "
        f"secured a massive victory.",
        f"The rivalry showdown did not disappoint. {winner(game)} added another memorable chapter by defeating "
        f"{loser(game)} in the postseason.",
        f"Playoff games are intense by nature, but rivalries take them to another level. {winner(game, True)} "
        f"survived the emotional battle.",
        f"Fans were treated to a rivalry game with everything on the line. {winner(game)} emerged victorious and "
        f"moved one step closer to a championship.",
        f"The postseason spotlight amplified an already fierce rivalry. {winner(game, True)} seized the "
        f"moment and defeated {loser(game)}."
    ]

    options = [close_playoff_game, blowout_playoff_game, rivalry_playoff_game]
    weight = [95, 60, 100]

    return [random.choice(options[headline_index]), weight[headline_index], game]

def conference_semis_headlines(game=None, headline_index=0):
    important_results = [
        f"The regular season ended with everything on the line, and {winner(game)} delivered. The result reshaped the "
        f"playoff picture at the final possible moment.",
        f"One final game produced one final twist in the standings. {winner(game, True)} secured a crucial "
        f"victory with postseason implications throughout the league.",
        f"The stakes could not have been higher in the season finale between {matchup_and(game)}. "
        f"{winner(game, True)} rose to the occasion when it mattered most.",
        f"The playoff race came down to the wire, and {winner(game)} took advantage. Their season-saving victory "
        f"capped off a dramatic regular season.",
        f"Fans could hardly have asked for a more meaningful finale. {winner(game, True)} secured a result "
        f"that will be remembered long after the regular season ends.",
        f"The final week delivered exactly the drama everyone hoped for. {winner(game), True} emerged victorious in a "
        f"game with major postseason consequences.",
        f"Months of competition came down to one decisive result. {winner(game, True)} earned the win and "
        f"altered the playoff landscape.",
        f"The regular season closed with pressure on both sides. {winner(game, True)} handled the moment "
        f"and walked away with a critical victory.",
        f"Every possession mattered in one of the season's most important games. {winner(game, True)} found a "
        f"way to secure the result they needed.",
        f"The postseason picture became much clearer after the final whistle. {winner(game), True} finished the "
        f"regular season with a statement victory."
    ]

    playoffs_in = [
        f"{winner_city(game)} has officially punched its ticket to the postseason. The opportunity to compete for a "
        f"championship remains alive.",
        f"The playoff field is now set, and {winner(game)} will be part of it. Their season continues.",
        f"{winner(game, True)} achieved one of its primary goals by securing a postseason berth. The "
        f"real challenge now begins.",
        f"The hard work of the regular season has paid off for {winner(game)}. A playoff spot is officially "
        f"theirs.",
        f"{winner(game, True)} will have a chance to compete on the postseason stage after securing "
        f"qualification this week.",
        f"The path was not always smooth, but {winner_city(game)} has reached the playoffs. Their championship hopes "
        f"remain intact.",
        f"{winner(game, True)} did enough throughout the season to earn a place in the postseason. Fans "
        f"now turn their attention to the playoffs.",
        f"Celebration is in order for {winner(game)}. Their season will continue beyond the regular schedule.",
        f"The playoff dream is now reality for {winner(game, True)}. They have officially secured "
        f"their place in the bracket.",
        f"{winner(game)} survived the long regular season and emerged with a postseason berth. The next "
        f"chapter begins now.",
        f"A playoff spot once seemed uncertain, but {winner(game)} made it happen. Their season is far from "
        f"over.",
        f"{winner(game, True)} secured the result it needed and will be playing in the postseason. The "
        f"stakes only get higher from here.",
        f"The door to the championship remains open for {winner(game)} after clinching a playoff berth.",
        f"{winner(game, True)} earned its way into the postseason field. Every game from this point "
        f"forward will carry enormous importance.",
        f"The regular season mission is complete for {winner(game)}. They are headed to the playoffs."
    ]

    playoffs_out = [
        f"The season has come to an end for {loser(game)}. Their playoff hopes officially fell short.",
        f"{loser(game, True)} fought hard but will not be part of the postseason field. The offseason "
        f"begins now.",
        f"The playoff race proved too difficult for {loser(game)} to overcome. Their season ends outside the "
        f"bracket.",
        f"{loser(game, True)} came up short in its pursuit of a postseason berth. The disappointment "
        f"will linger into the offseason.",
        f"The margin between success and failure was small, but {loser(game)} landed on the wrong side of it. "
        f"Their season is over.",
        f"{loser(game, True)} will be watching the playoffs rather than participating in them. Their "
        f"campaign has reached its conclusion.",
        f"The postseason dream slipped away from {loser(game)} this week. There will be no second chance "
        f"this season.",
        f"{loser(game, True)} entered the year with playoff ambitions but ultimately fell short of "
        f"qualification.",
        f"The final standings were not kind to {loser(game)}. Their season ends before the postseason begins.",
        f"{loser(game, True)} could not secure a place in the playoff field. Attention now shifts "
        f"toward next season."
    ]

    top_seeds = [
        f"{winner(game, True)} finished atop the division and earned a valuable first-round bye. The "
        f"extra rest could prove crucial in the playoffs.",
        f"The division crown belongs to {winner(game)}. Along with it comes the reward of skipping the opening "
        f"round of the postseason.",
        f"{winner(game, True)} secured first place in the division and positioned itself perfectly for "
        f"a championship run.",
        f"A strong regular season paid off for {winner(game)}. Their division title comes with the benefit of "
        f"a playoff bye.",
        f"{winner(game, True)} captured the division championship and earned extra time to prepare for "
        f"the postseason."
    ]

    upcoming_conference_semifinals = [
        f"The conference semifinals are here, and the matchup between {matchup_and(game)} has all the ingredients of a "
        f"classic.",
        f"A trip to the conference final is on the line when {matchup_and(game)} meet this week. Neither side will "
        f"want their season to end here.",
        f"The postseason spotlight shifts to the conference semifinals. {matchup(game, True)} should be one "
        f"of the most exciting games yet.",
        f"The stakes continue to rise as {matchup_and(game)} prepare for a conference semifinal showdown.",
        f"Only one team can advance when {matchup(game)} meet in the conference semifinals. Fans should expect an "
        f"intense battle."
    ]

    options = [important_results, playoffs_in, playoffs_out, top_seeds, upcoming_conference_semifinals]
    weight = [100, 80, 75, 75, 85]

    return [random.choice(options[headline_index]), weight[headline_index], game]

def conference_finals_headlines(game=None, headline_index=0):
    important_results = [
        f"{winner(game, True)} survived the conference semifinal and moved one step closer to a "
        f"championship.",
        f"The conference semifinal belonged to {winner(game)}. Their postseason journey continues after an impressive "
        f"victory.",
        f"{winner(game, True)} earned a crucial playoff win and secured a place in the conference final.",
        f"The road to a championship remains open for {winner(game)} after a successful conference semifinal "
        f"performance.",
        f"{winner(game, True)} cleared another postseason hurdle by defeating {loser(game)} in the conference "
        f"semifinal."
    ]

    team_moves_on = [
        f"{winner(game, True)} advanced beyond the conference semifinal and remains firmly in the "
        f"championship hunt.",
        f"The conference semifinal hurdle has been cleared by {winner(game)}. Their postseason run continues.",
        f"{winner(game, True)} earned advancement with a strong conference semifinal performance.",
        f"The journey continues for {winner(game)} after successfully navigating the conference semifinal round.",
        f"{winner(game, True)} kept its championship aspirations alive by advancing from the conference "
        f"semifinal."
    ]

    team_eliminated = [
        f"The season came to an end for {loser(game)} in the conference semifinal. Their playoff run stops "
        f"here.",
        f"{loser(game, True)} fought hard but could not survive the conference semifinal round.",
        f"The conference semifinal proved to be the final chapter of the season for {loser(game)}.",
        f"{loser(game, True)} saw its championship hopes end with a conference semifinal defeat.",
        f"The postseason journey is over for {loser(game)} after falling in the conference semifinal."
    ]

    upcoming_conference_finals = [
        f"A place in the championship round is on the line when {matchup_and(game)} meet in the conference final.",
        f"The conference final has arrived, {matchup_and(game)} are just one win away from the biggest stage.",
        f"Everything these teams have worked toward now comes down to the conference final between {matchup(game)}.",
        f"The conference championship race reaches its climax this week. {matchup(game, True)} should be "
        f"unforgettable.",
        f"Only one team can advance beyond the conference final. The showdown between {matchup_and(game)} carries "
        f"enormous stakes."
    ]

    options = [important_results, team_moves_on, team_eliminated, upcoming_conference_finals]
    weight = [90, 75, 50, 75]

    return [random.choice(options[headline_index]), weight[headline_index], game]


def semifinals_headlines(game=None, headline_index=0):
    important_results = [
        f"{winner(game, True)} claimed the conference championship and earned a place in the semifinals.",
        f"The conference title belongs to {winner(game)} after a memorable postseason victory.",
        f"{winner(game, True)} achieved one of the season's biggest milestones by winning the conference "
        f"final.",
        f"The {game.home_team.conference} conference final ended with celebration for {winner(game)} and heartbreak "
        f"for {loser(game)}.",
        f"{winner(game, True)} is moving on after capturing the conference championship in impressive fashion."
    ]

    team_moves_on = [
        f"{winner(game, True)} advanced through the conference final and is now one step closer to a "
        f"title.",
        f"The conference championship victory sends {winner(game)} into the semifinals.",
        f"{winner(game, True)} earned advancement by winning one of the season's most important games.",
        f"The conference final ended with {winner(game)} celebrating a hard-fought victory and a place in the "
        f"semifinals.",
        f"{winner_city(game)} continues its postseason journey after emerging victorious in the conference final."
    ]

    team_eliminated = [
        f"One win short of the next stage, {loser(game)} saw its season end in the conference final.",
        f"{loser(game, True)} came close, but the conference final marked the end of its championship "
        f"pursuit.",
        f"The conference final delivered heartbreak for {loser(game)}. Their season is officially over.",
        f"{loser(game, True)} fell just short of advancing and now turns its attention toward the "
        f"offseason.",
        f"The postseason run ended in the conference final for {loser(game)} after a difficult defeat."
    ]

    upcoming_semifinals = [
        f"The semifinals have arrived, and the matchup between {matchup(game)} promises high-level competition.",
        f"Only four teams remain, making the semifinal clash between {matchup_and(game)} must-watch action.",
        f"A championship appearance is within reach for both sides entering the semifinal between {matchup(game)}.",
        f"The pressure could not be greater as {matchup_and(game)} prepare to battle in the semifinals.",
        f"The road to the championship runs through the semifinal round. {matchup(game, True)} should deliver plenty of drama.",
        f"Every remaining team can see the championship on the horizon. The semifinal between {matchup(game)} is a critical step.",
        f"The semifinal stage is set, and {matchup_and(game)} will compete with everything on the line.",
        f"Fans are in for a treat when {matchup(game)} meet in one of the season's biggest games.",
        f"The stakes continue to rise as {matchup_and(game)} prepare for a semifinal showdown.",
        f"The championship picture will become much clearer after the semifinal between {matchup(game)}."
    ]

    options = [important_results, team_moves_on, team_eliminated, upcoming_semifinals]
    weight = [90, 75, 50, 75]

    return [random.choice(options[headline_index]), weight[headline_index], game]

def finals_headlines(game=None, headline_index=0):
    important_results = [
        f"{winner(game, True)} secured a place in the championship game with a hard-earned semifinal victory.",
        f"The semifinal ended with celebration for {winner(game)}. They are now one win away from a title.",
        f"{winner(game, True)} advanced through the semifinal and kept its championship dreams alive.",
        f"The journey continues for {winner(game)} after a successful performance in the semifinal round.",
        f"{winner(game, True)} earned the right to compete for a championship by winning its semifinal "
        f"matchup.",
        f"The semifinal stage belonged to {winner(game)}. Their reward is a trip to the final.",
        f"{winner(game, True)} overcame a difficult challenge and advanced beyond the semifinal round.",
        f"The championship game now awaits {winner(game)} after a crucial postseason victory.",
        f"{winner(game, True)} delivered when the pressure was highest and secured a place in the final.",
        f"The semifinal obstacle has been cleared by {winner(game)}. One final challenge remains."
    ]

    team_moves_on = [
        f"{winner(game, True)} advanced from the semifinal and secured a place in the championship game.",
        f"The semifinal victory keeps the dream alive for {winner(game)}. One challenge remains.",
        f"{winner(game, True)} punched its ticket to the final with an impressive postseason "
        f"performance.",
        f"The reward for {winner(game)} is a chance to compete for the championship after advancing from the "
        f"semifinal.",
        f"{winner_city(game)} is headed to the title game after successfully navigating the semifinal round."
    ]

    team_eliminated = [
        f"{loser(game, True)} came within one game of the championship but could not advance beyond "
        f"the semifinal.",
        f"The semifinal proved to be the final hurdle {loser(game)} could not overcome.",
        f"{loser(game, True)} saw its title hopes come to an end with a semifinal defeat.",
        f"The postseason journey is over for {loser(game)} after falling in the semifinal round.",
        f"{loser(game, True)} fought its way deep into the playoffs but ultimately came up short in the "
        f"semifinal."
    ]

    upcoming_finals = [
        f"The championship game has arrived, where {matchup_and(game)} will battle for the ultimate prize.",
        f"Everything this season has led to the final between {matchup_and(game)}. A champion will soon be crowned.",
        f"The biggest game of the year belongs to {matchup_and(game)}. Only one team can finish on top.",
        f"A championship is on the line when {matchup_and(game)} meet in the season's final showdown.",
        f"The wait is almost over. {matchup(game, True)} will decide who lifts the trophy.",
        f"Months of competition have produced one final matchup. {matchup_and(game, True)} now stand at the "
        f"center of the spotlight.",
        f"The championship stage is set for {matchup_and(game)}. Neither team is more than one win away from glory.",
        f"Fans could hardly ask for a better ending to the season than {matchup(game)} in the final.",
        f"The road to a championship ends here. {matchup_and(game, True)} will determine who claims the title.",
        f"Two teams remain, and both have earned their place. {matchup(game, True)} is all that stands between "
        f"them and a championship.",
        f"The trophy is within reach for both teams entering the final. {matchup(game, True)} should provide a "
        f"fitting conclusion to the season.",
        f"The championship dream remains alive for both sides as {matchup_and(game)} prepare for the season's biggest "
        f"game.",
        f"All eyes are on {matchup(game)} as the final finally arrives. The stakes could not be higher.",
        f"One final challenge remains for {matchup_and(game)}. The winner will be remembered as champion.",
        f"The season concludes with a championship showdown between {matchup(game)}. It does not get bigger than this."
    ]

    options = [important_results, team_moves_on, team_eliminated, upcoming_finals]
    weight = [90, 85, 50, 0]

    return [random.choice(options[headline_index]), weight[headline_index], game]