from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'demo'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

# Functions
def creating_session(subsession):
        # Import itertools
        import itertools

        # Define the treatments as a list of strings
        treatments = itertools.cycle(
            ['A', 'B', 'C']
        )

        # Loop through all players and assign them a treatment
        for player in subsession.get_players():
            participant = player.participant
            participant.treatment = next(treatments)

# PAGES
class MyPage(Page):
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        treatment = participant.treatment
        return dict(treatment=treatment)

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
