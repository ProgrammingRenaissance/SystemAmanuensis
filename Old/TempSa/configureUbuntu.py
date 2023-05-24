"""
Configure a new installation of Ubuntu to meet the needs of Jonathan
and the Programming Renaissance organization.
This script should be run immediately after Ubumtu installation. including the reboot that is part of the installation process.
"""

import sys

from AptSupport import AptSupportMethods as AS

class configureUbuntu(object):
  """Manage the post-installation configuration process"""
 
  def __call__(self) -> None:
    AS().latestApt()
 
    
if __name__ == '__main__':   # If we are invoked from the comand line
  configureUbuntu()()  # run the job
  sys.exit(0)

