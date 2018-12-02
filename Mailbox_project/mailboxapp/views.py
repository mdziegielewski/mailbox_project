from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.shortcuts import render, HttpResponse,redirect, HttpResponseRedirect
from .models import *
from django.db.models import Q


# Create your views here.





def person_data_validation(request, person):
    name = request.POST.get("name")
    surname = request.POST.get("surname")
    description = request.POST.get("description")
    person.name = name
    person.surname = surname
    person.description = description
    if name and surname:
        person.save()


class AddNewAddressView(View):
    def get(self,request,id):
        return render (request, "mailboxapp/add_address.html")

    def post(self,request,id):
        city = request.POST.get("city")
        street = request.POST.get("street")
        house_number = request.POST.get("house_number")
        flat_number = request.POST.get("flat_number")
        person_address = Person.objects.get(pk=id)

        Address.objects.create(city=city, street=street, house_number=house_number, flat_number=flat_number,
                            person_address=person_address)

        return redirect("modify", id=id)



class AddNewPhoneNumberView(View):
    def get(self, request, id):
        return render (request, "mailboxapp/add_phone.html")

    def post(self, request, id):
        phone_number = request.POST.get("phone_number")
        phone_type = request.POST.get("phone_type")
        person_phone = Person.objects.get(pk=id)

        result = Phone.objects.filter(phone_number=phone_number)

        if len(result) == 0:
            Phone.objects.create(phone_number = phone_number, phone_type = phone_type, person_phone = person_phone)
            return redirect("modify", id=id)
        else:
            return HttpResponse("Taki numer istnieje w bazie")



class AddNewEmailView(View):
    def get(self, request, id):
        return render (request,"mailboxapp/add_email.html")

    def post(self, request, id):
        email_address = request.POST.get("email_address")
        email_type = request.POST.get("email_type")
        person_email = Person.objects.get(pk=id)

        result = Email.objects.filter(email_address=email_address)

        if len(result) == 0:
            Email.objects.create(email_address=email_address, email_type=email_type, person_email=person_email)
            return redirect("modify", id=id)
        else:
            return HttpResponse("Taki adres email istnieje w bazie")






class AddNewPersonVeiw(View):   #dodawanie nowej osoby do bazy
    def get(self, request):
        return render (request, "mailboxapp/add_person.html")

    def post(self, request):
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        description = request.POST.get("description")

        Person.objects.create(name=" ".join(name.split()), surname=" ".join(surname.split()), description=" ".join(description.split()))
        return redirect("/main/")




class EditPersonView(View):
    def get(self,request, id):
        person = Person.objects.get(pk=id)
        address = Address.objects.all().filter(person_address_id=id)
        phone = Phone.objects.all().filter(person_phone_id=id)
        email = Email.objects.all().filter(person_email_id=id)
        groups = Groups.objects.all().filter(group_person=id)


        context = {
            'person' : person,
            'address': address,
            'phone' : phone,
            'email' : email,
            'groups' : groups,
        }
        return render (request, "mailboxapp/edit_person.html", context)

    def post(self,request,id):
        person_data_validation(request, Person.objects.get(pk=id))
        return redirect("/main/")




class DeletePersonView(View):
    def get(self,request,id):
        person = Person.objects.get(pk=id)

        context = {
            'person' : person
        }
        return render (request, "mailboxapp/delete_person.html", context)

    def post(self,request,id):
        if request.POST.get("decision") == "yes":
            person = Person.objects.get(pk=id)
            person.delete()
            return redirect("/main/")
        else:
            return redirect("/main/")



class DeleteAddressView(View):
    def get(self,request,id):
        person_id = Person.objects.get(pk=id)
        address = Address.objects.all().filter(person_address_id=id)

        context = {
            'address' : address,
        }
        return render (request, "mailboxapp/delete_address.html", context)

    def post(self,request,id):
        if request.POST.get("decision") == "yes":
            address_id = request.POST.get("addresses")
            person_id = Person.objects.get(pk=id)
            address = Address.objects.get(id=address_id)
            address.delete()

            return redirect("modify", id=id)
        else:
            return redirect("/main/")



class DeletePhoneNumberView(View):
    def get(self,request,id):
        person_id = Person.objects.get(pk=id)
        phone = Phone.objects.all().filter(person_phone_id=id)

        context = {
            'phone' : phone,
        }
        return render (request, "mailboxapp/delete_phone.html", context)

    def post(self,request,id):
        if request.POST.get("decision") == "yes":
            number_id = request.POST.get("phone")
            person_id = Person.objects.get(pk=id)
            phones = Phone.objects.get(id=number_id)
            phones.delete()
            return redirect("modify", id=id)
        else:
            return redirect("/main/")



class DeleteEmailAddressView(View):
    def get(self,request,id):
        person_id = Person.objects.get(pk=id)
        person_email_all = Email.objects.all().filter(person_email_id=id)

        context = {
            'person_email_all' : person_email_all,
        }
        return render (request, "mailboxapp/delete_email.html", context)

    def post(self,request,id):
        if request.POST.get("decision") == "yes":
            email_id = request.POST.get("email_addresses")
            person_id = Person.objects.get(pk=id)
            email = Email.objects.get(id=email_id)
            email.delete()
            return redirect("modify", id=id)
        else:
            return redirect("/main/")


class DeletePersonFromGroupView(View):
    def get(self,request,id):
        person_id = Person.objects.get(pk=id)
        person_groups_all = person_id.groups_set.all()

        context = {
            'person_groups_all' : person_groups_all,
        }
        return render(request, "mailboxapp/delete_person_from_group.html", context)

    def post(self,request,id):
        if request.POST.get("decision") == "yes":
            group_id = request.POST.get("person_from_group")
            person_id = Person.objects.get(pk=id)
            group = Groups.objects.get(id=group_id)
            group.group_person.remove(person_id)

            return redirect("modify", id=id)
        else:
            return redirect("/main/")



class DeleteGroupsView(View):
    def get(self,request):
        groups = Groups.objects.all()

        context = {
            'groups' : groups,
        }
        return render (request, "mailboxapp/delete_groups.html", context)

    def post(self,request):
        if request.POST.get("decision") == "yes":
            groups_id = request.POST.get("groups")
            groups = Groups.objects.get(pk=groups_id)
            groups.delete()
            return redirect("/main/")
        else:
            return redirect("/main/")



class ShowPersonView(View):
    def get(self,request,id):
        person = Person.objects.get(pk=id)
        person_address = Address.objects.all().filter(person_address_id=id)
        person_phone = Phone.objects.all().filter(person_phone_id=id)
        person_email = Email.objects.all().filter(person_email_id=id)
        person_groups = person.groups_set.all()



        context = {
            'person' : person,
            'person_address' : person_address,
            'person_phone' : person_phone,
            'person_email' : person_email,
            'person_groups' : person_groups,
        }
        return render (request, "mailboxapp/show_person.html", context)



class ShowPeopleView(View):
    def get(self,request):
        person = Person.objects.all()

        context = {
            'person' : person
        }
        return render(request, "mailboxapp/show_people.html", context)



class AddGroupsView(View):
    def get(self,request):
        return render (request, "mailboxapp/add_groups.html")

    def post(self,request):
        group_name = request.POST.get("group_name")

        result = Groups.objects.filter(group_name=group_name.capitalize())

        if len(result) == 0:
            base = Groups.objects.create(group_name=group_name.capitalize())
            base.save()
            return redirect("/main/")
        else:
            return HttpResponse("Taka grupa istnieje w bazie")




class AddGroupsPersonView(View):
    def get(self,request,id):
        person = Person.objects.get(pk=id)
        groups_all = Groups.objects.all()

        context = {
            'person' : person,
            'groups_all' : groups_all,
        }
        return render (request, "mailboxapp/add_groups_person.html", context)

    def post(self,request,id):
        person = Person.objects.get(pk=id)
        groups_id = request.POST.get("group_name_list")

        groups_pk = Groups.objects.get(pk=groups_id)
        groups_pk.group_person.add(Person.objects.get(pk=id))

        return redirect("modify", id=id)



class SearchBoxView(View):
    def get(self,request):
        groups_all = Groups.objects.all()
        context = {
            'groups_all': groups_all,
        }
        return render (request, "mailboxapp/search_box.html",context)

    def post(self,request):
        group_id = request.POST.get("group_name_list")
        group_pk = Groups.objects.get(pk=group_id)
        search = request.POST.get("search")

        group_person = list(group_pk.group_person.all().filter((Q(name=search) | Q(surname=search))))

        context = {
            'group_person' : group_person,
        }

        if group_person:
            return render (request, "mailboxapp/searched_people.html", context)
        else:
            return HttpResponse("Nie ma takiej osoby")
