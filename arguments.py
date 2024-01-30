import argparse

def create(args):
    print(f"Creating DB {args.name} with DB schema {args.schema}.")

def add(args):
    print(f"Adding switch {args.username} to database.")

def get(args):
    print(f"Get")

parser = argparse.ArgumentParser(description='Утилита для скачивания данных с сервера hub1.emsd.ru.')
#parser.add_argument('--date', metavar='date', nargs='+', default=None, help='Список дат файлов, для скачивания.')
subparsers = parser.add_subparsers(title='Subcommands',
                                   description='valid subcommands',
                                   help='description')

create_parser = subparsers.add_parser('create_db', help='create new db')
create_parser.add_argument('-n', metavar='db-filename', dest='name',
                           default='qwe', help='db filename')
create_parser.add_argument('-s', dest='schema', default='qweqwe',
                           help='db schema filename')
create_parser.set_defaults(func=create)

add_parser = subparsers.add_parser('add', help='add data to db')
add_parser.add_argument('username', help='Username add to db.')
add_parser.set_defaults(func=add)

if __name__ == "__main__":
    args = parser.parse_args()
    if not vars(args):
        parser.print_usage()
    else:
        args.func(args)
