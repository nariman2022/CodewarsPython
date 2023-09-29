# Since Nessie is a master of disguise, the only way accurately tell is to look for the phrase "tree fiddy".
# Note that the phrase can also be written as "3.50" or "three fifty".
# Your function should return true if you're talking with The Loch Ness Moster, false otherwise.

import re
def is_lock_ness_monster(string):
    x = re.search("tree fiddy|3\.50|three fifty", string)
    return bool(x)