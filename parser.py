from model import Skill, Contributor, Project


def parse_input(file_path):
    with open(file_path, 'r') as fh:
        lines = [l for l in fh.readlines()]
        num_contributors, num_projects = lines[0].split()
        contributors = []
        projects = []
        parsed_contributors = 0
        while lines:
            l = lines.pop(0)
            if parsed_contributors < num_contributors:
                num_contributors += 1
                name, skills_num = l.split()
                skills_num = int(skills_num)
                skills = []
                for i in range(skills_num):
                    skill = parse_skill(lines)
                    skills.append(skill)
                contributors.append(Contributor(name, skills))
            else:
                project_name, duration, score, best_before, roles_num = l.split()
                duration = int(duration)
                best_before = int(best_before)
                roles_num = int(roles_num)
                score = int(score)
                required_skills = []
                for i in range(roles_num):
                    skill = parse_skill(lines)
                    required_skills.append(skill)
                projects.append(Project(project_name, duration, score, best_before, required_skills))


def parse_skill(lines):
    l = lines.pop(0)
    skill_type, skill_level = l.split()
    skill_level = int(skill_level)
    skill = Skill(skill_type, skill_level)
    return skill


