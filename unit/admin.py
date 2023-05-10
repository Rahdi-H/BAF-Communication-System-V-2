from django.contrib import admin
from .models import LOS, Acknowledgement, CRPT, DispAck
from import_export import resources

# Register your models here.

class LOSResouce(resources.ModelResource):
    class Meta:
        model = LOS
        fields = ('serial', 'ref', 'sender', 'receiver_unit', 'date_of_rec', 'time_of_rec', 'datetime_of_action', 'action_taken_by', 'received_by', 'receiver_receiving_time', 'dispatched_to')
        export_order = ('serial', 'ref', 'originator', 'sender', 'receiver_unit', 'date_of_rec', 'time_of_rec', 'datetime_of_action', 'action_taken_by', 'received_by', 'receiver_receiving_time', 'dispatched_to')

class CRPTResouce(resources.ModelResource):
    class Meta:
        model = CRPT
        fields = ('serial', 'ref', 'sender', 'receiver_unit', 'date_of_rec', 'time_of_rec', 'datetime_of_action', 'action_taken_by', 'received_by', 'receiver_receiving_time', 'group', 'security_grade', 'dispatched_to')
        export_order = ('serial', 'ref', 'sender', 'receiver_unit', 'date_of_rec', 'time_of_rec', 'datetime_of_action', 'action_taken_by', 'received_by', 'receiver_receiving_time', 'group', 'security_grade', 'dispatched_to')

@admin.register(LOS)
class LOSAdmin(admin.ModelAdmin):
    list_display = ['serial', 'ref', 'sender', 'written_by', 'date_of_rec', 'time_of_rec', 'datetime_of_action', 'action_taken_by', 'received_by_fun' , 'receiver_receiving_time', 'dispatched_to_fun']

@admin.register(CRPT)
class CRPTAdmin(admin.ModelAdmin):
    list_display = ['serial', 'ref', 'sender', 'written_by', 'date_of_rec', 'time_of_rec', 'datetime_of_action', 'action_taken_by', 'received_by_fun' , 'receiver_receiving_time', 'group', 'security_grade', 'dispatched_to_fun']

@admin.register(Acknowledgement)
class AcknowledgementAdmin(admin.ModelAdmin):
    list_display = ['date', 'time', 'ref', 'user']

@admin.register(DispAck)
class DispAckAdmin(admin.ModelAdmin):
    list_display = ['ref', 'user', 'rec_office']