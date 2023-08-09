from django.db import models


class CustomerModel(models.Model):
    """Customer class model."""
    """TODO Decide if address should be separate model"""
    US_STATES = [("AL", "Alabama"), ("AK", "Alaska"), ("AZ", "Arizona"), ("AR", "Arkansas"), ("CA", "California"), ("CO", "Colorado"),
                 ("CT", "Connecticut"), ("DC", "Washington DC"), ("DE", "Delaware"), ("FL", "Florida"), ("GA", "Georgia"),
                 ("HI", "Hawaii"), ("ID", "Idaho"), ("IL", "Illinois"), ("IN", "Indiana"), ("IA", "Iowa"), ("KS", "Kansas"), ("KY", "Kentucky"),
                 ("LA", "Louisiana"), ("ME", "Maine"), ("MD", "Maryland"), ("MA", "Massachusetts"), ("MI", "Michigan"), ("MN", "Minnesota"),
                 ("MS", "Mississippi"), ("MO", "Missouri"), ("MT", "Montana"), ("NE", "Nebraska"), ("NV", "Nevada"), ("NH", "New Hampshire"),
                 ("NJ", "New Jersey"), ("NM", "New Mexico"), ("NY", "New York"), ("NC", "North Carolina"), ("ND", "North Dakota"), ("OH", "Ohio"),
                 ("OK", "Oklahoma"), ("OR", "Oregon"), ("PA", "Pennsylvania"), ("RI", "Rhode Island"), ("SC", "South Carolina"), ("SD", "South Dakota"),
                 ("TN", "Tennessee"), ("TX", "Texas"), ("UT", "Utah"), ("VT", "Vermont"), ("VA", "Virginia"), ("WA", "Washington"), ("WV", "West Virginia"),
                 ("WI", "Wisconsin"), ("WY", "Wyoming")]

    first_name = models.CharField(
        max_length=30, help_text='Enter first name of customer')
    last_name = models.CharField(
        max_length=30, help_text='Enter last name of customer')
    address = models.CharField(
        max_length=30, help_text='Enter address of customer')
    city = models.CharField(
        max_length=30, help_text='Enter the city of address')
    zip_code = models.CharField(
        max_length=10, help_text='Enter the zip code address')
    state = models.CharField(max_length=25, help_text='Enter state of address', choices=US_STATES)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
