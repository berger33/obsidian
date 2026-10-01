# Knowledge Federation

Infraestrutura para construir uma biblioteca federada de conhecimento em formato Obsidian, em lotes auditáveis e retomáveis.

## Fluxo rápido

```bash
python knowledge-federation/scripts/plan_batches.py --target 1000000 --batch-size 500
python knowledge-federation/scripts/generate_seed_manifest.py --batch batch-000001
python knowledge-federation/scripts/generate_batch.py --batch batch-000001
python knowledge-federation/scripts/audit_batch.py --batch batch-000001
python knowledge-federation/scripts/build_global_indexes.py
python knowledge-federation/scripts/export_zip.py --vault software-0001
```

## Segurança

Domínios regulados, como cannabis medicinal e psilocibina/micologia, são tratados com filtros de conteúdo. O sistema bloqueia geração operacional de cultivo/extração de substâncias controladas e prioriza notas legais, médicas, científicas, regulatórias, de rastreabilidade e perguntas para profissionais licenciados.
