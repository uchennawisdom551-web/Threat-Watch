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
    with open("../reports2/threat_report.txt", "w") as report:
                 
              for ip, failures in failed_attempts.items():
           
              
                   if failures >= 3:
                      print("=" * 40 + "\n")
                      report.write("=" * 40 + "\n")
                      report.write(" THREAT DETECTED!\n")
                      report.write(f"IP Address      : {ip}\n")
                      report.write(f"Failed Attempts : {failures}\n")
                      report.write(f"Severity        : High\n")
                      report.write("Threat          : Possible Brute Force Attack\n")
                      report.write("=" * 40+"\n")
                   elif failures <= 3:
                       report.write("=" * 40 +"\n")
                       report.write(" SUSPICIOUS\n")
                       report.write(f"IP Address      : {ip}\n")
                       report.write(f"Failed Attempts : {failures}\n")
                       report.write("Threat          : Negligeble\n")
                       report.write("=" * 40 + "\n")
       
                   if failures>= 6:
                        critical+=1
                   elif failures>=2:
                        high+=1
                   else:
                        low+=1
    
              report.write("=======Threat-Watch-Alert-Report========\n")          
              report.write(f"Suspicious Ip           : {low}\n")
              report.write(f"Medium Threats      : {high}\n")
              report.write(f"High Threats            : {critical}\n")
        
   
             
             
            
         
        
            

show_suspicious()
            
            
        
