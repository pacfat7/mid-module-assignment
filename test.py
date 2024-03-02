def test_(self):
  import unittest
  from main import shortest_path, graph

  class TestShortestPathFunction(unittest.TestCase):
      def test_direct_path(self):
          self.assertEqual(shortest_path(0, 1, 3, graph), 7)
          self.assertEqual(shortest_path(2, 3, 3, graph), 2)

      def test_path_with_intermediate(self):
          self.assertEqual(shortest_path(0, 2, 3, graph), 12)  
          self.assertEqual(shortest_path(0, 3, 3, graph), 10)  

      def test_no_path(self):
          self.assertEqual(shortest_path(1, 0, 3, graph), sys.maxsize)  

  if __name__ == '__main__':
      unittest.main()