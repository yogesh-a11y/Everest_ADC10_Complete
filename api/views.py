from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from jobs.models import Jobs
import json

@csrf_exempt
def view_get_post_jobs(req):

    if req.method=="GET":
        db_jobs=Jobs.objects.all()
        all_jobs=list(db_jobs.values())
        print(all_jobs)
        return JsonResponse({
            "jobs":all_jobs
        })

    elif req.method=="POST":
        body=json.loads(req.body)
        current_job=Jobs.objects.create(jobs_name=body['job_name'],jobs_Title=body['job_Title'],jobs_description=body['job_description'],location=body['location'],salary=body['salary'])
        current_job.save()
        return JsonResponse({
            "message":"job Created",
            "job":{
                "id":current_job.id,
                "job_name":current_job.jobs_name,
                "job_Title":current_job.jobs_Title,
                "job_description":current_job.jobs_description,
                "location":current_job.location,
                "salary":current_job.salary
            }
        })

@csrf_exempt
def view_getByID_updateByID_deleteByID(req,ID):
    current_job=Jobs.objects.get(id=ID)
    if req.method=="GET":
        return JsonResponse({
            "job":{
                "id":current_job.id,
                "job_name":current_job.jobs_name,
                "job_Title":current_job.jobs_Title,
                "job_description":current_job.jobs_description,
                "location":current_job.location,
                "price":current_job.salary
            }
        })

    elif req.method=="PUT":
        body=json.loads(req.body)
        current_job.job_name=body['job_name']
        current_job.job_description=body['job_description']
        current_job.location=body['location']
        current_job.salary=body['salary']
        current_job.jobs_Title=body['jobs_Title']

        current_job.save()

        return JsonResponse({
            "message":"Updated job",
            "job":{
                "id":current_job.id,
                "job_name":current_job.jobs_name,
                "job_description":current_job.jobs_description,
                "location":current_job.location,
                "price":current_job.price
            }
        })

    elif req.method=="DELETE":
        current_job.delete()

        return JsonResponse({
            "message":"job Deleted",
            "item":{
                "id":current_job.id,
                "job_name":current_job.jobs_name,
                "job_description":current_job.jobs_description,
                "job_Title":current_job.jobs_Title,
                "location":current_job.location,
                "price":current_job.price
            }
        })

def pagination(req,pageNo,items):
    start=pageNo*items
    end=start+items

    if req.method=="GET":
        db_jobs=Jobs.objects.all()
        all_jobs=list(db_jobs.values())
        print(all_jobs[start:end])
        return JsonResponse({
            "jobs":all_jobs[start:end]
        })


