import unittest
import random

import pytest

from ring_buffer.ring_buffer import RingBuffer

class TestRingBuffer(unittest.TestCase):
    
    def test_initialize_params(self):
        '''
        Test that buffer init params are returned
        correctly
        '''
        random_size = random.randrange(1, 100)
        buffer = RingBuffer(random_size)

        self.assertEqual(buffer.get_capacity(), random_size)
        self.assertFalse(buffer.is_full())
        self.assertTrue(buffer.is_empty())
        self.assertEqual(buffer.get_buffer_fill(), 0)

    def test_push(self):
        '''
        Test that buffer push works
        '''
        random_size = random.randrange(1, 100)
        buffer = RingBuffer(random_size)

        buffer.push(0)

    def test_pop(self):
        '''
        Test that buffer pop returns pushed value
        '''
        random_size = random.randrange(1, 100)
        buffer = RingBuffer(random_size)

        buffer.push(0)
        returned_element = buffer.pop()

        self.assertEqual(returned_element, 0)

    def test_push_full_fail(self):
        '''
        Test that pushing into a full
        buffer raises Runtime Exception
        and the "buffer full" message
        '''
        with pytest.raises(RuntimeError) as excinfo:
            random_size = random.randrange(1, 100)
            buffer = RingBuffer(random_size)
            for i in range(0, random_size + 1):
                buffer.push(i)
        
        self.assertEqual(str(excinfo.value), 'Buffer is full!')

    def test_pop_empty_fail(self):
        '''
        Test that popping from an empty buffer
        results in RuntimeException being raised
        along with "Buffer empty" exception message
        '''
        with pytest.raises(RuntimeError) as excinfo:
            random_size = random.randrange(1, 100)
            buffer = RingBuffer(random_size)
            buffer.pop()

        self.assertEqual(str(excinfo.value), 'Buffer is empty!')

    def test_buffer_fill_size_return(self):
        '''
        Test that buffer fill size is 
        correctly returned under various
        use scenarios
        '''

        # Test that buffer fill size is returned as
        # 0 when buffer is empty
        random_size = random.randrange(1, 100)
        buffer = RingBuffer(random_size)
        fill_size = buffer.get_buffer_fill()
        self.assertEqual(fill_size, 0)

        # Test that buffer fill size is returned as
        # the number of elements pushed when the
        # buffer is neither empty nor full
        random_size = random.randrange(1, 100)
        buffer = RingBuffer(random_size)
        for i in range(0, int(random_size/2)):
            buffer.push(i)

        fill_size = buffer.get_buffer_fill()
        self.assertEqual(fill_size, int(random_size/2))

        # Test that buffer fill size is correctly 
        # returned when buffer is full
        random_size = random.randrange(1, 100)
        buffer = RingBuffer(random_size)
        for i in range(0, random_size):
            buffer.push(i)

        fill_size = buffer.get_buffer_fill()
        self.assertEqual(fill_size, random_size)

    def test_get_capacity(self):
        '''
        Test that get_capacity method
        returns correct values
        '''
        random_size = random.randrange(1, 100)
        buffer = RingBuffer(random_size)
        for i in range(0, random.randrange(1, random_size)):
            buffer.push(i)

        buffer_capacity = buffer.get_capacity()
        self.assertEqual(buffer_capacity, random_size)

    def test_clear(self):
        '''
        Test that clear() method clears
        the buffer properly
        '''

        random_size = random.randrange(1, 100)
        buffer = RingBuffer(random_size)
        for i in range(0, random.randrange(1, random_size)):
            buffer.push(i)

        buffer.clear()
        self.assertTrue(buffer.is_empty())
        self.assertFalse(buffer.is_full())
        self.assertEqual(buffer.get_capacity(), random_size)
        self.assertEqual(buffer.get_buffer_fill(), 0)

if __name__ == '__main__':
    unittest.main()
