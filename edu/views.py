from django.views.generic import View
from django.shortcuts import get_object_or_404, render, redirect
from .models import Feed
class Index(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)
    

class TagStudy(View):
    template_name = 'tag_study.html'

    def get(self, request):
        feeds = Feed.objects.all().order_by('id')
        print(f"feed size: {len(feeds)}")
        return render(request,self.template_name,{'feed_list':feeds})
    
class NewContent(View):
    template_name = 'upload_form.html'

    def get(self, request):
       return render(request, self.template_name)
        
    
    def post(self, request):
        age = request.POST.get('age','0')
        print(f'나이:{age}')
        age = int(age)

        pwd = request.POST.get('pwd','')
        print(f'비밀번호:{pwd}')

        tel = request.POST.get('phone','')
        print(f'전화번호:{tel}')

        param = request.POST.get('content','')
        param2 = request.FILES.get('up_photo', False)
        print(f'내용:{param}')
        
        feed = Feed(content = param, photo = param2)
        feed.save()

        return redirect('edu:tag_study')