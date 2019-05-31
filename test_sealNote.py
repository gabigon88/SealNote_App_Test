import unittest
from time import sleep
from appium import webdriver
from sealNote_pageObject import sealNote_pageObject

class SealNoteTest(unittest.TestCase):
    def setUp(self):
        # app = ('D:\\sealnote25.apk') # 此為受測app的apk檔路徑，需為絕對路徑
        device='YT910R6JBG' # 此為設備號，手機連上電腦後在cmd下adb devices可查看
        pack='com.twistedplane.sealnote' # 此為app的package名稱
        activity='com.twistedplane.sealnote.SealnoteActivity'# 此為app的主activity

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.3'
        desired_caps['deviceName'] = device
        # desired_caps['app'] = app # 加上此行，則每次執行測試時都會重新安裝一次app
        desired_caps['appPackage'] = pack
        desired_caps['appActivity'] = activity

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # self.driver.implicitly_wait(10) # 隱性等待，全域影響，最長只等10秒
        self.sealNotePO = sealNote_pageObject(self.driver)

    def tearDown(self):
        self.driver.quit()

    def testCreatePlainText(self):
        testTitle = 'testTitle'
        testContent = 'testContent'
        self.sealNotePO.InitializePassword('123')
        self.sealNotePO.ClickAddNewNoteButton()
        self.sealNotePO.ClickAddPlainText()
        self.sealNotePO.InputTitle(testTitle)
        self.sealNotePO.InputContent(testContent)
        self.sealNotePO.ClickSaveNoteButton()

        title = self.sealNotePO.GetNoteTitle().text
        content = self.sealNotePO.GetNoteContent().text
        self.assertEqual(title, testTitle)
        self.assertEqual(content, testContent)

    def testCreateCardDetails(self):
        cardName = 'MyVisa'
        cardNumber = '123456789012'
        self.sealNotePO.InitializePassword('123')
        self.sealNotePO.ClickAddNewNoteButton()
        self.sealNotePO.ClickAddCardDetails()
        self.sealNotePO.InputCardName(cardName)
        self.sealNotePO.InputCardNumber(cardNumber)
        self.sealNotePO.InputCardValid('2019','2029')
        self.sealNotePO.InputCardCVV('000')
        # self.driver.hide_keyboard()
        # self.driver.swipe(100, 300, 100, 100, 500)
        self.sealNotePO.ClickSaveNoteButton()
        
        content = self.sealNotePO.GetNoteContent().text
        self.assertIn(cardName, content)
        self.assertIn(cardNumber[-4:], content) # 信用卡卡號在首頁只會顯示最後4碼

    def testCreateLoginDetails(self):
        url = 'www.test.com'
        account = 'testAccount'
        password = 'testPassword'
        self.sealNotePO.InitializePassword('123')
        self.sealNotePO.ClickAddNewNoteButton()
        self.sealNotePO.ClickAddLoginDetails()
        self.sealNotePO.InputUrl(url)
        self.sealNotePO.InputLoginAccount(account)
        self.sealNotePO.InputLoginPassword(password)
        self.sealNotePO.ClickSaveNoteButton()
        
        content = self.sealNotePO.GetNoteContent().text
        self.assertIn(url, content)
        self.assertIn(account, content)

if __name__ == '__main__':
    unittest.main()