from parser import log_parser
def show():
         result = log_parser("../logs/sample.log")
         failed_ips = {}
         print('========Detection-Report=======')                     
         for event in result: 
             ip = event["Ip"]
             if event['Status'] == 'FAILED':
               if ip not in failed_ips:
                  failed_ips[ip] = 1
               else:
                  failed_ips[ip] +=1
         for ip, failures in failed_ips.items():
                print("-" * 35)
                print(f"IP Address : {ip}")
                print(f"Failures   : {failures}")
         
                if failures >= 3:
                    print("Status     : ALERT!")
                else:
                   print("Status     : MODERATE")
                  
show()            
                     