from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from time import sleep


class Drogba:
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    username = 'Admin'
    password = 'admin123'
    search1 = 'Admin'
    username_locator = "username"  # Name
    password_locator = 'password'  # Name
    FirstName = 'Carlos'
    MiddleName = 'Smith'
    LastName = 'Junior'
    EmployeeId = '45678'
    submitButton_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    Search_locator = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div'
    Search1_locator = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input'
    Admin_locator = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'
    Userrole_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div'
    Admin1_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'
    Admin2_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/span'
    ESS_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[3]/span'
    Status1_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[2]/span'
    Status2_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[3]/span'
    Status_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]'
    Pim_locator = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    PimAdd_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    create_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span'
    FirstName_locator = 'firstName'
    MiddleName_locator = 'middleName'
    LastName_locator = 'lastName'
    Nickname_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input'
    OtherId_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input'
    LicenseNumber_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
    SSNNumber_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input'
    SINNumber_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input'
    MilitaryService_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input'
    License_ExpiryDate_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'
    Nationality_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div'
    Nationality1_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]'
    MaritalStatus_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div'
    MaritalStatus1_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]'
    Dob_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'
    Smoke_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[2]/div/div[2]/div/label/span/i'
    PimSaveButton_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'
    PimSaveButton1_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button'
    Gender_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
    BloodGroup_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div/div[1]'
    BloodGroup1_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div/div[1]'
    EmployeeId_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input'
    SaveButton_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
    LoginUsername_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
    LoignPassword_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
    ConfirmPassword_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'
    Street1_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    street2_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
    City_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input'
    state_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input'
    Pincode_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input'
    Country_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div'
    Country1_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[1]'
    Home_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input'
    Mobile_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input'
    Work_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
    Email_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input'
    OtherMail_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/input'
    ContactSaveButton_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button'
    EmergencyContact_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/a'
    EmergencyAdd_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
    EmergencyName_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    Relationship_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
    EmergencyHome_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input'
    EmergencyMobile_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input'
    EmergencyWork_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
    EmergencySaveButton_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]'
    Dependents_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/a'
    DependentsAdd_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
    DependentsName_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    DependentsDOB_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div/div/div[2]/div/div/input'
    DependentsRelationship_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div'
    DependentsRelationship1_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/span'
    DependentsSave_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]'
    Immigration_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[5]/a'
    ImmigrationAdd_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
    ImmigrationNumber_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input'
    IsuueDate_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div/input'
    ExpiryDate_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/div/div/input'
    EliglibilityStatus_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/input'
    IssuedBy_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div'
    IssuedBy1_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div[2]/div[100]/span'
    ReviewDate_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[6]/div/div[2]/div/div/input'
    Comments_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[7]/div/div[2]/textarea'
    ImmigrationSaveButton_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]'
    Job_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a'
    JoinedDate_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
    Jobtitle = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div'
    Jobtitle1_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/span'
    JobCategory_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div'
    JobCategory1_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[3]/span'
    SubUnit_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div'
    SubUnit1_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div[2]/div[3]/span'
    Location_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[1]'
    Location1_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div[2]/div[3]/span'
    EmploymentStatus_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div'
    EmploymentStatus1_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div[2]/div[2]/span'
    EmploymentSwitch_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/label/span'
    EmploymentSaveButton_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button'
    Jobspecification_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/div'
    Salary_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[7]/a'
    salaryAdd_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[5]/div[1]/div/button'
    Tax_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[8]/a'
    Salaryamount_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input'
    PayGrade_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div'
    PayGrade1_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/span'
    PayFrequency_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/div/div'
    PayFrequency1_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[3]/span'
    Currency_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div'
    Currency1_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[63]/span'
    SalaryComment_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div/div/div[2]/textarea'
    SalarySwitch_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/label/span'
    SalarySaveButton_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button[2]'
    TaxExemption_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
    TaxStatus_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div'
    TaxStatus1_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]/span'
    TaxState_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div'
    TaxState1_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div[25]/span'
    StateStatus_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div'
    StateStatus1_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div[4]/span'
    StateExemption_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
    Umemployment_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/div/div'
    Umemployment1_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/div/div[2]/div[25]/span'
    Workstate_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div'
    Workstate1_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div[2]/div[25]/span'
    TaxSaveButton_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button'
    Report_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[9]/a'
    ReportAdd_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div/button'
    ReportName_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
    ReportingMethod_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div'
    ReportingMethod1_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/span'
    ReportSaveButton_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[2]/button[2]'
    Qualification_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[10]/a'
    QualificationAdd_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div/button'
    Company_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    QualificationTitle_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
    FromDate_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div/input'
    ToDate_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div/input'
    QualificationSaveButton_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[4]/button[2]'
    Membership_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[11]/a'
    MembershipAdd_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
    MembershipDetails_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div'
    MembershipDetails1_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[3]/span'
    Subscription_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div'
    Subscription1_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/span'
    SubscriptionAmount_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input'
    SubscriptionCurrency_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div'
    SubscriptionCurrency1_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[63]/span'
    CommenceDate_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div/input'
    RenewalDate_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/input'
    MembershipSaveButton_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/button[2]'
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    # Method for login

    def Browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

# Method for login

    def login(self):
        sleep(5)
        self.driver.find_element(
            by=By.NAME, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(
            by=By.NAME, value=self.password_locator).send_keys(self.password)
        self.driver.find_element(
            by=By.XPATH, value=self.submitButton_locator).click()
    print("Invalid Username or Password")

    def search(self):
        sleep(5)

        self.driver.find_element(
            by=By.XPATH, value=self.Search_locator).click()

    def search1(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.Search1_locator).send_keys("admin")

    def PIM(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.Search1_locator).send_keys("Pim")

    def Leave(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.Search1_locator).send_keys("Leave")

    def Time(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.Search1_locator).send_keys("time")

    def Recruitment(self):
        sleep(6)
        self.driver.find_element(
            by=By.XPATH, value=self.Search1_locator).send_keys("recruitment")

    def My_Info(self):
        sleep(7)
        self.driver.find_element(
            by=By.XPATH, value=self.Search1_locator).send_keys("My_info")

    def performance(self):
        sleep(8)
        self.driver.find_element(
            by=By.XPATH, value=self.Search1_locator).send_keys("performance")

    def Dashboaard(self):
        sleep(9)
        self.driver.find_element(
            by=By.XPATH, value=self.Search1_locator).send_keys("dashboard")

    def Directory(self):
        sleep(10)
        self.driver.find_element(
            by=By.XPATH, value=self.Search1_locator).send_keys("directory")

    def Maintainence(self):
        sleep(11)
        self.driver.find_element(
            by=By.XPATH, value=self.Search1_locator).send_keys("maintainence")

    def Buzz(self):
        sleep(12)
        self.driver.find_element(
            by=By.XPATH, value=self.Search1_locator).send_keys("buzz")

    def Admin(self):
        sleep(13)
        self.driver.find_element(
            by=By.XPATH, value=self.Admin_locator).click()

    def UserRole(self):
        sleep(14)
        self.driver.find_element(
            by=By.XPATH, value=self.Userrole_locator).click()

    def UserRole1(self):
        sleep(15)
        self.driver.find_element(
            by=By.XPATH, value=self.Admin2_locator).click()

    def UserRole2(self):
        sleep(16)
        self.driver.find_element(
            by=By.XPATH, value=self.ESS_locator).click()

    def Status(self):
        sleep(17)
        self.driver.find_element(
            by=By.XPATH, value=self.Status_locator).click()

    def Status1(self):
        sleep(18)
        self.driver.find_element(
            by=By.XPATH, value=self.Status1_locator).click()

    def Status2(self):
        sleep(19)
        self.driver.find_element(
            by=By.XPATH, value=self.Status2_locator).click()

    def Pim(self):
        sleep(20)
        self.driver.find_element(
            by=By.XPATH, value=self.Pim_locator).click()

    def Pimadd(self):
        sleep(21)
        self.driver.find_element(
            by=By.XPATH, value=self.PimAdd_locator).click()

    def Pimadd1(self):
        sleep(22)
        self.driver.find_element(
            by=By.NAME, value=self.FirstName_locator).send_keys(self.FirstName)
        self.driver.find_element(
            by=By.NAME, value=self.MiddleName_locator).send_keys(self.MiddleName)
        self.driver.find_element(
            by=By.NAME, value=self.LastName_locator).send_keys(self.LastName)
        self.driver.find_element(
            by=By.XPATH, value=self.EmployeeId_locator).send_keys(self.EmployeeId)
        self.driver.find_element(
            by=By.XPATH, value=self.create_locator).click()
        self.driver.find_element(
            by=By.XPATH, value=self.LoginUsername_locator).send_keys('William38')
        self.driver.find_element(
            by=By.XPATH, value=self.LoignPassword_locator).send_keys('Paulcollin@8')
        self.driver.find_element(
            by=By.XPATH, value=self.ConfirmPassword_locator).send_keys('Paulcollin@8')
        self.driver.find_element(
            by=By.XPATH, value=self.SaveButton_locator).click()

    def PimAdd2(self):
        sleep(23)
        self.driver.find_element(
            by=By.XPATH, value=self.OtherId_locator).send_keys('3475869')
        self.driver.find_element(
            by=By.XPATH, value=self.Nickname_locator).send_keys('Golden')
        self.driver.find_element(
            by=By.XPATH, value=self.SSNNumber_locator).send_keys('5789765')
        self.driver.find_element(
            by=By.XPATH, value=self.License_ExpiryDate_locator).send_keys('23-10-2022')
        self.driver.find_element(
            by=By.XPATH, value=self.LicenseNumber_locator).send_keys('4578909')
        self.driver.find_element(
            by=By.XPATH, value=self.SINNumber_locator).send_keys('4590089689')
        self.driver.find_element(
            by=By.XPATH, value=self.Nationality_locator).click()
        self.driver.find_element(
            by=By.XPATH, value=self.Nationality1_locator).click()
        self.driver.find_element(
            by=By.XPATH, value=self.MaritalStatus_locator).click
        self.driver.find_element(
            by=By.XPATH, value=self.MaritalStatus1_locator).click()
        self.driver.find_element(
            by=By.XPATH, value=self.Dob_locator).send_keys('23-10-1990')
        self.driver.find_element(
            by=By.XPATH, value=self.MilitaryService_locator).send_keys('No')
        self.driver.find_element(
            by=By.XPATH, value=self.Smoke_locator).click()
        self.driver.find_element(
            by=By.XPATH, value=self.BloodGroup_locator).click()
        self.driver.find_element(
            by=By.XPATH, value=self.BloodGroup1_locator).click()
        self.driver.find_element(
            by=By.XPATH, value=self.PimSaveButton_locator).click()
        self.driver.find_element(
            by=By.XPATH, value=self.PimSaveButton1_locator).click()

    def Con(self):
        sleep(24)
        self.driver.find_element(
            by=By.XPATH, value='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a').click()

    def Contact(self):
        sleep(10)
        self.driver.find_element(
            by=By.XPATH, value=self.Street1_locator).send_keys('First')
        self.driver.find_element(
            by=By.XPATH, value=self.street2_locator).send_keys('North amsterdan')
        self.driver.find_element(
            by=By.XPATH, value=self.state_locator).send_keys('Berlin')
        self.driver.find_element(
            by=By.XPATH, value=self.City_locator).send_keys('Serien')
        self.driver.find_element(
            by=By.XPATH, value=self.Pincode_locator).send_keys('220508')

        self.driver.find_element(
            by=By.XPATH, value=self.Home_locator).send_keys('456788998987')
        self.driver.find_element(
            by=By.XPATH, value=self.Mobile_locator).send_keys('21089759599')
        self.driver.find_element(
            by=By.XPATH, value=self.Work_locator).send_keys('21058090999')
        self.driver.find_element(
            by=By.XPATH, value=self.Email_locator).send_keys('Villers@100gamil.com')
        self.driver.find_element(
            by=By.XPATH, value=self.OtherMail_locator).send_keys('Villers@011gmail.com')

    def ContactSave(self):
        sleep(10)
        self.driver.find_element(
            by=By.XPATH, value=self.Country_locator).click()

    def ContactSave1(self):
        sleep(10)
        self.driver.find_element(
            by=By.XPATH, value=self.Country1_locator).click()
        self.driver.find_element(
            by=By.XPATH, value=self.ContactSaveButton_locator).click()

    def Emergency(self):
        sleep(10)
        self.driver.find_element(
            by=By.XPATH, value=self.EmergencyContact_locator).click()

    def Emergency1(self):
        sleep(10)
        self.driver.find_element(
            by=By.XPATH, value=self.EmergencyAdd_locator).click()

    def Emergency2(self):
        sleep(10)
        self.driver.find_element(
            by=By.XPATH, value=self.EmergencyName_locator).send_keys('Batista')
        self.driver.find_element(
            by=By.XPATH, value=self.Relationship_locator).send_keys('Father')
        self.driver.find_element(
            by=By.XPATH, value=self.EmergencyHome_locator).send_keys('234576890')
        self.driver.find_element(
            by=By.XPATH, value=self.EmergencyMobile_locator).send_keys('456789303')
        self.driver.find_element(
            by=By.XPATH, value=self.EmergencyWork_locator).send_keys('9085783783')
        self.driver.find_element(
            by=By.XPATH, value=self.EmergencySaveButton_locator).click()

    def Dependents(self):
        sleep(10)
        self.driver.find_element(
            by=By.XPATH, value=self.Dependents_locator).click()

    def Dependents1(self):
        sleep(10)
        self.driver.find_element(
            by=By.XPATH, value=self.DependentsAdd_locator).click()

    def Dependents2(self):
        sleep(10)
        self.driver.find_element(
            by=By.XPATH, value=self.DependentsName_locator).send_keys('Archer')
        self.driver.find_element(
            by=By.XPATH, value=self.DependentsDOB_locator).send_keys('2012-01-02')

    def Dependents3(self):
        sleep(10)
        self.driver.find_element(
            by=By.XPATH, value=self.DependentsRelationship_locator).click()

    def Dependents4(self):
        sleep(10)
        self.driver.find_element(
            by=By.XPATH, value=self.DependentsRelationship1_locator).click()
        self.driver.find_element(
            by=By.XPATH, value=self.DependentsSave_locator).click()

    def Immigration(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.Immigration_locator).click()

    def Immigration1(self):
        sleep(10)
        self.driver.find_element(
            by=By.XPATH, value=self.ImmigrationAdd_locator).click()

    def Immigration2(self):
        sleep(10)
        self.driver.find_element(
            by=By.XPATH, value=self.ImmigrationNumber_locator).send_keys('78664679446')
        self.driver.find_element(
            by=By.XPATH, value=self.IsuueDate_locator).send_keys('2015-01-02')
        self.driver.find_element(
            by=By.XPATH, value=self.ExpiryDate_locator).send_keys('2031-01-02')
        self.driver.find_element(
            by=By.XPATH, value=self.EliglibilityStatus_locator).send_keys('Yes')
        self.driver.find_element(
            by=By.XPATH, value=self.ReviewDate_locator).send_keys('2018-01-02')
        self.driver.find_element(
            by=By.XPATH, value=self.Comments_locator).send_keys('Simply waste')

    def Immigration3(self):
        sleep(10)
        self.driver.find_element(
            by=By.XPATH, value=self.IssuedBy_locator).click()

    def Immigration4(self):
        sleep(10)
        self.driver.find_element(
            by=By.XPATH, value=self.IssuedBy1_locator).click()
        self.driver.find_element(
            by=By.XPATH, value=self.ImmigrationSaveButton_locator).click()

    def Job(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a').click()

    def Job1(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.JoinedDate_locator).send_keys('2012-01-03')
        self.driver.find_element(
            by=By.XPATH, value=self.Jobspecification_locator).click()

    def jobtitle(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.Jobtitle).click()

    def jobtitle1(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/span').click()

    def jobcategory(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.JobCategory_locator).click()

    def jobcategory1(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.JobCategory1_locator).click()

    def Subunit(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.SubUnit_locator).click()

    def Subunit1(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.SubUnit1_locator).click()

    def Location(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.Location_locator).click()

    def Location1(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.Location1_locator).click()

    def Employmentstatus(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.EmploymentStatus_locator).click()

    def Employmentstatus1(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.EmploymentStatus1_locator).click()
        self.driver.find_element(
            by=By.XPATH, value=self.EmploymentSwitch_locator).click()
        self.driver.find_element(
            by=By.XPATH, value=self.EmploymentSaveButton_locator).click()

    def Salary(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.Salary_locator).click()

    def SalaryAdd(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.salaryAdd_locator).click()

    def Salary1(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.Salaryamount_locator).click()
        self.driver.find_element(
            by=By.XPATH, value='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input').click()
        self.driver.find_element(
            by=By.XPATH, value=self.SalaryComment_locator).send_keys('Simply waste')
        self.driver.find_element(
            by=By.XPATH, value=self.SalarySwitch_locator).click()

    def Paygrade(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.PayGrade_locator).click()

    def Paygrade1(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.PayGrade1_locator).click()

    def Payfrequency(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.PayFrequency_locator).click()

    def Payfrequency1(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.PayFrequency1_locator).click()

    def Currency(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.Currency_locator).click()

    def Currency1(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.Currency1_locator).click()
        self.driver.find_element(
            by=By.XPATH, value=self.SalarySwitch_locator).click()
        self.driver.find_element(
            by=By.XPATH, value=self.SalarySaveButton_locator).click()

    def Tax(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.Tax_locator).click()

    def TaxAdd(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.TaxExemption_locator).click()
        self.driver.find_element(
            by=By.XPATH, value=self.TaxStatus_locator).click()

    def Taxstatus(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.TaxStatus1_locator).click()

    def Taxstate(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.TaxState_locator).click()

    def Taxstate1(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.TaxState1_locator).click()

    def Statestatus(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.StateStatus_locator).click()

    def statestatus1(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.StateStatus1_locator).click()

    def Umemployment(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.Umemployment_locator).click()

    def Unemployment1(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.Umemployment1_locator).click()

    def Workstate(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.Workstate_locator).click()

    def Workstate1(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.Workstate1_locator).click()
        self.driver.find_element(
            by=By.XPATH, value=self.TaxSaveButton_locator).click()

    def Report(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.Report_locator).click()

    def ReportAdd(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.ReportAdd_locator).click()

    def Report1(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.ReportName_locator).click()
        self.driver.find_element(
            by=By.XPATH, value=self.ReportingMethod_locator).click()

    def Report2(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.ReportingMethod1_locator).click()
        self.driver.find_element(
            by=By.XPATH, value=self.ReportSaveButton_locator).click()

    def Qualification(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.Qualification_locator).click()

    def QualificationAdd(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.QualificationAdd_locator).click()

    def Qualification1(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.Company_locator).click()
        self.driver.find_element(
            by=By.XPATH, value=self.QualificationTitle_locator).click()
        self.driver.find_element(
            by=By.XPATH, value=self.FromDate_locator).send_keys('2012-08-05')
        self.driver.find_element(
            by=By.XPATH, value=self.ToDate_locator).send_keys('2002-04-08')
        self.driver.find_element(
            by=By.XPATH, value=self.QualificationSaveButton_locator).click()

    def Membership(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.Membership_locator).click()

    def MembershipAdd(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.MembershipAdd_locator).click()

    def Membership1(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.SubscriptionAmount_locator).click()
        self.driver.find_element(
            by=By.XPATH, value=self.MembershipDetails_locator).click()

    def Membership2(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.MembershipDetails1_locator).click()
        self.driver.find_element(
            by=By.XPATH, value=self.Subscription_locator).click()

    def Membership3(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.Subscription1_locator).click()
        self.driver.find_element(
            by=By.XPATH, value=self.SubscriptionCurrency_locator).click()

    def Membership4(self):
        sleep(5)
        self.driver.find_element(
            by=By.XPATH, value=self.SubscriptionCurrency1_locator).click()
        self.driver.find_element(
            by=By.XPATH, value=self.CommenceDate_locator).send_keys('2023-10-05')
        self.driver.find_element(
            by=By.XPATH, value=self.RenewalDate_locator).send_keys('2030-10-05')
        self.driver.find_element(
            by=By.XPATH, value=self.MembershipSaveButton_locator).click()


Drogba().Browsing()


Drogba().login()

# Drogba().search()

# Drogba().search1()

# Drogba().Leave()

# Drogba().Maintainence()

# Drogba().Dashboaard()

# Drogba().Directory()

# Drogba().performance()

# Drogba().My_Info()

# Drogba().Recruitment()

# Drogba().PIM()

# Drogba().performance()

# Drogba().Time()

# Drogba().Admin()

Drogba().UserRole()

Drogba().UserRole1()

Drogba().UserRole2()

Drogba().Status()

Drogba().Status1()

Drogba().Status2()

Drogba().Pim()

Drogba().Pimadd()

Drogba().Pimadd1()

Drogba().PimAdd2()

Drogba().Con()

Drogba().Contact()

Drogba().ContactSave()

Drogba().ContactSave1()

Drogba().Emergency()

Drogba().Emergency1()

Drogba().Emergency2()

Drogba().Dependents()

Drogba().Dependents1()

Drogba().Dependents2()

Drogba().Dependents3()

Drogba().Dependents4()

Drogba().Immigration()

Drogba().Immigration1()

Drogba().Immigration2()

Drogba().Immigration3()

Drogba().Immigration4()

Drogba().Job()

Drogba().Job1()

Drogba().jobtitle()

Drogba().jobtitle1()

Drogba().jobcategory()

Drogba().jobcategory1()

Drogba().Subunit()

Drogba().Subunit1()

Drogba().Location()

Drogba().Location1()

Drogba().Employmentstatus()

Drogba().Employmentstatus1()

Drogba().Salary()

Drogba().SalaryAdd()

Drogba().Salary1()

Drogba().Paygrade()

Drogba().Paygrade1()

Drogba().Payfrequency()

Drogba().Payfrequency1()

Drogba().Currency()

Drogba().Currency1()

Drogba().Tax()

Drogba().TaxAdd()

Drogba().Taxstatus()

Drogba().Taxstate()

Drogba().Taxstate1()

Drogba().Statestatus()

Drogba().statestatus1()

Drogba().Umemployment()

Drogba().Unemployment1()

Drogba().Workstate()

Drogba().Workstate1()

Drogba().Report()

Drogba().ReportAdd()

Drogba().Report1()

Drogba().Report2()

Drogba().Qualification()

Drogba().QualificationAdd()

Drogba().Qualification1()

Drogba().Membership()

Drogba().MembershipAdd()

Drogba().Membership1()

Drogba().Membership2()

Drogba().Membership3()

Drogba().Membership4()
