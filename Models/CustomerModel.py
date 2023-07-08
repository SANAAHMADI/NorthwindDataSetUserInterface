class Customer:
    def __init__(self ,customerID, companyName ,contactName=None ,contactTitle=None , address=None ,
                 city=None ,region=None ,postalCode=None ,country=None ,phone=None ,fax=None):
        self.CustomerID = customerID
        self.CompanyName = companyName
        self.ContactName = contactName
        self.ContactTitle = contactTitle
        self.ADDRESS = address
        self.City = city
        self.Region = region
        self.PostalCode = postalCode
        self.Country = country
        self.Phone = phone
        self.Fax = fax

class CustomerIdDelete:
    def __init__(self, customerID = None):
        self.CustomerId = customerID





