from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        email_body = f"""
New Contact Message

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}
"""

        mail = EmailMessage(
            subject=subject or "New Contact Message",
            body=email_body,
            from_email=email,  # user email
            to=[settings.DEFAULT_FROM_EMAIL],  # your email
        )

        mail.send(fail_silently=False)

        # ✅ Redirect after POST (VERY IMPORTANT)
        return redirect("/?success=1")

    return render(request, "index.html")
