from optparse import OptionParser

def initial_command_options():
    """
    Initialization command line options
    """
    parser = OptionParser()
    parser.add_option('-r', '--remove', type=int)
    parser.add_option('-d', '--decrease', type=str)
    parser.add_option('-a', '--average', type=int)
    return parser.parse_args()

