from rest_framework import serializers

from staff.models import Department, Post, Staff


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title"]


class DepartmentSerializer(serializers.ModelSerializer):
    count_staff = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ["id", "title", "count_staff"]

    def get_count_staff(self, obj):
        return obj.staff_set.count()


class StaffSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    department = DepartmentSerializer()

    class Meta:
        model = Staff
        fields = ["id", "fullname", "photo", "post", "salary", "department", "age"]
