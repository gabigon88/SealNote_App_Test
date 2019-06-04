import unittest
from time import sleep
from appium import webdriver
from sealNote_pageObject import *

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

    def tearDown(self):
        self.driver.quit()

    def testWeakPassword(self):
        testPassword = '123'
        set_password_page = InitializePasswordPage(self.driver)
        set_password_page.InputPassword(testPassword)

        passwordStrength = set_password_page.GetPasswordStrength()
        self.assertEqual(passwordStrength, "Weak")

    def testSoSoPassword(self):
        testPassword = 'it2b8kmxa'
        set_password_page = InitializePasswordPage(self.driver)
        set_password_page.InputPassword(testPassword)

        passwordStrength = set_password_page.GetPasswordStrength()
        self.assertEqual(passwordStrength, "So-so")

    def testGoodPassword(self):
        testPassword = 'V35bsNhh9'
        set_password_page = InitializePasswordPage(self.driver)
        set_password_page.InputPassword(testPassword)

        passwordStrength = set_password_page.GetPasswordStrength()
        self.assertEqual(passwordStrength, "Good")

    def testStrongPassword(self):
        testPassword = 'a!wn=nggWGP-b85e'
        set_password_page = InitializePasswordPage(self.driver)
        set_password_page.InputPassword(testPassword)

        passwordStrength = set_password_page.GetPasswordStrength()
        self.assertEqual(passwordStrength, "Strong")        

    def testCreatePlainText(self):
        testTitle = 'testTitle'
        testContent = 'testContent'
        set_password_page = InitializePasswordPage(self.driver)
        set_password_page.InputPassword('123')
        set_password_page.ClickStartButton()
        notes_page = NotesPage(self.driver)
        notes_page.ClickAddButton()
        notes_page.ClickAddPlainText()
        add_plain_text_page = AddPlainTextPage(self.driver)
        add_plain_text_page.InputTitle(testTitle)
        add_plain_text_page.InputContent(testContent)
        add_plain_text_page.ClickSaveNoteButton()

        title = notes_page.GetNoteTitle()
        content = notes_page.GetNoteContent()
        self.assertEqual(title, testTitle)
        self.assertEqual(content, testContent)

    def testCreateCardDetails(self):
        cardName = 'MyVisa'
        cardNumber = '123456789012'
        set_password_page = InitializePasswordPage(self.driver)
        set_password_page.InputPassword('123')
        set_password_page.ClickStartButton()
        notes_page = NotesPage(self.driver)
        notes_page.ClickAddButton()
        notes_page.ClickAddCardDetails()
        add_card_details_page = AddCardDetailsPage(self.driver)
        add_card_details_page.InputCardName(cardName)
        add_card_details_page.InputCardNumber(cardNumber)
        add_card_details_page.InputCardValid('2019','2029')
        add_card_details_page.InputCardCVV('000')
        add_card_details_page.ClickSaveNoteButton()
        
        content = notes_page.GetNoteContent()
        self.assertIn(cardName, content)
        self.assertIn(cardNumber[-4:], content) # 信用卡卡號在首頁只會顯示最後4碼

    def testCreateLoginDetails(self):
        url = 'www.test.com'
        account = 'testAccount'
        password = 'testPassword'
        set_password_page = InitializePasswordPage(self.driver)
        set_password_page.InputPassword('123')
        set_password_page.ClickStartButton()
        notes_page = NotesPage(self.driver)
        notes_page.ClickAddButton()
        notes_page.ClickAddLoginDetails()
        add_login_details_page = AddLoginDetailsPage(self.driver)
        add_login_details_page.InputUrl(url)
        add_login_details_page.InputLoginAccount(account)
        add_login_details_page.InputLoginPassword(password)
        add_login_details_page.ClickSaveNoteButton()
        
        content = notes_page.GetNoteContent()
        self.assertIn(url, content)
        self.assertIn(account, content)

if __name__ == '__main__':
    unittest.main()