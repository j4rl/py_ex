from fpdf import FPDF

# Skapa PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Windows PowerShell & CMD Cheat Sheet", ln=True, align='C')
pdf.ln(5)

def add_section(title, rows):
    pdf.set_font("Arial", 'B', 14)
    pdf.set_text_color(0, 0, 128)
    pdf.cell(0, 10, title, ln=True)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", '', 11)
    for cmd, desc in rows:
        pdf.set_font("Arial", 'B', 11)
        pdf.multi_cell(0, 6, f"{cmd}", border=0)
        pdf.set_font("Arial", '', 11)
        pdf.multi_cell(0, 6, f"  {desc}", border=0)
        pdf.ln(1)
    pdf.ln(3)

# Data till PDF
general_cmds = [
    ("ipconfig", "Visar nätverksinformation (IP, gateway, DNS osv)"),
    ("ping <adress>", "Testar anslutning till en adress"),
    ("tracert <adress>", "Visar rutten paket tar till målet"),
    ("netstat -an", "Visar aktuella nätverksanslutningar"),
    ("tasklist", "Visar alla aktiva processer"),
    ("taskkill /PID <id> /F", "Dödar en process med angivet PID"),
    ("systeminfo", "Visar detaljerad systeminformation"),
    ("driverquery", "Lista alla installerade drivrutiner"),
]

file_cmds = [
    ("dir", "Lista filer och mappar i aktuell katalog"),
    ("cd <sökväg>", "Byt katalog"),
    ("mkdir <mapp>", "Skapa en ny mapp"),
    ("del <fil>", "Radera en fil"),
    ("copy <fil> <destination>", "Kopiera en fil"),
    ("move <fil> <destination>", "Flytta en fil"),
    ("rename <fil> <nytt_namn>", "Byt namn på en fil"),
]

ps_cmds = [
    ("Get-Process", "Visar aktiva processer"),
    ("Stop-Process -Name <namn>", "Dödar en process med namn"),
    ("Get-Service", "Lista alla tjänster"),
    ("Start-Service <namn> / Stop-Service <namn>", "Starta eller stoppa tjänst"),
    ("Get-EventLog -LogName System -Newest 20", "Visa senaste 20 systemloggar"),
    ("Get-Command", "Lista alla tillgängliga kommandon"),
    ("Get-Help <kommando>", "Visa hjälp för kommando"),
    ("Set-ExecutionPolicy RemoteSigned", "Tillåt att köra skript (kräver admin)"),
    ("Get-HotFix", "Visa installerade uppdateringar"),
    ("Get-Content <fil>", "Läser innehåll från en fil"),
    ("Measure-Object", "Räknar och summerar objekt, ex: `Get-ChildItem | Measure-Object`"),
]

cool_cmds = [
    ("sfc /scannow", "Systemfilsgranskning (reparerar korrupta filer)"),
    ("chkdsk C: /f /r", "Kolla och fixa hårddiskfel"),
    ("powercfg /batteryreport", "Skapar en batterirapport (för laptops)"),
    ("powercfg /sleepstudy", "Detaljerad energirapport (nyare laptops)"),
    ("whoami", "Visar inloggad användare"),
    ("shutdown /s /t 60", "Stänger av datorn om 60 sekunder"),
    ("shutdown /r /t 0", "Startar om datorn direkt"),
    ("assoc", "Visar koppling mellan filtyper och program"),
    ("clip", "Skickar utdata till Urklipp, t.ex. `ipconfig | clip`"),
]

# Lägg till sektioner i PDF
add_section("Allmänna systemkommandon", general_cmds)
add_section("Fil- & kataloghantering", file_cmds)
add_section("PowerShell-specifika kommandon", ps_cmds)
add_section("Bonus – Coola tricks", cool_cmds)

# Spara PDF
pdf_path = "CheatSheet.pdf"
pdf.output(pdf_path)
pdf_path
