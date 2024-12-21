import scrapy
import json

class DiceSpider(scrapy.Spider):
    name = "dice"
    allowed_domains = ["dice.com"]
    # Initial API URL with query parameters for job search
    start_urls = [
        "https://job-search-api.svc.dhigroupinc.com/v1/dice/jobs/search?q=Software&countryCode2=US&radius=30&radiusUnit=mi&page=1&pageSize=20&facets=employmentType%7CpostedDate%7CworkFromHomeAvailability%7CworkplaceTypes%7CemployerType%7CeasyApply%7CisRemote%7CwillingToSponsor&filters.workplaceTypes=Remote&filters.employmentType=CONTRACTS&filters.postedDate=ONE&currencyCode=USD&fields=id%7CjobId%7Cguid%7Csummary%7Ctitle%7CpostedDate%7CmodifiedDate%7CjobLocation.displayName%7CdetailsPageUrl%7Csalary%7CclientBrandId%7CcompanyPageUrl%7CcompanyLogoUrl%7CcompanyLogoUrlOptimized%7CpositionId%7CcompanyName%7CemploymentType%7CisHighlighted%7Cscore%7CeasyApply%7CemployerType%7CworkFromHomeAvailability%7CworkplaceTypes%7CisRemote%7Cdebug%7CjobMetadata%7CwillingToSponsor&culture=en&recommendations=true&interactionId=0&fj=true&includeRemote=true"
    ]

    def parse(self, response):
        # Parse the JSON response
        try:
            data = json.loads(response.text)
        except json.JSONDecodeError as e:
            self.logger.error(f"Error decoding JSON: {e}")
            return

        # Extract job details
        jobs = data.get("data", {}).get("jobs", [])
        for job in jobs:
            yield {
                "title": job.get("title"),
                "company": job.get("companyName"),
                "location": job.get("location"),
                "employment_type": job.get("employmentType"),
                "posted_date": job.get("datePosted"),
                "url": job.get("detailsPage"),
                "salary": job.get("salary", {}).get("amount") if job.get("salary") else None,
            }

        # Pagination: fetch the next page if available
        current_page = data.get("data", {}).get("pageNumber", 1)
        total_pages = data.get("data", {}).get("totalPages", 1)
        
        if current_page < total_pages:
            next_page = current_page + 1
            next_url = f"https://jobsearch.api.dice.com/api/v2/jobsearch?q=Software&countryCode=US&radius=30&radiusUnit=mi&page={next_page}&pageSize=20&filters.postedDate=ONE&filters.workplaceTypes=Remote&filters.employmentType=CONTRACTS&currencyCode=USD&language=en"
            yield scrapy.Request(url=next_url, callback=self.parse)
