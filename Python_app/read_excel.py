from xlrd import open_workbook

class Process(object):
    def __init__(self, ID, Name, Owner, Definition, Input, Extract, POC, QC, PCOMAS, Past_issues):
        self.ID = ID
        self.Name = Name
        self.Owner = Owner
        self.Definition = Definition
        self.Input = Input
        self.Extract = Extract
        self.POC = POC
        self.QC = QC
        self.PCOMAS = PCOMAS
        self.Past_issues = Past_issues

    def __str__(self):
        return("Process object:\n"
               "  Process_id = {0}\n"
               "  Name = {1}\n"
               "  Owner = {2}\n"
               "  Definition = {3}\n"
               "  InputFiles = {4}\n"
               "  Extract = {5}\n"
               "  POC = {6}\n"
               "  QC = {7}\n"
               "  PCOMAS = {8}\n"
               "  Past Issues = {9}\n"
               .format(self.ID, self.Name, self.Owner, self.Definition, self.Input, self.Extract, self.POC, self.QC, self.PCOMAS, self.Past_issues))

wb = open_workbook('/Users/Har/Downloads/input.xlsx')
for sheet in wb.sheets():
    number_of_rows = sheet.nrows
    number_of_columns = sheet.ncols

    items = []

    rows = []
    for row in range(1, number_of_rows):
        values = []
        for col in range(number_of_columns):
            value  = (sheet.cell(row,col).value)
            print value
            try:
                value = str(int(value))
            except ValueError:
                pass
            finally:
                values.append(value)
        item = Process(*values)
        items.append(item)
