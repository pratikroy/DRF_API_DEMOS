from jobs.models import JobBoard
from rest_framework import serializers
from datetime import datetime
from django.utils.timesince import timesince


class JobBoardSerializer(serializers.ModelSerializer):

    time_since_post = serializers.SerializerMethodField()

    class Meta:
        model = JobBoard
        fields = "__all__"

    def get_time_since_post(self, object):
        post_date = object.created_at
        current_date = datetime.now()
        time_delta = timesince(post_date, current_date)
        return time_delta

    # Object level validation
    def validate(self, data):
        if data['job_title'] == data['job_description']:
            raise serializers.\
            ValidationError("Title and description must be unique")
        return data

    # Field level validation
    def validate_company_name(self, value):
        if len(value) < 20:
            raise serializers.\
            ValidationError("Company name at least 20 chars long")
        return value
