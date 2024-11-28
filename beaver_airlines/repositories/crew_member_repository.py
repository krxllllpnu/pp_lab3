from beaver_airlines.models import CrewMember, Airplane
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count

class CrewMemberRepository:
    @staticmethod
    def get_crew_members_with_most_airplanes():
        return CrewMember.objects.annotate(
            airplane_count=Count('airplane_id')
        ).filter(
            airplane_count__gt=0
        ).order_by('-airplane_count').values(
            'crew_member_id',
            'first_name',
            'last_name',
            'position',
            'airplane_count'
        )

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