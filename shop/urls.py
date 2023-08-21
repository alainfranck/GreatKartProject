from django.urls import path
from . import views
urlpatterns = [
    path('vente/', views.vente, name='vente'),
    path('promotion/', views.promotion, name='promotion'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('chimique/', views.chimique, name='chimique'),
    path('habitation/', views.habitation, name='habitation'),
    path('bureau/', views.bureau, name='bureau'),
    path('commerce/', views.commerce, name='commerce'),
    path('hotel/', views.hotel, name='hotel'),
    path('entrepot/', views.entrepot, name='entrepot'),
    path('chantier/', views.chantier, name='chantier'),
    path('hopital/', views.hopital, name='hopital'),
    path('ecole/', views.ecole, name='ecole'),
    path('obligation/', views.obligation, name='obligation'),
    path('interdiction/', views.interdiction, name='interdiction'),
    path('faq/', views.faq, name='faq'),
    path('danger/', views.danger, name='danger'),
    path('interdiction/', views.interdiction, name='interdiction'),
    # detail secusigne
    path('detail-secusigne/<str:slug>', views.detailSecusigne, name="detail-secusigne"),
    
    path('guide/', views.guide, name='guide'),
    path('detail-guide/<str:slug>', views.detailGuide, name="detail-guide"),
    
    # get all orders
    path('orders-all/', views.get_orders, name='orders'), 
    ]