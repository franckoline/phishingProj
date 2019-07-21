from transitions import Machine


class Matter(object):
    pass


lump = Matter()
# Define some states...
states = ['Ta', 'Tb', 'Tc', 'Td', 'Te', 'Tf', 'Tg', 'Th', 'Ti', 'Tj','Tk', 'Tl', 'SafeFinal', 'UnsafeFinal']

machine = Machine(model=lump, states=['Ta', 'Tb', 'Tc', 'Td', 'Te', 'Tf', 'Tg', 'Th', 'Ti', 'Tj','Tk', 'Tl', 'SafeFinal', 'UnsafeFinal'], initial='Ta')
