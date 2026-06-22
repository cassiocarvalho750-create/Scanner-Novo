#!/usr/bin/env python3
"""
Orquestrador para a nuvem (GitHub Actions).
Roda os scanners B3 e EUA, salva os HTMLs na pasta 'site/' e monta um
index.html com links e horario da ultima atualizacao (em horario de Brasilia).
"""
import datetime, os, subprocess, sys, zoneinfo

SITE = "site"
os.makedirs(SITE, exist_ok=True)

def br_now():
    try:
        tz = zoneinfo.ZoneInfo("America/Sao_Paulo")
        return datetime.datetime.now(tz)
    except Exception:
        # fallback UTC-3
        return datetime.datetime.utcnow() - datetime.timedelta(hours=3)

def run(scanner, out_base):
    """roda um scanner e move o HTML gerado para site/"""
    print(f"== rodando {scanner} ==", flush=True)
    try:
        subprocess.run([sys.executable, scanner, "--out", out_base], check=True, timeout=3000)
    except subprocess.TimeoutExpired:
        print(f"[aviso] {scanner} demorou demais (timeout)", flush=True)
    except subprocess.CalledProcessError as e:
        print(f"[erro] {scanner} falhou: {e}", flush=True)
    # move HTML para site/
    src = out_base + ".html"
    if os.path.exists(src):
        dst = os.path.join(SITE, os.path.basename(src))
        os.replace(src, dst)
        print(f"  -> {dst}", flush=True)
        return os.path.basename(src)
    return None

def main():
    b3_html = run("scanner_b3.py", "scanner_b3")
    us_html = run("scanner_us.py", "scanner_us")

    now = br_now()
    stamp = now.strftime("%d/%m/%Y %H:%M") + " (Brasília)"

    def card(titulo, arquivo, cor):
        if arquivo:
            return f"""<a href="{arquivo}" style="text-decoration:none">
              <div style="background:{cor};color:#fff;border-radius:14px;padding:22px;margin:12px 0;
                          box-shadow:0 2px 8px rgba(0,0,0,.12)">
                <div style="font-size:20px;font-weight:700">{titulo}</div>
                <div style="font-size:13px;opacity:.9;margin-top:4px">Toque para ver os sinais →</div>
              </div></a>"""
        return f"""<div style="background:#bbb;color:#fff;border-radius:14px;padding:22px;margin:12px 0">
              <div style="font-size:20px;font-weight:700">{titulo}</div>
              <div style="font-size:13px;margin-top:4px">Relatório indisponível nesta rodada.</div></div>"""

    index = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>Scanner DIDI+ADX+BB</title>
    <style>body{{font-family:'Segoe UI',system-ui,Arial;max-width:560px;margin:auto;padding:24px;color:#222;background:#fafafa}}
    h1{{color:#1A4731;font-size:24px}}</style></head><body>
    <h1>Scanner DIDI + ADX + BB</h1>
    <p style="color:#666;font-size:14px">Última atualização: <b>{stamp}</b></p>
    {card("🇧🇷 B3 (Brasil)", b3_html, "#1A4731")}
    {card("🇺🇸 EUA", us_html, "#2E7D4F")}
    <p style="color:#888;font-size:12px;margin-top:24px">Atualiza automaticamente às 13h, 16h e 19h (seg–sex).
    Sinais técnicos para análise própria — confira gráfico, liquidez e R% antes de operar. Não é recomendação.</p>
    </body></html>"""
    with open(os.path.join(SITE,"index.html"),"w",encoding="utf-8") as f:
        f.write(index)
    print("index.html gerado em site/", flush=True)

if __name__=="__main__":
    main()
