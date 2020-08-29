from django.contrib import admin

# Register your models here.
from .models import  Quarterback,Runningback,Widereceiver,Tightend,Defense,Kicker,Player,Roster
from import_export.admin import ImportExportModelAdmin

@admin.register(Quarterback)
class QuarterbacksAdmin(ImportExportModelAdmin):
    list_display = ('name','team','position','Bye_Week','Projected_FPTS','Projected_OUTLOOK')


@admin.register(Runningback)
class RunningbackAdmin(ImportExportModelAdmin):
    list_display = ('name', 'team', 'position', 'bye_week','projected_fpts', 'projected_OUTLOOK')


@admin.register(Widereceiver)
class WidereceiverAdmin(ImportExportModelAdmin):
    list_display = ('name', 'team', 'position', 'bye_week','projected_fpts', 'projected_OUTLOOK')


@admin.register(Tightend)
class TightendAdmin(ImportExportModelAdmin):
    list_display = ('name', 'team', 'position', 'bye_week','projected_fpts','projected_OUTLOOK')

@admin.register(Defense)
class DefenseAdmin(ImportExportModelAdmin):
    list_display = ('team','bye_week','projected_fpts')

@admin.register(Kicker)
class KickerAdmin(ImportExportModelAdmin):
    list_display = ('name', 'team', 'position', 'bye_week', 'projected_fpts')



@admin.register(Player)
class KickerAdmin(ImportExportModelAdmin):
    list_display = ('name', 'team', 'position', 'bye_week')

admin.site.register(Roster)
