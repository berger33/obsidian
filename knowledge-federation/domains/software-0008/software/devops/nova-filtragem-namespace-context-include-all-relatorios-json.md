---
id: software.devops.tranche12.001149
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-12.md"
fontes: ["https://nova.docs.fairwinds.com/usage/", "https://nova.docs.fairwinds.com/quickstart/", "https://raw.githubusercontent.com/FairwindsOps/nova/master/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Fairwinds Nova: Escopo por Namespace (--namespace), Multi-Contexto (--context) e Exportação JSON

## Em uma frase
O Nova permite direcionar varreduras a um único namespace (`-n` / `--namespace`), alternar entre múltiplos clusters do `kubeconfig` (`--context`), incluir charts mesmo sem versão mais nova encontrada (`-a` / `--include-all`) e exportar relatórios estruturados em JSON (`--format json --output-file`).

## Por que importa
Em frotas com dezenas de clusters ou clusters multi-tenant onde uma equipe é responsável apenas pelo namespace `monitoring` ou `ingress-system`, varrer o cluster inteiro em formato texto dificulta a automação de tickets por squad.

## Como funciona
Usando `--context <cluster-ctx> -n <namespace> --format json --output-file report.json`, scripts de plataforma podem iterar sobre todos os contextos de produção, extrair os objetos JSON onde `.outdated == true` e rotear notificações apenas para o time dono daquele namespace.

## Exemplo
```bash
for ctx in eks-staging eks-prod; do
  nova find --context "$ctx" --helm --containers \
    --format json --output-file "nova-${ctx}.json"
done
jq '.helm[] | {release, namespace, installed: .Installed.version, latest: .Latest.version, outdated}' nova-eks-prod.json
```

## Limites e trade-offs
Executar `nova find` sem especificar `--context` em scripts de automação faz o binário usar qualquer contexto que esteja ativo por acaso no `kubeconfig` corrente.

## Como verificar
Sempre explicite `--context` e `--format json` em execuções automatizadas para garantir relatórios reprodutíveis e auditáveis por cluster.

## Conexões
- [[nova-combinado-pluto-polaris-goldilocks-governanca-upgrades]] — Veja também: Fairwinds Nova: Uso Combinado com Pluto, Polaris e Goldilocks no Planejamento de Upgrades de Cluster.
- [[nova-planejamento-atualizacao-minor-vs-major-helm-appversion]] — Veja também: Fairwinds Nova: Análise de Drift entre Chart Version e appVersion em Upgrades Graduais.

## Fontes
- [Fairwinds Nova GitHub — README.md & Quickstart (Helm Release & Container Image Scanning & v3.12.0+ Signed Immutable Images)](https://nova.docs.fairwinds.com/usage/) — README oficial e Quickstart do Fairwinds Nova detalhando nova find, nova find --containers e migração na v3.12.0+ para imagens assinadas e imutáveis em us-docker.pkg.dev/fairwinds-ops/oss/nova; consultado em 2026-10-03.
- [Fairwinds Nova Official Documentation — Usage & CLI Options (--poll-artifacthub, --desired-versions, --show-errored-containers & JSON Output)](https://nova.docs.fairwinds.com/quickstart/) — Guia oficial de uso do Nova cobrindo flags de CLI, repositórios privados (--url), nova generate-config, --desired-versions, --show-non-semver e estrutura de saída JSON; consultado em 2026-10-03.
- [Fairwinds Nova — Official Documentation Portal](https://raw.githubusercontent.com/FairwindsOps/nova/master/README.md) — Portal oficial de documentação do Fairwinds Nova; consultado em 2026-10-03.
