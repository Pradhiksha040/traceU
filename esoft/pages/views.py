from django.shortcuts import render, redirect
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings


def root_page_view(request):
    return render(request, "pages/index.html")


def dynamic_pages(request, slug):

    # ======================
    # CONTACT PAGE
    # ======================
    if slug == "contact":

        if request.method == "POST":

            name = request.POST.get("name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            subject = request.POST.get("subject")
            message = request.POST.get("message")

            full_message = f"""
Name: {name}
Email: {email}
Phone: {phone}

Message:
{message}
"""

            try:
                send_mail(
                    subject=subject,
                    message=full_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=["info@prajai.com"],
                    fail_silently=False,
                )

                messages.success(request, "Message sent successfully!")

            except Exception as e:
                messages.error(request, f"Error sending email: {e}")

            return redirect("pages:dynamic_pages", slug="contact")

    # ======================
    # LOAD PAGE
    # ======================
    template_name = f"pages/{slug}.html"

    try:
        return render(request, template_name)

    except TemplateDoesNotExist:
        raise Http404(f"{template_name} not found")