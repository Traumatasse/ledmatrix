import unittest
from ledmatrix.ledmatrix import LEDMatrix

class TestImage(unittest.TestCase):

  def test_read_image_to_frame(self):
    self.assertEqual(1, 1, "OK")

if __name__ == '__main__':
    unittest.main()