---
id: software.devops.tranche12.001143
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
fontes: ["https://nova.docs.fairwinds.com/usage/", "https://raw.githubusercontent.com/FairwindsOps/nova/master/README.md", "https://nova.docs.fairwinds.com/quickstart/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Fairwinds Nova: Uso com Repositórios Helm Privados (--url e --poll-artifacthub=false)

## Em uma frase
O Nova suporta auditoria de charts hospedados em repositórios Helm privados ou internos por meio da flag `--url` (`-u`) combinada com as credenciais já configuradas no `helm repo` local e a opção `--poll-artifacthub=false` para ambientes restritos.

## Por que importa
Em empresas que espelham todos os charts de terceiros em um Harbor, Artifactory ou ChartMuseum interno ou rodam em redes air-gapped sem saída para a internet pública, consultar o ArtifactHub externo falha por bloqueio de firewall ou retorna versões que ainda não foram homologadas internamente.

## Como funciona
Ao passar `--poll-artifacthub=false -u https://charts.internal.corp/stable -u https://charts.internal.corp/platform`, o Nova reutiliza a autenticação configurada no ambiente local do Helm e compara as releases instaladas no cluster exclusivamente contra os índices (`index.yaml`) dos repositórios internos autorizados.

## Exemplo
```bash
helm repo add internal-platform https://charts.internal.corp/platform
nova find --poll-artifacthub=false \
  --url https://charts.internal.corp/platform \
  --wide --format table
```

## Limites e trade-offs
Deixar `--poll-artifacthub=true` (valor padrão) em clusters que utilizam nomes de charts internos genéricos (como `api` ou `worker`) pode gerar falsos positivos ao casar o nome do release interno com um chart público homônimo no ArtifactHub.

## Como verificar
Desative `--poll-artifacthub=false` quando auditar charts proprietários ou espelhos internos e liste explicitamente as URLs dos repositórios corporativos via `--url`.

## Conexões
- [[nova-auditoria-imagens-containers-semver-minor-patch]] — Veja também: Fairwinds Nova: Auditoria de Imagens de Containers Desatualizadas com --containers.
- [[nova-configuracao-declarativa-generate-config-desired-versions]] — Veja também: Fairwinds Nova: Arquivo de Configuração (nova.yaml), Ignore Lists e Override de Versões Desejadas.

## Fontes
- [Fairwinds Nova GitHub — README.md & Quickstart (Helm Release & Container Image Scanning & v3.12.0+ Signed Immutable Images)](https://nova.docs.fairwinds.com/usage/) — README oficial e Quickstart do Fairwinds Nova detalhando nova find, nova find --containers e migração na v3.12.0+ para imagens assinadas e imutáveis em us-docker.pkg.dev/fairwinds-ops/oss/nova; consultado em 2026-10-03.
- [Fairwinds Nova Official Documentation — Usage & CLI Options (--poll-artifacthub, --desired-versions, --show-errored-containers & JSON Output)](https://raw.githubusercontent.com/FairwindsOps/nova/master/README.md) — Guia oficial de uso do Nova cobrindo flags de CLI, repositórios privados (--url), nova generate-config, --desired-versions, --show-non-semver e estrutura de saída JSON; consultado em 2026-10-03.
- [Fairwinds Nova — Official Documentation Portal](https://nova.docs.fairwinds.com/quickstart/) — Portal oficial de documentação do Fairwinds Nova; consultado em 2026-10-03.
