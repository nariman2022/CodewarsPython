# Given a string showing either flat road (_) or bumps (n). If you are able to reach home safely by encountering 15 bumps
# or less, return Woohoo!, otherwise return Car Dead

def bumps(road):
    return 'Woohoo!' if road.count('n') <= 15 else 'Car Dead'