    import React, { useEffect, useState } from "react";
    import axios from "axios";

    const JobList = () => {
    const [jobs, setJobs] = useState([]);
    const backendURL = process.env.REACT_APP_BACKEND_URL;




        useEffect(() => {
            const fetchJobs = async () => {
            try {
                debugger;
                const response = await axios.get(`${process.env.REACT_APP_BACKEND_URL}api/fetch-jobs/`);
                console.log("response", response)
                setJobs(response.data); // Set jobs state with data from Axios
            } catch (error) {
                console.error("Error fetching job listings:", error);
            }
            };
        
            fetchJobs();
        }, []);
    

    return (
        <div className="p-4">
        <h1 className="text-xl font-bold mb-4">Job Listings</h1>
        <div className="space-y-4">
            {jobs.map((job) => (
            <div key={job.id} className="p-4 border rounded">
                <h2 className="text-lg font-bold">{job.title}</h2>
                <p>{job.company_name}</p>
                <p>{job.location}</p>
                <a href={job.job_url} target="_blank" rel="noopener noreferrer" className="text-blue-500">
                View Details
                </a>
            </div>
            ))}
        </div>
        </div>
    );
    };

    export default JobList;
