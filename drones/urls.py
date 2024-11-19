from django.urls import include, path
from rest_framework.routers import SimpleRouter
from drones import views

router = SimpleRouter()
router.register(r'drone-categories', views.DroneCategoryViewSet)
router.register(r'drones', views.DroneViewSet)
router.register(r'pilots', views.PilotViewSet)
router.register(r'competitions', views.CompetitionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('colecoes/', views.ColecaoListCreate.as_view(), name='colecao-list'),
    path('colecoes/<int:pk>/', views.ColecaoDetail.as_view(), name='colecao-detail'),
]
