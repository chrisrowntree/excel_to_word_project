from docxtpl import DocxTemplate#
from datetime import datetime
import pandas as pd

doc = DocxTemplate("template.docx")

my_name = "Chris Rowntree"
my_address = "76 Fassett Road"
my_email = "chris.rowntree@gmail.com"
todays_date = datetime.today().strftime("%d %b, %Y")

my_context = { 'my_name' : my_name, 'my_address' : my_address, 'my_email' : my_email, 'todays_date' : todays_date }


df = pd.read_csv('fake_data.csv')

for index, row in df.iterrows():
    print(index)
    print(row)


for index, row in df.iterrows():
    context = {
        'name': row['name'],
        'address': row['address'],
        'email': row['email'],
        'company': row['company']
        } 
    
    context.update(my_context)
    doc.render(context)
    doc.save(f"generated_doc_{index}.docx")