from rest_framework.serializers import ModelSerializer

from orders.models import SalesOrder

#серриализатор поможет принять все данные с сервака и преобразовать их в читаемый вид.ю
#для джсон в том числе
class OrderSerializer(ModelSerializer):

    class Meta:
        model = SalesOrder
        fields = ['amount', 'description']
        #meta class просто для описания полей