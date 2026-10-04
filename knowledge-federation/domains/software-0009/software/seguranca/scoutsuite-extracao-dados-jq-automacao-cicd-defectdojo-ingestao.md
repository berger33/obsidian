---
id: software.seguranca.tranche11.001019
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/README.md", "https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/ScoutSuite/__main__.py"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Automação e Integração do Scout Suite em Pipelines CI/CD: Parsing do Payload JSON (`scoutsuite_results_*.js`) com **`jq`** e Ingestão no **DefectDojo**

## Em uma frase
Como o arquivo de resultados gerado pelo Scout Suite (`scoutsuite-results/scoutsuite_results_<nome>.js`) começa com uma linha de atribuição JavaScript (`scoutsuite_results =`) seguida de um objeto JSON puro contendo todo o inventário (`services.<servico>.findings.<regra>`), como processá-lo automaticamente em scripts de CI/CD ou com o **`jq`**?

## Por que importa
Basta pular a primeira linha do arquivo com **`tail -n +2 scoutsuite_results_*.js | jq ...`**!

## Como funciona
Além disso, o **OWASP DefectDojo** possui um importador nativo chamado **`Scout Suite Scan`** que consome diretamente o relatório do Scout Suite, deduplicando os achados de nuvem, associando severidades e acompanhando o SLA de remediação junto com os demais resultados de AppSec!

## Exemplo
```bash
# Extrair via jq todos os achados de severidade 'danger' com pelo menos 1 item afetado a partir do arquivo de resultados do Scout Suite
tail -n +2 /cases/cloud-audit/scout-aws/scoutsuite-results/scoutsuite_results_aws-prod-2026.js | \
  jq -r '.services | to_entries[] | .key as $svc | .value.findings | to_entries[] | select(.value.level == "danger" and .value.flagged_items > 0) | "[\($svc)] \(.key): \(.value.description) (\(.value.flagged_items) afetados)"'
```

## Limites e trade-offs
Olhe como o pipeline `tail -n +2 ... | jq` acima transforma o Scout Suite em um **Quality Gate de Segurança Cloud** automatizado: se o comando `jq` retornar qualquer achado `danger` com `flagged_items > 0` que não esteja coberto pelo arquivo `--exceptions`, seu job de auditoria noturna pode abrir um incidente automático ou falhar o pipeline!

## Como verificar
No repositório oficial do Scout Suite (`tools/`), você também encontra scripts auxiliares em Python para formatação e comparação de relatórios.

## Conexões
- [[scoutsuite-auditoria-alibaba-oci-digitalocean-kubernetes-multicloud]] — Veja também: Auditoria de Nuvens Alternativas e Clusters com Scout Suite: **Alibaba Cloud (`aliyun`), Oracle Cloud (`oci`), DigitalOcean (`do`) e Kubernetes (`k8s`)**.
- [[scoutsuite-comparacao-cspm-scoutsuite-prowler-steampipe-cartography]] — Veja também: Arquitetura Comparativa de Ferramentas Open-Source de Segurança Cloud: Quando Usar **Scout Suite vs Prowler vs Steampipe/Powerpipe vs CloudQuery vs Cartography**.
- [[scoutsuite-arquitetura-auditoria-multi-cloud-offline-nccgroup]] — Referência cruzada direta com scoutsuite-arquitetura-auditoria-multi-cloud-offline-nccgroup.
- [[scoutsuite-reexecucao-offline-fetch-local-update-comparacao-diffs]] — Referência cruzada direta com scoutsuite-reexecucao-offline-fetch-local-update-comparacao-diffs.

## Fontes
- [NCC Group Scout Suite Official GitHub — Multi-Cloud Security Auditing Tool](https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/README.md) — repositório oficial do Scout Suite cobrindo auditoria point-in-time offline para AWS, Azure, GCP, Alibaba Cloud, OCI, DigitalOcean e Kubernetes; consultado em 2026-10-03.
- [Scout Suite Official CLI & Engine Implementation (`ScoutSuite/__main__.py`)](https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/ScoutSuite/__main__.py) — implementação oficial dos provedores, parâmetros de autenticação, `--fetch-local`, `--update`, `--ruleset`, `--exceptions` e `--ip-ranges`; consultado em 2026-10-03.
