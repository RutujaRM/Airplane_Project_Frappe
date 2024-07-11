# Copyright (c) 2024, airplane_mode and contributors
# For license information, please see license.txt

from pkgutil import get_data
import frappe
from frappe.model.document import Document
import random
import itertools



class AirplaneTicket(Document):
  
    def validate(self):
        self.calculate_total_amount()           #To Calculate total Amount
        self.validate_status_before_submit()    #To Check status Borded or not 
        self.remove_duplicate_add_ons()         #To remove dublicate add-on method
    # 4 self.generate_random_seat()             #To Randmly generates seat numbers using number and alphabets
        self.checkStatus()                      #To Check status boarded or not
 

# 1) This function used to calculate total amount of ticket using flight price or add-ons 
    def calculate_total_amount(self):
        #  total amount with the flight price
        total_amount = self.flight_price or 0.0
        
        # Sum up the amounts of all the add-ons
        if self.add_ons:
            for add_on in self.add_ons:
                total_amount += add_on.amount   #get add-on amount fields price
        
        # Set the calculated total amount to the total_amount field
        self.total_amount = total_amount



# 2) This function used to check the ticket status it's boarded or not 
    def before_submit(self):
        self.validate_status_before_submit()
        self.remove_duplicate_add_ons()     # 3) Method

    def validate_status_before_submit(self):
        if self.status != "Boarded":          #if status is not match then throw an error
            frappe.throw("Cannot submit the Airplane Ticket unless the status is 'Boarded'. 🤨")


    

# 3) using this function used to remove dublicate add-ons items if repeated thrown message before submit
 
    def remove_duplicate_add_ons(self):       
        seen_types = set()               #create set which stores only unique values
        unique_add_ons = []              #create tuples 

        for add_on in self.add_ons:
            if add_on.item not in seen_types:   #if added type not present in seent types then it's added into that set
                seen_types.add(add_on.item)       
                unique_add_ons.append(add_on)  #all add-ons append into list/tuple
            else:
                 frappe.throw("Cannot Add Same Item's Multiple time Select Only Ones!!! 🙂")  #If same then throw an error message

        self.add_ons = unique_add_ons        #unique add-ons 


# 4) This function generates random seat number using numbers and alphabets
 
    # def before_insert(self):
    #     self.seat = self.generate_random_seat()
    #     # self.generate_random_seat()

    # def generate_random_seat(self):
    #     random_int = random.randint(1, 99)  # using random function generates randmoly numbers(start,end,increse by step)
    #     random_lett = random.choice('ABCDE')
    #     return f"{random_int}{random_lett}"


# 5) Assigns Proper seats sequentially rather than random

    def before_save(self):
        
        flight = frappe.get_doc('Airplane Flight', self.flight)
        airplane = frappe.get_doc('Airplane', flight.airplane)
        booking_count = frappe.db.count('Airplane Ticket', {'flight': self.flight})
        if booking_count >= airplane.capacity:
            frappe.throw('Seat not available in this flight. Check another one :)')
            return
    
    def seat_generator(self):
        seatDict = frappe.get_all('Airplane Ticket', filters={}, fields=["seat"])
        seatList  = [seat["seat"] for seat in seatDict]

        for number in range(1, 101):  # Generates numbers from 1 to 100
            for letter in 'ABCDE':    # Generates letters A to E for each number
                seat = f"{number}{letter}"  # Combine number and letter  # Initialize the seat generator
                if not seat in seatList:
                    return seat
        
    def before_insert(self):
        self.seat = self.seat_generator()

# 6) CheckStatus boarded or not
    def checkStatus(self):
        if self.status != "Boarded":
            frappe.throw("status is not boarded")






        
  
   
