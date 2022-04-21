from odoo import api,fields,models
from odoo.exceptions import Warning,ValidationError,UserError


class extend_contact(models.Model):
    _inherit='account.move'
    
   
    def print_page(self):
        return self.env.ref('print_contact.action_report_page').report_action(self)
    
    
    def print_listing(self):
        return self.env.ref('print_contact.action_report_listing').report_action(self)
    
    
    def print_checkin(self):
        return self.env.ref('print_contact.action_report_checkin').report_action(self)
        
    def print_wtssr(self):
        return self.env.ref('print_contact.action_report_wtssr').report_action(self)
    
    def print_msssr(self):
        return self.env.ref('print_contact.action_report_msssr').report_action(self)
        
    def print_imvoice(self):
        return self.env.ref('print_contact.action_report_invoice').report_action(self)
        
class extend_contacts(models.Model):
    _inherit='sale.order'
    
   
    def print_page(self):
        return self.env.ref('print_contact.action_report_sale').report_action(self)
        
    def print_quotation(self):
        return self.env.ref('print_contact.action_report_quotation').report_action(self)
        
    