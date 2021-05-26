from django.urls    import path
from products.views import ProductListView, ProductDetailView, OrderHistory, SellBiddingDetail

urlpatterns = [
    path('', ProductListView.as_view()),
    path("/<int:product_id>", ProductDetailView.as_view()),
    path("/<int:product_id>/order", OrderHistory.as_view()),
    path("/<int:product_id>/sellbidding", SellBiddingDetail.as_view()),
]