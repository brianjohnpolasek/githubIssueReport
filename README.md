# Github Issue Report
The purpose of this programe is to take an input of Github repositories in the format "owner/repository" and returns a String of Json data including all of the issues, as well as repository names corresponding to the most problematic day.

## Executing the Program
The key to this program is a python script named _githubIssuesReport.py_. This script can either be run by executing the python script with the input text file as a command line argument, or running the shell script named _executeGithubIssuesReport.sh_, which runs the program with the example input file provided. This shell script can be eddited to take in a custom text file of github repositories as well.

## Example Program Execution
**Example Input:** (Text file, for this example called _github_repos.txt_)
> owner1/repository1

> owner2/repository2

**Example Terminal Input**
> python githubIssuesReport.py github_repos.txt

**Example Output:**
```json
{
  "issues": [
    {
      "id": 38,
      "state": "open",
      "title": "Found a bug",
      "repository": "owner1/repository1",
      "created_at": "2011-04-22T13:33:48Z"
    },
    {
      "id": 23,
      "state": "open",
      "title": "Found a bug 2",
      "repository": "owner1/repository1",
      "created_at": "2011-04-22T18:24:32Z"
    },
    {
      "id": 24,
      "state": "closed",
      "title": "Feature request",
      "repository": "owner2/repository2",
      "created_at": "2011-05-08T09:15:20Z"
    }
  ],
  "top_day": {
    "day": "2011-04-22",
    "occurrences": {
      "owner1/repository1": 2,
      "owner2/repository2": 0
    }
  }
}
```

