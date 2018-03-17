import unittest
import random

from ring_buffer import RingBuffer

class TestRingBuffer(unittest.TestCase):
    
    def test_initialize_params(self):
        '''
        Test that buffer capacity is correctly 
        returned along with other init params
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

if __name__ == '__main__':
    unittest.main()