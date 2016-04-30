"""
'utils.py' implements utility methods.
"""

from operator import itemgetter

# Links two servers together
#   @params
#     server1 <Server> : first server
#     server2 <Server> : second server
#   @return
#     None
def link(server1, server2):
  server1.link(server2)
  server2.link(server1)

# Count wins across all strategies
#   @params
#     networks <see globals.py> : simulation data structure
#     ptime    <int>            : processing time of packet
#     wins     <{str:int}>      : maps strategies to win counts
#     ntrials  <int>            : number of simulation trials
#   @return
#     None
def count_wins(networks, ptime, wins, ntrials):
  for i in xrange(ntrials):
    winner = sorted(networks, key=lambda sim_obj : sim_obj['dat'][ptime][i])[-1]['typ']
    wins[winner] += 1

# Reset all networks
#   @params
#     networks <see globals.py> : simulation data structure
#   @return
#     None
def reset(networks):
  for sim_obj in networks:
    sim_obj['obj'].reset()

# Report simulation outcome
#   @params
#     wins    <{str:int}> : maps strategies to win counts
#     ptime   <int>       : processing time of packet
#     ntrials <int>       : number of simulation trials
def report(wins, ptime, ntrials):
  print 'PTIME = %d' % (ptime)
  for strategy, count in sorted(wins.items(), key=itemgetter(1))[::-1]:
    print '\t%s\t%f' % (strategy, count / float(ntrials))
