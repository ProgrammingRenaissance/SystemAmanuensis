"""Program to extract XML from a large file and store it in individual files."""

from argparse import ArgumentParser as ap
from pathlib import Path
import sys
from typing import Dict, Final
import Library.Src.PRscript
from Library.Src.PRscript import PRscript as sc, PRargs as ag

blocknames: Path = Path('blockNames.txt')

class extractXml(sc):
    def __init__(self) -> None:
        try:
            self.blockNames() = []
            self.argHandler(  # Capture the command line arguments
                       prog='extractXml',
                       description='Extracts each 2nd level XML block into a separate file')
        except Exception as ex:  # We got an unhandled exception
            self.shutdown()
            raise ex  # Get out

    @property  # should be in extractXml.py
    def blockNames(self) -> List[str]:
        return self._blockNames
    
    @blockNames.setter
    def blockNames(self, blocks:List[str]) -> None:
        print('Entered blockNames setter')
        self._blockNames=blocks

    def shutdown(self) -> None:
        pass

    def handleCollectBlocks(self) -> None:
        pass

    def handleSplitting(self) -> None:
        pass    

    def __call__(self) -> None:
    	"""The mainline of the script"""    
        args:Dict[str, str] = Src.exArgs.getArgs()
        if args[Src.exArgs.collectblock]:
            self.handleCollectBlocks()
        else:
            self.handleSplitting()


class myArgs(ag):
    """Command line arguments for the extractXML script"""
    
    # Define argument dictionary keys
    _srcfile: Final[str] ='srcXml'
    _targetdir:Final[str = 'targetdir'
    _collectblock:Final[str] ='collectBlock'
    _collectblockfile:Final[str] = 'candidateBlockNamesFile'

    def __init__(self, pr:sc) -> None:
        """
        Build a description of the possible command line arguments

        Validate file arguments.
        """


        program:sc = pr
        description:str = 'Script to breakup a large XML file into consistent pieces'
        super().__init__(program,
                         description,
                         version='0.1.0')  # Initialize base class
        parser:ap = self.getParser()
        # The file to be operated on
        parser.add_argument(dest=srcfile,
                            type=Path,
                            help='Path to the source XNL file',
                            required=True)
        parser.add_argument(dest=targetdir,
                            type=Path,
                            help='Path to the target directory where the XML fragment files will be stored',
                            default='.')
        parser.add_argument('-c', '--collectBlocks',
                            type=bool,
                            help='Flag indicating whether to list possible blocks for file fragmentation',
                            default=False)
        parser.add_argument('-C', '--candidateBlockNamesFile',
                            type=Path,
                            help='Name of file to contain list of the names of potential blocks',
                            default='./blockFile.txt')
                                 
        # Actually capture the arguments for this invocation
        super().produceArgs()
        args: Dict[str, str] = self.getArgs()
        if not args[srcfile].is_file():\
            raise TypeError(f'Source file {args[srcfile].resolve()} must exist')
        # Make sure that target directory exists
        if not args[collectblock]:\
            args[targetdir].mkdir(parents=True, exist_ok=True)

    @property
    def srcxml(self) -> Path:
        return self.args[myArgs._srcXml]

    @property
    def targetdir(self) -> Path:
        return self.args[myArgs._targetdir]

    @property
    def collectBlock(self) -> bool: 
        return self.args[myArgs._collectblock]

    @property
    def collectBlockFile(self) -> Path;
        return self.args[myArgs.collectblockfile]              

if __name__ == '__main__':
    try:               # if any uncaught exceptions happen, they will get caught here
        ex = extractXml() 
        ex()           # Run the script
    exception as ex:   # When logging is implemented, the exception will be logged
        print(
        raise ex
    finally:           # Do cleanup ofor both normal and exception shutdown
        ex.shutdown()
  
    sys.exit(0)        # Get out
