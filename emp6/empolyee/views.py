from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, render_to_response


from.models import Registers,Employees,Leaves,Payments,Users,Admins


# def index(request):
# 	return render(request,'empolyee/index11.html')
def index(request):
	registers=Registers.objects.all()
	context={
	'registers':registers,
	}
	return render(request,'empolyee/index.html',context)


def detail(request,register_id):
	try:
		registers = Registers.objects.get(pk=register_id)
	except Registers.DoesNotExist:
		raise Http404("please Register .................")
	return render(request,'empolyee/detail.html',{'registers':registers})

def registers(request):
	return render(request,'empolyee/registers.html')

def registers1(request):
	return render(request,'empolyee/registers1.html')
def create1(request):
	registers=Registers.objects.all()
	context={
	'registers':registers,
	}
	for registers in registers:
		if (registers.em_name==request.POST['name'] and registers.em_father_mother_name==request.POST['em_father_mother_name'] and registers.em_dob==request.POST['em_dob']):
			a=registers.id
			print(a)
			registers = Registers.objects.get(pk=a)
			if(registers.em_type=="fulltime"):
				return render(request,'empolyee/fulltime1.html',{'registers':registers})
			elif(registers.em_type=="Parttime"):
				return render(request,'empolyee/parttime1.html',{'registers':registers})
			elif(registers.em_type=="intends"):
				return render(request,'empolyee/intends1.html',{'registers':registers})
			else:
				return render(request,'empolyee/index.html')
def join(request):
	id1=request.POST['idel']
	print(id1)
	registers = Registers.objects.get(pk=id1)
	a=registers.em_name
	a1=registers.em_dob
	a2=registers.em_address
	a3=registers.em_mobile
	a4=registers.em_email
	a5=registers.em_alternate_no
	a5=registers.em_type
	print(a,a1,a2,a3,a4,a5)
	employees = Employees(name =a,dob =a1,address=a2,mobile=a3,email=a4,alternate_no=a5,date_join=request.POST['DOB'],post=request.POST['sel'],type1=request.POST['Payrole'],dep=request.POST['Department'],remarks=request.POST['Remarks'])
	employees.save()
	return render(request,'empolyee/login.html')

def create(request):
    registers = Registers(em_name =request.POST['name'],em_father_mother_name =request.POST['em_father_mother_name'],em_dob=request.POST['em_dob'],em_address=request.POST['em_address'],em_aadher_number=request.POST['em_aadher_number'],em_mobile=request.POST['em_mobile'],em_email=request.POST['em_email'],em_alternate_no=request.POST['em_alternate_no'],em_type=request.POST['em_type'])
    registers.save()
    return redirect('/empolyee/registers1')

#log in empolyee
def signup(request):
	return render(request,'empolyee/signup.html')
def signup1(request):
	joins = Employees.objects.all()
	for registers in joins:
		if (registers.name==request.POST['name']):
			for registers in joins:
				if (registers.email==request.POST['em_email']):
					users = Users(name =request.POST['name'],email =request.POST['em_email'],username=request.POST['username'],password=request.POST['password'])
					users.save()
					return render(request,'empolyee/login.html')
	else:
		return render(request,'empolyee/signup.html')

  #   users = Users(name =request.POST['name'],email =request.POST['em_email'],username=request.POST['username'],password=request.POST['password'])
  #   users.save()
    # return redirect('/empolyee/login.html')

def login(request):
	return render(request,'empolyee/login.html')

def next(request):
	registers = Registers.objects.get(pk=register_id)
	context={
	'registers':registers,
	}
	print(registers)
	if(0==0):
		print("fullif")
		return render(request,'empolyee/index11.html',context)
  	# elif(person['Type']=="PARTTIME"):
   #  	print("partif")
   #  	return render(request,'empolyee/index11.html',context)
  	# else:
   #  	return render(request,'empolyee/index11.html',context
   	# employee = Empolyees(name =request.POST['name'],dob =request.POST['dob'],address=request.POST['em_dob'],mobile=request.POST['em_address'],email=request.POST['em_aadher_number'],alternate_no=request.POST['em_mobile'],date_join=request.POST['em_email'],post=request.POST['em_alternate_no'],type1=request.POST['em_type'],dep=request.POST['em_type'],remarks=request.POST['em_type'])
 #    employee.save()	


