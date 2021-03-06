from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, FormView, RedirectView
from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy

from customauth.models import User
from customauth.forms import UserCreationForm
from api.models import Token
from api.solvers import ipopt

from urllib.parse import urlencode
from urllib.request import Request, urlopen

class Index(TemplateView):
    template_name = 'webinterface/index.html'
	
class RegisterView(CreateView):
	form_class = UserCreationForm
	model = User
	template_name = 'webinterface/register.html'
	success_url = reverse_lazy('webinterface:dashboard')
	
	def form_valid(self, form):
		valid = super(RegisterView, self).form_valid(form)
		email, password = form.cleaned_data.get('email'), form.cleaned_data.get('password1')
		user = authenticate(email=email, password=password)
		login(self.request, user)
		return valid
	
class LoginView(FormView):
	form_class = AuthenticationForm
	template_name = 'webinterface/login.html'
	
	success_url = reverse_lazy('webinterface:dashboard')
	
	def form_valid(self, form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)
	
		if user is not None and user.is_active:
			# login the user
			login(self.request, user)
			
			return super(LoginView, self).form_valid(form)
		else:
			return self.form_invalid(form)
			
class LogoutView(RedirectView):
	url = reverse_lazy('webinterface:index')

	def get(self, request, *args, **kwargs):
		logout(request)
		return super(LogoutView, self).get(request, *args, **kwargs)
		
class DashboardView(TemplateView):
	template_name = 'webinterface/dashboard.html'

	def get(self,request):
		tokens = Token.objects.filter(user=request.user)
		
		context = {}
		context['tokens'] = tokens
		context['problem'] = '{\n\t"variables":[\n\t\t"x[j] for j in range(4)"\n\t],\n\t"parameters": [\n\t\t"A = 25",\n\t\t"B = 40",\n\t\t"C = 1",\n\t\t"D = 5"\n\t],\n\t"objective":\n\t\t"x[0]*x[3]*(x[0]+x[1]+x[2])+x[2]",\n\t"constraints":[\n\t\t"x[0]*x[1]*x[2]*x[3] >= A",\n\t\t"x[0]**2+x[1]**2+x[2]**2+x[3]**2 = B",\n\t\t"x[j] >= C for j in range(4)",\n\t\t"x[j] <= D for j in range(4)"\n\t]\n}'
		context['response'] = ''
		
		return render(request,self.template_name,context)
		
	def post(self,request):
		context = {}
		
		# get the problem from the request
		token = request.POST['token']
		json_problem = request.POST['problem']

		# call the solver
		response = ipopt(token,json_problem)
		
		tokens = Token.objects.filter(user=request.user)
		
		context = {}
		context['tokens'] = tokens
		context['problem'] = json_problem
		context['response'] = response
		
		return render(request,self.template_name,context)
