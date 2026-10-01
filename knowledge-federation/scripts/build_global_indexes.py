#!/usr/bin/env python3
from kf_common import *

def main():
    con = connect()
    ensure_home_vault()
    rows = con.execute("SELECT domain, subdomain, COUNT(*) c FROM notes GROUP BY domain, subdomain ORDER BY domain, subdomain").fetchall()
    batches = con.execute("SELECT status, COUNT(*) c FROM batches GROUP BY status").fetchall()
    content = "# Índice Global\n\n## Contagem por domínio/subdomínio\n\n"
    for r in rows:
        content += f"- **{r['domain']}/{r['subdomain']}**: {r['c']} notas\n"
    content += "\n## Status dos lotes\n\n"
    for b in batches:
        content += f"- {b['status']}: {b['c']}\n"
    (ROOT / "00-home-vault" / "Indice-Global.md").write_text(content, encoding="utf-8")
    print("Índice global atualizado.")

if __name__ == "__main__":
    main()
