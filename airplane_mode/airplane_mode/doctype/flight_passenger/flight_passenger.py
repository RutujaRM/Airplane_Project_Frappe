# Copyright (c) 2024, airplane_mode and contributors
# For license information, please see license.txt


"""Error :- This not import the module or load it """

import frappe
from frappe.model.document import Document

class FlightPassenger(Document):
    def get_full_name(self):
        """Returns the FlightPassenger's full name"""
        return f"{self.first_name} {self.last_name}"
    
    def before_save(self):
        """Sets the full name before saving the document"""
        self.full_name = self.get_full_name()
