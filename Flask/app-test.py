from app import app
import unittest

req = [1, 4, -1, "hello", "world", 0, 10, 7]
resp = {"valid_entries": 4, "invalid_entries": 4, "min": 1, "max": 10, "average": 5.5}


class Testing_Module(unittest.TestCase):

    def test_items(self):
        """For Testing items (Question 1)"""
        app.testing = True
        client = app.test_client()

        print("The request is POST to /items with json string >")
        print(req)

        print("\nThe response should be >")
        print(resp)

        print("\nSending Request")
        r = client.post('/items', json=req)

        self.assertEqual(r.status_code, 200)
        # print("Request Status:", r.status_code)
        self.assertEqual(r.get_json(), resp)
        # print("Response:", r.get_json())

        print("Test Passed")


if __name__ == "__main__":
    unittest.main()
