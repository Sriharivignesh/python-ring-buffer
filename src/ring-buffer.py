

class RingBuffer(object):
    def __init__(self, size):
        '''
        Initialise the buffer
        '''
        self.head = 0
        self.tail = 0
        self.max_size = size
        self.buffer = [0 for i in xrange(0, size)]
        self.full = False
        self.empty = True

    def push(self, element):
        '''
        Push an element into the buffer
        '''
        if (self.is_full()):
            raise RuntimeError('Buffer is full!')

        self.buffer[self.head] = element
        self.head = (self.head + 1) % self.max_size

        self.empty = False
        if self.head == self.tail:
            self.full = True

    def pop(self):
        '''
        Pop an element from the buffer
        '''
        if(self.is_empty()):
            raise RuntimeError('Buffer is empty!')

        element = self.buffer[self.tail]

        self.tail = (self.tail + 1) % self.max_size

        self.full = False
        if self.tail == self.head:
            self.empty = True

        return element

    def get_capacity(self):
        '''
        Return buffer's capacity
        '''
        return self.max_size

    def is_empty(self):
        '''
        Return true if buffer is empty else false
        '''
        return self.empty

    def is_full(self):
        '''
        Return true is buffer is full else false
        '''
        return self.full

    def get_buffer_size(self):
        '''
        Return current buffer occupied size
        '''
        if self.head >= self.tail:
            return self.head - self.tail

        return ((self.max_size - self.tail) + (self.head - 0))

    def clear(self):
        '''
        Clear the buffer
        '''
        self.buffer = [0 for i in xrange(0, self.max_size)]
        self.head = 0
        self.tail = 0
        self.full = False
        self.empty = True
