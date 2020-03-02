from profile_app.viewsets import DetailViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user',DetailViewset)
