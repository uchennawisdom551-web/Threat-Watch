import json
def cloud():
   event = 0
   with open("cloudtrail.json", "r")as trail:
         Variable  =    json.load(trail)
         for value in Variable:
            event+=1
            print("☆" * 35)
            print(f'Event#{event}')
            print()
            print()
            for add, number in value.items():
              print(f'{add:<20} : {number}')
   return Variable
            
            
            
                     
                                       