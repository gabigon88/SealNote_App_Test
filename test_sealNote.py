import unittest
from time import sleep
from appium import webdriver
from sealNote_pageObject import *

class SealNoteTest(unittest.TestCase):
    def setUp(self):        
        ''' 我的實體手機 '''
        device='YT910R6JBG' # 此為設備號，手機連上電腦後在cmd下adb devices可查看
        androidVer = '4.4.3' # 此為設備號android版本
        
        ''' 夜神模擬器 '''
        # device='127.0.0.1:62001'
        # androidVer = '5'

        # app = ('D:\\sealnote25.apk') # 此為受測app的apk檔路徑，需為絕對路徑
        pack='com.twistedplane.sealnote' # 此為app的package名稱
        activity='com.twistedplane.sealnote.SealnoteActivity' # 此為app的主activity

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = androidVer
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

    def toInitializePassword(self, password='123'):
        """ 初次開啟app時，設定密碼 """
        set_password_page = InitializePasswordPage(self.driver)
        set_password_page.InputPassword('123')
        set_password_page.ClickStartButton()

    def toCreatePlainText(self, title='testTitle', content='testContent', tag=None):
        """ 建立一個PlainText的Note """
        global notes_page, add_plain_text_page # 要使用全域變數，其他呼叫此函式的function還用會到這些page
        notes_page = NotesPage(self.driver)
        notes_page.ClickAddButton()
        notes_page.ClickAddPlainText()
        add_plain_text_page = AddPlainTextPage(self.driver)
        add_plain_text_page.InputTitle(title)
        add_plain_text_page.InputContent(content)
        if tag != None:
            add_plain_text_page.InputTags(tag)
        add_plain_text_page.ClickSaveNoteButton()

    def testCreatePlainText(self):
        testTitle = 'testTitle'
        testContent = 'testContent'
        self.toInitializePassword()
        self.toCreatePlainText(testTitle, testContent)

        title = notes_page.GetNoteTitle()
        content = notes_page.GetNoteContent()
        self.assertEqual(title, testTitle)
        self.assertEqual(content, testContent)

    def testCreateCardDetails(self):
        cardName = 'MyVisa'
        cardNumber = '123456789012'
        self.toInitializePassword()
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
        self.toInitializePassword()
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

    def testAddTag(self):
        testTag = 'testTag'
        self.toInitializePassword()
        self.toCreatePlainText(tag=testTag)
        notes_page.ClickOverflowButton().ClickEditTags()

        edit_tags_page = EditTagsPage(self.driver)
        tag = edit_tags_page.GetTagNameOf(0)
        self.assertEqual(tag, testTag)
        
    def testArchiveNote(self):
        testTitle = 'testTitle'
        testContent = 'testContent'
        self.toInitializePassword()
        self.toCreatePlainText(testTitle, testContent)
        notes_page.OpenNoteOf(0)
        add_plain_text_page.ClickArchiveButton()
        notes_page.ClickMenuButton().ClickGoArchivePage()
    
        archive_page = ArchivePage(self.driver)
        title = archive_page.GetNoteTitle()
        content = archive_page.GetNoteContent()
        self.assertEqual(title, testTitle)
        self.assertEqual(content, testContent)

    def testDeleteNote(self):
        testTitle = 'testTitle'
        testContent = 'testContent'
        self.toInitializePassword()
        self.toCreatePlainText(testTitle, testContent)
        notes_page.OpenNoteOf(0)
        add_plain_text_page.ClickDeleteButton()
        notes_page.ClickMenuButton().ClickGoTrashPage()
    
        trash_page = TrashPage(self.driver)
        title = trash_page.GetNoteTitle()
        content = trash_page.GetNoteContent()
        self.assertEqual(title, testTitle)
        self.assertEqual(content, testContent)

if __name__ == '__main__':
    unittest.main()