import graphene
from graphene_django import DjangoObjectType


from .models import Course


class CourseType(DjangoObjectType):
    class Meta:
        model = Course
        exclude = ()


class Query(graphene.ObjectType):
    courses = graphene.List(CourseType)
    course_by_id = graphene.Field(CourseType, id=graphene.Int()) # arugment must be declared here 

    def resolve_courses(self, info):
        return Course.objects.all()

    def resolve_course_by_id(self, info, id):
        try:
            course = Course.objects.get(id=id)
            return course 

        except Exception as e:
            return Exception(f"Error: {str(e)}")


class CreateCourse(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String()
        language = graphene.String(default_value="English")
        price = graphene.Int()
        currency = graphene.String(default_value="NPR")

    ok = graphene.Boolean()
    course = graphene.Field(CourseType)

    def mutate(self, info, title, description, language, price, currency):
        try: 
            course = Course.objects.create(
                title=title,
                description=description,
                language=language,
                price=price,
                currency=currency
            )
            return CreateCourse(course=course, ok=True)
        except Exception:
            return CreateCourse(course=None, ok=False)

class Mutation(graphene.ObjectType):
    create_course = CreateCourse.Field()