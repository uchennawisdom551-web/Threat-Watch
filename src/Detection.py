from pydroid1 import woo

def show_suspicious():

    Variable = woo()
    failed_attempts = {}
    print()
    print()
    critical=0
    high = 0
    low = 0 
    for event in Variable:
        status = event["Status"]
 
        if "FAILED" in status:
            ip = event["Ip"]

            if ip in failed_attempts:
                failed_attempts[ip]+=1
            else:
                failed_attempts[ip]=1
    with open("../reports/threat_report.txt", "w") as report:
                 while True:
                  print()
                  print()
                  print("======= ThreatWatch =========")
                  print("1.Show Risk Level ")
                  print("2.Show Threat Report ")
                  print("3. Exit")

                  choice = int (input("Enter a Number: "))

                  if choice ==3:
                            break
                    
                  if choice == 1:
                   for ip, failures in failed_attempts.items():
                    if failures >=3:
                        print("=" * 40 + "\n")
                        print(" THREAT DETECTED!\n")
                        print(f"{critical:<10}      : {ip}\n")
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
       
                    
                  
                  if choice == 2:
                   for ip, failures in failed_attempts.items():
                    if failures>= 6:
                         critical+=1
                    elif failures==3:
                         high+=1
                    else:
                         low+=1
                   print("=======Threat-Watch-Alert-Report========\n")          
                   print(f"Suspicious Ip           : {low}\n")
                   print(f"Medium Threats      : {high}\n")
                   print(f"High Threats            : {critical}\n")
        
   
             
             
            
         
        
            

show_suspicious()
            
            
        
