class Supplier:
    def __init__(self,companyName ,contactName,contactTitle,address=None, city=None,
                 region=None, postalCode=None, country=None,phone=None,fax=None,homePage=None ):

        self.CompanyName=companyName
        self.ContactName=contactName
        self.ContactTitle=contactTitle
        self.Address=address
        self.City=city
        self.Region=region
        self.PostalCode=postalCode
        self.Country=country
        self.Phone=phone
        self.Fax=fax
        self.HomePage=homePage

class SupplierIdDelete:
    def __init__(self, supplierID = None):
        self.SupplierID = supplierID
