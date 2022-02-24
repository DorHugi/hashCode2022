from copy import deepcopy, copy

from AbstractSolver import Solver


class NaiveSolver(Solver):
    def solve(self, contributors, projects):
        taken_projects = {}
        # contributors, projects = map(deepcopy, [contributors, projects])
        projects.sort(key=lambda p: p.score, reverse=True)
        # add secondary sorting based on "best before"
        for project in projects:
            for start_date in range(project.best_before - project.duration):
                selected_contributors = NaiveSolver.can_take_project(project, contributors, start_date,
                                                                     project.duration)
                if selected_contributors:
                    for contributor in selected_contributors:
                        contributor.update_project_taken(project, start_date)
                    taken_projects[project.name] = [sc.name for sc in selected_contributors]
        return taken_projects

    @staticmethod
    def can_take_project(project, contributors, start_date, duration):
        available_contributors = copy(contributors)
        selected_contributors = []
        for required_skill in project.required_skills:
            selected_contributor = NaiveSolver.can_fill_required_skill(required_skill, available_contributors,
                                                                       start_date, duration)
            if not selected_contributor:
                return False
            else:
                selected_contributors.append(selected_contributor)
                available_contributors.remove(selected_contributor)
        return selected_contributors

    @staticmethod
    def can_fill_required_skill(required_skill, available_contributors, start_date, duration):
        for ac in available_contributors:
            if ac.is_fit_for_job(required_skill) and ac.is_free(start_date, start_date + duration):
                return ac
        return None
