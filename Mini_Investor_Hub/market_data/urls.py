from django.urls import path
from .views import RealtimeDataView, HistoricalDataView, MetadataView

urlpatterns = [
    path('realtime/', RealtimeDataView.as_view(), name='realtime_data'),
    path('history/', HistoricalDataView.as_view(), name='historical_data'),
    path('metadata/', MetadataView.as_view(), name='metadata'),
]