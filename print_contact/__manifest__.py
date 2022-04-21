{
        'name':'Printing of contacts',
        'description':'Provide contacts pdfs reports',
        'summary':'Many PDFs available for provide contacts reports.',
       
        'depends':['base','account','sale'],
        'application':False,        
        'version':'1.0',
        'license':'AGPL-3',
        
        
        'data':[
            'views/print_buttons.xml',
            
            'report/print_page.xml',
            'report/print_listing.xml',
            'report/print_checkin.xml',
            'report/print_wtssr.xml',
            'report/print_msssr.xml',
            'report/print_sale.xml',
             'report/print_invoice.xml',
              'report/print_quotation.xml',
            ],
         
        
}

