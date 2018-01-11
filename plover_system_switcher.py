'''
Functionality to switch systems in Plover with commands.
'''

from plover.engine import StenoEngine


def switch_system(engine: StenoEngine, system: str) -> None:
    '''
    Command to switch the current system in Plover.

    :param engine: The active Plover engine that is executing the command.
    :type engine: plover.engine.StenoEngine

    :param system: The name of the requested system to switch Plover to using.
    :type system: str
    '''

    engine.config = {'system_name': system}
