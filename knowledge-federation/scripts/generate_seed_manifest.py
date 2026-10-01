#!/usr/bin/env python3
from kf_common import *
import argparse, random

SAFE_TEMPLATES = {
  "software": ["{sub} - conceito essencial {i}", "{sub} - padrao pratico {i}", "{sub} - erro comum {i}", "{sub} - checklist de IA {i}"],
  "ia": ["{sub} - conceito de IA {i}", "{sub} - avaliacao e risco {i}", "{sub} - ferramenta ou tecnica {i}", "{sub} - prompt e verificacao {i}"],
  "vibe-coding": ["{sub} - workflow de orquestracao {i}", "{sub} - prompt operacional {i}", "{sub} - criterio de aceite {i}", "{sub} - revisao de entrega IA {i}"],
  "jogos": ["{sub} - sistema de jogo {i}", "{sub} - decisao tecnica {i}", "{sub} - pipeline com IA {i}", "{sub} - teste e playtest {i}"],
  "cannabis-medicinal": ["{sub} - nota legal e terapeutica {i}", "{sub} - rastreabilidade e seguranca {i}", "{sub} - pergunta para profissional licenciado {i}", "{sub} - evidencia cientifica {i}"],
  "micologia": ["{sub} - taxonomia e seguranca {i}", "{sub} - pesquisa cientifica {i}", "{sub} - legislacao e riscos {i}", "{sub} - cogumelos legais comparativo {i}"],
  "negocio-carreira-produto": ["{sub} - decisao de produto {i}", "{sub} - validacao com IA {i}", "{sub} - metrica e risco {i}", "{sub} - carreira e portfolio {i}"]
}

def infer_type(domain, sub):
    if "glossario" in sub: return "glossario"
    if domain == "jogos" and sub in ["engines"]: return "engine"
    if "ferramenta" in sub: return "ferramenta"
    return "conceito"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", required=True)
    args = ap.parse_args()
    con = connect()
    b = con.execute("SELECT * FROM batches WHERE batch_id=?", (args.batch,)).fetchone()
    if not b:
        raise SystemExit(f"Lote não encontrado: {args.batch}")
    templates = SAFE_TEMPLATES.get(b["domain"], SAFE_TEMPLATES["software"])
    items = []
    for i in range(1, b["planned_count"] + 1):
        title = templates[(i-1) % len(templates)].format(sub=b["subdomain"].replace('-', ' '), i=f"{i:04d}").title()
        sl = slugify(title)
        note_id = f"{slugify(b['domain'])}.{slugify(b['subdomain'])}.{i:06d}"
        risk_legal = "alto" if b["domain"] in ["cannabis-medicinal", "micologia"] else "baixo"
        risk_medical = "alto" if b["domain"] in ["cannabis-medicinal", "micologia"] else "baixo"
        items.append({
            "id": note_id,
            "slug": sl,
            "title": title,
            "domain": b["domain"],
            "subdomain": b["subdomain"],
            "type": infer_type(b["domain"], b["subdomain"]),
            "level": "iniciante" if i % 3 else "intermediario",
            "risk_legal": risk_legal,
            "risk_medical": risk_medical,
            "operational_content": False,
            "status": "planned"
        })
    manifest = {"batch_id": args.batch, "vault": b["vault"], "domain": b["domain"], "subdomain": b["subdomain"], "items": items}
    mp = manifest_path(args.batch)
    write_json(mp, manifest)
    con.execute("UPDATE batches SET manifest_path=?, status=?, updated_at=? WHERE batch_id=?", (str(mp.relative_to(ROOT)), "drafting", now(), args.batch))
    con.commit()
    print(f"Manifesto criado: {mp} ({len(items)} notas planejadas)")

if __name__ == "__main__":
    main()
