from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self, _driver):
        self.driver = _driver
        self.wait = WebDriverWait(_driver, 10)
    
    def close(self):
        self.driver.close()

class InitializePasswordPage(BasePage):
    def __init__(self, _driver):
        super(InitializePasswordPage, self).__init__(_driver)
        startBtn_ID = 'com.twistedplane.sealnote:id/password_action_button'
        self.wait.until(EC.visibility_of_element_located((By.ID, startBtn_ID)))
    
    def InputPassword(self, password):
        passwordTF_ID = 'com.twistedplane.sealnote:id/password_input'
        self.driver.find_element_by_id(passwordTF_ID).send_keys(password)

    def ClickStartButton(self):
        startBtn_ID = 'com.twistedplane.sealnote:id/password_action_button'
        self.driver.find_element_by_id(startBtn_ID).click()

    def GetPasswordStrength(self):
        passworAssess_ID = 'com.twistedplane.sealnote:id/password_meter_text'
        return self.driver.find_element_by_id(passworAssess_ID).text

class EditTagsPage(BasePage):
    def __init__(self, _driver):
        super(EditTagsPage, self).__init__(_driver)
        goBackBtn_ID = 'android:id/up'
        self.wait.until(EC.visibility_of_element_located((By.ID, goBackBtn_ID)))

    def GoBackPage(self):
        goBackBtn_ID = 'android:id/up'
        self.driver.find_element_by_id(goBackBtn_ID).click()

    def RenameTagOf(self, index, NewTagName):
        listTags_ID = 'com.twistedplane.sealnote:id/text1'
        renameTF_ID = 'com.twistedplane.sealnote:id/input_rename'
        renameBtn_ID = 'android:id/button1'
        self.driver.find_elements_by_id(listTags_ID)[index].click()
        self.driver.find_element_by_id(renameTF_ID).claer()
        self.driver.find_element_by_id(renameTF_ID).send_keys(NewTagName)
        self.driver.find_element_by_id(renameBtn_ID).click()

    def DeleteTagOf(self, index):
        listDeleteBtn_ID = 'com.twistedplane.sealnote:id/delete_button'
        self.driver.find_elements_by_id(listDeleteBtn_ID)[index].click()

    def GetTagNameOf(self, index):
        listTags_ID = 'com.twistedplane.sealnote:id/text1'
        return self.driver.find_elements_by_id(listTags_ID)[index].text

class HomePage(BasePage):
    def __init__(self, _driver):
        super(HomePage, self).__init__(_driver)
        menuBtn_ID = 'android:id/up'
        self.wait.until(EC.visibility_of_element_located((By.ID, menuBtn_ID)))

    def ClickMenuButton(self):
        menuBtn_ID = 'android:id/up'
        self.driver.find_element_by_id(menuBtn_ID).click()
        return self
    
    def ClickGoNotesPage(self):
        self.driver.find_elements_by_id('com.twistedplane.sealnote:id/text1')[0].click()

    def ClickGoArchivePage(self):
        self.driver.find_elements_by_id('com.twistedplane.sealnote:id/text1')[1].click()

    def ClickGoTrashPage(self):
        self.driver.find_elements_by_id('com.twistedplane.sealnote:id/text1')[2].click()

    def ClickOverflowButton(self):
        overflowBtn_AccessID = '更多選項'
        self.driver.find_element_by_accessibility_id(overflowBtn_AccessID).click()
        return self
    
    def ClickEditTags(self):
        self.driver.find_elements_by_id('android:id/title')[0].click()
    
    def ClickSettings(self):
        self.driver.find_elements_by_id('android:id/title')[1].click()

    def ClickAbout(self):
        self.driver.find_elements_by_id('android:id/title')[2].click()

    def ClickLogout(self):
        self.driver.find_elements_by_id('android:id/title')[3].click()

    def GetNoteTitle(self):
        noteTitle_ID = 'com.twistedplane.sealnote:id/card_header_inner_simple_title'
        return self.driver.find_element_by_id(noteTitle_ID).text

    def GetNoteContent(self):
        noteContent_ID = 'com.twistedplane.sealnote:id/cardcontent_note'
        return self.driver.find_element_by_id(noteContent_ID).text
    
    def OpenNoteOf(self, index):
        listNotes_ID = 'com.twistedplane.sealnote:id/list_cardId'
        self.driver.find_elements_by_id(listNotes_ID)[index].click()
    
class NotesPage(HomePage):
    def ClickAddButton(self):
        addBtn_ID = 'com.twistedplane.sealnote:id/action_new_note'
        self.driver.find_element_by_id(addBtn_ID).click()
        return self

    def ClickAddPlainText(self):
        self.driver.find_elements_by_id('android:id/title')[0].click()
        
    def ClickAddCardDetails(self):
        self.driver.find_elements_by_id('android:id/title')[1].click()

    def ClickAddLoginDetails(self):
        self.driver.find_elements_by_id('android:id/title')[2].click()

class AddNotesPage(BasePage):
    def __init__(self, _driver):
        super(AddNotesPage, self).__init__(_driver)
        titleTF_ID = 'com.twistedplane.sealnote:id/note_activity_title'
        self.wait.until(EC.visibility_of_element_located((By.ID, titleTF_ID)))
   
    def InputTags(self, tags):
        tagTF_ID = 'com.twistedplane.sealnote:id/note_activity_tags'
        inputTags = " ".join(tags) # send_keys()每次輸入時會清空text field，只好先組合要輸入的tag
        self.driver.find_element_by_id(tagTF_ID).send_keys(inputTags)
        self.driver.keyevent(62) # 鍵盤事件，62為空白鍵
        
    def InputTitle(self, title):
        titleTF_ID = 'com.twistedplane.sealnote:id/note_activity_title'
        self.driver.find_element_by_id(titleTF_ID).send_keys(title)

    def ClickSaveNoteButton(self):
        saveBtn_ID = 'com.twistedplane.sealnote:id/action_save_note'
        self.driver.find_element_by_id(saveBtn_ID).click()

    def ClickArchiveButton(self):
        archiveBtn_ID = 'com.twistedplane.sealnote:id/action_archive'
        self.driver.find_element_by_id(archiveBtn_ID).click()

    def ClickDeleteButton(self):
        deleteBtn_ID = 'com.twistedplane.sealnote:id/action_note_delete'
        self.driver.find_element_by_id(deleteBtn_ID).click()
        
class AddPlainTextPage(AddNotesPage):
    def InputContent(self, content):
        contentTF_ID = 'com.twistedplane.sealnote:id/note_activity_note'
        self.driver.find_element_by_id(contentTF_ID).send_keys(content)
    
class AddCardDetailsPage(AddNotesPage):    
    def InputCardName(self, cardName):
        cardNameTF_ID = 'com.twistedplane.sealnote:id/note_card_name'
        self.driver.find_element_by_id(cardNameTF_ID).send_keys(cardName)

    def InputCardNumber(self, cardNumber):
        cardNumberTF_ID = 'com.twistedplane.sealnote:id/note_card_number'
        self.driver.find_element_by_id(cardNumberTF_ID).send_keys(cardNumber)
    
    def InputCardValid(self, fromYear, uptoYear):
        cardFromYearTF_ID = 'com.twistedplane.sealnote:id/note_card_valid_from'
        cardUptoYearTF_ID = 'com.twistedplane.sealnote:id/note_card_valid_upto'
        self.driver.find_element_by_id(cardFromYearTF_ID).send_keys(fromYear)
        self.driver.find_element_by_id(cardUptoYearTF_ID).send_keys(uptoYear)

    def InputCardCVV(self, cvvNumber):
        cardCVVTF_ID = 'com.twistedplane.sealnote:id/note_card_cvv'
        self.driver.find_element_by_id(cardCVVTF_ID).send_keys(cvvNumber)
    
    def InputAdditionalNotes(self, content):
        cardAdditionalNoteTF_ID = 'com.twistedplane.sealnote:id/note_card_note'
        self.driver.find_element_by_id(cardAdditionalNoteTF_ID).send_keys(content)

class AddLoginDetailsPage(AddNotesPage):    
    def InputUrl(self, url):
        urlTF_ID = 'com.twistedplane.sealnote:id/note_login_url'
        self.driver.find_element_by_id(urlTF_ID).send_keys(url)

    def InputLoginAccount(self, account):
        loginAccountTF_ID = 'com.twistedplane.sealnote:id/note_login_name'
        self.driver.find_element_by_id(loginAccountTF_ID).send_keys(account)

    def InputLoginPassword(self, password):
        loginPasswordTF_ID = 'com.twistedplane.sealnote:id/note_login_password'
        self.driver.find_element_by_id(loginPasswordTF_ID).send_keys(password)   

    def InputAdditionalNotes(self, content):
        loginAdditionalNoteTF_ID = 'com.twistedplane.sealnote:id/note_additional_note'
        self.driver.find_element_by_id(loginAdditionalNoteTF_ID).send_keys(content)

class ArchivePage(HomePage):
    pass

class TrashPage(HomePage):
    pass