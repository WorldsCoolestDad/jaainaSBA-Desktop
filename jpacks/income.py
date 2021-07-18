class Income:
    def __init__(self, job_date, client, buyer, platform, pay):
        self.job_date = job_date
        self.client = client
        self.buyer = buyer
        self.platform = platform
        self.pay = pay

    def save_records(self):
        print("Saving record.....")

    def get_records(self):
        print("Getting records...")

    def display_records(self):
        return self.job_date,self.client,self.buyer,self.platform,self.pay
