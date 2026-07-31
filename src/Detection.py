import json
from pydroid1 import woo

def show_suspicious():

    Variable = woo()
    # A Dictionary meant for storing logs with Failed login_attmpts 
    failed_attempts = {}
    report_data = []
    for event in Variable:
        status = event["Status"]
        #Counts the number of failed login_attempts 
        if "FAILED" in status:
            ip = event["Ip"]

            if ip in failed_attempts:
                failed_attempts[ip]+=1
            else:
                failed_attempts[ip]=1
                
                #JSON report built 
            for ip, failures in failed_attempts.items():
                     if failures >= 3:
                        severity = "High"
                        threat = "Possible Brute Force        Attack"
                     else:
                       severity = "Low"
                       threat = "Negligible"
                     report = { "Ip": ip,
                                       "Failed_Attempts": failures,
                                            "Severity": severity,
                                            "Threat": threat}
                              
                     report_data.append(report)   
    
                    
                                 
                       #opens a new file named Json                                       
                     with open("../reports/threat_report.json", "w") as file:
                      json.dump(report_data, file, indent=4)  
                     
    #Program Menu  
    while True:
    #  try:
          print()
          print()
          print("======= ThreatWatch =========")
          print("1.Show Risk Level ")
          print("2.Show Threat Report ")
          print("3. Exit")

          choice = int (input("Enter a Number: "))

          if choice ==3:
                 break
         #Speccifically Displays the Ip addresses and thier level of impacts if any
          if choice == 1:
            for ip, failures in failed_attempts.items():
                if failures >=3:
                   print("=" * 40 + "\n")
                   print(" THREAT DETECTED!\n")
                   print(f"Ip_Address  : {ip}\n")
                   print(f"Failed Attempts : {failures}\n")
                   print(f"Severity      : High\n")
                   print("Threat          : Possible Brute Force Attack\n")
                             
                   print("=" * 40+"\n")
                          
                elif failures < 3:
                     print("=" * 40 +"\n")
                     print(" SUSPICIOUS\n")
                     print(f"IP Address      : {ip}\n")
                     print(f"Failed Attempts      :{failures}\n")
                     print("Threat  :Negligeble\n")
                     print("=" * 40 + "\n")
                                 
          elif choice == 2:
                   critical = 0
                   high = 0
                   low = 0
                   for ip, failures in failed_attempts.items():        
                                
                            if failures>= 6:
                               critical+=1
                            elif failures==3:
                                high+=1
                            else:
                                 low+=1
                  #Prints the level of Risks being conveyed 
                   print("=======Threat-Watch-Alert-Report========\n")          
                 
                        
                   print(f"Suspicious Ip           : {low}\n")
                   print(f"Medium Threats      : {high}\n")
                   print(f"High Threats            : {critical}\n")
        
     # except:
           #print("Pls enter a valid number")
   
             
             
                             
                                                              
                     
                    
                  
                   
          
         
        
            

show_suspicious()
            
            
        
        
