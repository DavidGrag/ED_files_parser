import pygsheets
import config  # remove this!

# spreadsheetid = 'your_spreadsheet_id'
# service_file = 'path_to_your_service_json_file.json'

"""
1. How to get spreadsheet id
link example=>docs.google.com/spreadsheets/d/1txa5dHdG3Yv7kVIwgp1ZLAqNasdwdgsOXUtq5JkVERgrtsdgfxs/edit#gid=2623593171
copy the part of the link between /d/ and /
in this case it is ==> 1txa5dHdG3Yv7kVIwgp1ZLAqNasdwdgsOXUtq5JkVERgrtsdgfxs
2. How to get service file
Search in Google "Creation of service account google API for google sheets"
"""


def fill_sheet(sheet_name, data):
    """Fills google spreadsheet with files main data"""
    gc = pygsheets.authorize(service_file=config.service_file)
    sh = gc.open_by_key(config.test)
    try:
        sh.add_worksheet(sheet_name)
    except Exception as ex:
        print('Sheet exists!')
        print(ex)
        pass
    wks_write = sh.worksheet_by_title(sheet_name)
    wks_write.clear('A1', None, '*')
    wks_write.set_dataframe(data, (1, 1), encoding='utf-8', fit=True)
    wks_write.frozen_rows = 1
