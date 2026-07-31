from cloud_parser import cloud

popsmoke = cloud()

Dicy = {}
ID = {}

for things in popsmoke:
   name = things["userName"]
   ip =  things["sourceIPAddress"]
   status = things["status"]
   
   if "Failed" in status:
       
       ID[ip] = name
       if ip in Dicy:
         Dicy[ip]+=1
       else:
         Dicy[ip] =1


print()       
print()
print('Failed_Ips')
print("☆" * 35)
for ip, failures in Dicy.items():
     print(f'Ip         : {ip}')
     print(f'User       : {ID[ip]}')
     print(f'Status     : {status}')
     print()
     
     print('-' * 35)

