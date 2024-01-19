# selinux/serializers.py

from rest_framework import serializers
from .models import Selinux, SElinuxEvent, SetroubleshootEntry, message, suggestion


class SElinuxEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = SElinuxEvent
        fields = ['digest', 'hostname', 'event', 'date', 'time', 'serial_num', 'event_kind', 'session', 'subj_prime', 'subj_sec', 'subj_kind', 'action', 'result', 'obj_prime', 'obj_sec', 'obj_kind', 'how']

class SelinuxDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selinux
        fields = ['hostname', 'detected', 'updated', 'status', 'mount', 'rootdir', 'policyname', 'current_mode', 'configured_mode', 'mslstatus', 'memprotect', 'maxkernel', 'total', 'preventions', 'messages']
        
#    hostname = models.CharField(max_length=128, primary_key=True)
#   detected = models.DateField()
#   updated = models.DateField()
#    status = models.CharField(max_length=50, default='active')
#    mount = models.CharField(max_length=50, blank=True, null=True)
#    rootdir = models.CharField(max_length=50, blank=True, null=True)
#    policyname = models.CharField(max_length=50, blank=True, null=True)
#    current_mode = models.CharField(max_length=50, blank=True, null=True)
#    configured_mode = models.CharField(max_length=50, blank=True, null=True)
#    mslstatus = models.CharField(max_length=50, blank=True, null=True)
#    memprotect = models.CharField(max_length=50, blank=True, null=True)
#    maxkernel = models.CharField(max_length=50,  blank=True, null=True)
#    total = models.CharField(max_length=50, blank=True, null=True)
#    preventions = models.CharField(max_length=50, blank=True, null=True)
#    messages = models.CharField(max_length=50, blank=True, null=True)

class SetroubleshootEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = SetroubleshootEntry
        fields = '__all__'

class messageSerializer(serializers.ModelSerializer):
    class Meta:
        model = message
        fields = '__all__'
class suggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = suggestion
        fields = '__all__'

class SelinuxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selinux
        fields = '__all__'