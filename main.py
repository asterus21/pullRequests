import argparse
from git import Repo

from datetime import datetime


class Timestamp:
    
    def __init__(self, message=''):
        self.message = message
    

    def __str__(self):
        return f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} {self.message}'


class Script(Timestamp):

    def __init__(self, pa6, pagrid, ab) -> None:        
        super().__init__()
        print(Timestamp('Starting the script...'))
        self.pa6 = pa6
        self.pagrid = pagrid
        self.ab = ab


    def __str__(self):
        return super().__str__()


    def print_output(self, output, repo):
        print(Timestamp(f'Pulling: {repo.remotes.origin.url}'))
        print(Timestamp(output))


    def pull_repo(self, path):
        repo = Repo(path)
        output = repo.git.pull()
        self.print_output(output, repo)


    def start_script(self, args):
        for arg in args:
            self.pull_repo(arg)


if __name__ == '__main__':    
    parser = argparse.ArgumentParser()
    parser.add_argument('-pa',   action='store', dest='pa',   help='path to PA 6.5 help',  type=str)
    parser.add_argument('-grid', action='store', dest='grid', help='path to PA Grid help', type=str)
    parser.add_argument('-ab',   action='store', dest='ab',   help='path to AB help',      type=str)
    args = parser.parse_args()

    script = Script(args.pa, args.grid, args.ab)
    if args.pa:
        script.pull_repo(args.pa)
    elif args.grid:
        script.pull_repo(args.grid)
    elif args.ab:
        script.pull_repo(args.ab)
    else:
        paths = ['D:/gitbash/help/', 'D:/gitbash/help.7/', 'D:/gitbash/help.ab/']
        script.start_script(paths)
