from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework import status
from .serializers import RegisterSerializer
from .services import send_otp_email
from .models import OTP

User = get_user_model()
# Create your views here.

class RegisterView(APIView):

    def post(self,request):
        serialInstance = RegisterSerializer(data = request.data)
        serialInstance.is_valid(raise_exception=True)
        serialInstance.save()

        return Response(
            {
                "message": "User registered successfully"
            }
        )
    

class ProfileView(APIView):
    permission_classed = [IsAuthenticated]

    def get(self,request):
       return Response({
           'email':request.user.email,
           'username':request.user.username
       })

class ForgetPasswordView(APIView):

    def post(self,request):
        email = request.data.get('email')

        if not User.objects.filter(email = email).exists():
            return Response({
                "error": "User not found"
            }, status=404)
        
        send_otp_email(email)

        return Response({
            'message': "OTP sent successfully"
        })
    
class ResetPasswordView(APIView):

    def post(self,request):
        email = request.data.get('email')
        newPassword = request.data.get('password')
        otp = request.data.get('otp')

        try:
            user = User.objects.get(email=email)

            otp_obj = OTP.objects.filter(user = user,code = otp).last()

            if not otp_obj:
                return Response({
                    "error": "Invalid OTP"
                },status=404)
            
            if otp_obj.is_expired():
                return Response({
                    'error':'OTP expired'
                },status=404)

            user.set_password(newPassword)
            user.save()

            otp_obj.delete()
            return Response({
                    "message": "Password reset successful"
                })

        except User.DoesNotExist:
            return Response({
                "error": "User not found"
            },status=404)
        
class DeleteAccountView(APIView):
    # This ensures only the logged-in user can delete their account
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        
        # Completely delete the user from PostgreSQL
        user.delete()
        
        return Response(
            {"message": "Your account has been permanently deleted."}, 
            status=status.HTTP_200_OK
        )


