import time

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.switchToFrameByIndex = None
        self.driver = driver

    ################
    ### Locators ###
    ################
    _search_box = "search"
    _search_course_icon = "search-course-button"
    _course = "//h4[contains(text(),'JavaScript for beginners')]"
    _all_courses = "//h1[contains(text(),'All Courses')]"
    _enroll_button = "div#zen_cs_desc_with_promo_dynamic button"
    _cc_num = "//input[@aria-label='Credit or debit card number']"
    _cc_exp = "cc-exp"
    _cc_cvv = "cc_cvc"
    _submit_enroll = "//button[@id='confirm-purchase']/parent::div"
    _enroll_error_message = "//div[@id='new_card']//div[contains(text(),'The card number is not a valid credit card number.')]"
    _zip = "postal"
    _agree_to_terms_checkbox = "agreed_to_terms_checkbox"

    ############################
    ### Element Interactions ###
    ############################
    def enterCourseName(self, name):
        self.sendKeys(name, locator=self._search_box)
        self.elementClick(locator=self._search_course_icon)

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button)

    def enterCardNum(self, num):
        # This frame takes at least 6 seconds to show, it may take more for you
        time.sleep(6)
        # self.switchToFrame(name="__privateStripeFrame8")
        self.SwitchFrameByIndex(self._cc_num, locatorType="xpath")
        self.sendKeysWhenReady(num, locator=self._cc_num, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        # self.switchToFrame(name="__privateStripeFrame9")
        self.SwitchFrameByIndex(self._cc_exp, locatorType="name")
        self.sendKeys(exp, locator=self._cc_exp, locatorType="name")
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        # self.switchToFrame(name="__privateStripeFrame10")
        self.SwitchFrameByIndex(self._cc_cvv, locatorType="name")
        self.sendKeys(cvv, locator=self._cc_cvv, locatorType="name")
        self.switchToDefaultContent()

    def enterZip(self, zip):
        # self.switchToFrame(name="__privateStripeFrame11")
        self.SwitchFrameByIndex(self._zip, locatorType="name")
        self.sendKeys(zip, locator=self._zip, locatorType="name")
        self.switchToDefaultContent()

    def clickAgreeToTermsCheckbox(self):
        self.elementClick(locator=self._agree_to_terms_checkbox)

    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvv, zip):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        self.enterZip(zip)

    def enrollCourse(self, num="", exp="", cvv="", zip=""):
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv, zip)
        self.clickAgreeToTermsCheckbox()

    def verifyEnrollFailed(self):
        result = self.isEnabled(locator=self._submit_enroll, locatorType="xpath",
                                info="Enroll Button")
        return not result