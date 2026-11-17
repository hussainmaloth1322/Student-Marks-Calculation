
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StudentMarksTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")

        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get("http://127.0.0.1:5000")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get("http://127.0.0.1:5000")

    def enter_details(self, m1, m2, m3):
        self.driver.find_element(
            By.ID, "studentName"
        ).send_keys("Hussain")

        self.driver.find_element(
            By.ID, "rollNumber"
        ).send_keys("101")

        self.driver.find_element(By.ID, "m1").send_keys(str(m1))
        self.driver.find_element(By.ID, "m2").send_keys(str(m2))
        self.driver.find_element(By.ID, "m3").send_keys(str(m3))

        self.driver.find_element(
            By.XPATH, "//button[@type='submit']"
        ).click()

    def test_1_home_page(self):
        self.assertIn(
            "Student Marks Calculator",
            self.driver.page_source
        )

    def test_2_student_name_field(self):
        self.assertTrue(
            self.driver.find_element(
                By.ID, "studentName"
            ).is_displayed()
        )

    def test_3_roll_number_field(self):
        self.assertTrue(
            self.driver.find_element(
                By.ID, "rollNumber"
            ).is_displayed()
        )

    def test_4_subject_mark_fields(self):
        for field in ["m1", "m2", "m3"]:
            self.assertTrue(
                self.driver.find_element(
                    By.ID, field
                ).is_displayed()
            )

    def test_5_calculate_marks(self):
        self.enter_details(80, 82, 80)

        result = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.ID, "result")
            )
        )

        WebDriverWait(self.driver, 10).until(
            lambda driver: "242" in result.text
        )

        self.assertIn("242", result.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
