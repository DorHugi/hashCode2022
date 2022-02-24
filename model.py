class Skill:
    def __init__(self, type, level):
        self.level = level
        self.type = type

    def __str__(self):
        return f'Skill: {self.type} {self.level}'

    def __repr__(self):
        return f'Skill: {self.type} {self.level}'

class Project:
    #  Roles is an array of skills
    def __init__(self, name, duration, score, best_before, required_skills):
        self.required_skills = required_skills
        self.best_before = best_before
        self.score = score
        self.name = name
        self.duration = duration

    def __str__(self):
        return f'Project: {self.name} {self.duration} {self.score} {self.best_before} {self.required_skills}'

    def __repr__(self):
        return f'Project: {self.name} {self.duration} {self.score} {self.best_before} {self.required_skills}'


class Contributor:
    def __init__(self, name, skills):
        self.skills = skills
        self.name = name

    def __str__(self):
        return f'Contributor: {self.name} {self.skills}'

    def __repr__(self):
        return f'Contributor: {self.name} {self.skills}'
