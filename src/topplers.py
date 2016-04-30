"""
'topplers.py' implements toppling order strategies.
"""

from copy   import deepcopy
from random import randint

# Blindly selects servers to stabilize
#   @params
#     network <Network> : network object to stabilize
#   @return
#     <[str]> list of server ids that toppled in the given order
def blind_topple(network):
  events = []
  server_ids = {server.id for server in network.servers}
  # Attempt to topple each server until every server has toppled at most once
  while server_ids:
    server_i = randint(0, len(network.servers) - 1)
    server = network.servers[server_i]
    if server.id in events:
      # Already toppled
      continue
    elif server.stabilize():
      events.append(server.id)
      server_ids.remove(server.id)
    # Check whether invariant is met: every server has either toppled or is
    # stable; if so, time step ends
    all_stable = True
    for server in network.servers:
      if len(server.queue) < len(server.neighbors) or server.id in events:
        continue
      else:
        all_stable = False
        break
    if all_stable:
      return events
  return events

# Selects server with maximum queue length to stabilize
#   @params
#     network <Network> : network object to stabilize
#   @return
#     <[str]> list of server ids that toppled in the given order
def max_topple(network):
  events = []
  server_ids = {server.id for server in network.servers}
  # Attempt to topple each server until every server has toppled at most once
  while server_ids:
    server = sorted(network.servers[len(events):], key=lambda s : len(s.queue))[-1]
    if server.stabilize():
      idx = network.servers.index(server)
      events.append(server.id)
      network.servers.insert(0, network.servers.pop(idx))
      server_ids.remove(server.id)
    # Check whether invariant is met: every server has either toppled or is
    # stable; if so, time step ends
    all_stable = True
    for server in network.servers:
      if len(server.queue) < len(server.neighbors) or server.id in events:
        continue
      else:
        all_stable = False
        break
    if all_stable:
      return events
  return events
