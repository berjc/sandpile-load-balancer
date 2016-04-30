"""
'run.py' implements script to run SLB model simulation.
"""

from packet     import Packet
from random     import randint
from matplotlib import pyplot as plt
from utils      import reset, count_wins, report
from globals    import networks, SIZE, NTRIALS, PTIMES, STRATEGIES

NTIME_STEPS = 200
NSERVERS = SIZE**2

win_freqs = {strategy : [] for strategy in STRATEGIES}

if __name__ == '__main__':
  # Run SLB model simulation
  for ptime in PTIMES:
    for i in xrange(NTRIALS):
      reset(networks)
      for j in xrange(NTIME_STEPS):
        loc = randint(0, NSERVERS - 1)
        pkt = Packet('id-%d' % (j), ptime)
        for sim_obj in networks:
          network = sim_obj['obj']
          network.step()
          network.add(pkt, loc)
          sim_obj['dat'][ptime][i] += network.latency()

  # Count and report win frequencies
  for ptime in PTIMES:
    win_counts = {strategy : 0 for strategy in STRATEGIES}
    count_wins(networks, ptime, win_counts, NTRIALS)
    report(win_counts, ptime, NTRIALS)
    for strategy, count in win_counts.iteritems():
      win_freqs[strategy].append(count / float(NTRIALS))

  # Plot simulation resuslts
  plt.plot(PTIMES, win_freqs[STRATEGIES[0]], 'bs-', label=STRATEGIES[0])
  plt.plot(PTIMES, win_freqs[STRATEGIES[1]], 'gs-', label=STRATEGIES[1])
  plt.plot(PTIMES, win_freqs[STRATEGIES[2]], 'ys-', label=STRATEGIES[2])
  plt.plot(PTIMES, win_freqs[STRATEGIES[3]], 'rs-', label=STRATEGIES[3])
  plt.plot(PTIMES, win_freqs[STRATEGIES[4]], 'ms-', label=STRATEGIES[4])
  plt.title('Percent of Trials as Best Strategy vs. Processing Time')
  plt.xlabel('Processing Time')
  plt.ylabel('Percent of Trials as Best Strategy')
  plt.legend(loc='center right')
  plt.show()
