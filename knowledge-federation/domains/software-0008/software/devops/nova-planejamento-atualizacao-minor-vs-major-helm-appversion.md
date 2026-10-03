---
id: software.devops.tranche12.001150
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

# Fairwinds Nova: Análise de Drift entre Chart Version e appVersion em Upgrades Graduais

## Em uma frase
A saída JSON e tabular do Nova diferencia a versão do pacote Helm (`Installed.version` vs `Latest.version`) da versão da aplicação empacotada (`Installed.appVersion` vs `Latest.appVersion`), além de separar `Latest`, `Latest Minor` e `Latest Patch` para imagens de container.

## Por que importa
Pular diretamente três versões major de um chart Helm crítico (como `prometheus-operator`, `argocd` ou `vault`) sem observar o salto de `appVersion` e as migrações de CRDs intermediárias é uma das principais causas de indisponibilidade em manutenção de plataforma.

## Como funciona
Ao inspecionar o JSON emitido por `nova find --helm --containers`, a equipe de SRE identifica primeiro as atualizações de `Latest Patch` e `Latest Minor` (que corrigem CVEs mantendo compatibilidade retroativa) e planeja janelas dedicadas com revisão de `CHANGELOG` e atualização prévia de CRDs quando há salto major entre `Installed.version` e `Latest.version`.

## Exemplo
```bash
nova find --helm --containers --format json | \
  jq '{
    outdated_charts: [.helm[] | select(.outdated) | {release, namespace, installed: .Installed, latest: .Latest}],
    containers: [.container_images[]? | select(.outdated)]
  }'
```

## Limites e trade-offs
Automatizar `helm upgrade` cego para a versão `Latest` reportada pelo Nova quando há mudança de versão major do chart quebra valores customizados (`values.yaml`) cujo schema mudou entre versões principais.

## Como verificar
Separe a automação de patches (`Latest Patch`) da revisão assistida de upgrades major de charts Helm, validando sempre o diff com `helm diff upgrade` antes de aplicar.

## Conexões
- [[nova-filtragem-namespace-context-include-all-relatorios-json]] — Veja também: Fairwinds Nova: Escopo por Namespace (--namespace), Multi-Contexto (--context) e Exportação JSON.

## Fontes
- [Fairwinds Nova GitHub — README.md & Quickstart (Helm Release & Container Image Scanning & v3.12.0+ Signed Immutable Images)](https://nova.docs.fairwinds.com/usage/) — README oficial e Quickstart do Fairwinds Nova detalhando nova find, nova find --containers e migração na v3.12.0+ para imagens assinadas e imutáveis em us-docker.pkg.dev/fairwinds-ops/oss/nova; consultado em 2026-10-03.
- [Fairwinds Nova Official Documentation — Usage & CLI Options (--poll-artifacthub, --desired-versions, --show-errored-containers & JSON Output)](https://nova.docs.fairwinds.com/quickstart/) — Guia oficial de uso do Nova cobrindo flags de CLI, repositórios privados (--url), nova generate-config, --desired-versions, --show-non-semver e estrutura de saída JSON; consultado em 2026-10-03.
- [Fairwinds Nova — Official Documentation Portal](https://raw.githubusercontent.com/FairwindsOps/nova/master/README.md) — Portal oficial de documentação do Fairwinds Nova; consultado em 2026-10-03.
