

import csv
import random


factors_values=[{"Artistic_fact":0},
                {"Conventional_fact":0},
                {"Enterprising_fact":0},
                {"Social_fact":0},
                {"Investigative_fact":0},
                {"Realistic_fact":0}
               ]

Artistic_fact=0
Conventional_fact=0
Enterprising_fact=0
Investigative_fact=0
Realistic_fact=0
Social_fact=0

single_fact_que_file="singlefactor_que.csv"
multi_fact_que_file="ref_documents\\multifactor_que.csv"



single_fact_que_list=[]


current_quiz_questions=[]

current_quiz_e_ques=0
current_quiz_a_ques=0
current_quiz_i_ques=0
current_quiz_r_ques=0
current_quiz_c_ques=0
current_quiz_s_ques=0

suggestion=[]



with open(single_fact_que_file,'r') as singlefactquefile:
    reader = csv.DictReader(singlefactquefile)
    for row in reader:
        single_fact_que_list.append(row)
        
while(len(current_quiz_questions)<=30):
    
    que=random.choice(single_fact_que_list)
    que_primary_fact=que["Q_id"][-1]
    
    match que_primary_fact:
        case 'e':
            if(current_quiz_e_ques==5):
                pass
            else:
                if que in current_quiz_questions:
                    pass
                else:
                    current_quiz_questions.append(que)
                    current_quiz_e_ques=current_quiz_e_ques+1
                              
        case 'a':
            if(current_quiz_a_ques==5):
                pass
            else:
                if que in current_quiz_questions:
                    pass
                else:
                    current_quiz_questions.append(que)
                    current_quiz_a_ques=current_quiz_a_ques+1
                          
        case 'i':
            if(current_quiz_i_ques==5):
                pass
            else:
                if que in current_quiz_questions:
                    pass
                else:
                    current_quiz_questions.append(que)
                    current_quiz_i_ques=current_quiz_i_ques+1
                         
        case 'r':
            if(current_quiz_r_ques==5):
                pass
            else:
                if que in current_quiz_questions:
                    pass
                else:
                    current_quiz_questions.append(que)
                    current_quiz_r_ques=current_quiz_r_ques+1
                       
        case 'c':
            if(current_quiz_c_ques==5):
                pass
            else:
                if que in current_quiz_questions:
                    pass
                else:
                    current_quiz_questions.append(que)
                    current_quiz_c_ques=current_quiz_c_ques+1
                          
        case 's':
            if(current_quiz_s_ques==5):
                pass
            else:
                if que in current_quiz_questions:
                    pass
                else:
                    current_quiz_questions.append(que)
                    current_quiz_s_ques=current_quiz_s_ques+1
                    
           
            
    if(len(current_quiz_questions)==30):
        break
    
# for question in current_quiz_questions:
#     print(question) to see all the questions

roll=("Enter your roll no:")
    

print()
print()
for question in current_quiz_questions:
    print()
    print(question["Question"]+':')
    print()
    print()
    choice=int(input("Enter any number from (dislike)1-5(like) :"))
    print()
    
    match question["primaryfact"]:
        
        case 'a':
            
            match choice:
                
                case 5:
                    Artistic_fact+=5
                    Conventional_fact+=.10
                    Enterprising_fact+=.10
                    Investigative_fact+=.10
                    Realistic_fact+=.10
                    Social_fact+=.10
                case 4:
                    Artistic_fact+=2.5
                    Conventional_fact+=.10
                    Enterprising_fact+=.10
                    Investigative_fact+=.10
                    Realistic_fact+=.10
                    Social_fact+=.10
                case 3:
                    Artistic_fact+=0.5
                    Conventional_fact+=.10
                    Enterprising_fact+=.10
                    Investigative_fact+=.10
                    Realistic_fact+=.10
                    Social_fact+=.10
                case 2:
                    Artistic_fact+=0.10
                    Conventional_fact+=.10
                    Enterprising_fact+=.10
                    Investigative_fact+=.10
                    Realistic_fact+=.10
                    Social_fact+=.10
                case 1:    
                    Artistic_fact+=0
                    Conventional_fact+=.10
                    Enterprising_fact+=.10
                    Investigative_fact+=.10
                    Realistic_fact+=.10
                    Social_fact+=.10 

        case 'c':
            
            match choice:
                
                case 5:
                    Artistic_fact+=.10
                    Conventional_fact+=5
                    Enterprising_fact+=.10
                    Investigative_fact+=.10
                    Realistic_fact+=.10
                    Social_fact+=.10
                case 4:
                    Artistic_fact+=.10
                    Conventional_fact+=2.5
                    Enterprising_fact+=.10
                    Investigative_fact+=.10
                    Realistic_fact+=.10
                    Social_fact+=.10
                case 3:
                    Artistic_fact+=0.10
                    Conventional_fact+=.5
                    Enterprising_fact+=.10
                    Investigative_fact+=.10
                    Realistic_fact+=.10
                    Social_fact+=.10
                case 2:
                    Artistic_fact+=0.10
                    Conventional_fact+=.10
                    Enterprising_fact+=.10
                    Investigative_fact+=.10
                    Realistic_fact+=.10
                    Social_fact+=.10
                case 1:    
                    Artistic_fact+=0.10
                    Conventional_fact+=0
                    Enterprising_fact+=.10
                    Investigative_fact+=.10
                    Realistic_fact+=.10
                    Social_fact+=.10
                    
        case 'e':
            
            match choice:
                
                case 5:
                    Artistic_fact+=.10
                    Conventional_fact+=.10
                    Enterprising_fact+=5
                    Investigative_fact+=.10
                    Realistic_fact+=.10
                    Social_fact+=.10
                case 4:
                    Artistic_fact+=.10
                    Conventional_fact+=.10
                    Enterprising_fact+=2.5
                    Investigative_fact+=.10
                    Realistic_fact+=.10
                    Social_fact+=.10
                case 3:
                    Artistic_fact+=0.10
                    Conventional_fact+=.10
                    Enterprising_fact+=.5
                    Investigative_fact+=.10
                    Realistic_fact+=.10
                    Social_fact+=.10
                case 2:
                    Artistic_fact+=0.10
                    Conventional_fact+=.10
                    Enterprising_fact+=.10
                    Investigative_fact+=.10
                    Realistic_fact+=.10
                    Social_fact+=.10
                case 1:    
                    Artistic_fact+=0.10
                    Conventional_fact+=.10
                    Enterprising_fact+=0
                    Investigative_fact+=.10
                    Realistic_fact+=.10
                    Social_fact+=.10
    
        case 'i':
            
            match choice:
                
                case 5:
                    Artistic_fact+=.10
                    Conventional_fact+=.10
                    Enterprising_fact+=.10
                    Investigative_fact+=5
                    Realistic_fact+=.10
                    Social_fact+=.10
                case 4:
                    Artistic_fact+=.10
                    Conventional_fact+=.10
                    Enterprising_fact+=.10
                    Investigative_fact+=2.5
                    Realistic_fact+=.10
                    Social_fact+=.10
                case 3:
                    Artistic_fact+=0.10
                    Conventional_fact+=.10
                    Enterprising_fact+=.10
                    Investigative_fact+=.5
                    Realistic_fact+=.10
                    Social_fact+=.10
                case 2:
                    Artistic_fact+=0.10
                    Conventional_fact+=.10
                    Enterprising_fact+=.10
                    Investigative_fact+=.10
                    Realistic_fact+=.10
                    Social_fact+=.10
                case 1:    
                    Artistic_fact+=0.10
                    Conventional_fact+=.10
                    Enterprising_fact+=.10
                    Investigative_fact+=0
                    Realistic_fact+=.10
                    Social_fact+=.10
                    
        case 'r':
            
            match choice:
                
                case 5:
                    Artistic_fact+=.10
                    Conventional_fact+=.10
                    Enterprising_fact+=.10
                    Investigative_fact+=.10
                    Realistic_fact+=5
                    Social_fact+=.10
                case 4:
                    Artistic_fact+=.10
                    Conventional_fact+=.10
                    Enterprising_fact+=.10
                    Investigative_fact+=.10
                    Realistic_fact+=2.5
                    Social_fact+=.10
                case 3:
                    Artistic_fact+=0.10
                    Conventional_fact+=.10
                    Enterprising_fact+=.10
                    Investigative_fact+=.10
                    Realistic_fact+=.5
                    Social_fact+=.10
                case 2:
                    Artistic_fact+=0.10
                    Conventional_fact+=.10
                    Enterprising_fact+=.10
                    Investigative_fact+=.10
                    Realistic_fact+=.10
                    Social_fact+=.10
                case 1:    
                    Artistic_fact+=0.10
                    Conventional_fact+=.10
                    Enterprising_fact+=.10
                    Investigative_fact+=.10
                    Realistic_fact+=0
                    Social_fact+=.10
                    
        case 's':
            
            match choice:
                
                case 5:
                    Artistic_fact+=.10
                    Conventional_fact+=.10
                    Enterprising_fact+=.10
                    Investigative_fact+=.10
                    Realistic_fact+=.10
                    Social_fact+=5
                case 4:
                    Artistic_fact+=.10
                    Conventional_fact+=.10
                    Enterprising_fact+=.10
                    Investigative_fact+=.10
                    Realistic_fact+=.10
                    Social_fact+=2.5
                case 3:
                    Artistic_fact+=0.10
                    Conventional_fact+=.10
                    Enterprising_fact+=.10
                    Investigative_fact+=.10
                    Realistic_fact+=.10
                    Social_fact+=.5
                case 2:
                    Artistic_fact+=0.10
                    Conventional_fact+=.10
                    Enterprising_fact+=.10
                    Investigative_fact+=.10
                    Realistic_fact+=.10
                    Social_fact+=.10
                case 1:    
                    Artistic_fact+=0.10
                    Conventional_fact+=.10
                    Enterprising_fact+=.10
                    Investigative_fact+=.10
                    Realistic_fact+=.10
                    Social_fact+=0
   
   
   
print()
print()
print()
                 

factors_values[0]["Artistic_fact"]=Artistic_fact

factors_values[1]["Conventional_fact"]=Conventional_fact

factors_values[2]["Enterprising_fact"]=Enterprising_fact

factors_values[3]["Social_fact"]=Social_fact

factors_values[4]["Investigative_fact"]=Investigative_fact

factors_values[5]["Realistic_fact"]=Realistic_fact





for i in range(6):
    for j in range(6):
        if(list(factors_values[i].values())[0]>=list(factors_values[j].values())[0]):
            temp=factors_values[i]
            factors_values[i]=factors_values[j]
            factors_values[j]=temp
            


threelettercode=[]
joblist=[]

suggested_job=[]

threelettercode.append((str(list(factors_values[0].keys())))[2])
threelettercode.append((str(list(factors_values[1].keys())))[2])
threelettercode.append((str(list(factors_values[2].keys())))[2])

print(threelettercode)

match threelettercode[0]:
    case 'S':
        with open("ref_documents\Jobs_Social.csv",'r') as predfile:
            reader = csv.DictReader(predfile)
            for row in reader:
                joblist.append(row) 
        
               

        for i in joblist:
            if (threelettercode[0] and threelettercode[1] and threelettercode[2]) in i["Interest Code"]:
                suggested_job.append(i["Occupation"])
                
    case 'C':
        with open("ref_documents\Jobs_Conventional.csv",'r') as predfile:
            reader = csv.DictReader(predfile)
            for row in reader:
                joblist.append(row) 
        
               

        for i in joblist:
            if (threelettercode[0] and threelettercode[1] and threelettercode[2]) in i["Interest Code"]:
                suggested_job.append(i["Occupation"])
                
                
    case 'E':
        with open("ref_documents\Jobs_Enterprising.csv",'r') as predfile:
            reader = csv.DictReader(predfile)
            for row in reader:
                joblist.append(row) 
        
               

        for i in joblist:
            if (threelettercode[0] and threelettercode[1] and threelettercode[2]) in i["Interest Code"]:
                suggested_job.append(i["Occupation"])
                
    case 'I':
        with open("ref_documents\Jobs_Investigative.csv",'r') as predfile:
            reader = csv.DictReader(predfile)
            for row in reader:
                joblist.append(row) 
        
               

        for i in joblist:
            if (threelettercode[0] and threelettercode[1] and threelettercode[2]) in i["Interest Code"]:
                suggested_job.append(i["Occupation"])
                
    case 'R':
        with open("ref_documents\Jobs_Realistic.csv",'r') as predfile:
            reader = csv.DictReader(predfile)
            for row in reader:
                joblist.append(row) 
        
               

        for i in joblist:
            if (threelettercode[0] and threelettercode[1] and threelettercode[2]) in i["Interest Code"]:
                suggested_job.append(i["Occupation"])
                
    case 'A':
        with open("ref_documents\Jobs_Artistic.csv",'r') as predfile:
            reader = csv.DictReader(predfile)
            for row in reader:
                joblist.append(row) 
        
               

        for i in joblist:
            if (threelettercode[0] and threelettercode[1] and threelettercode[2]) in i["Interest Code"]:
                suggested_job.append(i["Occupation"])
                
                

five_suggestions=[]

for i in range(5):
    job=random.choice(suggested_job)
    five_suggestions.append(job)

print()
print()

print(suggested_job)



     



