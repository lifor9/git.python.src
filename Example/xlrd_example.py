# coding=utf-8
import xlrd
import calendar


# workbook = xlrd.open_workbook(filename)
#
# print workbook.sheet_name()  # 시트목록을 출력(list형식)
#
# worksheet_name = workbook.sheet_by_name(sheetname)  # 시트이름으로 시트 가져오기
# worksheet_index = workbook.sheet_by_index(index)  # 시트번호(인덱스)로 시트 가져오기
#
# num_rows = worksheet_name.nrows  # 줄 수 가져오기
# num_cols = worksheet_name.ncols  # 칸 수 가져오기
#
# row_val = worksheet_name.row_values(row_index)  # 줄 값 가져오기(list형식)
# cell_val = worksheet_name.cell_value(row_index, cell_index)  # 셀 값 가져오기

#workbook = xlrd.open_workbook('example.xls')
#worksheet = workbook.sheet_by_index(0)
#nrows = sheet.nrows
#
#row_val = []
#for row_num in range(nrows):
#    row_val.append(worksheet.row_values(row_num))

print (calendar.calendar(2019))