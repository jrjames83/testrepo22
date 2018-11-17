import json
import random
from collections import Counter

# curl --data "text=80215" https://eaqsml6ex9.execute-api.us-east-1.amazonaws.com/weather/weather

def pick_student():
    students = ['Aihua Chen',
     'Alex Rosheim',
     'Andres Herrera',
     'Chad Anderson',
     'Christopher Benavides',
     'Damian McDonald',
     'Damon Chick',
     'Deidra Nguyen',
     'Ermias Gebregziabher',
     'Eva-Marie Hamilton',
     'Fiorella Enciso',
     'Glen Dinolfo',
     'James Harmon',
     'Jarred Armijo',
     'Jen Wilson',
     'Jennifer Over',
     'john schlafly',
     'John Sudderth',
     'Jonathan Heston',
     'Kirstin Nordentoft',
     'Laura Talkington',
     'Megan Sabella',
     'Michael Afreh',
     'Michael Dendinger',
     'Monica Evans',
     'Natalee Reese',
     'ramneek bali',
     'Royal Taylor',
     'Ryan Heller',
     'Salar Saljoughi',
     'Summer He']
    return random.choice(students)
    

def lambda_handler(event, context):
    student = pick_student()
    
    return {
        'statusCode': 200,
        'headers': { 'Content-Type': 'application/json' },
        'body': json.dumps(
            { 'text': 'Why thanks {}, we look forward to your response! '.format(student)})
    }
