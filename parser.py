from model import Skill, Contributor, Project


def parse_input(file_path):
    with open(file_path, 'r') as fh:
        lines = [l for l in fh.readlines()]
        num_contributors, num_projects = lines[0].split()
        num_contributors = int(num_contributors)
        num_projects = int(num_projects)
        contributors = []
        projects = []
        parsed_contributors = 0
        lines.pop(0)
        while lines:
            l = lines.pop(0)
            if parsed_contributors < num_contributors:
                parsed_contributors += 1
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
    return projects, contributors


def parse_skill(lines):
    l = lines.pop(0)
    skill_type, skill_level = l.split()
    skill_level = int(skill_level)
    skill = Skill(skill_type, skill_level)
    return skill


def create_output_file(output_file_path, selected_projects):
    lines = []
    projects_num = str(len(selected_projects))
    lines.append(projects_num)
    for k, v in selected_projects.items():
        lines.append(k)
        lines.append(' '.join(v))
    lines = [x + '\n' for x in lines]

    with open(output_file_path, 'w') as fh:
        fh.writelines(lines)


