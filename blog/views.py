from django.shortcuts import render
from .models import Post
# Create your views here.
def post_list(request):
	return render(request,"blog/post_list.html",{'all_posts':Post.objects.all()})