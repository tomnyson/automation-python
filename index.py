#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from time import sleep
from appium.webdriver.applicationstate import ApplicationState
from appium import webdriver
import desired_capabilities


class AppiumTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('automation.zip')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    # def test_lock(self):
    #     self.driver.lock(-1)
    #     try:
    #         self.assertTrue(self.driver.is_locked())
    #     finally:
    #         self.driver.unlock()
    #     self.assertFalse(self.driver.is_locked())

    def test_basic(self):
        try:   
            sleep(2)
            #get number a
            elem_a = self.driver.find_element_by_accessibility_id('a')
            elem_a.send_keys('1')
            #get number b
            elem_b = self.driver.find_element_by_accessibility_id('b').send_keys('2')
            result = self.driver.find_element_by_accessibility_id('result')
            btnclick = self.driver.find_element_by_accessibility_id('btnAdd')
            btnclick.click()
            # get result
            number1 = self.driver.find_element_by_xpath('//XCUIElementTypeTextField[@name="a"]')
            number2 = self.driver.find_element_by_xpath('//XCUIElementTypeTextField[@name="b"]')
            sleep(1)
            number_result = self.driver.find_element_by_accessibility_id('result')
            total = number1.text +  number2.text
            #self.assertEqual(number_result.text,total)
            print ('resullt  hiih',number_result.text)
            # print (elem_a.tag_name)
            # print (elem_a.parent)
            # print (elem_a.location)
            # print (elem_a.size)
            # compare result
        except Exception as err:
            print(err)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AppiumTests)
    unittest.TextTestRunner(verbosity=2).run(suite)