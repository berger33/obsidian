---
id: software.devops.tranche12.001144
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

# Fairwinds Nova: Arquivo de Configuração (nova.yaml), Ignore Lists e Override de Versões Desejadas

## Em uma frase
O comando `nova generate-config --config=nova.yaml` gera um arquivo de configuração declarativo onde equipes de plataforma podem fixar `desired-versions`, ignorar charts ou releases específicos (`chart-ignore-list`, `release-ignore-list`) e padronizar flags de saída.

## Por que importa
Durante janelas em que uma nova versão major de um chart upstream (por exemplo, `ingress-nginx` ou `grafana`) possui incompatibilidades conhecidas com a versão atual do Kubernetes do cluster, a equipe precisa fixar uma versão alvo homologada em vez da última versão absoluta do repositório.

## Como funciona
Por meio da flag `--desired-versions chart=versao` (`-d`) ou do mapa `desired-versions` no `nova.yaml`, o Nova sobrescreve a versão alvo de referência para aquele chart e marca o campo `"overridden": true` na saída JSON. Releases internos que não devem ser comparados com catálogos externos são filtrados com `--chart-ignore-list` ou `--release-ignore-list`.

## Exemplo
```bash
nova generate-config --config=nova.yaml
nova find --config=nova.yaml \
  --desired-versions metrics-server=5.10.10,cert-manager=v1.14.4 \
  --release-ignore-list legacy-internal-app \
  --wide --format table
```

## Limites e trade-offs
Adicionar charts críticos de segurança (como `cert-manager` ou `external-secrets`) em `chart-ignore-list` permanentemente para limpar alertas do relatório esconde dívida técnica e vulnerabilidades reais.

## Como verificar
Prefira usar `desired-versions` documentando o motivo do pin temporário no controle de versão em vez de ocultar o chart com `chart-ignore-list`.

## Conexões
- [[nova-repositorios-helm-privados-artifacthub-poll-url]] — Veja também: Fairwinds Nova: Uso com Repositórios Helm Privados (--url e --poll-artifacthub=false).
- [[nova-containers-errored-non-semver-timeout-diagnostico-registries]] — Veja também: Fairwinds Nova: Diagnóstico de Erros de Registry e Tags Não-SemVer (--show-errored-containers e --show-non-semver).

## Fontes
- [Fairwinds Nova GitHub — README.md & Quickstart (Helm Release & Container Image Scanning & v3.12.0+ Signed Immutable Images)](https://nova.docs.fairwinds.com/usage/) — README oficial e Quickstart do Fairwinds Nova detalhando nova find, nova find --containers e migração na v3.12.0+ para imagens assinadas e imutáveis em us-docker.pkg.dev/fairwinds-ops/oss/nova; consultado em 2026-10-03.
- [Fairwinds Nova Official Documentation — Usage & CLI Options (--poll-artifacthub, --desired-versions, --show-errored-containers & JSON Output)](https://raw.githubusercontent.com/FairwindsOps/nova/master/README.md) — Guia oficial de uso do Nova cobrindo flags de CLI, repositórios privados (--url), nova generate-config, --desired-versions, --show-non-semver e estrutura de saída JSON; consultado em 2026-10-03.
- [Fairwinds Nova — Official Documentation Portal](https://nova.docs.fairwinds.com/quickstart/) — Portal oficial de documentação do Fairwinds Nova; consultado em 2026-10-03.
