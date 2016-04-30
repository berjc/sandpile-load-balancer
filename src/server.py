"""
'server.py' implements the Server class.
"""

class Server:

  # Server constructor
  #   @params
  #     id          <int>  : server identifier
  #     distributor <func> : func to distribute packets to neighbors
  #   @return
  #     <Server>
  def __init__(self, id, distributor):
    self.id = id
    self.queue = []
    self.serving = None
    self.neighbors = []
    self.distribute = distributor

  # Resets servers
  #   @params
  #     None
  #   @return
  #     None
  def reset(self):
    self.serving = None
    self.queue = []

  # Link adjacent server
  #   @params
  #     neighbor <Server> : server object
  #   @return
  #     None
  def link(self, neighbor):
    self.neighbors.append(neighbor)

  # Serve packet
  #   @params
  #     packet <Packet> : packet object
  #   @return
  #     None
  def serve(self, packet):
    self.queue.append(packet)

  # Update server state at start of timestep
  #   @params
  #     None
  #   @return
  #     None
  def update(self):
    # Update packet being served
    if self.serving:
      # Decrement processing time of packet
      self.serving.ptime -= 1
      if self.serving.ptime == 0:
        # Remove processed packet
        self.serving = None
        if self.queue:
          # Process packet from queue
          self.serving = self.queue.pop(0)
    elif self.queue:
      self.serving = self.queue.pop(0)

    # Update latencies    
    if self.serving:
      self.serving.latency += 1
    for packet in self.queue:
      packet.latency += 1

  # Stabilizes server
  #   @params
  #     None
  #   @return
  #     <boolean> whether server toppled or not
  def stabilize(self):
    if len(self.queue) >= len(self.neighbors):
      self.distribute(self)
      return True
    return False
