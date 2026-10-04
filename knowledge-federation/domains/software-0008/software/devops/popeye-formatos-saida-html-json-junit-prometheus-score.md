---
id: software.devops.tranche11.001076
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/derailed/popeye/master/README.md", "https://popeyecli.io/docs/codes.html", "https://github.com/derailed/popeye"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Formatos de saída do Popeye (-o): standard, jurassic, yaml, html, json, junit, prometheus e score

## Em uma frase
Por meio da flag **`-o` / `--out`**, o Popeye exporta seus relatórios de auditoria em **oito formatos distintos**: `standard` (padrão colorido com ícones), `jurassic` (texto puro sem ícones nem cores), `yaml`, `html`, `json`, `junit`, `prometheus` e `score` (retornando um único valor numérico de `0` a `100`).

## Por que importa
Enquanto engenheiros no terminal preferem a saída visual `standard`, pipelines de CI/CD precisam de relatórios `junit` ou de um número puro (`-o score`) para aprovar/reprovar stages, auditores de governança preferem páginas `html` autocontidas e sistemas de observabilidade consomem `json` ou `prometheus`.

## Como funciona
Conforme as tabelas *Output Formats* e *Report Morphology* do README oficial (`derailed/popeye`): (1) **`standard`** (default) usa 256 cores e emojis por severidade (`✅` Ok, `🔊` Info, `😱` Warn, `💥` Error); (2) **`jurassic`** substitui ícones e cores por códigos ASCII (`OK`, `I`, `W`, `E`) para terminais ou logs de CI sem suporte ANSI; (3) **`yaml`** e **`json`** estruturam toda a árvore de achados e contagens para processamento programático; (4) **`html`** gera um relatório visual completo pronto para navegador; (5) **`junit`** formata os achados como suíte de testes XML JUnit; (6) **`prometheus`** despeja o relatório no formato de exposição de métricas Prometheus; e (7) **`score`** retorna apenas o valor inteiro do **Popeye Score (`0–100`)**.

## Exemplo
```bash
# Obter apenas a nota numérica (0-100) do cluster ou gerar um relatório HTML completo no diretório atual
popeye -n producao -o score

POPEYE_REPORT_DIR=$(pwd) popeye -n producao --save --out html --output-file relatorio-producao.html
```

## Limites e trade-offs
No modo `standard`, terminais sem suporte a 256 cores (ou ambientes Nix onde `TERM` não está definido adequadamente) podem falhar no PreFlight Check de cores; nesses ambientes, defina `export TERM=xterm-256color` ou utilize `-o jurassic`.

## Como verificar
Execute `popeye -n default -o json | jq .popeye.score` para extrair a nota geral do namespace a partir da saída estruturada JSON.

## Conexões
- [[popeye-configuracao-spinach-yaml-allocations-excludes-overrides]] — Veja também: Configuração avançada do Popeye com SpinachYAML (-f spinach.yaml): allocations, excludes, FQN, rx:, overrides e registries.
- [[popeye-persistencia-relatorios-save-s3-minio-docker]] — Veja também: Persistência de relatórios do Popeye: --save, POPEYE_REPORT_DIR, --output-file e upload direto para AWS S3 e MinIO.
- [[popeye-linter-cluster-kubernetes-vivo-readonly]] — Referência cruzada direta com popeye-linter-cluster-kubernetes-vivo-readonly.
- [[popeye-metricas-prometheus-pushgateway-grafana]] — Referência cruzada direta com popeye-metricas-prometheus-pushgateway-grafana.

## Fontes
- [Popeye GitHub — README.md (Live Cluster Linter, Resource Linters Table, SpinachYAML, Output Formats, S3/MinIO, Prometheus & CronJob RBAC)](https://raw.githubusercontent.com/derailed/popeye/master/README.md) — README oficial do derailed/popeye (Apache-2.0) detalhando linters e aliases, arquivo spinach.yaml (allocations, excludes, FQN, rx:, overrides, registries), formatos de saída (-o), upload S3/MinIO, métricas Pushgateway e CronJob in-cluster (--force-exit-zero); consultado em 2026-10-03.
- [Popeye Official Documentation — Error Codes Reference (popeyecli.io/docs/codes.html)](https://popeyecli.io/docs/codes.html) — Tabela oficial completa de códigos de erro e níveis de severidade (0 a 3) do Popeye para Containers (100–113), Pods (200–209), Security (300–308), General (400–407), Workloads (500–508), HPA (600–605), Nodes (700–712), PDB, PV/PVC, Services e NetworkPolicies; consultado em 2026-10-03.
- [Popeye — Official GitHub Repository](https://github.com/derailed/popeye) — Repositório oficial do Popeye; consultado em 2026-10-03.
