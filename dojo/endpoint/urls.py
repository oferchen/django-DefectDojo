from django.conf.urls import url

from dojo.endpoint import views

urlpatterns = [
    # endpoints
    url(r'^endpoint$', views.all_endpoints,
        name='endpoint'),
    url(r'^endpoint/host$', views.all_endpoint_hosts,
        name='endpoint_host'),
    url(r'^endpoint/vulnerable$', views.vulnerable_endpoints,
        name='vulnerable_endpoints'),
    url(r'^endpoint/host/vulnerable$', views.vulnerable_endpoint_hosts,
        name='vulnerable_endpoint_hosts'),
    url(r'^endpoint/(?P<eid>\d+)$', views.view_endpoint,
        name='view_endpoint'),
    url(r'^endpoint/host/(?P<eid>\d+)$', views.view_endpoint_host,
        name='view_endpoint_host'),
    url(r'^endpoint/(?P<eid>\d+)/edit$', views.edit_endpoint,
        name='edit_endpoint'),
    url(r'^endpoints/(?P<pid>\d+)/add$', views.add_endpoint,
        name='add_endpoint'),
    url(r'^endpoint/(?P<eid>\d+)/delete$', views.delete_endpoint,
        name='delete_endpoint'),
    url(r'^endpoints/add$', views.add_product_endpoint,
        name='add_product_endpoint'),
    url(r'^endpoint/(?P<eid>\d+)/add_meta_data$', views.add_meta_data,
        name='add_endpoint_meta_data'),
    url(r'^endpoint/(?P<eid>\d+)/edit_meta_data$', views.edit_meta_data,
        name='edit_endpoint_meta_data'),
    url(r'^endpoint/bulk$', views.endpoint_bulk_update_all,
        name='endpoints_bulk_all'),
    url(r'^product/(?P<pid>\d+)/endpoint/bulk_product$', views.endpoint_bulk_update_all,
        name='endpoints_bulk_update_all_product'),
    url(r'^endpoint/(?P<fid>\d+)/bulk_status$', views.endpoint_status_bulk_update,
        name='endpoints_status_bulk'),
    url(r'^endpoint/migrate$', views.migrate_endpoints_view,
        name='endpoint_migrate'),
]