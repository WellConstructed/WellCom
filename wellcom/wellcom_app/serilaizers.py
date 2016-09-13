from rest_framework import serializers
from .models import Well, Note, DeviceData, Usage, WaterTest


class WellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Well
        fields = ('name', 'latitude', 'longitude', 'country', 'date_installed', 'last_update')


class NoteSerializer(serializers.ModelSerializer):
    well_set = WellSerializer(many=True, read_only=True)

    class Meta:
        model = Note
        fields = ('title', 'text', 'created', 'well_set')


class DeviceDataSerializer(serializers.ModelSerializer):
    well_set = WellSerializer(many=True, read_only=True)

    class Meta:
        model = DeviceData
        fields = ('timestamp', 'temperature_c', 'well_set')


class UsageSerializer(serializers.ModelSerializer):
    well_set = WellSerializer(many=True, read_only=True)

    class Meta:
        model = Usage
        fields = ('date', 'usage_count', 'well_set')


class WaterTestSerializer(serializers.ModelSerializer):
    well_set = WellSerializer(many=True, read_only=True)

    class Meta:
        model = WaterTest
        fields = ('date', 'pH', 'turbidity_ntu', 'app_true_colour_hz', 'conductivity_uscm', 'temperature_c', 'total_iron', 'calcium', 'magnesium', 'chloride', 'sulphate', 'suspended_solids', 'total_dissolved_solids', 'total_solids', 'total_alkalinity', 'total_hardness', 'calcium_hardness', 'magnesium_hardness', 'copper', 'nitrite_nitrogen', 'nitrate_nitrogen', 'fluoride', 'mpn_index_tc_per_deciliter', 'ammonia_nitrogen', 'manganese', 'aluminum')
