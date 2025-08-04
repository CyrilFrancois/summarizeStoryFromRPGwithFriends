from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI() #No need for OpenAI(api_key=os.getenv("OPENAI_API_KEY")) because already loaded with dotenv

def generate_chatgpt_response(prompt):
    response = client.chat.completions.create(
    model=os.getenv("SUMMARY_MODEL"),
    messages=[
        {"role": "system", "content": "Vous êtes un résumeurs d'histoires fantastiques médiévales."},
        {"role": "user", "content": prompt}
    ],
    )
    return response.choices[0].message.content

# Usage example
if __name__ == "__main__":
    with open(os.getenv("STORY"), 'r', encoding='utf-8') as file:
        story = file.read()
    with open(os.getenv("CONTEXT"), 'r', encoding='utf-8') as file:
        context = file.read()

    prompt = f"""Résume de manière très détaillée l'histoire suivante, sans faire de condensation, en respectant les consignes suivantes :
                Garde tous les noms des personnages, lieux, factions, objets ou concepts importants.
                Décris les événements dans l'ordre chronologique, en développant chaque scène clé.
                Précise les motivations, émotions et évolutions des personnages.
                Mentionne les conséquences des actions et les rebondissements majeurs.
                Ne saute aucune étape de l'histoire, même les passages longs ou complexes.
                Le résumé doit être long, structuré, immersif, avec un style narratif fluide.
                Vise un résumé détaillé d'au moins 1000 mots si le contenu le permet.
                Fait un très long résumé.

                Contexte du jeu :
                {context}

                Histoire à résumer en détails:
                {story}"""
    
    chatgpt_response = generate_chatgpt_response(prompt)

    with open("summaryFromStory.txt", "w", encoding='utf-8') as f:
        f.write(chatgpt_response)
    print("makeSummaryFromStory done!")
