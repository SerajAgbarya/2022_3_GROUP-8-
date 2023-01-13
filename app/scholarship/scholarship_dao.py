from app.models import ScholarshipRequest


def get_scholarship_request(current_user):
    res = ScholarshipRequest.objects.filter(user_id=current_user)
    if len(res) == 0:
        return None
    return res[0]


def get_or_create_scholar_ship_request(current_user):
    sc = get_scholarship_request(current_user)
    if sc is None:
        return create_scholarship_request()
    return sc


def have_approved_request(current_user):
    request = get_scholarship_request(current_user)
    if request is not None:
        return request.status == ScholarshipRequest.APPROVED
    return False


def create_scholarship_request():
    return ScholarshipRequest()
