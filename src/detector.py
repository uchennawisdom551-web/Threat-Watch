from parser import log_parser
def show():
         print('========Threat_Detection=======')
         result = log_parser("../logs/sample.log")
         print(result)
         failed_ips = {}
         for events in result: 
             ip = events["Ip"]
             if events['Status'] == 'FAILED':
               if ip not in failed_ips:
                  failed_ips[ip] = 1
               else:
                  failed_ips[ip] +=1
         
         for ip, failures in failed_ips.items():
           print(f"{ip} -> {failures} failures")

           if failures >= 3:
                     print("ALERT!")
     
                  
show()            
                     