import self as self
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Homepage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

locators = {
"sign_in": ("ID", "signin"),
"user_name": ("CSS", ".username")
}

def Click(element, self):
    wait = WebDriverWait(self.driver, 10)
    a = wait.until(EC.element_to_be_clickable(element))
    a.click()

def sendkeys(value, xpath, exceldata,self):
    if (value == ""):
        a=WebDriverWait(self.driver, 10).until(EC.visibility_of(xpath))
        a.send_keys(str(exceldata))
        return a

# fun for find element by ID
def ele(x,self):
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, x)))
    elem = self.driver.find_element(By.ID, x)
    return elem

def xpath(xpath):
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, xpath)))
    elem = driver.find_element(By.XPATH, xpath)
    return elem

# fun for date picker
def picker(value):
    date = driver.find_elements(By.XPATH, "//div[@class='mat-calendar-body-cell-content mat-focus-indicator']")
    for element in date:
        datas = element.text
        if datas == value:
            element.click()
            break

def doc_proof_dropdown(value):
    dropdown = Select(driver.find_element(By.ID, 'ckyc_failure_depositor_proof_type'))
    dropdownvalue = dropdown.first_selected_option.get_attribute("value")
    if (dropdownvalue == ""):
        dropdown.select_by_value(value)
    return dropdown

def account_type(value):
    dropdown = Select(driver.find_element(By.XPATH, "(//select[@formcontrolname='bank_type'])[1]"))
    dropdownvalue = dropdown.first_selected_option.get_attribute("value")
    if (dropdownvalue == ""):
        dropdown.select_by_value(value)
    return dropdown

def mat_ins(value):
    dropdown = Select(driver.find_element(By.XPATH, "//select[@formcontrolname='inv_maturity_instruction_type']"))
    dropdownvalue = dropdown.first_selected_option.get_attribute("value")
    if (dropdownvalue == ""):
        dropdown.select_by_value(value)

def add_drop_down(value, elem):
    dropdown = Select(elem)
    dropdownvalue=dropdown.first_selected_option.get_attribute("value")
    if(dropdownvalue == ""):
        dropdown.select_by_value(value)

def error_msg():
    try:
     if xpath('//span[@class="errMsg"]').is_displayed():
         print("Error Occured")
    except:
        print('Screen sucessfully completed')

pan = xpath('//*[@id="pan2"]')
firstname = ele('firstName')
lastname = ele('lastName')
dobclick = xpath('//*[@id="depositer-details"]/form/div/div[2]/div/div[3]/div[1]/div[6]/div/input')
mail = ele('email')
invest_edit = xpath("(//i[@class='icon icon-edit'])[1]")
investamount2 = ele('scheme_install_amount')
tenure12 = xpath("//label[text()='12']")
tenure24 = xpath("//label[text()='24']")
tenure36 = xpath("//label[text()='36']")
tenure48 = xpath("//label[text()='48']")
tenure60 = xpath("//label[text()='60']")
continue1 = xpath("(//button[@class='button button--yellow'])[1]")
driver.switch_to.frame(xpath("//iframe[@class='razorpay-checkout-frame']"))
payment_num = xpath('//input[@class="input-one-click-checkout phone-field-one-click-checkout main svelte-18u3466"]')
netbanking = xpath("(//div[@class='title svelte-1r0bvhf'])[1]")
bank = xpath("(//label[@class='radio-label mfix'])[1]")
make_payment = xpath("(//button[@class='svelte-13mgn3i'])[2]")
sucess_click = xpath("//button[@class='success']")
netbanking_air=xpath('(//a[@class="menu-link"])[2]')
bankname_air=xpath('//span[@class="bankLogo lo-nbmahnetbnk"]')
button_air=xpath('(//input[@class="btn"])[2]')
doc_type = ele('ckyc_failure_depositor_proof_type')
doc_num = ele("ckyc_failure_depositor_proof_no")
proof_front = ele("ckyc_failure_depositor_proof_front")
proof_back = ele("ckyc_failure_depositor_proof_back")
continue2 = xpath("//button[@class='button button--yellow button--small']")
address1 = ele('depositor_address_1')
address2 = ele('depositor_address_2')
depositor_pincode = ele('depositor_pincode')
upload_photo = xpath('//*[@id="depositor_photo"]')
account_number = xpath("//input[@formcontrolname='bank_accountNumber']")
confirm_account_number = xpath("//input[@formcontrolname='bank_confirmAccountNumber']")
ifsc = xpath("//input[@formcontrolname='bank_IFSC']")
acc_name = xpath("//input[@formcontrolname='bank_personName']")
acc_type = xpath("//select[@formcontrolname='bank_type']")
cheque_upload = xpath("//input[@formcontrolname='bankOCR']")
occupation = xpath("//select[@formcontrolname='inv_occupation_type']")
father_name = xpath("//input[@formcontrolname='father_name']")
marital_status = xpath("//select[@formcontrolname='inv_marital_status']")
fd_tenure = xpath("//select[@formcontrolname='deposit_fd_tenure_type']")
fd_payout = xpath("//select[@formcontrolname='deposit_fd_payout_type']")
nom = xpath('//input[@formcontrolname="is_nominee"]')
nom_rel = xpath("//select[@formcontrolname='nominee_relationship']")
nom_title = xpath("//select[@formcontrolname='nominee_title']")
nom_fir_name = xpath("//input[@formcontrolname='nominee_firstName']")
nom_last_name = xpath("//input[@formcontrolname='nominee_lastName']")
nom_dob = xpath("//input[@formcontrolname='nominee_dob']")
year = xpath("//button[@class='mat-focus-indicator mat-calendar-period-button mat-button mat-button-base']")
nom_add_same=xpath('//input[@formcontrolname="nominee_applicant_address_same"]')
nom_ad1 = xpath("//input[@formcontrolname='nominee_address_1']")
nom_ad2 = xpath("//input[@formcontrolname='nominee_address_2']")
nom_pincode = xpath("//input[@formcontrolname='nominee_address_pincode']")
editscheme=xpath('//button[@class="button button--black button--small mb-md-15"]')
popup=ele('modal-close-btn')
hover=xpath("//div[@class='head-link'][1]")
rd = ele('main_nav_rd')
mobile = ele('cus_mobile')
pincode = ele('cus_pincode')
amount = ele('cus_investment_amount')
invest_now = ele('pf-apply-btn')
digital_payment = xpath("//span[@class='switch-handle']")
otp1 = ele('otpCode1')
otp2 = ele('otpCode2')
otp3 = ele('otpCode3')
otp4 = ele('otpCode4')
otp5 = ele('otpCode5')
otp6 = ele('otpCode6')
otp_verify = ele('otpVerifybtn')






