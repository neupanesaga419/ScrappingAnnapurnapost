
import requests 

# search_data = "नेपाली"
search_data = "दैलेख"

articles = {

}

for i in range(1,4):

    payload = {
        "title":search_data,
        "page":i
    }

    r = requests.get("https://bg.annapurnapost.com/api/search", params=payload)

    if r.status_code == 200:
        data = r.json()
        for item in data['data']['items']:
            key_name = f"article_{item['id']}"
            articles[key_name] = {
                "title":item["title"],
                "author":item["author"],
                "content":item["content"],
            }

file_name = f"{search_data}.json"

with open(file_name, "w+", encoding="utf-8") as f:
    import json
    data = json.dumps(articles, indent=4, ensure_ascii=False)
    f.writelines(data)


