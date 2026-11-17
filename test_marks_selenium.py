"""Browser-based checks for the Flask marks calculator."""
import json
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = "http://localhost:5000"

class MarksBrowserTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=options)

    def tearDown(self):
        if hasattr(self, "driver"):
            self.driver.quit()

    def get_json(self, url):
        self.driver.get(url)
        return json.loads(self.driver.find_element("tag name", "body").text)

    def test_total_and_average(self):
        result = self.get_json(
            f"{BASE_URL}/calculate?m1=80&m2=90&m3=70"
        )
        self.assertEqual(result["total"], 240)
        self.assertEqual(result["average"], 80.0)

    def test_reject_out_of_range_marks(self):
        result = self.get_json(
            f"{BASE_URL}/calculate?m1=120&m2=90&m3=70"
        )
        self.assertIn("error", result)

if __name__ == "__main__":
    unittest.main()
