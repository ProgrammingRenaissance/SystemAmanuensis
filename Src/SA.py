"""
A temporary framework for the System Amanuensis product
until a Kivy based implementation can be developed.
"""

from Library.Src import Cmd
from sys import argv
from typing import List, Optional, Union

# Forward declaration of variables
current_commands:List[Union[Cmd, str]]  # type: ignore

class SystemAmanuensis():
  """
  A command line interface for the System Amanuensis product, If none is supplied,
  a prompt will be made for a command.
 
  * The user chooses a command as the initial input to SA.
  * This command then prompts for any needed data unless already supplied on the
    command line. This architecture supports both interactive use and non-interactive
    use from scripts.
  * Once all the command arguments have been collected, the command is run and the
    results are returned to the caller., if any, Commands are run asynchronously unless
    a pipe is supplied for a given action. In that case, the entire pipe can run
    asynchronously. but the user can control whether individual commands within the
    pipe run asynchronously.
  * Wait for another command to be entered. Loop indefinitely until Ctrl-D is received,
    signaling the end of use of this package or the close method is called to close
    the package.
  """

  def add_cmd(self, cmd:Optional[str])->None:
    if type(cmd) != None:
      self.current_commands.append(cmd)

  def remove_cmd(self, cmd:str)->None:
    pass

  def build_cmd(self, cmd:str)->None:
    pass

  def __init__(self, initialCmd:Optional[str])->None:
    self.current_commands = [] # we have an empty list of commands
    self.add_cmd(initialCmd) # Add the command from the command line if any

  
  def __close__(self)->None:
    """
    Do a final shutdown of System Amanuensis 
    """
    for cmd in self.current_commands:
      try:
        cmd.__close__() # Close each running command, if any
      except AttributeError:
        pass # Ignore the exception so we can continue with other commands
             # The command is missing a __close__ method. Once logging has been
             # implemented  this error should be logged so that it can be corrected.

  def doSA(self) -> None:
    """
      Implements the internal logic of System Amanuensis
    """
    if len(self.current_commands) > 0: # We got at least one command on the
                                       # command line
      for cmd in self.current_commands:
        if type(cmd) == str:
          self.remove_cmd(cmd) # Construct any command for which we only had the name
          self.build_cmd(cmd) # Builds the command we will need with selected options
    pass

  def __call__(self)->None:
    if __name__ != '__main__':
      try: # This code catches a keyboard interrupt and closes the application
        pass # Access to the System Amanuensis infrastructure
      except KeyboardInterrupt:
        pass # Discard the interrupt. Once logging is implemented. log it
      finally:
        self.__close__() # Close System Amanuensis
      pass # Invoke System Amanuensis infrastructure from the command line

if __name__ == '__main__':
  doit:bool = False
  if len(argv) == 2:
    doit = True if type(argv[1]) == str else False
    if doit:
      sa:SystemAmanuensis = SystemAmanuensis(argv[1])
  # Only construct the System Amanuensis if we have one command in the argument list
  # and it is a string, meaning that the actual command will have to be built

  try: # This code catches a keyboard interrupt and closes the application
    sa() # Run System Amanuensis
  except KeyboardInterrupt:
    pass # Ignore the exception
  finally:
    sa.__close__() # Always close running commands
