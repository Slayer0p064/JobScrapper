import requests
from django.http import JsonResponse
from .models import Job

def fetch_and_save_jobs(request):
    # API URL
    url = "https://job-search-api.svc.dhigroupinc.com/v1/dice/jobs/search"

    # Query parameters
    params = {
        "q": "Software",
        "countryCode2": "US",
        "radius": 30,
        "radiusUnit": "mi",
        "page": 1,
        "pageSize": 20,
        "facets": "employmentType|postedDate|workFromHomeAvailability|workplaceTypes|employerType|easyApply|isRemote|willingToSponsor",
        "filters.workplaceTypes": "Remote",
        "filters.employmentType": "CONTRACTS",
        "filters.postedDate": "ONE",
        "currencyCode": "USD",
        "fields": "id|jobId|guid|summary|title|postedDate|modifiedDate|jobLocation.displayName|detailsPageUrl|salary|clientBrandId|companyPageUrl|companyLogoUrl|companyLogoUrlOptimized|positionId|companyName|employmentType|isHighlighted|score|easyApply|employerType|workFromHomeAvailability|workplaceTypes|isRemote|debug|jobMetadata|willingToSponsor",
        "culture": "en",
        "recommendations": "true",
        "interactionId": 0,
        "fj": "true",
        "includeRemote": "true"
    }

    # Headers
    headers = {
        "x-api-key": "1YAt0R9wBg4WfsF9VB2778F5CHLAPMVW3WAZcKd8"
    }

    try:
        # Fetch data from API
        response = requests.get(url, headers=headers, params=params)
        jobs_data = response.json().get("data", [])

        # Save jobs to database
        for job in jobs_data:
            Job.objects.update_or_create(
                job_id=job.get("jobId"),
                defaults={
                    "title": job.get("title"),
                    "company_name": job.get("companyName"),
                    "location": job.get("jobLocation", {}).get("displayName"),
                    "posted_date": job.get("postedDate"),
                    "details_url": job.get("detailsPageUrl"),
                    "salary": job.get("salary"),
                    "location_type": ",".join(job.get("workplaceTypes", [])),
                    "employement": job.get("employerType"),
                    "updated_date": job.get("modifiedDate"),





                },
            )

        return JsonResponse({"status": "success", "message": "Jobs fetched and saved successfully."})
    except requests.RequestException as e:
        return JsonResponse({"status": "error", "message": str(e)})
