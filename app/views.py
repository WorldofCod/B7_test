from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.models import Book
# Create your views here.

def home(request):
    if request.method == "POST":    
        book_title = request.POST.get("btitle")  #get -frontend madhun ghenya sathi
        book_author = request.POST.get("bauthor")
        book_price = request.POST.get("bprice")
        book_ispublished = request.POST.get("bpub")
        book_id = request.POST.get("bid")
        if not book_id:  #new entry in table
            # print(book_name, type(book_price), book_qty, book_is_published)
            if book_ispublished == "Yes":
                book_ispublished = True
            else:
                book_ispublished = False
            book_obj = Book(title=book_title,author=book_author,price=book_price,ispublished=book_ispublished)
            # book_obj= Book(name=book_name,price=float(book_price), qty=int(book_qty),is_published = book_is_published)
            book_obj.save()
            return redirect('show_books')
        else:
            book_obj = Book.objects.get(id=book_id)
            book_obj.title = book_title
            book_obj.author = book_author
            book_obj.price = book_price
            if book_ispublished == "Yes":
                book_ispublished = True
            else:
                book_ispublished = False
            book_obj.ispublished = book_ispublished
            book_obj.save()
            # return HttpResponse("Book updated successfully...!")
            return redirect("show_books")
    else:
            return render(request, "home.html")
        
def show_books(request):
    books = Book.objects.all()  # manager
    return render(request, "show_books.html", {"all_books": books})


def edit_book(request, pk):
    book_obj = Book.objects.get(id=pk)
    return render(request, "home.html", {"book": book_obj})


def hard_delete(request, pk):
    book_obj = Book.objects.get(id=pk)
    book_obj.delete()
    return redirect("show_books")


def book_restore(request,pk):
    book_obj = Book.objects.get(id=pk)
    book_obj.is_deleted = False
    book_obj.save()
    return redirect('show_books')

def active_books(request):
    books = Book.objects.filter(is_deleted=0)                        #later:# manager
    return render(request, "active_book.html", {"all_books": books})

def inactive_books(request):
    books = Book.objects.filter(is_deleted=1)   #jo deleted aahe 
    return render(request, "inactive_book.html", {"all_books": books})
    
    
    
# Class Based views
from django.views import View
class Home(View):
    def get(self,request):
        print("In get method")
        return HttpResponse("GET method",status=200)
    def post(self,request):
        print(request.POST)
        # ptitle = request.POST.get('title')
        # pauthor = request.POST.get('author')
        # pprice = request.POST.get('price')
        # pis_published = request.POST.get('is_published')
        # pis_deleted = request.POST.get('is_deleted')
        # print(ptitle,pauthor,pprice,pis_published,pis_deleted)
        # b_obj = Book(title=ptitle,author=pauthor,price=pprice,ispublished =pis_published,is_deleted=pis_deleted)
        # b_obj.save()
        print("In post method")
        return HttpResponse("POST method",status=201)
    def put(self,request):
        print("In put method")
        return HttpResponse("PUT method")
    def patch(self,request):
        print("In patch method")
        return HttpResponse("PATCH method")
    def delete(self,request):
        print("In delete method")
        return HttpResponse("DELTE method",status = 204)