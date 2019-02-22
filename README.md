# githubIssueReport
Python program that take an input of Github repositories in the format "owner/repository" and returns a String of Json data including all of the issues, as well as repository names corresponding to the most problematic day.

Example Input: (Text file)
> owner1/repository1
> owner2/repository2

Example Output:
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
