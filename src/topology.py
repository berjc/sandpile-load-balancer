"""
'topology.py' implemenets network topology generators.
"""

from utils  import link
from server import Server

DEFAULT_SIZE = 2

# Single server network
#   @params
#     size <int> : default parameter
#   @return
#     None
def gen_single_server_network(network, size=None):
  network.servers.append(Server('id-0', network.distribute))

# Dual server network
#   @params
#     size <int> : default parameter
#   @return
#     None
def gen_dual_server_network(network, size=None):
  s0 = Server('id-0', network.distribute)
  s1 = Server('id-1', network.distribute)
  link(s0, s1)
  network.servers += [s0, s1]

# Ring server network
#   @params
#     size <int> : number of servers in ring
#   @return
#     None
def gen_ring_network(network, size=None):
  if not size:
    size = DEFAULT_SIZE
  first = next = Server('id-0', network.distribute)
  network.servers.append(first)
  for i in xrange(1, size):
    _next = Server('id-%d' % (i), network.distribute)
    link(next, _next)
    next = _next
    network.servers.append(next)
  next.link(first)

# Generates torus network
#   @params
#     size <int> : circumference of torus
#   @return
#     None
def gen_torus_network(network, size=None):
  if not size:
    size = DEFAULT_SIZE
  # Generate all servers
  for i in xrange(size**2):
    network.servers.append(Server('id-%d' % (i), network.distribute))
  # Link across rows
  for i in xrange(size**2):
    if i % size != 0:
      s1 = network.servers[i]
      s2 = network.servers[i - 1]
      link(s1, s2)
  # Link across row edges
  i = 0
  while i < size**2:
    s1 = network.servers[i]
    s2 = network.servers[i + size - 1]
    link(s1, s2)
    i += size
  # Link down columns
  for i in xrange(size**2 - size):
    s1 = network.servers[i]
    s2 = network.servers[i + size]
    link(s1, s2)
  # Link down column edges
  for i in xrange(size):
    s1 = network.servers[i]
    s2 = network.servers[-1 * size + i]
    link(s1, s2)
