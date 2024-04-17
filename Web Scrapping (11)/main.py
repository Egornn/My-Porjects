import requests
from bs4 import BeautifulSoup
import csv

def scrape_allrecipes():
    url = "https://www.allrecipes.com/"

    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        recipe_section = soup.find("section", {"class": "carousel"})


        if recipe_section:
            recipe_links = recipe_section.find_all("a", {"class": "mntl-card-list-items"})

            with open("allrecipes.csv", "w", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Recipe Name", "Rating"])

                for link in recipe_links:
                    name = link.text.strip()
                    
                    rating = "N/A"
                    if link.find("span", {"class": "rating-star"}):
                        rating = link.find("span", {"class": "rating-star"})["data-ratingstars"]
                    
                    writer.writerow([name, rating])
            
            print("Data successfully saved to allrecipes.csv")
        else:
            print("Recipe section not found on the page.")
    else:
        print("Failed to retrieve the page.")

scrape_allrecipes()
