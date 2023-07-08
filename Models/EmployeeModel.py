class Employee:
    def __init__(self, lastName, firstName, title, titleOfCourtesy, birthDate, hireDate,
                 address=None, city=None, region=None, postalCode=None, country=None, homePhone=None,
                 extension=None, notes=None):
        self.LastName = lastName
        self.FirstName = firstName
        self.Title = title
        self.TitleOfCourtesy = titleOfCourtesy
        self.BirthDate = birthDate
        self.HireDate = hireDate
        self.Address = address
        self.City = city
        self.Region = region
        self.PostalCode = postalCode
        self.Country = country
        self.HomePhone = homePhone
        self.Extension = extension
        self.Notes = notes


class EmloyeeIdDelete:
    def __init__(self, emloyeeID = None):
        self.EmloyeeID = emloyeeID
