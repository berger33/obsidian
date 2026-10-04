---
id: software.devops.tranche11.001073
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
fontes: ["https://popeyecli.io/docs/codes.html", "https://raw.githubusercontent.com/derailed/popeye/master/README.md", "https://github.com/derailed/popeye"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Níveis de severidade (0 a 3) e códigos de erro do Popeye para Containers (100–113), Pods (200–209) e Segurança (300–308)

## Em uma frase
O Popeye classifica cada achado em quatro níveis de severidade — **`0: Ok` (`✅`)**, **`1: Info` (`🔊`)**, **`2: Warning` (`😱`)** e **`3: Error` (`💥`)** — utilizando códigos numéricos padronizados por domínio: **100–113 para Containers**, **200–209 para Pods** e **300–308 para Segurança**.

## Por que importa
Conhecer os códigos numéricos exatos do Popeye (documentados em `popeyecli.io/docs/codes.html`) é indispensável tanto para interpretar rapidamente os relatórios e métricas Prometheus (`popeye_code_total`) quanto para configurar regras cirúrgicas de exclusão (`excludes`) ou alteração de severidade (`overrides`) no arquivo `spinach.yaml`.

## Como funciona
Conforme a tabela oficial de códigos (`popeyecli.io/docs/codes.html`):
- **Containers (100–113)**: `100` (imagem Docker sem tag, Sev 3), `101` (tag `latest` em uso, Sev 2), `102`/`103`/`104` (sem probes / sem liveness / sem readiness, Sev 2), `105` (probe usa número de porta em vez de porta nomeada, Sev 1), `106`/`107` (sem requests/limits ou sem limits, Sev 2), `108` (porta não nomeada, Sev 1), `109`/`110` (CPU/Memória atual vs Request atingiu limiar, Sev 2), `111`/`112` (CPU/Memória atual vs Limit atingiu limiar, Sev 3) e `113` (imagem não hospedada em um registry permitido, Sev 3);
- **Pods (200–209)**: `200`/`201` (terminating, Sev 2), `202`/`203` (waiting, Sev 3), `204` (pod não pronto, Sev 3), `205` (múltiplos restarts, Sev 2), `206` (sem PodDisruptionBudget definido, Sev 1), `207` (unhappy phase, Sev 3), `208` (pod órfão sem controlador, Sev 2) e `209` (gerenciado por múltiplos PDBs, Sev 2);
- **Segurança (300–308)**: `300`/`308` (uso da ServiceAccount `default`, Sev 2/3), `301`/`303` (token da ServiceAccount montado automaticamente, Sev 2), `302`/`306` (pod/container rodando potencialmente como `root`, Sev 2) e `304`/`305`/`307` (referência a Secret, imagePullSecret ou ServiceAccount inexistente, Sev 3/2).

## Exemplo
```yaml
# Trecho de spinach.yaml sobrescrevendo a severidade do código 206 (ausência de PDB) e ignorando o código 105 em pods específicos
popeye:
  overrides:
    - code: 206
      severity: 1
```

## Limites e trade-offs
Códigos de severidade `3` (`Error` `💥`, como `100` imagem sem tag, `111`/`112` uso de CPU/MEM estourando o limit, ou `304` Secret referenciado que não existe) fazem o processo do Popeye terminar com **código de saída diferente de zero**, a menos que a flag `--force-exit-zero` seja passada.

## Como verificar
Execute `popeye -n default` e consulte os códigos numéricos exibidos entre colchetes (ex.: `[POP-106]`, `[POP-306]`) contra a referência oficial em `popeyecli.io/docs/codes.html`.

## Conexões
- [[popeye-catalogo-linters-recursos-aliases-selecao]] — Veja também: Catálogo de Linters do Popeye: recursos auditados, aliases de CLI (-s) e detecção de recursos órfãos.
- [[popeye-codigos-workloads-hpa-nodes-services-networkpolicies]] — Veja também: Códigos de diagnóstico do Popeye para Geral (400–407), Workloads (500–508), HPA (600–605), Nodes (700–712), PV/PVC (1000–1004), Services (1100–1110) e NetworkPolicies (1200–1206).
- [[popeye-linter-cluster-kubernetes-vivo-readonly]] — Referência cruzada direta com popeye-linter-cluster-kubernetes-vivo-readonly.
- [[popeye-configuracao-spinach-yaml-allocations-excludes-overrides]] — Referência cruzada direta com popeye-configuracao-spinach-yaml-allocations-excludes-overrides.

## Fontes
- [Popeye GitHub — README.md (Live Cluster Linter, Resource Linters Table, SpinachYAML, Output Formats, S3/MinIO, Prometheus & CronJob RBAC)](https://popeyecli.io/docs/codes.html) — README oficial do derailed/popeye (Apache-2.0) detalhando linters e aliases, arquivo spinach.yaml (allocations, excludes, FQN, rx:, overrides, registries), formatos de saída (-o), upload S3/MinIO, métricas Pushgateway e CronJob in-cluster (--force-exit-zero); consultado em 2026-10-03.
- [Popeye Official Documentation — Error Codes Reference (popeyecli.io/docs/codes.html)](https://raw.githubusercontent.com/derailed/popeye/master/README.md) — Tabela oficial completa de códigos de erro e níveis de severidade (0 a 3) do Popeye para Containers (100–113), Pods (200–209), Security (300–308), General (400–407), Workloads (500–508), HPA (600–605), Nodes (700–712), PDB, PV/PVC, Services e NetworkPolicies; consultado em 2026-10-03.
- [Popeye — Official GitHub Repository](https://github.com/derailed/popeye) — Repositório oficial do Popeye; consultado em 2026-10-03.
