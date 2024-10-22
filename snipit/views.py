from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import hashlib
from .models import URL

@csrf_exempt
def shorten_url(request):
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        
        # Generate MD5 hash
        short_url_hash = hashlib.md5(original_url.encode()).hexdigest()[:6]
        
        # Check if short_url already exists
        url_obj, created = URL.objects.get_or_create(
            original_url=original_url,
            defaults={
                'short_url': short_url_hash,
                'expiry_date': timezone.now() + timezone.timedelta(days=30)
            }
        )
        
        response_data = {
            'original_url': original_url,
            'short_url': request.build_absolute_uri(f'/{url_obj.short_url}/'),
            'expiry_date': url_obj.expiry_date
        }
        return JsonResponse(response_data)

    return JsonResponse({'error': 'POST request required.'}, status=405)


@csrf_exempt
def redirect_url(request, short_url):
    url = get_object_or_404(URL, short_url=short_url)

    # Check if the URL is expired
    if url.expiry_date < timezone.now():
        return JsonResponse({'error': 'This URL has expired.'}, status=410)
    
    # Increment hit count
    url.hit_count += 1
    url.save()

    # Redirect to the original URL
    return redirect(url.original_url)