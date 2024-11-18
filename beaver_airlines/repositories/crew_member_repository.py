from beaver_airlines.models import CrewMember, Airplane
from django.core.exceptions import ObjectDoesNotExist

class CrewMemberRepository:

    @staticmethod
    def get_all():
        return CrewMember.objects.all()

    @staticmethod
    def get_by_id(crew_member_id):
        try:
            return CrewMember.objects.get(pk=crew_member_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def create(first_name, last_name, position=None, airplane_id=None):
        airplane = None
        if airplane_id:
            try:
                airplane = Airplane.objects.get(pk=airplane_id)
            except ObjectDoesNotExist:
                return None
        crew_member = CrewMember(first_name=first_name, last_name=last_name, position=position, airplane=airplane)
        crew_member.save()
        return crew_member

    @staticmethod
    def update(crew_member_id, **kwargs):
        try:
            crew_member = CrewMember.objects.get(pk=crew_member_id)
            for key, value in kwargs.items():
                setattr(crew_member, key, value)
            crew_member.save()
            return crew_member
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def delete(crew_member_id):
        try:
            crew_member = CrewMember.objects.get(pk=crew_member_id)
            crew_member.delete()
            return True
        except ObjectDoesNotExist:
            return False