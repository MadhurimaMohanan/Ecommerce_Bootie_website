from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .models import P_admin,P_product,P_user,cart

# Create your views here.
class login_page(View):
    def get(self,request):
        return render(request,'admin/admin_login.html')

class login_func(View):
    def post(self,request):
        email=request.POST['email']
        password=request.POST['password']
        check=P_admin.objects.filter(email=email,password=password)
        if check:
            admin = check[0]
            request.session['adminid']=admin.id
            aid=request.session['adminid']
            adminid=P_admin.objects.get(id=aid)
            return HttpResponseRedirect('/products_table/')
        else:
            return render(request,'admin/admin_login.html')

class products_table(View):
    def get(self,request):
        products=P_product.objects.all()
        return render(request,'admin/products.html',{'products':products})

class add_product(View):
    def post(self,request):
        try:
            request.session['adminid']
            if 'adminid' in request.session:
                product_name=request.POST['product_name']
                try:
                    image=request.FILES['image']
                except:
                    image=False
                price=request.POST['price']
                myproduct=P_product()
                myproduct.product_name=product_name
                myproduct.image=image
                myproduct.price=price
                myproduct.save()
                return HttpResponseRedirect('/products_table/')
        except KeyError:
            pass
        print("Does not exist")
        return HttpResponseRedirect('/login_page/')


class update_product(View):
    def post(self,request):
        try:
            request.session['adminid']
            if 'adminid' in request.session:
                pid=request.POST['product_id']
                product_name=request.POST['product_name']
                try:
                    image=request.FILES['image']
                except:
                    image=False
                price=request.POST['price']
                myproduct=P_product.objects.get(id=pid)
                myproduct.product_name=product_name
                if image != False:
                    myproduct.image=image
                myproduct.price=price
                myproduct.save()
                return HttpResponseRedirect('/products_table/')
        except KeyError:
            pass
        print("Does not exist")
        return HttpResponseRedirect('/login_page/')

class delete_product(View):
    def post(self,request):
        try:
            request.session['adminid']
            if 'adminid' in request.session:
                pid=request.POST['product_id']
                myproduct=P_product.objects.all().get(id=pid)
                myproduct.delete()
                return HttpResponseRedirect('/products_table/')
        except KeyError:
            pass
        print("Does not exist")
        return HttpResponseRedirect('/login_page/')

def admin_logout(request):
    if request.session.has_key('adminid'):
        del request.session['adminid']
        return HttpResponseRedirect('/login_page/')
    else:
        return HttpResponseRedirect('/products_table/')

class index(View):
    def get(self,request):
        return render(request,'index.html')

class register(View):
    def get(self,request):
        return render(request,'register.html')

class login(View):
    def get(self,request):
        return render(request,'login.html')

class shop(View):
    def get(self,request):
        products=P_product.objects.all()
        return render(request,'shop.html',{'products':products})

class user_register(View):
    def post(self,request):
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        phone_no=request.POST['phone_no']
        check=P_user.objects.filter(email=email)
        if check:
            return render(request,'register.html',{'msg':'already registered'})
        else:
            user=P_user()
            user.name=name
            user.email=email
            user.password=password
            user.phone_no=phone_no
            user.save()
            return render(request,'login.html')

class user_login(View):
    def post(self,request):
        email=request.POST['email']
        password=request.POST['password']
        check=P_user.objects.filter(email=email,password=password)
        if check:
            user = check[0]
            request.session['userid']=user.id
            aid=request.session['userid']
            userid=P_user.objects.get(id=aid)
            return HttpResponseRedirect('/')
        else:
            return render(request,'login.html')

class cart_view(View):
    def get(self,request):
        uid=request.session['userid']
        userid=P_user.objects.get(id=uid)
        mycart=cart.objects.filter(user=userid)
        total_items = mycart.count()
        print(total_items)
        return render(request,'cart.html',{'mycart':mycart,'total_items' :total_items})

class add_cart(View):
    def post(self,request):
        uid=request.session['userid']
        userid=P_user.objects.get(id=uid)
        pid=request.POST['product_id']
        myproduct=P_product.objects.all().get(id=pid)
        check=cart.objects.filter(user=userid,product=myproduct)
        if check:
            return HttpResponseRedirect('/shop/',{'msg':'alreday added'})
        mycart=cart()
        mycart.user=userid
        mycart.product=myproduct
        mycart.save()
        return HttpResponseRedirect('/cart_view/')

class delete_cart(View):
    def post(self,request):
        uid=request.session['userid']
        userid=P_user.objects.get(id=uid)
        cid=request.POST['cart_id']
        mycart=cart.objects.get(id=cid)
        mycart.delete()
        return HttpResponseRedirect('/cart_view/')


def user_logout(request):
    if request.session.has_key('userid'):
        del request.session['userid']
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
        
        





