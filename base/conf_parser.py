from configparser import ConfigParser


def config(filename='db.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    datebase = {}
    if parser.has_section(section):
        params = parser.items(section)
        for par in params:
            datebase[par[0]] = par[1]
        else:
            raise Exception('Section {0} is not found in the {1} file'.format(section, filename))
        return datebase
