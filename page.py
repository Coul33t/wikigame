import wikipedia
import json
import types
import os
import random

class Page:
    def __init__(self):
        self.page = None
        self.words_found = []
        self.hide_word = []
        self.lang = "fr"

    def get_page_from_cached(self, filename=""):
        if filename:
            with open ("cached/" + filename + ".json", "r") as f:
                self.page = json.load(f)
        
        else:
            onlyfiles = [f for f in os.listdir("cached/") if os.path.isfile(os.path.join("cached/", f))]
            file = random.choice(onlyfiles)
            with open("cached/" + file, "r") as f:
                self.page = json.load(f)
                print(f"[INFO] Loaded page {self.page['title']}")


    def get_random_page(self, nb_pages=1, cache=True):
        wikipedia.set_lang(self.lang)

        if nb_pages > 10:
            print(f"[WARNING] nb_pages > 10. Setting it to 10 (max value for API).")
            nb_pages = 10

        names  = wikipedia.random(nb_pages)

        for name in names:
            self.page = wikipedia.page(name)

            if(cache):
                print(f"Page {name} will be cached.")
                #WikipediaPage is not JSON serializable. Make it so!
                to_cache = {}
                
                to_cache["title"] = self.page.title
                to_cache["summary"] = self.page.summary
                to_cache["content"] = self.page.content
                to_cache["categories"] = self.page.categories
                to_cache["pageid"] = self.page.pageid

                # TODO: use pathlib or whatever it's called
                with open("cached/" + name + ".json", "w") as f:
                    json.dump(to_cache, f, indent=4)

    def display_page(self):
        print(self.page.contents)