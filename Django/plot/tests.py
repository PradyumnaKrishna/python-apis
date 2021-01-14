from django.test import TestCase
from django.test import Client


# # Create your tests here.
class MainTest(TestCase):

    def setUp(self):
        pass

    def test_plot(self):
        req1 = dict(x=1, y=1)
        req2 = dict(x=1, y=5)
        req3 = dict(x=5, y=1)
        req4 = dict(x=5, y=2)
        req5 = dict(x=5, y=5)

        resp1 = dict(status="accepted")
        resp2 = dict(status="Success [1, 1] [1, 5] [5, 1] [5, 5] ")

        c = self.client

        print("Sending 1st POST request to /plot with json string >", req1)
        print("The response should be >", resp1)
        self.assertEqual(c.post('/plot', req1, content_type='application/json').json(), resp1)
        print("Response Matched\n")

        print("Sending 2nd POST request to /plot with json string >", req2)
        print("The response should be >", resp1)
        self.assertEqual(c.post('/plot', req2, content_type='application/json').json(), resp1)
        print("Response Matched\n")

        print("Sending 3rd POST request to /plot with json string >", req3)
        print("The response should be >", resp1)
        self.assertEqual(c.post('/plot', req3, content_type='application/json').json(), resp1)
        print("Response Matched\n")

        print("Sending 4th POST request to /plot with json string >", req4)
        print("The response should be >", resp1)
        self.assertEqual(c.post('/plot', req4, content_type='application/json').json(), resp1)
        print("Response Matched\n")

        print("Sending 5th POST request to /plot with json string >", req5)
        print("The response should be >", resp2)
        self.assertEqual(c.post('/plot', req5, content_type='application/json').json(), resp2)
        print("Response Matched\n")

        print("\n\nTest Passed")
