from django.contrib import admin
from .models import FileData, File
import xlrd
from django.conf import settings
from django.contrib.auth.models import Group
admin.site.site_header = 'Excel Admin Dashboard'


class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'excelFile')
    list_filter = ('title',)
    change_form_template = 'admin/excel/admin_excelfile.html'

    def change_view(self, request, object_id, form_url='', extra_context=None):

        excel_file = File.objects.all()
        context = list()
        for i in excel_file:
            location = i.excelFile.url
            location = settings.BASE_DIR + location
            workbook = xlrd.open_workbook(location)
            sheet = workbook.sheet_by_index(0)
            sheet.cell_value(0, 0)
            num_rows = sheet.nrows
            num_cols = sheet.ncols
            for data in range(1, num_rows):
                for col in range(0, num_cols):
                    context.append(sheet.cell_value(data, col))
                y, m, d, h, i, s = xlrd.xldate_as_tuple(context[9], workbook.datemode)
                context[9] = "{0} - {1} - {2}".format(y, m, d)
                row_data = FileData(id=data, email_id=context[0], first_name=context[1], last_name=context[2], gender=context[3], address=context[4], city=context[5], state=context[6], ZIP=context[7], mobile=context[8], date_of_birth=context[9])
                row_data.save()
                context = []
        return super(FileAdmin, self).change_view(request, object_id, form_url, extra_context,)


admin.site.unregister(Group)
admin.site.register(File, FileAdmin)
admin.site.register(FileData)

# Register your models here.
