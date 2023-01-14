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


def update_scholarship_request_entity(current_user, form_data, scholar_ship_request):
    keys_to_check = ['degree_year', 'age', 'financial_situation', 'parent_work', 'special_needs', 'tenant']
    if all(key in form_data for key in keys_to_check):
        scholar_ship_request.degree_year = int(form_data['degree_year'])
        scholar_ship_request.age = int(form_data['age'])
        scholar_ship_request.financial_situation = form_data['financial_situation']
        scholar_ship_request.parent_work = form_data['parent_work']
        scholar_ship_request.special_needs = form_data['special_needs']
        scholar_ship_request.tenant = form_data['tenant']
        scholar_ship_request.user_id = current_user
    else:
        raise ValueError('missing mandatory keys')
