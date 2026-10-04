---
id: software.devops.tranche11.001077
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

# Persistência de relatórios do Popeye: --save, POPEYE_REPORT_DIR, --output-file e upload direto para AWS S3 e MinIO

## Em uma frase
O Popeye permite persistir relatórios em disco usando **`--save`**, **`POPEYE_REPORT_DIR`** e **`--output-file`**, ou enviá-los diretamente para buckets de armazenamento de objetos **AWS S3 (`s3://`)** e **MinIO (`minio://`)** via **`--s3-bucket`**, **`--s3-region`** e **`--s3-endpoint`**.

## Por que importa
Quando o Popeye roda dentro de um container efêmero no Docker ou como um `CronJob` de auditoria dentro do Kubernetes, a saída em memória do pod se perde quando o container termina. Salvar automaticamente o relatório HTML/JSON em um diretório mapeado ou enviá-lo direto para um bucket S3/MinIO cria um histórico imutável de auditorias de conformidade do cluster.

## Como funciona
Conforme a seção *Saving Scans* do README oficial (`derailed/popeye`): (1) passar **`--save`** grava o relatório por padrão em um diretório temporário (impresso no `STDOUT`) com o nome `lint_<cluster-name>_<time-UnixNano>.<output-extension>`; (2) definir a variável de ambiente **`POPEYE_REPORT_DIR`** grava o relatório em `<POPEYE_REPORT_DIR>/<cluster>/<context>`, e **`--output-file`** fixa o nome do arquivo; e (3) passar **`--s3-bucket s3://meu-bucket/caminho`** (ou `minio://meu-bucket/caminho` combinado com `--s3-endpoint localhost:9000` e `--s3-region`, autenticando via `AWS_ACCESS_KEY_ID` e `AWS_SECRET_ACCESS_KEY`) cria o bucket se não existir e faz o upload direto do relatório gerado.

## Exemplo
```bash
# Salvar um relatório JSON do Popeye diretamente em um bucket AWS S3 ou servidor MinIO compatível
popeye --s3-bucket s3://auditoria-k8s-popeye/prod \
  --s3-region us-west-2 \
  --out json \
  --save \
  --output-file scan-prod.json

# Executar o Popeye via container Docker oficial mapeando o kubeconfig e o diretório /tmp para preservar o relatório salvo
docker run --rm -it \
  -v "$HOME/.kube:/root/.kube" \
  -e POPEYE_REPORT_DIR=/tmp/popeye \
  -v /tmp:/tmp \
  quay.io/derailed/popeye --context prod -n default --save --output-file relatorio.txt
```

## Limites e trade-offs
Ao executar `docker run --rm ... quay.io/derailed/popeye --save` sem mapear o diretório de saída (`-v /tmp:/tmp`), o Popeye gravará o relatório no `/tmp` interno do container e o arquivo será destruído imediatamente quando o container sair devido à flag `--rm`.

## Como verificar
Após executar o comando com `POPEYE_REPORT_DIR=$(pwd) popeye --save --out html --output-file report.html`, verifique o arquivo gerado no subdiretório `<cluster>/<context>/report.html`.

## Conexões
- [[popeye-formatos-saida-html-json-junit-prometheus-score]] — Veja também: Formatos de saída do Popeye (-o): standard, jurassic, yaml, html, json, junit, prometheus e score.
- [[popeye-metricas-prometheus-pushgateway-grafana]] — Veja também: Observabilidade contínua com Popeye: publicação de métricas no Prometheus Pushgateway e dashboards Grafana.
- [[popeye-execucao-in-cluster-cronjob-rbac-force-exit-zero]] — Referência cruzada direta com popeye-execucao-in-cluster-cronjob-rbac-force-exit-zero.

## Fontes
- [Popeye GitHub — README.md (Live Cluster Linter, Resource Linters Table, SpinachYAML, Output Formats, S3/MinIO, Prometheus & CronJob RBAC)](https://raw.githubusercontent.com/derailed/popeye/master/README.md) — README oficial do derailed/popeye (Apache-2.0) detalhando linters e aliases, arquivo spinach.yaml (allocations, excludes, FQN, rx:, overrides, registries), formatos de saída (-o), upload S3/MinIO, métricas Pushgateway e CronJob in-cluster (--force-exit-zero); consultado em 2026-10-03.
- [Popeye Official Documentation — Error Codes Reference (popeyecli.io/docs/codes.html)](https://popeyecli.io/docs/codes.html) — Tabela oficial completa de códigos de erro e níveis de severidade (0 a 3) do Popeye para Containers (100–113), Pods (200–209), Security (300–308), General (400–407), Workloads (500–508), HPA (600–605), Nodes (700–712), PDB, PV/PVC, Services e NetworkPolicies; consultado em 2026-10-03.
- [Popeye — Official GitHub Repository](https://github.com/derailed/popeye) — Repositório oficial do Popeye; consultado em 2026-10-03.
