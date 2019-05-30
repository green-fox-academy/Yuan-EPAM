from optparse import OptionParser

def initialize_command_options():
    parser = OptionParser()
    parser.add_option('-i', '--init_db', type='string',
                        help='initialize database')
    parser.add_option('-a', '--add_json', type='string', 
                       help='add json data to database')
    return parser.parse_args()