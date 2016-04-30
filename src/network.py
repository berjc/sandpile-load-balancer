"""
'network.py' implements the Network class.
"""

from utils  import link
from random import randint

class Network:

  # Network constructor
  #   @params
  #     toppler      <func> : func to decide toppling order of servers
  #     distributor  <func> : func to distribute packets to neighbors
  #     gen_topology <func> : func to generate topology of network
  #     size         <int>  : size of network topology
  #   @return
  #     <Network>
  def __init__(self, toppler, distributor, gen_topology, size):
    self.servers = []
    self.topple = toppler
    self.distribute = distributor
    gen_topology(self, size)

  # Resets network
  #   @params
  #     None
  #   @return
  #     None
  def reset(self):
    for server in self.servers:
      server.reset()

  # Adds packet to network
  #   @params
  #     packet <Packet> : packet to be added to network
  #     loc    <int>    : server to add to, default to None
  #   @return
  #     None
  def add(self, packet, loc=None):
    server_i = loc if loc != None else randint(0, len(self.servers) - 1)
    self.servers[server_i].serve(packet)

  # Runs network for one timestep
  #   @params
  #     None
  #   @return
  #     <[str]> list of server ids that toppled in the given order
  def step(self):
    # Update all servers
    for server in self.servers:
      server.update()
    return self.topple(self)

  # Reports sum of latencies over all packets in network
  #   @params
  #     None
  #   @return
  #     <int> sum of latencies over all packets in network
  def latency(self):
    latencies = []
    for server in self.servers:
      if server.serving:
        # Account for packet being processed
        latencies.append(server.serving.latency)
      for packet in server.queue:
        latencies.append(packet.latency)
    return 0 if not latencies else sum(latencies)
