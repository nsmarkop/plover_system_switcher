'''
Functionality to switch systems in Plover with commands.
'''

from plover.engine import StenoEngine


def switch_system(engine: StenoEngine, system: str) -> None:
    '''
    Command to switch the current system in Plover.
    '''

    engine.config = {'system_name': system}
