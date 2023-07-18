import os
location = '/home/sambit/Desktop/Coding Folder/Companies List'
file ='wikipedia_output.csv'
path = os.path.join(location,file)

try:
	os.remove(path)
except:
	pass



import wikipediaapi

wiki = wikipediaapi.Wikipedia('en')
page = wiki.page('List of insurance companies in the United States')

print(page.exists())
print("Title: {}".format(page.title))

import re

text = page.text



''' Very doubtful code here '''


# Search for company names
company_names = re.findall(r'^\d+\.\s(.+)\n', text, flags=re.MULTILINE)

print(company_names[0])

# Search for website URLs
website_urls = re.findall(r'(https?:\/\/[^\s]+)', text)

# Combine company names and website URLs into a list of dictionaries
companies = [{'name': name, 'website': website} for name, website in zip(company_names, website_urls)]

selected_companies = companies[:300]
selected_company_names = [company['name'] for company in selected_companies]
selected_company_websites = [company['website'] for company in selected_companies]

''' very doubtful code ends here '''

import pandas as pd

data = pd.DataFrame(selected_company_websites)
data.to_csv('wikipedia_output.csv')

print("Command has run")
