from app import app
import unittest


class TestingModule(unittest.TestCase):

    def test_items(self):
        """For Testing items (Question 1)"""
        app.testing = True
        client = app.test_client()

        req = [1, 4, -1, "hello", "world", 0, 10, 7]

        print("The request is POST to /items with json string >")
        print(req)

        resp = {
            "valid_entries": 4,
            "invalid_entries": 4,
            "min": 1,
            "max": 10,
            "average": 5.5
        }

        print("\nThe response should be >")
        print(resp)

        print("\nSending Request")
        r = client.post('/items', json=req)

        self.assertEqual(r.status_code, 200)
        # print("Request Status:", r.status_code)
        self.assertEqual(r.get_json(), resp)
        # print("Response:", r.get_json())

        print("Test Passed")

    def test_booking(self):
        """For Testing booking (Question 2)"""
        app.testing = True
        client = app.test_client()

        req1 = dict(slot=2, name="John")
        req2 = dict(slot=2, name="Rick")

        resp1 = dict(status="confirmed booking for John in slot 2")
        resp2 = dict(status="slot full, unable to save booking for Rick in slot 2")
        resp3 = dict(status="canceled booking for John in slot 2")
        resp4 = [dict(name="Diana", slot=2)]
        resp5 = dict(status="no booking for the name John in slot 2")

        print("Sending 1st POST request to /booking with json string >", req1)
        print("The response should be >", resp1)
        self.assertEqual(client.post('/booking', json=req1).get_json(), resp1)
        print("Response Matched\n")

        print("Sending 2nd POST request to /booking with json string >", req2)
        print("The response should be >", resp2)
        self.assertEqual(client.post('/booking', json=req2).get_json(), resp2)
        print("Response Matched\n")

        print("Sending 3rd POST request to /cancel with json string >", req1)
        print("The response should be >", resp3)
        self.assertEqual(client.post('/cancel', json=req1).get_json(), resp3)
        print("Response Matched\n")

        print("Sending 1st GET request to /booking")
        print("The response should be >", resp4)
        self.assertEqual(client.get('/booking').get_json(), resp4)
        print("Response Matched\n")

        print("Sending 4th POST request to /cancel with json string >", req1)
        print("The response should be >", resp5)
        self.assertEqual(client.post('/cancel', json=req1).get_json(), resp5)
        print("Response Matched\n")

        print("\nTest Passed")


if __name__ == "__main__":
    unittest.main()
