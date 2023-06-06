from rest_framework import routers

from staff.api.views import DepartmentViewSet, StaffViewSet

router = routers.DefaultRouter()
router.register('staff', StaffViewSet)
router.register('departments', DepartmentViewSet)
