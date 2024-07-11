# # Copyright (c) 2024, airplane_mode and contributors
# # For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class Register(Document):
	





#8888888888888888888888888888888888888888888888888888888888888
	


# from frappe.model.document import Document

# class Register(Document):
#     def autoname(self):
#         if self.first_name and self.last_name:
#             self.full_name = f"{self.first_name} {self.last_name}"
#         else:
#             self.full_name = self.first_name or self.last_name
#         self.name = self.full_name

#     def validate(self):
#         self.full_name = f"{self.first_name} {self.last_name}" if self.first_name and self.last_name else self.first_name or self.last_name



import frappe
from frappe.model.document import Document
import re

class Register(Document):
    def validate_first_name(self):
        p = r'^[a-zA-Z\-]+$'
        if re.match(p, self.first_name):
            return True
        else:
            frappe.throw("Invalid first name")

    def validate_last_name(self):
        p = r'^[a-zA-Z\-]+$'
        if re.match(p, self.last_name):
            return True
        else:
            frappe.throw("Invalid last name")

    def validate(self):
        self.validate_first_name()
        self.validate_last_name()
        self.full_name = f"{self.first_name} {self.last_name}" if self.first_name and self.last_name else self.first_name or self.last_name


    def validateEmail(self):
        p = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        if re.match(p,self.email):
            return True
        else:
            frappe.throw("invalid email")
            
def validatePhone(self):
        n=r'^\+?\d{1,3}\d{10}$'
        if re.match(p,self.phone_number):
            return True
        else:
            frappe.throw("invalid phone Number")		