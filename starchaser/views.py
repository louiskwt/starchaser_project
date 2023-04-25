from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['links'] = [
            {
                "url": "https://www.instagram.com/hk.starchaser/",
                "title": "我的 IG Page",
                "color":  "orange",
            },
            {
                "url": "https://www.youtube.com/@dsestarchaser/featured",
                "title": "我的 YouTube  頻道",
                "color":  "green",
            },
            {
                "url": "https://portal.dsestarchaser.me",
                "title": "學生登入",
                "color":  "yellow", 
            }
        ]
        return context