"""
'distributors.py' implements packet distribution strategies.
"""

from copy   import deepcopy
from random import randint, shuffle

# Blindly distribute packets to neighbors
#   @params
#     server <Server> : server object to topple
#   @return
#     None
def blind_distribute(server):
  servers = server.neighbors
  shuffle(servers)
  packets = server.queue[-len(servers):]
  del server.queue[-len(servers):]
  shuffle(packets)
  for i in xrange(len(servers)):
    servers[i].serve(packets.pop())

# Distribute most delayed packets to least delayed servers
#   @params
#     server <Server> : server object to topple
#   @return
#     None
def max_distribute(server):
  packets = [server.queue.pop() for i in xrange(len(server.neighbors))]
  packets = sorted(packets, key=lambda p : p.latency)[::-1]
  neighbors = sorted(server.neighbors, key=lambda n : len(n.queue))
  for i in xrange(len(neighbors)):
    neighbors[i].serve(packets[i])

# Distribute least delayed packets to least delayed servers
#   @params
#     server <Server> : server object to topple
#   @return
#     None
def min_distribute(server):
  packets = [server.queue.pop() for i in xrange(len(server.neighbors))]
  packets = sorted(packets, key=lambda p : p.latency)
  neighbors = sorted(server.neighbors, key=lambda n : len(n.queue))
  for i in xrange(len(neighbors)):
    neighbors[i].serve(packets[i])
