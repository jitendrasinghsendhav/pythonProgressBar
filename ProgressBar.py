import sys
import time

bar_character = "#" # "#" "-" "_", ".", "=", "~"
progressBarWidth = 50

def initiateBar():
  sys.stdout.write("[[[%s]" % (" " * progressBarWidth))
  sys.stdout.write( "\b"* progressBarWidth)
  sys.stdout.flush()


def progressBar(completed):
  sys.stdout.write("\b\b\b" + bar_character + str(completed)+"%")
  sys.stdout.flush()


initiateBar()

for i in range(101):
  progressBar(i)
