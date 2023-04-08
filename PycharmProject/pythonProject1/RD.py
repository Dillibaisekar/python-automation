import os.path
import time
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import RD_xpath

def panscreen():
    if driver.current_url == 'https://sitsfl.stfc.in/recurring-deposit-online/personal-information':
        panvalue=RD_xpath.pan.get_attribute("value")
        RD_xpath.sendkeys(panvalue, RD_xpath.pan, pan_data)
        driver.execute_script("window.scrollTo(0, 800)")
        firstnamevalue=RD_xpath.firstname.get_attribute("value")
        RD_xpath.sendkeys(firstnamevalue, RD_xpath.firstname, firstname_data)
        lastnamevalue=RD_xpath.lastname.get_attribute("value")
        RD_xpath.sendkeys(lastnamevalue, RD_xpath.lastname, lastname_data)
        dobvalue = RD_xpath.dobclick.get_attribute("value")
        print("Selected DOB Value {}".format(dobvalue))
        if(dobvalue == ""):
            RD_xpath.dobclick.click()
            RD_xpath.year.click()
            RD_xpath.picker('2003')
            RD_xpath.picker('MAY')
            RD_xpath.picker('21')
        mailvalue=RD_xpath.mail.get_attribute("value")
        RD_xpath.sendkeys(mailvalue,RD_xpath.mail,mail_data)
        RD_xpath.invest_edit.click()
        RD_xpath.investamount2.clear()
        RD_xpath.tenure36.click()
        RD_xpath.tenure48.click()
        RD_xpath.tenure12.click()
        RD_xpath.tenure24.click()
        RD_xpath.tenure60.click()
        RD_xpath.continue1.click()
        RD_xpath.error_msg()

def razorpay():
    RD_xpath.payment_num.send_keys('9791399767')
    RD_xpath.ele('redesign-v15-cta').click()
    RD_xpath.netbanking.click()
    RD_xpath.bank.click()
    RD_xpath.make_payment.click()
    RD_xpath.sucess_click.click()

def airpay():
    RD_xpath.netbanking_air.click()
    RD_xpath.bankname_air.click()
    RD_xpath.button_air.click()

def addressinfo():
    if driver.current_url == "https://sitsfl.stfc.in/recurring-deposit-online/address-information":
        RD_xpath.doc_type.click()
        RD_xpath.doc_proof_dropdown('RDAID')
        doc_numvalue=RD_xpath.doc_num.get_attribute("value")
        RD_xpath.sendkeys(doc_numvalue,RD_xpath.doc_num,doc_num_data)
        frontpath=os.path.abspath(proof_front_data)
        RD_xpath.proof_front.send_keys(frontpath)
        backpath=os.path.abspath(proof_back_data)
        RD_xpath.proof_back.send_keys(str(backpath))
        RD_xpath.continue2.click()
        address1value=RD_xpath.address1.get_attribute("value")
        RD_xpath.sendkeys(address1value,RD_xpath.address1,address1_data)
        address2value=RD_xpath.address2.get_attribute("value")
        RD_xpath.sendkeys(address2value,RD_xpath.address2,address2_data)
        depositor_pincodevalue=RD_xpath.depositor_pincode.get_attribute("value")
        RD_xpath.sendkeys(depositor_pincodevalue,RD_xpath.depositor_pincode,pincode_data)
        RD_xpath.depositor_pincode.click()
        RD_xpath.depositor_pincode.send_keys(Keys.ARROW_DOWN)
        RD_xpath.depositor_pincode.send_keys(Keys.ENTER)
        uploadpath=os.path.abspath((photo_upload_data))
        RD_xpath.upload_photo.send_keys(str(uploadpath))
        RD_xpath.continue2.click()
        RD_xpath.error_msg()

def bankscreen():
    if driver.current_url == "https://sitsfl.stfc.in/recurring-deposit-online/bank-information":
        driver.execute_script("window.scrollTo(0,200)")
        account_numbervalue=RD_xpath.account_number.get_attribute("value")
        RD_xpath.sendkeys(account_numbervalue,RD_xpath.account_number,acc_num_data)
        confirm_account_numbervalue = RD_xpath.confirm_account_number.get_attribute("value")
        RD_xpath.sendkeys(confirm_account_numbervalue, RD_xpath.confirm_account_number, con_acc_num_data)
        ifscvalue=RD_xpath.ifsc.get_attribute("value")
        RD_xpath.sendkeys(ifscvalue,RD_xpath.ifsc,ifsc_data)
        RD_xpath.ifsc.click()
        acc_namevalue=RD_xpath.acc_name.get_attribute("value")
        RD_xpath.sendkeys(acc_namevalue,RD_xpath.acc_name,acc_name_data)
        RD_xpath.acc_type.click()
        RD_xpath.account_type('RDSA')
        chequepath=os.path.abspath(cheque_upload_data)
        RD_xpath.cheque_upload.send_keys(str(chequepath))
        RD_xpath.continue2.click()

def additionaldetails():
    if driver.current_url == "https://sitsfl.stfc.in/recurring-deposit-online/additional-details":
        RD_xpath.mat_ins("RDCFD")
        RD_xpath.add_drop_down("PROFL", RD_xpath.occupation)
        father_namevalue=RD_xpath.father_name.get_attribute("value")
        RD_xpath.sendkeys(father_namevalue,RD_xpath.father_name,fathername_data)
        marital_statusvalue=RD_xpath.marital_status.get_attribute('disabled')
        if (marital_statusvalue!='true' or marital_statusvalue==''):
            RD_xpath.add_drop_down("RDUNM", RD_xpath.marital_status)
        RD_xpath.add_drop_down("36", RD_xpath.fd_tenure)
        RD_xpath.add_drop_down("QTR", RD_xpath.fd_payout)
        nomvalue=RD_xpath.nom.get_attribute("checked")
        if nomvalue=='true':
            RD_xpath.nom_rel.click()
            RD_xpath.add_drop_down("FATHR", RD_xpath.nom_rel)
            nom_fir_namevalue = RD_xpath.nom_fir_name.get_attribute("value")
            RD_xpath.sendkeys(nom_fir_namevalue, RD_xpath.nom_fir_name, nom_first_name_data)
            nom_last_namevalue = RD_xpath.nom_last_name.get_attribute("value")
            RD_xpath.sendkeys(nom_last_namevalue, RD_xpath.nom_last_name, nom_last_name_data)
            RD_xpath.nom_dob.click()
            RD_xpath.year.click()
            nom_dobvalue = RD_xpath.nom_dob.get_attribute("value")
            if (nom_dobvalue == ""):
                RD_xpath.year.click()
                RD_xpath.picker("1994")
                RD_xpath.picker("OCT")
                RD_xpath.picker("13")
                RD_xpath.add_drop_down("FATHR", RD_xpath.nom_rel)
            nom_add_samevalue=RD_xpath.nom_add_same.get_attribute('checked')
            if nom_add_samevalue!='true':
                nom_ad1value = RD_xpath.nom_ad1.get_attribute("value")
                RD_xpath.sendkeys(nom_ad1value, RD_xpath.nom_ad1, nom_ad1_data)
                nom_ad2value = RD_xpath.nom_ad2.get_attribute("value")
                RD_xpath.sendkeys(nom_ad2value, RD_xpath.nom_ad2, nom_ad2_data)
                nom_pincodevalue = RD_xpath.nom_pincode.get_attribute("value")
                RD_xpath.sendkeys(nom_pincodevalue, RD_xpath.nom_pincode, nom_pincode_data)
                RD_xpath.Click(RD_xpath.nom_pincode)
                RD_xpath.nom_pincode.send_keys(Keys.ARROW_DOWN)
                RD_xpath.nom_pincode.send_keys(Keys.ENTER)
        RD_xpath.continue2.click()
def paymentfailure():
    if driver.current_url == "https://sitsfl.stfc.in/recurring-deposit-online/payment-status":
        if RD_xpath.editscheme:
            RD_xpath.editscheme.click()
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
    driver.maximize_window()
    driver.get('https://sitsfl.stfc.in')
    if RD_xpath.popup.is_displayed():
            RD_xpath.popup.click()
    else:
        print("popup not available")
    element_hover = RD_xpath.hover
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
    RD_xpath.rd.click()
    mobile_data = dataSheet['Mobile_Number'][ind]
    RD_xpath.mobile.send_keys(str(mobile_data))
    pin_data = dataSheet['Pincode'][ind]
    RD_xpath.pincode.send_keys(str(pin_data))
    amount_data = dataSheet['Amount'][ind]
    RD_xpath.amount.send_keys(str(amount_data))
    RD_xpath.invest_now.click()
    RD_xpath.otp1.send_keys(str(otp1_data))
    RD_xpath.otp2.send_keys(str(otp2_data))
    RD_xpath.otp3.send_keys(str(otp3_data))
    RD_xpath.otp4.send_keys(str(otp4_data))
    RD_xpath.otp5.send_keys(str(otp5_data))
    RD_xpath.otp6.send_keys(str(otp6_data))
    RD_xpath.otp_verify.click()
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











