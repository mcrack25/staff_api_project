from django import forms
from django_filters import rest_framework as filters

from staff.models import Department, Post, Staff


class StaffFilter(filters.FilterSet):
    post = filters.ModelMultipleChoiceFilter(
        field_name="post__title",
        queryset=Post.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        label="Должности",
        required=False,
    )
    department = filters.ModelMultipleChoiceFilter(
        field_name="department__title",
        queryset=Department.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        label="Подразделения",
        required=False,
    )
    fullname = filters.CharFilter(method="filter_by_fullname", label="ФИО")

    def filter_by_fullname(self, queryset, name, value):
        return queryset.filter(_fullname__icontains=value)

    class Meta:
        model = Staff
        fields = ["post", "department", "fullname"]


class DepartmentFilter(filters.FilterSet):
    title = filters.CharFilter(method="filter_by_title")

    class Meta:
        model = Department
        fields = {
            "title": ["exact"],
            "director": ["exact"],
        }

    def filter_by_title(self, queryset, name, value):
        return queryset.filter(title__icontains=value)
