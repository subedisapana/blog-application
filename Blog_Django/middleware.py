from django.shortcuts import redirect
from Blog.views import blog


class MyCustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user:
            if not request.user.is_authenticated and view_func == blog:
                return redirect('homepage')



