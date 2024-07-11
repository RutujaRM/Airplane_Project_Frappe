# Copyright (c) 2024, airplane_mode and contributors
# For license information, please see license.txt

# import frappe
# from frappe.website.website_generator import WebsiteGenerator


# class AirplaneFlight(WebsiteGenerator):

#  #To change the states inside airplane flight
#     def on_submit(self):
#             self.status = 'Completed'
#             self.save() 


# import frappe
# from frappe.website.website_generator import WebsiteGenerator

# class AirplaneFlight(WebsiteGenerator):
      
      
#     def on_submit(self):
#         # Set the status field to Completed
#         self.status = "Completed"
#         self.save()


from frappe.website.website_generator import WebsiteGenerator

class AirplaneFlight(WebsiteGenerator):
    def on_submit(self):
        super(AirplaneFlight, self).on_submit()
        self.status = "Completed"
        self.save(ignore_permissions=True)


