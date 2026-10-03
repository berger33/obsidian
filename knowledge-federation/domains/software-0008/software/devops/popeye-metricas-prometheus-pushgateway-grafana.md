---
id: software.devops.tranche11.001078
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

# Observabilidade contínua com Popeye: publicação de métricas no Prometheus Pushgateway e dashboards Grafana

## Em uma frase
O Popeye pode publicar telemetria de conformidade diretamente em um **Prometheus Pushgateway** (`--push-gtwy-url`), expondo cinco métricas do tipo gauge — `popeye_severity_total`, `popeye_code_total`, `popeye_linter_tally_total`, `popeye_report_errors_total` e `popeye_cluster_score` — para visualização histórica no Grafana.

## Por que importa
Executar o Popeye manualmente no terminal mostra apenas uma fotografia pontual. Enviar as métricas de cada varredura horária para o Prometheus permite criar alertas no Alertmanager caso o `popeye_cluster_score` caia abaixo de 80 ou caso surjam erros de severidade 3 (`popeye_severity_total`) após um deploy.

## Como funciona
Conforme a seção *The Prom Queen!* do README oficial (`derailed/popeye`), ao passar o argumento **`--push-gtwy-url http://pushgateway:9091`** (e credenciais se aplicável), o Popeye empurra ao final do scan os seguintes gauges Prometheus:
1. **`popeye_severity_total`**: contagens totais agrupadas por nível de severidade (`Ok`, `Info`, `Warn`, `Error`);
2. **`popeye_code_total`**: contagens agrupadas por código numérico de linter do Popeye (`100`, `106`, `306` etc.);
3. **`popeye_linter_tally_total`**: contagens agregadas por linter de recurso (`pods`, `services`, `nodes` etc.);
4. **`popeye_report_errors_total`**: total de erros de execução do scan;
5. **`popeye_cluster_score`**: a nota geral (`0–100`) do relatório do cluster.

## Exemplo
```bash
# Executar a varredura do Popeye em todos os namespaces e publicar as métricas no Prometheus Pushgateway
popeye -A -f spinach.yaml --push-gtwy-url http://prometheus-pushgateway.monitoring:9091
```

## Limites e trade-offs
Conforme observa a nota técnica do próprio README oficial, quando você combina `--save` (que grava o artefato em disco com timestamp UnixNano) com `--push-gtwy-url`, a métrica `popeye_cluster_score` inclui uma label adicional para rastrear o artefato persistido, o que aumenta a cardinalidade da série temporal a cada push; para manter cardinalidade baixa e previsível no Prometheus, evite combinar `--save` na mesma invocação que faz push ao Pushgateway.

## Como verificar
Após executar `popeye --push-gtwy-url http://localhost:9091`, consulte `curl -s http://localhost:9091/metrics | grep popeye_` para confirmar a presença dos cinco gauges publicados.

## Conexões
- [[popeye-persistencia-relatorios-save-s3-minio-docker]] — Veja também: Persistência de relatórios do Popeye: --save, POPEYE_REPORT_DIR, --output-file e upload direto para AWS S3 e MinIO.
- [[popeye-execucao-in-cluster-cronjob-rbac-force-exit-zero]] — Veja também: Execução do Popeye in-cluster via CronJob Kubernetes, flag --force-exit-zero e perfil RBAC somente-leitura.
- [[popeye-formatos-saida-html-json-junit-prometheus-score]] — Referência cruzada direta com popeye-formatos-saida-html-json-junit-prometheus-score.
- [[popeye-codigos-erro-severidades-containers-pods-seguranca]] — Referência cruzada direta com popeye-codigos-erro-severidades-containers-pods-seguranca.

## Fontes
- [Popeye GitHub — README.md (Live Cluster Linter, Resource Linters Table, SpinachYAML, Output Formats, S3/MinIO, Prometheus & CronJob RBAC)](https://raw.githubusercontent.com/derailed/popeye/master/README.md) — README oficial do derailed/popeye (Apache-2.0) detalhando linters e aliases, arquivo spinach.yaml (allocations, excludes, FQN, rx:, overrides, registries), formatos de saída (-o), upload S3/MinIO, métricas Pushgateway e CronJob in-cluster (--force-exit-zero); consultado em 2026-10-03.
- [Popeye Official Documentation — Error Codes Reference (popeyecli.io/docs/codes.html)](https://popeyecli.io/docs/codes.html) — Tabela oficial completa de códigos de erro e níveis de severidade (0 a 3) do Popeye para Containers (100–113), Pods (200–209), Security (300–308), General (400–407), Workloads (500–508), HPA (600–605), Nodes (700–712), PDB, PV/PVC, Services e NetworkPolicies; consultado em 2026-10-03.
- [Popeye — Official GitHub Repository](https://github.com/derailed/popeye) — Repositório oficial do Popeye; consultado em 2026-10-03.
