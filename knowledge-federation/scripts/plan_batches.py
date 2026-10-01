#!/usr/bin/env python3
from kf_common import *
import argparse, math

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", type=int, default=None)
    ap.add_argument("--batch-size", type=int, default=500)
    ap.add_argument("--reset", action="store_true")
    args = ap.parse_args()
    cfg = load_config()
    target = args.target or cfg.get("target_notes", 1000000)
    con = connect()
    if args.reset:
        con.executescript("DELETE FROM links; DELETE FROM notes; DELETE FROM batches;")
        con.commit()
    existing = con.execute("SELECT COUNT(*) c FROM batches").fetchone()["c"]
    if existing:
        print(f"Batches já planejados: {existing}. Use --reset para recriar.")
        return
    domains = cfg["domains"]
    batch_no = 1
    for domain, spec in domains.items():
        d_target = spec.get("target_notes", 0)
        subs = spec.get("subdomains", ["geral"])
        per_sub = max(1, math.ceil(d_target / len(subs)))
        for sub in subs:
            remaining = per_sub
            while remaining > 0:
                size = min(args.batch_size, remaining)
                batch_id = f"batch-{batch_no:06d}"
                vault_index = ((batch_no - 1) // 20) + 1
                vault = vault_for(domain, vault_index)
                t = now()
                con.execute("""INSERT INTO batches(batch_id,domain,subdomain,vault,planned_count,status,created_at,updated_at)
                               VALUES(?,?,?,?,?,?,?,?)""", (batch_id, domain, sub, vault, size, "planned", t, t))
                batch_no += 1
                remaining -= size
    con.commit()
    print(f"Planejados {batch_no-1} lotes para alvo aproximado de {target} notas.")

if __name__ == "__main__":
    main()
