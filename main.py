from NaiveSolver import NaiveSolver
from parser import *
if __name__ == '__main__':

    for file_name in ['a', 'b','f']:
        print('solving file:', file_name)

        projects, contributors = parse_input('input_data/' + file_name)
        solver = NaiveSolver()
        taken_projects = solver.solve(contributors, projects)


        create_output_file(file_name+'.sol', taken_projects)
