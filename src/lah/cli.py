import argparse
import lah.db.utils as utils 
import pandas as pd
from tabulate import tabulate
def hello_msg():
    return "hello"

def cmd():    
    parser = argparse.ArgumentParser(prog='ProgramName', description='What the program does')

    parser.add_argument('-s', '--scount') # positional argument
    parser.add_argument('-t', '--top', type=int) # option that takes a value
    parser.add_argument('-d', '--dt') # on/off flag
    parser.add_argument('-p', '--pretty',action='store_true') # on/off flag

    args = parser.parse_args()
    print(args.scount, args.top, args.dt)

    if args.scount:
        print(f"-s => {args.scount}")
        # TODO 명령어 카운트
        print(utils.count(args.scount))
    elif args.top:
        print(f"-t => {args.top}")
        if args.dt:
            print(f"-d => {args.dt}")
            #TODO 특정 날짜의 명령어 TOP N
            table = utils.top(args.top, args.dt)
            if args.pretty:
                print(tabulate(table,headers="keys", tablefmt="pipe"))
            else:
                print(table)
        else:
            #parser.print_help()
            parser.error("-t 옵션은 -d 옵션과 함께 사용하시오!")
    else:
        # TODO - 사용법을 출력한다. 
        parser.print_help()
