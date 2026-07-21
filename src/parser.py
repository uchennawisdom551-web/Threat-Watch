def log_parser(file_path):
    print("==========Threat-Visuals=========")
    
    events  = []    
    with open(file_path, "r")as  file:
        
        event_now = 1
        for line in file:
            count = line.strip().split()
            event = {"Date": count[0],
            "time": count[1],
            "Ip": count[2],
            "Status": count[3] }
            events.append(event)
            print(f"\nEvent#:{event_now}")
            for key, count in event.items():
                 print(f'{key:<10}:{count}')
      
            print("-" * 35)
            event_now +=1
            
        return events
      
           
      
        
         
          
          
#log_parser('../logs/sample.log')


#how does Date variable  know  which line stripped is its own value 
#Why cant just returning event solve the whole issue why do we need a List variable.(events)

#and for the "for event in yup:"why doesnt it mark the events arcording to the Ip addresess disnticted.
