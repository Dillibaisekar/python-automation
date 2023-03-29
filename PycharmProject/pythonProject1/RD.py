import time
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# fun for find element by ID
def ele(id):
    elem = driver.find_element(By.ID, id)
    return elem

def xpath(xpath):
    elem = driver.find_element(By.XPATH, xpath)
    return elem

def link_text(text):
    elem = driver.find_element(By.LINK_TEXT, text)
    return elem

# fun for date picker
def picker(value):
    date = driver.find_elements(By.XPATH, "//div[@class='mat-calendar-body-cell-content mat-focus-indicator']")
    for element in date:
        datas = element.text
        # print(datas)
        if datas == value:
            element.click()
            break


def doc_proof_dropdown(value):
    dropdown = Select(driver.find_element(By.ID, 'ckyc_failure_depositor_proof_type'))
    dropdown.select_by_value(value)
    return dropdown

def account_type(value):
    dropdown = Select(
        driver.find_element(By.XPATH, "(//select[@class='form__control ng-untouched ng-pristine ng-invalid'])[1]"))
    dropdown.select_by_value(value)
    return dropdown

def mat_ins(value):
    dropdown = Select(driver.find_element(By.XPATH, "//select[@formcontrolname='inv_maturity_instruction_type']"))
    dropdown.select_by_value(value)

def add_drop_down(value, elem):
    dropdown = Select(elem)
    dropdown.select_by_value(value)

def wait(ele):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((ele)))

dataSheet = pd.read_excel(r'InputFiles\rd_data.xlsx')
for ind in dataSheet.index:
    c = webdriver.ChromeOptions()
    c.add_argument("--incognito")
    driver = webdriver.Chrome(options=c)
    driver.get("https://sitsfl.stfc.in/")
    driver.maximize_window()
    element_hover = driver.find_element(By.XPATH, "//div[@class='head-link'][1]")
    ActionChains(driver).move_to_element(element_hover).perform()
    rd = ele('main_nav_rd')
    wait(rd)
    otp1_data = dataSheet['OTP1'][ind]
    otp2_data = dataSheet['OTP2'][ind]
    otp3_data = dataSheet['OTP3'][ind]
    otp4_data = dataSheet['OTP4'][ind]
    otp5_data = dataSheet['OTP5'][ind]
    otp6_data = dataSheet['OTP6'][ind]
    pan_data = dataSheet['PAN'][ind]
    firstname_data = dataSheet['First_name'][ind]
    lastname_data = dataSheet['Last_name'][ind]
    mail_data = dataSheet['Mail'][ind]
    investamt_data = dataSheet['Investment amount'][ind]
    tenure_data = dataSheet['Tenure'][ind]
    instalment_data_data = dataSheet['Installment_date'][ind]
    doc_type_data = dataSheet['Doc_type'][ind]
    doc_num_data = dataSheet['Doc_num'][ind]
    proof_front_data = dataSheet['Proof_front'][ind]
    proof_back_data = dataSheet['Proof_back'][ind]
    address1_data = dataSheet['Address1'][ind]
    address2_data = dataSheet['Address2'][ind]
    pincode_data = dataSheet['Pincode'][ind]
    area_data = dataSheet['Area'][ind]
    photo_upload_data = dataSheet['Photo_upload'][ind]
    acc_num_data = dataSheet['Account_number'][ind]
    con_acc_num_data = dataSheet['Confirm_acc_number'][ind]
    ifsc_data = dataSheet['IFSC'][ind]
    acc_name_data = dataSheet['Acc_name'][ind]
    cheque_upload_data = dataSheet['Cheque_upload'][ind]
    mat_ins_data = dataSheet['Maturity_instruction'][ind]
    occupation_data = dataSheet['Occupation'][ind]
    fathername_data = dataSheet['Father_name'][ind]
    marital_status_data = dataSheet['Marital_status'][ind]
    fd_tenure_data = dataSheet['Fd_tenure'][ind]
    fd_payout_data = dataSheet['FD_payout'][ind]
    nom_relationship = dataSheet['Nom_relationship'][ind]
    nom_title_data = dataSheet['Nom_title'][ind]
    nom_first_name_data = dataSheet['Nom_first_name'][ind]
    nom_last_name_data = dataSheet['Nom_last_name'][ind]
    nom_ad1_data = dataSheet['Nom_ad1'][ind]
    nom_ad2_data = dataSheet['Nom_ad2'][ind]
    nom_pincode_data = dataSheet['Nom_pincode'][ind]
    print(nom_pincode_data)
    rd.click()
    mobile = ele('cus_mobile')
    pincode = ele('cus_pincode')
    amount = ele('cus_investment_amount')
    invest_now = ele('pf-apply-btn')
    wait(mobile)
    mobile_data = dataSheet['Mobile_Number'][ind]
    mobile.send_keys(str(mobile_data))
    pin_data = dataSheet['Pincode'][ind]
    pincode.send_keys(str(pin_data))
    amount_data = dataSheet['Amount'][ind]
    amount.send_keys(str(amount_data))
    invest_now.click()
    #      Done with landing screen
    #      OTP screen
    otp1 = ele('otpCode1')
    otp2 = ele('otpCode2')
    otp3 = ele('otpCode3')
    otp4 = ele('otpCode4')
    otp5 = ele('otpCode5')
    otp6 = ele('otpCode6')
    otp_verify = ele('otpVerifybtn')
    wait(otp1)
    otp1.send_keys(str(otp1_data))
    otp2.send_keys(str(otp2_data))
    otp3.send_keys(str(otp3_data))
    otp4.send_keys(str(otp4_data))
    otp5.send_keys(str(otp5_data))
    otp6.send_keys(str(otp6_data))
    otp_verify.click()
    if driver.current_url == 'https://sitsfl.stfc.in/recurring-deposit-online/personal-information':
        pan = xpath('//*[@id="pan2"]')
        wait(pan)
        pan.send_keys(str(pan_data))
        pan.click()
        firstname = ele('firstName')
        lastname = ele('lastName')
        dobclick = xpath('//*[@id="depositer-details"]/form/div/div[2]/div/div[3]/div[1]/div[6]/div/input')
        driver.execute_script("window.scrollTo(0, 800)")
        wait(firstname)
        firstname.clear()
        lastname.clear()
        firstname.send_keys(str(firstname_data))
        lastname.send_keys(str(lastname_data))
        dobclick.click()
        dobyear = xpath(
            "//button[@class='mat-focus-indicator mat-calendar-period-button mat-button mat-button-base']")
        dobyear.click()
        # y=1999
        picker('2003')
        picker('MAY')
        picker('21')
        mail = ele('email')
        mail.clear()
        mail.send_keys(str(mail_data))
        # xpath for scheme selection
        invest_edit = xpath("(//i[@class='icon icon-edit'])[1]")
        invest_edit.click()
        investamount2 = ele('scheme_install_amount')
        investamount2.clear()
        tenure12 = xpath("//label[text()='12']")
        tenure24 = xpath("//label[text()='24']")
        tenure36 = xpath("//label[text()='36']")
        tenure48 = xpath("//label[text()='48']")
        tenure60 = xpath("//label[text()='60']")
        tenure36.click()
        tenure48.click()
        tenure12.click()
        tenure24.click()
        tenure60.click()
        # installment_date = xpath("(//i[@class='icon icon-edit'])[2]")
        # installment_date.click()
        # picker('31')
        #
        # time.sleep(2)
        #
        # bg = xpath("//h2[text()='RD Investment Summary']")
        # bg.click()

        # terms_cond = xpath('//*[@id="depositer-details"]/form/div/div[3]/div[1]/div[4]/div/div[1]/div/div/label')
        # terms_cond.click()
        continue1 = xpath("(//button[@class='button button--yellow'])[1]")
        continue1.click()
        print('done')
        # to automate the payment gateway (switch to iframe)
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='razorpay-checkout-frame']"))
        netbanking = xpath("(//div[@class='title svelte-1r0bvhf'])[1]")
        wait(netbanking)
        netbanking.click()
        bank = xpath("(//label[@class='radio-label mfix'])[1]")
        wait(bank)
        bank.click()
        make_payment = xpath("(//button[@class='svelte-13mgn3i'])[2]")
        wait(make_payment)
        make_payment.click()
        sucess_click = xpath("//button[@class='success']")
        wait(sucess_click)
        sucess_click.click()

    #         done with PAN screen
    if driver.current_url == "https://sitsfl.stfc.in/recurring-deposit-online/address-information":
        #    # CKYC screen
        doc_type = ele('ckyc_failure_depositor_proof_type')
        wait(doc_type)
        doc_type.click()
        doc_proof_dropdown('RDAID')
        doc_num = xpath("//input[@class='form__control ng-untouched ng-dirty ng-invalid']")
        doc_num.send_keys(str(doc_num_data))
        proof_front = xpath('//*[@id="ckyc_failure_depositor_proof_front"]')
        wait(proof_front)
        proof_front.send_keys(proof_front_data)
        proof_back = xpath('//*[@id="ckyc_failure_depositor_proof_back"]')
        proof_back.send_keys(str(proof_back_data))
        continue2 = xpath("//button[@class='button button--yellow button--small']")
        continue2.click()
        address1 = ele('depositor_address_1')
        address1.send_keys(str(address1_data))
        address2 = ele('depositor_address_2')
        address2.send_keys(str(address2_data))
        depositor_pincode = ele('depositor_pincode')
        depositor_pincode.send_keys(str(pincode_data))
        depositor_pincode.click()
        depositor_pincode.send_keys(Keys.ARROW_DOWN)
        depositor_pincode.send_keys(Keys.ENTER)
        upload_photo = xpath('//*[@id="depositor_photo"]')
        upload_photo.send_keys(str(photo_upload_data))
        continue2.click()
    if driver.current_url == "https://sitsfl.stfc.in/recurring-deposit-online/bank-information":
        driver.execute_script("window.scrollTo(0,200)")
        digital_payment = xpath("//span[@class='switch-handle']")
        digital_payment.click()
        account_number = xpath("//input[@formcontrolname='bank_accountNumber']")
        account_number.clear()
        account_number.send_keys(str(acc_num_data))
        confirm_account_number = xpath("//input[@formcontrolname='bank_confirmAccountNumber']")
        confirm_account_number.send_keys(str(con_acc_num_data))
        ifsc = xpath("//input[@formcontrolname='bank_IFSC']")
        ifsc.send_keys(str(ifsc_data))
        acc_name = xpath("//input[@formcontrolname='bank_personName']")
        acc_name.send_keys(str(acc_name_data))
        acc_type = xpath("//select[@formcontrolname='bank_type']")
        acc_type.click()
        account_type('RDSA')
        cheque_upload = xpath("//input[@formcontrolname='bankOCR']")
        cheque_upload.send_keys(str(cheque_upload_data))
        continue2 = xpath("//button[@class='button button--yellow button--small']")
        continue2.click()
    # Additional details screen
    if driver.current_url == "https://sitsfl.stfc.in/recurring-deposit-online/additional-details":
        maturity_instruction = xpath("//select[@formcontrolname='inv_maturity_instruction_type']")
        wait(maturity_instruction)
        maturity_instruction.click()
        mat_ins("RDCFD")
        occupation = xpath("//select[@formcontrolname='inv_occupation_type']")
        occupation.click()
        add_drop_down("PROFL", occupation)
        father_name = xpath("//input[@formcontrolname='father_name']")
        father_name.send_keys(str(fathername_data))
        marital_status = xpath("//select[@formcontrolname='inv_marital_status']")
        marital_status.click()
        add_drop_down("RDUNM", marital_status)
        fd_tenure = xpath("//select[@formcontrolname='deposit_fd_tenure_type']")
        fd_tenure.click()
        add_drop_down("36", fd_tenure)
        fd_payout = xpath("//select[@formcontrolname='deposit_fd_payout_type']")
        fd_payout.click()
        add_drop_down("QTR", fd_payout)
        print("success")
        #     Nominee details
        nominee = xpath("(//span[@class='switch-handle'])[2]")
        nominee.click()
        nom_rel = xpath("//select[@formcontrolname='nominee_relationship']")
        nom_rel.click()
        add_drop_down("FATHR", nom_rel)
        # nom_title = xpath("//select[@formcontrolname='nominee_title']")
        # nom_title.click()
        # add_drop_down("Mr.", nom_title)
        nom_fir_name = xpath("//input[@formcontrolname='nominee_firstName']")
        nom_fir_name.send_keys(str(nom_first_name_data))
        nom_last_name = xpath("//input[@formcontrolname='nominee_lastName']")
        nom_last_name.send_keys(str(nom_last_name_data))
        nom_dob = xpath("//input[@formcontrolname='nominee_dob']")
        nom_dob.click()
        nom_year = xpath(
            "//button[@class='mat-focus-indicator mat-calendar-period-button mat-button mat-button-base']").click()
        picker("1994")
        picker("OCT")
        picker("13")
        nom_ad1 = xpath("//input[@formcontrolname='nominee_address_1']")
        nom_ad1.send_keys(nom_ad1_data)
        nom_ad2 = xpath("//input[@formcontrolname='nominee_address_2']")
        nom_ad2.send_keys(nom_ad2_data)
        nom_pincode = xpath("//input[@formcontrolname='nominee_address_pincode']")
        nom_pincode.send_keys(str(nom_pincode_data))
        nom_pincode.click()
        nom_pincode.send_keys(Keys.ARROW_DOWN)
        nom_pincode.send_keys(Keys.ENTER)
        continue2 = xpath("//button[@class='button button--yellow button--small']")
        continue2.click()
        print("Lead created successfully")
        break
