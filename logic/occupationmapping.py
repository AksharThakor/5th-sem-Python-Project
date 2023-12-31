import csv

# Load the provided CSV file
input_file = "Sem 5\\pyhton\\project\\occupation mapping\\tempmachine\\jobs_Conventional.csv"
output_file = "Jobs_Conventional_With_Broader_Occupation.csv"

# Create a dictionary to store the broader occupation information
occupation_mapping_conventional = {
    "Amusement and Recreation Attendants": "Leisure and Hospitality",
    "Baristas": "Food Service and Hospitality",
    "Conveyor Operators and Tenders": "Manufacturing and Production",
    "Cooks, Fast Food": "Food Service and Hospitality",
    "Cutters and Trimmers, Hand": "Manufacturing and Production",
    "Derrick Operators, Oil and Gas": "Oil and Gas Industry",
    "Dining Room and Cafeteria Attendants and Bartender Helpers": "Food Service and Hospitality",
    "Dishwashers": "Food Service and Hospitality",
    "Door-to-Door Sales Workers, News and Street Vendors, and Related Workers": "Sales and Marketing",
    "Fallers": "Forestry and Logging",
    "Farmworkers and Laborers, Crop, Nursery, and Greenhouse": "Agriculture",
    "Fast Food and Counter Workers": "Food Service and Hospitality",
    "Food Preparation Workers": "Food Service and Hospitality",
    "Helpers--Painters, Paperhangers, Plasterers, and Stucco Masons": "Construction and Building Trades",
    "Landscaping and Groundskeeping Workers": "Agriculture",
    "Laundry and Dry-Cleaning Workers": "Cleaning and Housekeeping",
    "Maids and Housekeeping Cleaners": "Cleaning and Housekeeping",
    "Rock Splitters, Quarry": "Mining and Quarrying",
    "Sewing Machine Operators": "Manufacturing and Production",
    "Bill and Account Collectors": "Financial Services",
    "Cargo and Freight Agents": "Logistics and Transportation",
    "Cashiers": "Retail and Customer Service",
    "Correspondence Clerks": "Clerical and Administrative",
    "Costume Attendants": "Arts and Entertainment",
    "Counter and Rental Clerks": "Retail and Customer Service",
    "Court, Municipal, and License Clerks": "Legal and Government",
    "Credit Authorizers, Checkers, and Clerks": "Financial Services",
    "Data Entry Keyers": "Clerical and Administrative",
    "Dispatchers, Except Police, Fire, and Ambulance": "Emergency Services",
    "File Clerks": "Clerical and Administrative",
    "Freight Forwarders": "Logistics and Transportation",
    "Gambling and Sports Book Writers and Runners": "Gaming and Sports Betting",
    "Gambling Cage Workers": "Gaming and Sports Betting",
    "Gambling Change Persons and Booth Cashiers": "Gaming and Sports Betting",
    "Gambling Dealers": "Gaming and Sports Betting",
    "Hotel, Motel, and Resort Desk Clerks": "Hospitality and Tourism",
    "Inspectors, Testers, Sorters, Samplers, and Weighers": "Quality Control and Inspection",
    "Insurance Claims and Policy Processing Clerks": "Insurance and Claims Processing",
    "Library Assistants, Clerical": "Libraries and Education",
    "Mail Clerks and Mail Machine Operators, Except Postal Service": "Mail and Logistics",
    "Medical Secretaries and Administrative Assistants": "Healthcare Administration",
    "Meter Readers, Utilities": "Utilities and Energy",
    "Office Clerks, General": "Clerical and Administrative",
    "Order Clerks": "Sales and Customer Service",
    "Orderlies": "Healthcare Support",
    "Pharmacy Aides": "Healthcare Support",
    "Photographic Process Workers and Processing Machine Operators": "Photography and Imaging",
    "Postal Service Clerks": "Mail and Logistics",
    "Postal Service Mail Carriers": "Mail and Logistics",
    "Postal Service Mail Sorters, Processors, and Processing Machine Operators": "Mail and Logistics",
    "Procurement Clerks": "Logistics and Procurement",
    "Production, Planning, and Expediting Clerks": "Manufacturing and Production",
    "Public Safety Telecommunicators": "Emergency Services",
    "Receptionists and Information Clerks": "Clerical and Administrative",
    "Reservation and Transportation Ticket Agents and Travel Clerks": "Travel and Tourism",
    "Secretaries and Administrative Assistants, Except Legal, Medical, and Executive": "Clerical and Administrative",
    "Shipping, Receiving, and Inventory Clerks": "Logistics and Inventory",
    "Stockers and Order Fillers": "Logistics and Inventory",
    "Switchboard Operators, Including Answering Service": "Clerical and Administrative",
    "Telephone Operators": "Clerical and Administrative",
    "Tellers": "Financial Services",
    "Title Examiners, Abstractors, and Searchers": "Real Estate and Title Services",
    "Weighers, Measurers, Checkers, and Samplers, Recordkeeping": "Quality Control and Inspection",
    "Word Processors and Typists": "Clerical and Administrative",
    "Grinding and Polishing Workers, Hand": "Manufacturing and Production",
    "Billing and Posting Clerks": "Financial Services",
    "Bookkeeping, Accounting, and Auditing Clerks": "Accounting and Financial Analysis",
    "Brokerage Clerks": "Financial Services",
    "Computer Numerically Controlled Tool Programmers": "Manufacturing and Production",
    "Court Reporters and Simultaneous Captioners": "Legal Services",
    "Customs and Border Protection Officers": "Law Enforcement and Customs",
    "Dental Assistants": "Healthcare Support",
    "Energy Auditors": "Energy and Sustainability",
    "Executive Secretaries and Executive Administrative Assistants": "Clerical and Administrative",
    "Government Property Inspectors and Investigators": "Government and Inspection",
    "Human Resources Assistants, Except Payroll and Timekeeping": "Human Resources",
    "Insurance Appraisers, Auto Damage": "Insurance and Claims Processing",
    "Interviewers, Except Eligibility and Loan": "Interviewing and Surveys",
    "Legal Secretaries and Administrative Assistants": "Legal Services",
    "Library Technicians": "Libraries and Education",
    "Loan Interviewers and Clerks": "Financial Services",
    "Medical Transcriptionists": "Healthcare Support",
    "New Accounts Clerks": "Financial Services",
    "Occupational Health and Safety Technicians": "Health and Safety",
    "Ophthalmic Medical Technicians": "Healthcare Support",
    "Ophthalmic Medical Technologists": "Healthcare Support",
    "Paralegals and Legal Assistants": "Legal Services",
    "Payroll and Timekeeping Clerks": "Human Resources and Payroll",
    "Pharmacy Technicians": "Healthcare Support",
    "Phlebotomists": "Healthcare Support",
    "Police Identification and Records Officers": "Law Enforcement and Records",
    "Quality Control Analysts": "Quality Control and Analysis",
    "Surgical Assistants": "Healthcare Support",
    "Surveying and Mapping Technicians": "Surveying and Mapping",
    "Tax Examiners and Collectors, and Revenue Agents": "Tax and Revenue Services",
    "Tax Preparers": "Tax and Accounting",
    "Web Developers": "Web Development and IT",
    "Accountants and Auditors": "Accounting and Auditing",
    "Actuaries": "Actuarial Science",
    "Budget Analysts": "Financial Analysis",
    "Claims Adjusters, Examiners, and Investigators": "Insurance and Claims Processing",
    "Clinical Data Managers": "Healthcare Data Management",
    "Compensation, Benefits, and Job Analysis Specialists": "Compensation and Benefits",
    "Compliance Managers": "Regulatory Compliance",
    "Cost Estimators": "Cost Estimation",
    "Credit Analysts": "Credit Analysis",
    "Database Administrators": "Database Management",
    "Document Management Specialists": "Document Management",
    "Environmental Compliance Inspectors": "Environmental Compliance",
    "Information Security Analysts": "Information Security",
    "Insurance Underwriters": "Insurance Underwriting",
    "Loan Officers": "Loan Origination and Analysis",
    "Logistics Analysts": "Logistics Analysis",
    "Proofreaders and Copy Markers": "Proofreading and Editing",
    "Purchasing Agents, Except Wholesale, Retail, and Farm Products": "Purchasing and Procurement",
    "Regulatory Affairs Specialists": "Regulatory Affairs",
    "Sales Representatives, Wholesale and Manufacturing, Except Technical and Scientific Products": "Sales and Wholesale",
    "Social and Human Service Assistants": "Social and Human Services",
    "Social Science Research Assistants": "Social Science Research",
    "Statistical Assistants": "Statistical Analysis",
    "Treasurers and Controllers": "Treasury and Controller",
    "Web Administrators": "Web Administration",
    "Medical and Health Services Managers": "Healthcare Administration",
    "Archivists": "Archiving",
    "Judicial Law Clerks": "Legal Services",
    "Librarians and Media Collections Specialists": "Libraries and Media",
    "Statisticians": "Statistics",
    "Bioinformatics Scientists": "Bioinformatics",
    "Biostatisticians": "Biostatistics",
    "Chief Executives": "Executive Leadership",
    "Chief Sustainability Officers": "Sustainability Leadership",
    "Curators": "Curation",
    "Economists": "Economics",
    "Education Administrators, Postsecondary": "Education Administration",
    "Financial Quantitative Analysts": "Quantitative Analysis",
    "Investment Fund Managers": "Investment Management",
    "Mathematicians": "Mathematics",
    "Operations Research Analysts": "Operations Research",
    "Pharmacists": "Pharmacy",
    "Survey Researchers": "Survey Research",
    "Teaching Assistants, Postsecondary": "Teaching Assistance",
    "Clinical Nurse Specialists": "Nursing",
}

# Read the CSV and add the broader occupation field and write data from dictionary to create new file
with open(input_file, 'r', newline='') as input_csv:
    reader = csv.DictReader(input_csv)
    with open(output_file, 'w', newline='') as output_csv:
        fieldnames = ["Interest Code", "Occupation", "Broader Occupation"]
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        writer.writeheader()
        new_info={}
        for row in reader:
            specific_occupation = row["Occupation"]
            new_info["Interest Code"]=row["Interest Code"]
            new_info["Occupation"]=row["Occupation"]
            if specific_occupation in occupation_mapping_conventional:
                new_info["Broader Occupation"] = occupation_mapping_conventional[specific_occupation]
            else:
                new_info["Broader Occupation"] = "N/A"
            writer.writerow(new_info)


print(f"Data with broader occupation fields has been written to {output_file}.")