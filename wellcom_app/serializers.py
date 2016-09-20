from rest_framework import serializers
from .models import Well, Note, DeviceData, Usage, WaterTest, Test, DeviceOutput


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ('id', 'well', 'title', 'text', 'created')


class DeviceDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceData
        fields = ('id', 'well', 'timestamp', 'temperature_c')


class UsageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usage
        fields = ('id', 'well', 'timestamp')


class WaterTestSerializer(serializers.ModelSerializer):

    class Meta:
        model = WaterTest
        fields = ('id', 'well', 'date', 'pH', 'turbidity_ntu',
                  'app_true_colour_hz',
                  'conductivity_uscm', 'temperature_c', 'total_iron',
                  'calcium', 'magnesium', 'chloride', 'sulphate',
                  'suspended_solids', 'total_dissolved_solids', 'total_solids',
                  'total_alkalinity', 'total_hardness', 'calcium_hardness',
                  'magnesium_hardness', 'copper', 'nitrite_nitrogen',
                  'nitrate_nitrogen', 'fluoride', 'mpn_index_tc_per_deciliter',
                  'ammonia_nitrogen', 'manganese', 'aluminum')


class WellSerializer(serializers.ModelSerializer):
    note_set = NoteSerializer(many=True, read_only=True)
    device_data_set = DeviceDataSerializer(many=True, read_only=True)
    usage_set = UsageSerializer(many=True, read_only=True)
    water_test_set = WaterTestSerializer(many=True, read_only=True)

    class Meta:
        model = Well
        fields = ('id', 'name', 'latitude', 'longitude', 'country',
                  'date_installed', 'last_update', 'note_set',
                  'device_data_set', 'usage_set', 'water_test_set')


class DeviceOutputSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceOutput
        fields = ('id', 'well', 'batt_voltage_mv', 'batt_percent_charged',
                  'adc_voltage_mv', 'start_time', 'end_time',
                  'temp_readings_c', 'reading_interval_s'
                  )


class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = ('id', 'text', 'timestamp')
