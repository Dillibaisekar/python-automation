import os.path
import time
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

def Click(element):
    wait = WebDriverWait(driver, 10)
    a = wait.until(EC.element_to_be_clickable(element))
    a.click()

def sendkeys(value, xpath, exceldata):
    if (value == ""):
        a=WebDriverWait(driver, 10).until(EC.visibility_of(xpath))
        a.send_keys(str(exceldata))
        return a

# fun for find element by ID
def ele(x):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, x)))
    elem = driver.find_element(By.ID, x)
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

def panscreen():
    if driver.current_url == 'https://sitsfl.stfc.in/recurring-deposit-online/personal-information':
        pan = xpath('//*[@id="pan2"]')
        panvalue=pan.get_attribute("value")
        sendkeys(panvalue,pan,pan_data)
        firstname = ele('firstName')
        lastname = ele('lastName')
        dobclick = xpath('//*[@id="depositer-details"]/form/div/div[2]/div/div[3]/div[1]/div[6]/div/input')
        driver.execute_script("window.scrollTo(0, 800)")
        firstnamevalue=firstname.get_attribute("value")
        sendkeys(firstnamevalue,firstname,firstname_data)
        lastnamevalue=lastname.get_attribute("value")
        sendkeys(lastnamevalue,lastname,lastname_data)
        dobvalue = dobclick.get_attribute("value")
        print("Selected DOB Value {}".format(dobvalue))
        if(dobvalue == ""):
            dobclick.click()
            dobyear = xpath(
                "//button[@class='mat-focus-indicator mat-calendar-period-button mat-button mat-button-base']")
            dobyear.click()
            picker('2003')
            picker('MAY')
            picker('21')
        mail = ele('email')
        mailvalue=mail.get_attribute("value")
        sendkeys(mailvalue,mail,mail_data)
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
        continue1 = xpath("(//button[@class='button button--yellow'])[1]")
        continue1.click()
        error_msg()
        # to automate the payment gateway (switch to iframe)
        driver.switch_to.frame(xpath("//iframe[@class='razorpay-checkout-frame']"))
        payment_num=xpath('//input[@class="input-one-click-checkout phone-field-one-click-checkout main svelte-18u3466"]')
        payment_num.send_keys('9791399767')
        ele('redesign-v15-cta').click()
        netbanking = xpath("(//div[@class='title svelte-1r0bvhf'])[1]")
        netbanking.click()
        bank = xpath("(//label[@class='radio-label mfix'])[1]")
        bank.click()
        make_payment = xpath("(//button[@class='svelte-13mgn3i'])[2]")
        make_payment.click()
        sucess_click = xpath("//button[@class='success']")
        sucess_click.click()
def addressinfo():
    if driver.current_url == "https://sitsfl.stfc.in/recurring-deposit-online/address-information":
        #    # CKYC screen
        doc_type = ele('ckyc_failure_depositor_proof_type')
        doc_type.click()
        doc_proof_dropdown('RDAID')
        doc_num = ele("ckyc_failure_depositor_proof_no")
        doc_numvalue=doc_num.get_attribute("value")
        sendkeys(doc_numvalue,doc_num,doc_num_data)
        proof_front = ele("ckyc_failure_depositor_proof_front")
        # proof_frontvalue=proof_front.get_attribute("value")
        # sendkeys(proof_frontvalue,proof_front,proof_front_data)
        frontpath=os.path.abspath(proof_front_data)
        proof_front.send_keys(frontpath)
        proof_back = ele("ckyc_failure_depositor_proof_back")
        # proof_backvalue=proof_back.get_attribute("value")
        # sendkeys(proof_backvalue,proof_back,proof_back_data)
        backpath=os.path.abspath(proof_back_data)
        proof_back.send_keys(str(backpath))
        continue2 = xpath("//button[@class='button button--yellow button--small']")
        continue2.click()
        address1 = ele('depositor_address_1')
        address1value=address1.get_attribute("value")
        sendkeys(address1value,address1,address1_data)
        address2 = ele('depositor_address_2')
        address2value=address2.get_attribute("value")
        sendkeys(address2value,address2,address2_data)
        depositor_pincode = ele('depositor_pincode')
        depositor_pincodevalue=depositor_pincode.get_attribute("value")
        sendkeys(depositor_pincodevalue,depositor_pincode,pincode_data)
        depositor_pincode.click()
        depositor_pincode.send_keys(Keys.ARROW_DOWN)
        depositor_pincode.send_keys(Keys.ENTER)
        upload_photo = xpath('//*[@id="depositor_photo"]')
        uploadpath=os.path.abspath((photo_upload_data))
        upload_photo.send_keys(str(uploadpath))
        # upload_photovalue=upload_photo.get_attribute("value")
        # sendkeys(upload_photovalue,upload_photo,photo_upload_data)
        continue2.click()
        error_msg()

def bankscreen():
    if driver.current_url == "https://sitsfl.stfc.in/recurring-deposit-online/bank-information":
        driver.execute_script("window.scrollTo(0,200)")
        # digital_payment = xpath("//span[@class='switch-handle']")
        # digital_payment.click()
        account_number = xpath("//input[@formcontrolname='bank_accountNumber']")
        account_numbervalue=account_number.get_attribute("value")
        sendkeys(account_numbervalue,account_number,acc_num_data)
        confirm_account_number = xpath("//input[@formcontrolname='bank_confirmAccountNumber']")
        confirm_account_numbervalue = confirm_account_number.get_attribute("value")
        sendkeys(confirm_account_numbervalue, confirm_account_number, con_acc_num_data)
        ifsc = xpath("//input[@formcontrolname='bank_IFSC']")
        ifscvalue=ifsc.get_attribute("value")
        sendkeys(ifscvalue,ifsc,ifsc_data)
        ifsc.click()
        acc_name = xpath("//input[@formcontrolname='bank_personName']")
        acc_namevalue=acc_name.get_attribute("value")
        sendkeys(acc_namevalue,acc_name,acc_name_data)
        acc_type = xpath("//select[@formcontrolname='bank_type']")
        acc_type.click()
        account_type('RDSA')
        cheque_upload = xpath("//input[@formcontrolname='bankOCR']")
        chequepath=os.path.abspath(cheque_upload_data)
        cheque_upload.send_keys(str(chequepath))
        continue2 = xpath("//button[@class='button button--yellow button--small']")
        continue2.click()

def additionaldetails():
    if driver.current_url == "https://sitsfl.stfc.in/recurring-deposit-online/additional-details":
        mat_ins("RDCFD")
        occupation = xpath("//select[@formcontrolname='inv_occupation_type']")
        add_drop_down("PROFL", occupation)
        father_name = xpath("//input[@formcontrolname='father_name']")
        father_namevalue=father_name.get_attribute("value")
        sendkeys(father_namevalue,father_name,fathername_data)
        marital_status = xpath("//select[@formcontrolname='inv_marital_status']")
        marital_statusvalue=marital_status.get_attribute('disabled')
        if (marital_statusvalue!='true' or marital_statusvalue==''):
            add_drop_down("RDUNM", marital_status)
        fd_tenure = xpath("//select[@formcontrolname='deposit_fd_tenure_type']")
        add_drop_down("36", fd_tenure)
        fd_payout = xpath("//select[@formcontrolname='deposit_fd_payout_type']")
        add_drop_down("QTR", fd_payout)
        #     Nominee details
        nom = xpath('//input[@formcontrolname="is_nominee"]')
        nomvalue=nom.get_attribute("checked")
        if nomvalue=='true':
            nom_rel = xpath("//select[@formcontrolname='nominee_relationship']")
            nom_rel.click()
            add_drop_down("FATHR", nom_rel)
            # nom_title = xpath("//select[@formcontrolname='nominee_title']")
            nom_fir_name = xpath("//input[@formcontrolname='nominee_firstName']")
            nom_fir_namevalue = nom_fir_name.get_attribute("value")
            sendkeys(nom_fir_namevalue, nom_fir_name, nom_first_name_data)
            nom_last_name = xpath("//input[@formcontrolname='nominee_lastName']")
            nom_last_namevalue = nom_last_name.get_attribute("value")
            sendkeys(nom_last_namevalue, nom_last_name, nom_last_name_data)
            nom_dob = xpath("//input[@formcontrolname='nominee_dob']")
            nom_dob.click()
            nom_year = xpath(
                "//button[@class='mat-focus-indicator mat-calendar-period-button mat-button mat-button-base']").click()
            nom_dobvalue = nom_dob.get_attribute("value")
            if (nom_dobvalue == ""):
                nom_year = xpath(
                    "//button[@class='mat-focus-indicator mat-calendar-period-button mat-button mat-button-base']")
                nom_year.click()
                picker("1994")
                picker("OCT")
                picker("13")
                add_drop_down("FATHR", nom_rel)
            nom_add_same=xpath('//input[@formcontrolname="nominee_applicant_address_same"]')
            nom_add_samevalue=nom_add_same.get_attribute('checked')
            if nom_add_samevalue!='true':
                nom_ad1 = xpath("//input[@formcontrolname='nominee_address_1']")
                nom_ad1value = nom_ad1.get_attribute("value")
                sendkeys(nom_ad1value, nom_ad1, nom_ad1_data)
                nom_ad2 = xpath("//input[@formcontrolname='nominee_address_2']")
                nom_ad2value = nom_ad2.get_attribute("value")
                sendkeys(nom_ad2value, nom_ad2, nom_ad2_data)
                nom_pincode = xpath("//input[@formcontrolname='nominee_address_pincode']")
                nom_pincodevalue = nom_pincode.get_attribute("value")
                sendkeys(nom_pincodevalue, nom_pincode, nom_pincode_data)
                Click(nom_pincode)
                nom_pincode.send_keys(Keys.ARROW_DOWN)
                nom_pincode.send_keys(Keys.ENTER)
        continue2 = xpath("//button[@class='button button--yellow button--small']")
        continue2.click()
def paymentfailure():
    if driver.current_url == "https://sitsfl.stfc.in/recurring-deposit-online/payment-status":
        if xpath('//button[@class="button button--black button--small mb-md-15"]'):
            xpath('//button[@class="button button--black button--small mb-md-15"]').click()
            panscreen()
            addressinfo()
            bankscreen()
            addressinfo()
            congratulations()
def congratulations():
    if driver.current_url == "https://sitsfl.stfc.in/recurring-deposit-online/rd-confirmation":
        print("Lead created successfully")

dataSheet = pd.read_excel(r'InputFiles\rd_data.xlsx')
for ind in dataSheet.index:
    c = webdriver.ChromeOptions()
    c.add_argument("--incognito")
    driver = webdriver.Chrome(options=c)
    driver.get("https://sitsfl.stfc.in")
    driver.maximize_window()
    try:
        if ele('modal-close-btn').is_displayed():
            ele('modal-close-btn').click()
    except:
        print("popup not available")
    element_hover = xpath("//div[@class='head-link'][1]")
    ActionChains(driver).move_to_element(element_hover).perform()
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
    rd = ele('main_nav_rd')
    rd.click()
    mobile = ele('cus_mobile')
    pincode = ele('cus_pincode')
    amount = ele('cus_investment_amount')
    invest_now = ele('pf-apply-btn')
    mobile_data = dataSheet['Mobile_Number'][ind]
    mobile.send_keys(str(mobile_data))
    pin_data = dataSheet['Pincode'][ind]
    pincode.send_keys(str(pin_data))
    amount_data = dataSheet['Amount'][ind]
    amount.send_keys(str(amount_data))
    invest_now.click()
    otp1 = ele('otpCode1')
    otp2 = ele('otpCode2')
    otp3 = ele('otpCode3')
    otp4 = ele('otpCode4')
    otp5 = ele('otpCode5')
    otp6 = ele('otpCode6')
    otp_verify = ele('otpVerifybtn')
    otp1.send_keys(str(otp1_data))
    otp2.send_keys(str(otp2_data))
    otp3.send_keys(str(otp3_data))
    otp4.send_keys(str(otp4_data))
    otp5.send_keys(str(otp5_data))
    otp6.send_keys(str(otp6_data))
    otp_verify.click()
    time.sleep(10)
    panscreen()
    time.sleep(15)
    addressinfo()
    time.sleep(5)
    bankscreen()
    time.sleep(5)
    additionaldetails()
    time.sleep(15)
    paymentfailure()
    congratulations()
    break











