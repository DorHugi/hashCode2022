class Skill:
    def __init__(self, type, level):
        self.level = level
        self.type = type


class Project:
    #  Roles is an array of skills
    def __init__(self, name, duration, score, best_before, required_skills):
        self.required_skills = required_skills
        self.best_before = best_before
        self.score = score
        self.name = name
        self.duration = duration


class Contributor:
    def __init__(self, name, skills):
        self.skills = skills
        self.name = name
