# Amazon Test
1. System Requirement  
Python must be installed  
'pip' must be installed  
Chrome browser must be installed
allure-report should be installed. Follow this link for instruction https://docs.qameta.io/allure/#_installing_a_commandline  
  
  
2. Install Required Libraries  
From project root folder run command [pip install -r requirements.txt]   

3. Running Test  
a. Run by Behave runner  
From project root folder run command [behave]  
b. Run by Allure-Behave runner  
From project root folder run command [behave -f allure_behave.formatter:AllureFormatter -o allure-result -D browser=chrome]    

4. Viewing Report  
a. Behave test report is generated as [behave-report.json] when the test completes.  
b. Run [allure serve allure-result] to view Allure report  
c. Screen capture for run test(open the link by browser has flash installed) https://screencast.com/t/EdBoYght9