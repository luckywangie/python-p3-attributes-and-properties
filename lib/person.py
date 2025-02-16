class Person:
    approved_jobs = ["Admin", "Customer Service", "Human Resources", "ITC", "Production", "Legal",
                     "Finance", "Sales", "General Management", "Research & Development", "Marketing", "Purchasing"]

    def __init__(self, name="Unknown", job="Unknown"):
        self.name = name
        self.job = job

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()  # Convert to title case before saving
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_job(self):
        return self._job

    def set_job(self, job):
        if job in Person.approved_jobs:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    name = property(get_name, set_name)
    job = property(get_job, set_job)


#test
person1 = Person(name="john doe", job="Finance")
print(person1.name) 
print(person1.job)  
person1.name = "jane smith" 
print(person1.name)  
person1.name = "" 
person1.job = "Doctor"  
person1.job = "Marketing" 
print(person1.job)  
