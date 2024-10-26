import requests
import os

# Configura tu token personal de acceso y el repositorio que deseas monitorizar
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # O ingresa directamente tu token aquí
REPO = "usuario/repositorio"  # Cambia esto por el repo que quieras usar
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

def get_latest_issues():
    """Obtiene los últimos issues abiertos en el repositorio."""
    url = f"https://api.github.com/repos/{REPO}/issues?state=open"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al obtener issues: {response.status_code}")
        return []

def post_comment(issue_number, comment):
    """Publica un comentario en el issue especificado."""
    url = f"https://api.github.com/repos/{REPO}/issues/{issue_number}/comments"
    payload = {"body": comment}
    response = requests.post(url, json=payload, headers=HEADERS)
    if response.status_code == 201:
        print(f"Comentario publicado en el issue #{issue_number}.")
    else:
        print(f"Error al comentar: {response.status_code}")

def main():
    issues = get_latest_issues()
    if issues:
        for issue in issues:
            issue_number = issue["number"]
            title = issue["title"]
            print(f"Respondiendo al issue #{issue_number}: {title}")

            # Publica un comentario rápido en el issue
            comentario = "¡Hola! Estoy aquí para ayudar. ¿En qué puedo apoyarte?"
            post_comment(issue_number, comentario)
    else:
        print("No hay issues abiertos para responder.")

if __name__ == "__main__":
    main()
