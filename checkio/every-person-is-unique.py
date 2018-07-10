import datetime


class Person:
    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city,
                 gender='unknown'):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender

    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def age(self):
        now = datetime.datetime.strptime("2018-01-01", "%Y-%m-%d")
        birth = datetime.datetime.strptime(self.birth_date, "%d.%m.%Y")
        return divmod((now - birth).days, 365)[0]

    def work(self):
        if self.gender == "male":
            line = "He is a "
        elif self.gender == "female":
            line = "She is a "
        else:
            line = "Is a "
        line += self.job
        return line

    def money(self):
        earned = self.working_years * 12 * self.salary
        return '{0:,}'.format(earned).replace(',', ' ')

    def home(self):
        return "Lives in {0.city}, {0.country}".format(self)
