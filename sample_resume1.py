from io import BytesIO
from pdfdocument.document import PDFDocument

from datetime import date
import random
import sys
certificate_courses = open('certificate_courses.csv',encoding='utf8',errors='ignore').read().split(',')
courses = open('course.csv',encoding='utf8',errors='ignore').readlines()
colleges = open('colleges.csv',encoding='utf8',errors='ignore').readlines()[1:]    
companies = open('social_candidate_pos.csv',encoding='utf8').readlines()    
cities = open('cities.csv',encoding='utf8').readlines()[1:]    
names = open('Indian-Male-Names.csv',encoding='utf8').readlines()
skills = open('skills.csv',encoding='utf8').readlines()

def getSkills(skill_count):
    s=[]
    for i in range(skill_count):
      x=skills[random.randint(0,len(skills)-1)].replace('\n','')
      s+=[x]
    return s
def getEmployment():
  i = random.randint(0,len(companies)-1)
  company = companies[i].split(',')
  e={"company_name": company[6],
      "company_type": "","company_domains":'software development',
      "designation": company[5],"tenure":['"'+company[1]+ '-'+ company[0].zfill(2) +'","' +company[3]+ '-'+company[2].zfill(2) + '"'],
      "description": "Worked in software development using various technologies with MNC clients", "skills":{}   
      }
  return e
def makemPdf(company_count=5,skill_count=10):
  pdf = PDFDocument("qa.pdf")
  pdf.init_report()
  pdf.h1("Q.A " + names[random.randint(0,len(names)-1)].title())
  pdf.h2("qa"+str(random.randint(0,10000000000))+'@example.com' )
  pdf.h2(cities[random.randint(0,len(cities)-1)].replace('\n','') + ', India')
  pdf.h2("+91-" + str(random.randint(9000000000,9999999999)) )
  execSummary="I am a software professional. I like to solve problems. I am a fast learner and like to work on new technologies. I am a self starter and good communicator. I  have worked with MNC clients. I can work independently or in a team "
  pdf.p(execSummary)
  pdf.hr()
  pdf.h2("Experience Summary")
  emp=[]
  for c in range(company_count):
    e= getEmployment()
    e['skills'] = getSkills(skill_count)
    emp+=[e]
  for s in emp:
    pdf.h1(s['company_name'] + ',    ' + s['designation'] ) 
    pdf.h2(cities[random.randint(0,len(cities)-1)].replace('\n','') + ',    ' +s['tenure'][0].replace('"','').replace(',',' to ')) 
    pdf.h2("Description: " + s['description'])
    l=""
    for m in s['skills']:
      l += m + ","
    pdf.h3("Skills: "+l[:-1])
    pdf.hr()
  pdf.h2("Education")
  pdf.h3(courses[random.randint(0,len(courses)-1)].replace('\n','') + ' ' + str(random.randint(2000,2010)))
  pdf.h3(colleges[random.randint(0,len(colleges)-1)])
  pdf.h2('\n Certifications')
  pdf.h3('Certificate course in ' + certificate_courses[random.randint(0,len(certificate_courses)-1)] + ' ' + str(random.randint(2000,2020)))
  pdf.h3('Certificate course in ' + certificate_courses[random.randint(0,len(certificate_courses)-1)] + ' ' + str(random.randint(2000,2020)))
  pdf.generate()
if __name__ == "__main__":
    if len(sys.argv) == 3:
      makemPdf(int(sys.argv[1]),int(sys.argv[2]))
    else: 
      makemPdf()
