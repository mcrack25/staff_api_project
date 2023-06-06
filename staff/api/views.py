from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from staff.api.filters import DepartmentFilter, StaffFilter
from staff.api.paginators import StandardResultsSetPagination
from staff.api.serializers import DepartmentSerializer, StaffSerializer
from staff.models import Department, Staff


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    filterset_class = StaffFilter
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination


class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filterset_class = DepartmentFilter

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="director",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Director ID",
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
