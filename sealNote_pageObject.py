from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class sealNote_pageObject(object):
    def __init__(self, _driver):
        self.driver = _driver
        self.wait = WebDriverWait(_driver, 10)

    def close(self):
        self.driver.close()

    def InitializePassword(self, password):
        passwordTF_ID = 'com.twistedplane.sealnote:id/password_input'
        commitBtn_ID = 'com.twistedplane.sealnote:id/password_action_button'
        self.wait.until(EC.visibility_of_element_located((By.ID, passwordTF_ID)))
        self.driver.find_element_by_id(passwordTF_ID).send_keys(password)
        self.driver.find_element_by_id(commitBtn_ID).click()

    def ClickAddNewNoteButton(self):
        creatBtn_ID = 'com.twistedplane.sealnote:id/action_new_note'
        self.wait.until(EC.visibility_of_element_located((By.ID, creatBtn_ID)))
        self.driver.find_element_by_id(creatBtn_ID).click()

    def ClickAddPlainText(self):
        self.driver.find_elements_by_id('android:id/title')[0].click()
        
    def ClickAddCardDetails(self):
        self.driver.find_elements_by_id('android:id/title')[1].click()

    def ClickAddLoginDetails(self):
        self.driver.find_elements_by_id('android:id/title')[2].click()
                
    def ClickSaveNoteButton(self):
        saveBtn_ID = 'com.twistedplane.sealnote:id/action_save_note'
        self.driver.find_element_by_id(saveBtn_ID).click()
    
    def InputTags(self, tag):
        tagTF_ID = 'com.twistedplane.sealnote:id/note_activity_tags'
        self.driver.find_element_by_id(tagTF_ID).send_keys(tag)
        self.driver.keyevent(66) # 鍵盤事件，66為TAB鍵
        
    def InputTitle(self, title):
        titleTF_ID = 'com.twistedplane.sealnote:id/note_activity_title'
        self.driver.find_element_by_id(titleTF_ID).send_keys(title)
    
    def InputContent(self, content):
        contentTF_ID = 'com.twistedplane.sealnote:id/note_activity_note'
        self.driver.find_element_by_id(contentTF_ID).send_keys(content)
    
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
    
    def InputCardAdditionalNote(self, content):
        cardAdditionalNoteTF_ID = 'com.twistedplane.sealnote:id/note_card_note'
        self.driver.find_element_by_id(cardAdditionalNoteTF_ID).send_keys(content)

    def InputUrl(self, url):
        urlTF_ID = 'com.twistedplane.sealnote:id/note_login_url'
        self.driver.find_element_by_id(urlTF_ID).send_keys(url)

    def InputLoginAccount(self, account):
        loginAccountTF_ID = 'com.twistedplane.sealnote:id/note_login_name'
        self.driver.find_element_by_id(loginAccountTF_ID).send_keys(account)

    def InputLoginPassword(self, password):
        loginPasswordTF_ID = 'com.twistedplane.sealnote:id/note_login_password'
        self.driver.find_element_by_id(loginPasswordTF_ID).send_keys(password)   

    def InputLoginAdditionalNote(self, content):
        loginAdditionalNoteTF_ID = 'com.twistedplane.sealnote:id/note_additional_note'
        self.driver.find_element_by_id(loginAdditionalNoteTF_ID).send_keys(content)

    def GetNoteTitle(self):
        noteTitle_ID = 'com.twistedplane.sealnote:id/card_header_inner_simple_title'
        return self.driver.find_element_by_id(noteTitle_ID)

    def GetNoteContent(self):
        noteContent_ID = 'com.twistedplane.sealnote:id/cardcontent_note'
        return self.driver.find_element_by_id(noteContent_ID)


