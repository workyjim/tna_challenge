from local.models import LocalItem
from django.http.response import HttpResponse

# Create your views here.
def details(request, item_id):
    item = None

    try:
        item = LocalItem.objects.get(pk=item_id)
    except LocalItem.DoesNotExist:
        # item will remain none; no action required
        pass
    except Exception:
        # unexpected problem, throw up the stack
        raise

    if item is None:
        return HttpResponse("no record found", content_type="text/plain")
    else:
        return HttpResponse(str(item), content_type="text/plain")
