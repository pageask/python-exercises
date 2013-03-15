class Candidate:

    def __init__(self, years_of_experience, github_points,
                 languages_worked_with, applied_recently, age):
        self.years_of_experience = years_of_experience
        self.github_points = github_points
        self.languages_worked_with = languages_worked_with
        self.applied_recently = applied_recently
        self.age = age

    def experienced_programmer(self):
        return (
            "Python" in self.languages_worked_with and
            self.age >= 15 and
            self.applied_recently == False and
            (self.years_of_experience >= 2 or self.github_points >= 500))
