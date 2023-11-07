import gtable
import pandas as pd
from parserClass import Parser


links = {
        'Profiles': 'https://www.digitalcombatsimulator.com/ru/files/filter/type-is-profile/apply/?PER_PAGE=100&PAGEN_1=',
        'Utilities': 'https://www.digitalcombatsimulator.com/ru/files/filter/type-is-utility/apply/?PER_PAGE=100&PAGEN_1=',
        'Docs': 'https://www.digitalcombatsimulator.com/ru/files/filter/type-is-document/apply/?PER_PAGE=100&PAGEN_1=',
        'Sounds': 'https://www.digitalcombatsimulator.com/ru/files/filter/type-is-sound/apply/?PER_PAGE=100&PAGEN_1=',
        'Mods': 'https://www.digitalcombatsimulator.com/ru/files/filter/type-is-mod/apply/?PER_PAGE=100&PAGEN_1=',
        'Liveries': 'https://www.digitalcombatsimulator.com/ru/files/filter/type-is-skin/game-is-world/apply/?PER_PAGE=100&PAGEN_1='
        }


def main():

    for name, link in links.items():

        parser = Parser(link)
        parser.parsing(show_info=True)
        data = parser.data
        columns = ['NAME', 'LINK', 'AUTHOR', 'SIZE KB', 'DATE', 'DOWNLOADS', 'AIRCRAFT', 'VERSION', 'LICENSE']
        df = pd.DataFrame(data=data, columns=columns)
        gtable.fill_sheet(name, df)  # writes the data in google spreadsheet


if __name__ == '__main__':
    main()
    print('Done')
