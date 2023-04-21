from django.urls import include, path
from rest_framework import routers
from school import views



router = routers.DefaultRouter()
router.register(r'students',views.StudentViewSet,basename='student')
router.register(r'enrollments',views.EnrollmentViewSet,basename='enrollment')
router.register(r'courses',views.CourseViewSet,basename='course')
router.register(r'levels',views.LevelViewSet,basename='level')

urlpatterns = [
    path('',include(router.urls)),
]