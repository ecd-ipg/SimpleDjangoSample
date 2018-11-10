from django.views import View
from django.shortcuts import render
from ecd_ipg_sample.models.ipg_demo_back import IpgDemoBack
from ecd_ipg_sample.request.ipg_request import get_token, submit_confirm, submit_reverse


class IpgDemoView(View):
    template_name = "ipg_demo.html"

    def get(self, request, *args, **kwargs):

        lang = request.GET.get('lang', "fa")

        return render(request, self.template_name, {
            'token': get_token(lang),
            'lang': lang
        })


class IpgDemoBackView(View):
    template_name = "ipg_demo_back.html"

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        ipg_demo_back = IpgDemoBack()
        ipg_demo_back.set_by_post(request.POST)

        if ipg_demo_back.state == '1':
            # Successful

            # STEP 1 :
            # FIND YOUR TRANSACTION RECORD BY YOUR BUY_ID or TOKEN
            # ipg_demo_back->buy_id
            # ipg_demo_back->token

            # STEP 2:
            # CHECK RETURNED AMOUNT (ipg_demo_back->amount) WITH YOUR RECORD AMOUNT
            # These two should be equal

            # NOW!!!

            # IF ALL IS OK
            # submit_confirm(ipg_demo_back)

            # ELSE
            # submit_reverse(ipg_demo_back)

            submit_confirm(ipg_demo_back)
        else:
            submit_reverse(ipg_demo_back)

        return render(request, self.template_name, {
            'ipg_demo_back': ipg_demo_back
        })