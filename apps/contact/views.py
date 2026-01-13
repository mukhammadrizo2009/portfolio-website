from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactSerializer
from .telegram import send_telegram_message

class ContactAPIView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()
            
            message = (
                 "📩 > New Message | Your Personal Website<\n\n"
                f"👤 Name: {contact.name}\n"
                f"📧 Email: {contact.email}\n"
                f"📞 Whatsapp: {contact.whatsapp_number}\n"
                f"📎 Telegram: @{contact.telegram_username}\n\n"
                f"💬 Message:\n{contact.message}\n"
            )
            send_telegram_message(message)

            return Response(
                {'message': "Message sent succesfully!"},
                status=status.HTTP_201_CREATED
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)