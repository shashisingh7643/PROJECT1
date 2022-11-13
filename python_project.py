from openpyxl.styles import Font
wb_obj=openpyxl.load_workbook("C:\\Users\\ABC\\Desktop\\Entry1pi.xlsx")
comp_name=input("Enter the company Name:")
title=input("Enter the title of the document:")
sheet_obj=wb_obj.active
sheet_obj.merge_cells("B2:E2")
sheet_obj['B2'].font=Font(bold=true,size=27)
sheet_obj['B2'].value=(comp_name)
sheet_obj['B3'].value=(title)
sheet_obj['B3'].font=Font(bold=true,size=20)
sheet_obj['A4']="Date"
sheet_obj['A4'].font=Font(bold=true,size=20)
sheet_obj['B4']="Bill No"
sheet_obj['B4'].font=Font(bold=true,size=20)
sheet_obj['C4']="Company Name"
sheet_obj['C4'].font=Font(bold=true,size=20)
sheet_obj['D4']="Amount"
sheet_obj['D4'].font=Font(bold=true,size=20)
no_of_entries=int(input("Enter the number of entries"))
for i in range(no_of_enteries):
    date=input("Date  "+str(i+1))
    bill_no=int(input("Bill "+str(i+1)))
    name_of_parcel=input("Name of parcel "+str(i+1))
    date=[['date','bill_no','name_of_parcel']]
    for d in data:
        sheet_obj.append(data)

wb_obj.save('Entry.xlsx')
print(type(wb_obj))
