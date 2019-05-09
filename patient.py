def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    count=0
    for i in patient_medical_speciality_list:
        if i==x:
            count=count+1 
            i=i+1
patient_medical_speciality_list=[ 102,'E',302,'P',305,'E',401,'O',656,'E',987,'O']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}

x=max(patient_medical_speciality_list,key=patient_medical_speciality_list.count)
if x=="P":
  print("Pediatrics")
elif x=="O":
  print("Orthopedics")
elif x=="E":                
  print("ENT")
else:    
    print("")
