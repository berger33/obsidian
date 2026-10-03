---
id: software.devops.tranche12.001145
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

# Fairwinds Nova: Diagnóstico de Erros de Registry e Tags Não-SemVer (--show-errored-containers e --show-non-semver)

## Em uma frase
Quando o Nova escaneia imagens de containers com `--containers`, as flags `--show-errored-containers`, `--show-non-semver` e `--timeout` permitem diagnosticar falhas de autenticação/rede em registries privados e identificar workloads que não utilizam versionamento semântico.

## Por que importa
Por padrão, o `nova find --containers` captura erros de conexão com registries silenciosamente e omite tags não-SemVer para não quebrar a execução, o que pode fazer o operador acreditar que todas as imagens privadas estão atualizadas quando na verdade não foram escaneadas.

## Como funciona
Habilitar `--show-errored-containers` exibe na saída exatamente quais imagens retornaram erro de autenticação, rate limit ou timeout ao consultar o registry remoto. Para imagens com milhares de tags no repositório remoto, ajustar `--timeout 30` evita cancelamentos prematuros (o padrão é 10 segundos).

## Exemplo
```bash
nova find --containers \
  --show-errored-containers \
  --show-non-semver \
  --timeout 30 \
  --format table
```

## Limites e trade-offs
Ignorar a verificação com `--show-errored-containers` em clusters que puxam imagens de registries privados ou do Docker Hub sem credenciais autenticadas resulta em cobertura de auditoria incompleta por rate limiting.

## Como verificar
Execute periodicamente `nova find --containers --show-errored-containers` para validar se o scanner possui acesso de leitura e timeout suficiente para todos os registries utilizados pelo cluster.

## Conexões
- [[nova-configuracao-declarativa-generate-config-desired-versions]] — Veja também: Fairwinds Nova: Arquivo de Configuração (nova.yaml), Ignore Lists e Override de Versões Desejadas.
- [[nova-migracao-registry-imagens-assinadas-imutaveis-pkg-dev]] — Veja também: Fairwinds Nova: Migração de Registry (us-docker.pkg.dev) e Imagens Assinadas e Imutáveis.

## Fontes
- [Fairwinds Nova GitHub — README.md & Quickstart (Helm Release & Container Image Scanning & v3.12.0+ Signed Immutable Images)](https://nova.docs.fairwinds.com/usage/) — README oficial e Quickstart do Fairwinds Nova detalhando nova find, nova find --containers e migração na v3.12.0+ para imagens assinadas e imutáveis em us-docker.pkg.dev/fairwinds-ops/oss/nova; consultado em 2026-10-03.
- [Fairwinds Nova Official Documentation — Usage & CLI Options (--poll-artifacthub, --desired-versions, --show-errored-containers & JSON Output)](https://raw.githubusercontent.com/FairwindsOps/nova/master/README.md) — Guia oficial de uso do Nova cobrindo flags de CLI, repositórios privados (--url), nova generate-config, --desired-versions, --show-non-semver e estrutura de saída JSON; consultado em 2026-10-03.
- [Fairwinds Nova — Official Documentation Portal](https://nova.docs.fairwinds.com/quickstart/) — Portal oficial de documentação do Fairwinds Nova; consultado em 2026-10-03.
