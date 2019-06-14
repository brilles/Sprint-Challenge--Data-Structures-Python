class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item
    self.current += 1
    if self.current == (len(self.storage)):
      self.current = 0

  def get(self):
    cleanBuffer = []
    for i in range(0, len(self.storage)):
      if self.storage[i] is not None:
        cleanBuffer.append(self.storage[i])
    return cleanBuffer
