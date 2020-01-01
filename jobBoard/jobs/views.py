from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from jobs.models import JobBoard
from jobs.serializers import JobBoardSerializer

# Create your views here.
class JobListCreateApiView(APIView):

    def get(self, request):
        jobs = JobBoard.objects.filter(is_available=True)
        serializer = JobBoardSerializer(jobs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobBoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobDetailApiView(APIView):

    def get_object(self, pk):
        job = get_object_or_404(JobBoard, pk=pk)
        return job

    def get(self, request, pk):
        job = self.get_object(pk)
        serializer = JobBoardSerializer(job)
        return Response(serializer.data)

    def put(self, request, pk):
        job = self.get_object(pk)
        serializer = JobBoardSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        job = self.get_object(pk)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
