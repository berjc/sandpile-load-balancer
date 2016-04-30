"""
'packet.py' implements the Packet class.
"""

class Packet:

  # Packet constructor
  #   @params
  #     id    <int> : packet identifier
  #     ptime <int> : processing time of packet
  #   @return
  #     <Packet>
  def __init__(self, id, ptime):
    self.id = id
    self._ptime = self.ptime = ptime
    self.latency = 0  # delay to response

  # Update packet latency
  #   @params
  #     None
  #   @return
  #     None
  def update(self):
    self.latency += 1
