# script para fazer download das paginas da plataforma OpenAI
import subprocess
import os

URLS = {
    "limits_pricing/rate-limits.md":
        "https://platform.openai.com/docs/guides/rate-limits",

    "models/model-selection.md":
        "https://platform.openai.com/docs/guides/model-selection",

    "limits_pricing/pricing.md":
        "https://platform.openai.com/docs/pricing",
}

RAW_DIR = "raw_html"
MD_DIR = "markdown"

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(MD_DIR, exist_ok=True)

for md_path, url in URLS.items():
    html_file = os.path.join(RAW_DIR, md_path.replace("/", "_") + ".html")
    md_file = os.path.join(MD_DIR, md_path)

    os.makedirs(os.path.dirname(md_file), exist_ok=True)

    subprocess.run([
        "curl.exe",
        "-L",
        "-H", "User-Agent: Mozilla/5.0",
        "-H", "Accept-Language: en-US,en;q=0.9",
        url,
        "-o", html_file
    ], check=True)

    subprocess.run([
        "pandoc",
        html_file,
        "-o", md_file,
        "--wrap=none",
        "--markdown-headings=atx"
    ], check=True)

    print(f"✔ Gerado: {md_file}")

