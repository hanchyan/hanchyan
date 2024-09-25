import requests

# Your Google Apps Script web app URL
web_app_url = "https://script.google.com/macros/s/AKfycbytm525C472abzDgybx2mwIT7UNmVrM9qJhoqBb5kOd_6D9k0pHYkxx4U3IciRxPnedBg/exec"


response = requests.get(web_app_url)
entries = response.json()  # Assuming the response is in JSON format


# Sample HTML entry template
entry_template = """
    <div class="trade-entry">
        <span class="trade-date">{date}</span>
        <div class="trade-details">
            <p><strong>Stock:</strong> {stock}</p>
            <p><strong>Action:</strong> {action}</p>
            <p><strong>Reason:</strong> {reason}</p>
            <img src="{imageUrl}" alt="{stock} trade screenshot" class="trade-image">
        </div>
    </div>
"""

# Create the entries HTML
entries_html = ""
for entry in entries:
    entries_html += entry_template.format(
        date=entry["date"],
        stock=entry["stock"],
        action=entry["action"],
        reason=entry["reason"],
        imageUrl=entry["imageUrl"]
    )
# Read the existing index.html
with open('index.html', 'r') as file:
    html_content = file.read()

# Replace the entries-container content
updated_html = html_content.replace('<div id="entries-container"></div>', f'<div id="entries-container">{entries_html}</div>')

# Save the updated index.html
with open('index.html', 'w') as file:
    file.write(updated_html)
