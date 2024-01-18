from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework import status
from .models import CarModel
from .serializers import CarSerializer


# class CarsView(APIView):
#     def get(self, *args, **kwargs):
#         return Response({"message": "Hello from get"})
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         pk = kwargs['pk']
#         print(pk)
#         print(data)
#         print(self.request.query_params.dict())
#         return Response({"message": "Hello from post"})
#
#     def put(self, *args, **kwargs):
#         return Response({"message": "Hello from put"})
#
#     def patch(self, *args, **kwargs):
#         return Response({"message": "Hello from patch"})
#
#     def delete(self, *args, **kwargs):
#         return Response({"message": "Hello from delete"})

# CRUD
# class CarsListCreateView(APIView):
#     def get(self, *args, **kwargs):
#         cars = CarModel.objects.all()
#         res = [model_to_dict(item) for item in cars]
#         return Response(res)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         car = CarModel.objects.create(**data)
#         car_dict = model_to_dict(car)
#         print(car_dict)
#         return Response(car_dict)
#
#
# class CarsRetrieveUpdateDestroyView(APIView):
#     def get(self, *args, **kwargs):
#         pk = kwargs['pk']
#         try:
#             car = CarModel.objects.get(pk=pk)
#         except CarModel.DoesNotExist:
#             raise Http404()
#         car_dict = model_to_dict(car)
#         return Response(car_dict)
#
#     def put(self, *args, **kwargs):
#         pk = kwargs['pk']
#         try:
#             car = CarModel.objects.get(pk=pk)
#         except CarModel.DoesNotExist:
#             raise Http404()
#         data = self.request.data
#         car.brand = data['brand']
#         car.price = data['price']
#         car.year = data['year']
#         car.save()
#         to_dict = model_to_dict(car)
#         return Response(to_dict)
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs['pk']
#         try:
#             car = CarModel.objects.get(pk=pk)
#             car.delete()
#         except CarModel.DoesNotExist:
#             raise Http404()
#
#         return Response('deleted')

class CarsListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        # print(dict(serializer.validated_data))
        # car = CarModel.objects.create(**data)
        # car_dict = model_to_dict(car)
        # print(car_dict)
        return Response(serializer.data, status.HTTP_201_CREATED)


class CarsRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()
        serializer = CarSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()
        data = self.request.data
        serializer = CarSerializer(car, data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_200_OK)

        serializer.save()
        return Response(serializer.data)

    def patch(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()
        data = self.request.data
        serializer = CarSerializer(car, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
            car.delete()
        except CarModel.DoesNotExist:
            raise Http404()

        return Response(status=status.HTTP_204_NO_CONTENT)
