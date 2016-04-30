"""
'globals.py' implements global variables for the simulator.
"""

from network      import Network
from topology     import gen_torus_network
from topplers     import blind_topple, max_topple
from distributors import blind_distribute, max_distribute, min_distribute

SIZE = 5
NTRIALS = 1000
GENERATOR = gen_torus_network

STRATEGIES = [
  'blind_both',
  'max_distr',
  'min_distr',
  'max_topple',
  'max_both'
]

PTIMES = [
  1, 2, 3, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 100
]

networks = [
  {
    'obj' : Network(blind_topple, blind_distribute, GENERATOR, SIZE),
    'dat' : {ptime : [0] * NTRIALS for ptime in PTIMES},
    'typ' : STRATEGIES[0]
  }, {
    'obj' : Network(blind_topple, max_distribute, GENERATOR, SIZE),
    'dat' : {ptime : [0] * NTRIALS for ptime in PTIMES},
    'typ' : STRATEGIES[1]
  }, {
    'obj' : Network(blind_topple, min_distribute, GENERATOR, SIZE),
    'dat' : {ptime : [0] * NTRIALS for ptime in PTIMES},
    'typ' : STRATEGIES[2]
  }, {
    'obj' : Network(max_topple, blind_distribute, GENERATOR, SIZE),
    'dat' : {ptime : [0] * NTRIALS for ptime in PTIMES},
    'typ' : STRATEGIES[3]
  }, {
    'obj' : Network(max_topple, max_distribute, GENERATOR, SIZE),
    'dat' : {ptime : [0] * NTRIALS for ptime in PTIMES},
    'typ' : STRATEGIES[4]
  }
]
