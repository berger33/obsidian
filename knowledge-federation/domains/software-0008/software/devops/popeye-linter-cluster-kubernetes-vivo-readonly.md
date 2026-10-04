---
id: software.devops.tranche11.001071
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

# Popeye: sanitizador e linter somente-leitura para clusters Kubernetes vivos

## Em uma frase
O Popeye (`derailed/popeye`, Apache-2.0, criado pelo mesmo autor do K9s) é um utilitário somente-leitura (*readonly*) que escaneia clusters Kubernetes **em execução** (e não arquivos estáticos em disco) para detectar configurações incorretas, recursos órfãos/inutilizados, incompatibilidades de portas, problemas de RBAC e sobre/subalocação de CPU e memória.

## Por que importa
Analisadores estáticos de YAML em CI/CD não conseguem saber se um `Service` aplicado no cluster realmente seleciona algum `Pod` ativo, se um `Secret`, `ConfigMap` ou `ServiceAccount` está órfão sem nenhum consumidor, se um `PersistentVolumeClaim` ficou preso em `Pending` ou se um container em produção está consumindo 95% do seu limite de memória. O Popeye inspeciona o estado vivo do cluster na prática.

## Como funciona
Conforme descrevem o README oficial (`derailed/popeye`) e `popeyecli.io`, o Popeye conecta-se ao cluster via `kubeconfig` (ou `ServiceAccount` in-cluster) usando apenas verbos de leitura (`get`, `list`), executa um conjunto curado de **linters** sobre os recursos implantados e, caso o cluster possua o **`metrics-server`**, cruza as especificações com o consumo real de CPU e memória (alertando por padrão quando o uso ultrapassa 80% de CPU/MEM). Ao final, gera um relatório categorizado por severidade e calcula o **Popeye Score** (de `0` a `100`) da saúde de configuração do cluster.

## Exemplo
```bash
# Instalar o Popeye via Homebrew ou Go e executar uma varredura em todos os namespaces (-A)
brew install derailed/popeye/popeye

# Escanear um namespace específico ou todos os namespaces do contexto atual
popeye -n producao
popeye -A
```

## Limites e trade-offs
Como o Popeye é estritamente uma ferramenta somente-leitura (*readonly*), ele nunca altera nem remove recursos no seu cluster; cabe ao operador ou ao pipeline GitOps corrigir os manifestos ou remover os recursos órfãos apontados pelo relatório.

## Como verificar
Execute `popeye version` para validar a instalação e rode `popeye -n default` verificando o cabeçalho de resumo e o **Popeye Score** ao final da saída no terminal (garantindo `export TERM=xterm-256color` em terminais Nix/Linux).

## Conexões
- [[popeye-catalogo-linters-recursos-aliases-selecao]] — Veja também: Catálogo de Linters do Popeye: recursos auditados, aliases de CLI (-s) e detecção de recursos órfãos.
- [[popeye-codigos-erro-severidades-containers-pods-seguranca]] — Referência cruzada direta com popeye-codigos-erro-severidades-containers-pods-seguranca.
- [[k9s-visoes-diagnostico-pulses-xray-popeye-usedby]] — Referência cruzada direta com k9s-visoes-diagnostico-pulses-xray-popeye-usedby.

## Fontes
- [Popeye GitHub — README.md (Live Cluster Linter, Resource Linters Table, SpinachYAML, Output Formats, S3/MinIO, Prometheus & CronJob RBAC)](https://raw.githubusercontent.com/derailed/popeye/master/README.md) — README oficial do derailed/popeye (Apache-2.0) detalhando linters e aliases, arquivo spinach.yaml (allocations, excludes, FQN, rx:, overrides, registries), formatos de saída (-o), upload S3/MinIO, métricas Pushgateway e CronJob in-cluster (--force-exit-zero); consultado em 2026-10-03.
- [Popeye Official Documentation — Error Codes Reference (popeyecli.io/docs/codes.html)](https://popeyecli.io/docs/codes.html) — Tabela oficial completa de códigos de erro e níveis de severidade (0 a 3) do Popeye para Containers (100–113), Pods (200–209), Security (300–308), General (400–407), Workloads (500–508), HPA (600–605), Nodes (700–712), PDB, PV/PVC, Services e NetworkPolicies; consultado em 2026-10-03.
- [Popeye — Official GitHub Repository](https://github.com/derailed/popeye) — Repositório oficial do Popeye; consultado em 2026-10-03.
