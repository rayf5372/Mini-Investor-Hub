from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer 
from .dao import MarketDataDAO

class HistoricalDataView(APIView):
    renderer_classes = [JSONRenderer]
    def get(self, request):
        tickers = request.query_params.getlist('tickers')
        start_date = request.query_params.get('start_date', '')
        end_date = request.query_params.get('end_date', '')
        
        dao = MarketDataDAO()
        data = dao.get_historical_data(tickers, start_date, end_date)
        
        return Response(data)
    
class RealtimeDataView(APIView):
    renderer_classes = [JSONRenderer]
    def get(self, request):
        tickers = request.query_params.getlist('tickers')
        
        dao = MarketDataDAO()
        data = dao.get_realtime_data(tickers)
        
        return Response(data)
    
class MetadataView(APIView):
    renderer_classes = [JSONRenderer]
    def get(self, request):
        tickers = request.query_params.getlist('tickers')
        
        dao = MarketDataDAO()
        data = dao.get_metadata(tickers)
        
        return Response(data)