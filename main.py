from fastapi import FastAPI
from google_play_scraper import search
import google_play_scraper

app = FastAPI()
@app .get("/")
async def read_root():
    return {"To get the details of the app use - /google_store/domain_name"}


@app .get("/google_store/{domain_name}")
async def google_store(domain_name: str):
    try:
        results = search(domain_name, 1)
        if len(results) > 0:
            app_id = results[0]['appId']
            app_details = google_play_scraper.app(app_id)
            return {
                "App Title": app_details['title'],
                "Developer": app_details['developer'],
                "Genre": app_details['genre'],
                "Rating": app_details['score'],
                "Installs": app_details['installs'],
                "URL": app_details['url'],
            
            }
        else:
            return {"message": f"No app found for the domain name: {domain_name}"}
    except Exception as e:
        return {"error": str(e)}
 
 #if __name__ == "__main__":
 #    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
