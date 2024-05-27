import unittest
import basic as b

class TestYourModule(unittest.TestCase):
    def test_hash(self):
        # Test the hash function with some sample inputs
        self.assertEqual(b.hash("hello"), "0074753320500541411425004185135710016648875001417290519")  # ans

    def test_todict(self):
        f = open("sample.json", 'a')
        f.write("{ }")
        f.close()
        self.assertEqual(b.todict("sample.json"), {})  # ans

        # Clean up
        b.os.remove("sample.json")

    def test_tojson(self):
        # make test
        temp_file = "test_output.json"
        f = open(temp_file, 'a')
        f.write("{ }")
        f.close()
        my_dict = {"key1": "value1", "key2": "value2"}

        b.tojson(temp_file, my_dict)

        with open(temp_file, "r") as json_file:
            loaded_dict = b.json.load(json_file)
            self.assertEqual(loaded_dict, my_dict)

        # Clean up
        b.os.remove(temp_file)

    def test_getch(self):
        user_input = '1'
        print("press 1")
        actual_output = b.getch()

        self.assertEqual(actual_output, user_input)

if __name__ == "__main__":
    unittest.main()