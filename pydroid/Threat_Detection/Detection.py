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
                failed_attempts[ip] += 1
            else:
                failed_attempts[ip] = 1
                         
    for ip, failures in failed_attempts.items():
        
        if failures >= 3:
            
            print("=" * 40)
            print(" THREAT DETECTED!")
            print(f"IP Address      : {ip}")
            print(f"Failed Attempts : {failures}")
            print(f"Severity        : High ")
            print("Threat          : Possible Brute Force Attack")
            print("=" * 40)
        elif failures <= 3:
            print("=" * 40)
            print(" SUSPICIOUS")
            print(f"IP Address      : {ip}")
            print(f"Failed Attempts : {failures}")
            print("Threat          : Negligeble")
            print("=" * 40)
       
        if failures>= 4:
              critical+=1
              
        elif failures>=2:
              high+=1
        elif failures<2:
              low+=1
    print()       
    print("=======Threat-Watch-Alert-Report========")          
    print(f"Suspicious Ip      : {low}")
    print(f"Low Threats        : {high}")
    print(f"High Threats       : {critical}")
        
   
             
             
            
         
        
            

show_suspicious()
            
            
        
