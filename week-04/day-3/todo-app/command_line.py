from optparse import OptionParser

def initial_command_options():
    """
    Initialization command line options
    """
    parser = OptionParser()
    parser.add_option('-l', '--list', action= 'store_true', default= True)
    parser.add_option('-a', '--add', type='string')
    parser.add_option('-r', '--remove', type='int')
    return parser.parse_args()

