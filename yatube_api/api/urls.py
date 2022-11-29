from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views
from api.views import PostViewSet, CommentViewSet, GroupViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"posts/(?P<post_id>\d+)/comments", CommentViewSet,
                basename="comments")
router.register(r"groups", GroupViewSet)

urlpatterns = [
    path("v1/", include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
