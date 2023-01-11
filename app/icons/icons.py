from django.http import FileResponse


def get_student_user_icon(request):
    img = open(f'./app/icons/user-icon.png', 'rb')
    response = FileResponse(img)
    return response
