import unittest
from time import sleep
from appium import webdriver

class SealNoteTest(unittest.TestCase):
    def setUp(self):
        #app = ('D:\\sealnote25.apk') #此為受測app的apk檔路徑，需為絕對路徑
        device='YT910R6JBG' #此為設備號，手機連上電腦後在cmd下adb devices可查看
        pack='com.twistedplane.sealnote' #此為app的package名稱
        activity='com.twistedplane.sealnote.SealnoteActivity'#此為app的主activity

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.3'
        desired_caps['deviceName'] = device
        #desired_caps['app'] = app #加上此行，則每次執行測試時都會重新安裝一次app
        desired_caps['appPackage'] = pack
        desired_caps['appActivity'] = activity

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(3000)
        passwordTF_ID = 'com.twistedplane.sealnote:id/password_input'
        commitBtn_ID = 'com.twistedplane.sealnote:id/password_action_button'
        self.driver.find_element_by_id(passwordTF_ID).send_keys('123')
        self.driver.find_element_by_id(commitBtn_ID).click()

    def tearDown(self):
        self.driver.quit()

    def testCreateNewNote(self):
        testTitle = 'testTitle'
        testContent = 'OHO'
        creatBtn_ID = 'com.twistedplane.sealnote:id/create_note_button'
        self.driver.find_element_by_id(creatBtn_ID).click()

        titleTF_ID = 'com.twistedplane.sealnote:id/note_activity_title'
        self.driver.find_element_by_id(titleTF_ID).send_keys(testTitle)

        contentTF_ID = 'com.twistedplane.sealnote:id/note_activity_note'
        self.driver.find_element_by_id(contentTF_ID).send_keys(testContent)

        saveBtn_ID = 'com.twistedplane.sealnote:id/action_save_note'
        self.driver.find_element_by_id(saveBtn_ID).click()

        title = self.driver.find_element_by_id('com.twistedplane.sealnote:id/card_header_inner_simple_title')
        content = self.driver.find_element_by_id('com.twistedplane.sealnote:id/cardcontent_note')
        self.assertEqual(title.text, testTitle)
        self.assertEqual(content.text, testContent)
        
if __name__ == '__main__':
    unittest.main()