from django.contrib import admin
from .models import LOS, Acknowledgement, CRPT
from import_export import resources

# Register your models here.

class LOSResouce(resources.ModelResource):
    class Meta:
        model = LOS
        fields = ('serial', 'ref', 'originator', 'sender', 'receiver_unit', 'date_of_rec', 'time_of_rec', 'datetime_of_action', 'action_taken_by', 'received_by', 'receiver_receiving_time', 'dispatched')
        export_order = ('serial', 'ref', 'originator', 'sender', 'receiver_unit', 'date_of_rec', 'time_of_rec', 'datetime_of_action', 'action_taken_by', 'received_by', 'receiver_receiving_time', 'dispatched')

class CRPTResouce(resources.ModelResource):
    class Meta:
        model = CRPT
        fields = ('serial', 'ref', 'originator', 'sender', 'receiver_unit', 'date_of_rec', 'time_of_rec', 'datetime_of_action', 'action_taken_by', 'received_by', 'receiver_receiving_time', 'group', 'security_grade', 'dispatched')
        export_order = ('serial', 'ref', 'originator', 'sender', 'receiver_unit', 'date_of_rec', 'time_of_rec', 'datetime_of_action', 'action_taken_by', 'received_by', 'receiver_receiving_time', 'group', 'security_grade', 'dispatched')

@admin.register(LOS)
class LOSAdmin(admin.ModelAdmin):
    list_display = ['serial', 'ref', 'originator', 'sender', 'written_by', 'date_of_rec', 'time_of_rec', 'datetime_of_action', 'action_taken_by', 'received_by_fun' , 'receiver_receiving_time', 'dispatched']

@admin.register(Acknowledgement)
class AcknowledgementAdmin(admin.ModelAdmin):
    list_display = ['date', 'time', 'ref', 'user']

@admin.register(CRPT)
class CRPTAdmin(admin.ModelAdmin):
    list_display = ['serial', 'ref', 'originator', 'sender', 'written_by', 'date_of_rec', 'time_of_rec', 'datetime_of_action', 'action_taken_by', 'received_by_fun' , 'receiver_receiving_time', 'group', 'security_grade', 'dispatched']