import base64

from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404
from rest_framework import status, serializers
from rest_framework.response import Response

from recipes.models import Ingredient, RecipeIngredient
from users.models import Subscription


class Base64ImageField(serializers.ImageField):
    """Кастомное поле для изображений."""

    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


def create_ingredients(ingredients, recipe):
    """Вспомогательная функция для cоздания ингредиентов."""
    ingredient_list = []

    for ingredient in ingredients:
        current_ingredient = get_object_or_404(Ingredient,
                                               id=ingredient.get('id'))
        amount = ingredient.get('amount')
        ingredient_list.append(
            RecipeIngredient(
                recipe=recipe,
                ingredient=current_ingredient,
                amount=amount
            )
        )
    RecipeIngredient.objects.bulk_create(ingredient_list)


def create_model_instance(request, instance, serializer_name):
    """Вспомогательная функция для добавления рецепта."""
    serializer = serializer_name(
        data={'user': request.user.id, 'recipe': instance.id, },
        context={'request': request}
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


def delete_model_instance(request, model_name, instance, error_message):
    """Вспомогательная функция для удаления рецепта."""
    if not model_name.objects.filter(user=request.user,
                                     recipe=instance).exists():
        return Response({'errors': error_message},
                        status=status.HTTP_400_BAD_REQUEST)

    model_name.objects.filter(user=request.user, recipe=instance).delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


def check_request(self, obj, model):
    """Проверяем, что request есть, user не аноним."""
    request = self.context.get('request')

    if not request or request.user.is_anonymous:
        return False

    if model == Subscription:
        return model.objects.filter(user=request.user, author=obj.id).exists()

    return model.objects.filter(recipe=obj, user=request.user).exists()
