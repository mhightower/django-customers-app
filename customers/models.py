from django.db import models


class CustomerModel(models.Model):
    """Customer class model."""

    AL = "AL"
    AK = "AK"
    AZ = "AZ"
    AR = "AR"
    CA = "CA"
    CO = "CO"
    CT = "CT"
    DC = "DC"
    DE = "DE"
    FL = "FL"
    GA = "GA"
    HI = "HI"
    ID = "ID"
    IL = "IL"
    IN = "IN"
    IA = "IA"
    KS = "KS"
    KY = "KY"
    LA = "LA"
    ME = "ME"
    MD = "MD"
    MA = "MA"
    MI = "MI"
    MN = "MN"
    MS = "MS"
    MO = "MO"
    MT = "MT"
    NE = "NE"
    NV = "NV"
    NH = "NH"
    NJ = "NJ"
    NM = "NM"
    NY = "NY"
    NC = "NC"
    ND = "ND"
    OH = "OH"
    OK = "OK"
    OR = "OR"
    PA = "PA"
    RI = "RI"
    SC = "SC"
    SD = "SD"
    TN = "TN"
    TX = "TX"
    UT = "UT"
    VT = "VT"
    VA = "VA"
    WA = "WA"
    WV = "WV"
    WI = "WI"
    WY = "WY"

    US_STATES = [(AL, "Alabama"), (AK, "Alaska"), (AZ, "Arizona"), (AR, "Arkansas"), (CA, "California"), (CO, "Colorado"),
                 (CT, "Connecticut"), (DC, "Washington DC"), (DE, "Delaware"), (FL, "Florida"), (GA, "Georgia"),
                 (HI, "Hawaii"), (ID, "Idaho"), (IL, "Illinois"), (IN, "Indiana"), (IA, "Iowa"), (KS, "Kansas"),
                 (KY, "Kentucky"), (LA, "Louisiana"), (ME, "Maine"), (MD, "Maryland"), (MA, "Massachusetts"),
                 (MI, "Michigan"), (MN, "Minnesota"), (MS, "Mississippi"), (MO, "Missouri"), (MT, "Montana"),
                 (NE, "Nebraska"), (NV, "Nevada"), (NH, "New Hampshire"), (NJ, "New Jersey"), (NM, "New Mexico"),
                 (NY, "New York"), (NC, "North Carolina"), (ND, "North Dakota"), (OH, "Ohio"), (OK, "Oklahoma"),
                 (OR, "Oregon"), (PA, "Pennsylvania"), (RI, "Rhode Island"), (SC, "South Carolina"), (SD, "South Dakota"),
                 (TN, "Tennessee"), (TX, "Texas"), (UT, "Utah"), (VT, "Vermont"), ( VA, "Virginia"), (WA, "Washington"),
                 (WV, "West Virginia"), (WI, "Wisconsin"), (WY, "Wyoming")]

    first_name = models.CharField(
        max_length=30, help_text='Enter first name of customer')
    last_name = models.CharField(
        max_length=30, help_text='Enter last name of customer')
    address = models.CharField(
        max_length=30, help_text='Enter address of customer')
    city = models.CharField(
        max_length=30, help_text='Enter the city of address')
    zip_code = models.CharField(
        max_length=10, help_text='Enter the zip code of address')
    state = models.CharField(
        max_length=25, help_text='Enter state of address', choices=US_STATES)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
