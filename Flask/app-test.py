from app import app
import unittest


# Test all question with given request/response
class TestingModule(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_items(self):
        """For Testing items (Question 1)"""

        req = [1, 4, -1, "hello", "world", 0, 10, 7]

        print('=' * 20)
        print("Items Testing Module")

        print("\n\nThe request is POST to /items with json string >")
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

        with self.app as client:
            r = client.post('/items', json=req)

        self.assertEqual(r.status_code, 200)
        # print("Request Status:", r.status_code)
        self.assertEqual(r.get_json(), resp)
        # print("Response:", r.get_json())

        print("Test Passed")

    def test_booking(self):
        """For Testing booking (Question 2)"""

        req1 = dict(slot=2, name="John")
        req2 = dict(slot=2, name="Rick")

        resp1 = dict(status="confirmed booking for John in slot 2")
        resp2 = dict(status="slot full, unable to save booking for Rick in slot 2")
        resp3 = dict(status="canceled booking for John in slot 2")
        resp4 = [dict(name="Diana", slot=2)]
        resp5 = dict(status="no booking for the name John in slot 2")

        print('=' * 20)
        print("Booking Testing Module")

        print("Sending 1st POST request to /booking with json string >", req1)
        print("The response should be >", resp1)
        with self.app as client:
            self.assertEqual(client.post('/booking', json=req1).get_json(), resp1)
        print("Response Matched\n")

        print("Sending 2nd POST request to /booking with json string >", req2)
        print("The response should be >", resp2)
        with self.app as client:
            self.assertEqual(client.post('/booking', json=req2).get_json(), resp2)
        print("Response Matched\n")

        print("Sending 3rd POST request to /cancel with json string >", req1)
        print("The response should be >", resp3)
        with self.app as client:
            self.assertEqual(client.post('/cancel', json=req1).get_json(), resp3)
        print("Response Matched\n")

        print("Sending 1st GET request to /booking")
        print("The response should be >", resp4)
        with self.app as client:
            self.assertEqual(client.get('/booking').get_json(), resp4)
        print("Response Matched\n")

        print("Sending 4th POST request to /cancel with json string >", req1)
        print("The response should be >", resp5)
        with self.app as client:
            self.assertEqual(client.post('/cancel', json=req1).get_json(), resp5)
        print("Response Matched\n")

        print("\nTest Passed")

    def test_plot(self):
        """For Testing Plot (Question 3)"""

        req1 = dict(x=1, y=1)
        req2 = dict(x=1, y=5)
        req3 = dict(x=5, y=1)
        req4 = dict(x=5, y=2)
        req5 = dict(x=5, y=5)

        resp1 = dict(status="accepted")
        resp2 = dict(status="Success (1, 1) (1, 5) (5, 1) (5, 5) ")

        sess_data = [(1, 1), (1, 5), (5, 1), (5, 2), (5, 5)]
        rect_coord = [(1, 1), (1, 5), (5, 1), (5, 5)]

        print('=' * 20)
        print("Plot Testing Module")

        with self.app as client:
            print("Sending 1st POST request to /plot with json string >", req1)
            print("The response should be >", resp1)
            self.assertEqual(client.post('/plot', json=req1).get_json(), resp1)
            print("Response Matched\n")

            print("Sending 2nd POST request to /plot with json string >", req2)
            print("The response should be >", resp1)
            self.assertEqual(client.post('/plot', json=req2).get_json(), resp1)
            print("Response Matched\n")

            print("Sending 3rd POST request to /plot with json string >", req3)
            print("The response should be >", resp1)
            self.assertEqual(client.post('/plot', json=req3).get_json(), resp1)
            print("Response Matched\n")

            print("Sending 4th POST request to /plot with json string >", req4)
            print("The response should be >", resp1)
            self.assertEqual(client.post('/plot', json=req4).get_json(), resp1)
            print("Response Matched\n")

            print("Sending 5th POST request to /plot with json string >", req5)
            print("The response should be >", resp2)
            self.assertEqual(client.post('/plot', json=req5).get_json(), resp2)
            print("Response Matched\n")

            print("\nChecking session Data")
            with client.session_transaction() as sess:
                self.assertEqual(sess['coord'], sess_data)
                self.assertEqual(sess['RectCoord'], rect_coord)
            print("Session Data Matched")

        print("\n\nTest Passed")


if __name__ == "__main__":
    unittest.main()
