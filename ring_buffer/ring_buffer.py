class RingBuffer:
    def __init__(self, capacity):
        self.cur = 0  # current
        self.capacity = capacity  # size
        self.the_buffer = []  # empty

    def append(self, item):
        if len(self.the_buffer) < self.capacity:  # compare len of the buffer and the capacity...
            self.the_buffer.append(item)  # append the item...
        elif len(self.the_buffer) == self.capacity:  # if len of the buffer == capacity.
            self.the_buffer[self.cur] = item
            self.cur = (self.cur + 1) % self.capacity  # must use paranthesis if not error happens.

    def get(self):
        if self.the_buffer is not None:
            # I used [:] to finish it up.
            # to get the part I want.
            return self.the_buffer[:self.cur] + self.the_buffer[self.cur:]
