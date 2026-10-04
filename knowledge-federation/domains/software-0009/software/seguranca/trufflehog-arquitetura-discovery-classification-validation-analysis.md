---
id: software.seguranca.tranche01.000011
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/README.md", "https://github.com/trufflesecurity/trufflehog/blob/main/CONTRIBUTING.md", "https://github.com/trufflesecurity/trufflehog"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# TruffleHog: arquitetura dos 4 pilares (`Discovery`, `Classification`, `Validation` e `Analysis`) para credenciais vazadas

## Em uma frase
O **TruffleHog** (mantido pela Truffle Security sob licença AGPL-3.0) é uma plataforma e CLI de segurança de credenciais estruturada em quatro etapas: **Discovery** (descoberta em dezenas de fontes), **Classification** (classificação em mais de 800 tipos de segredos), **Validation** (verificação ativa se a credencial está viva) e **Analysis** (mapeamento de permissões e recursos acessíveis).

## Por que importa
Scanners baseados apenas em regex/entropia geram centenas de alertas sobre chaves revogadas há anos ou strings aleatórias, fazendo a equipe de resposta a incidentes perder horas investigando falsos positivos.

## Como funciona
Conforme o README oficial do TruffleHog: 1) **Discovery** extrai candidatos de Git, GitHub, GitLab, S3, GCS, Docker images, Filesystems, Postman, Jenkins, Elasticsearch, Jira e Slack; 2) **Classification** identifica a qual serviço exatamente o segredo pertence (AWS, Stripe, Cloudflare, Postgres, chave privada SSL); 3) **Validation** tenta autenticar de forma segura contra a API do provedor para confirmar se o segredo está **ativo (`verified`)**; e 4) **Analysis** detalha quem criou a chave e quais permissões ela possui.

## Exemplo
```bash
# Escaneando um repositório Git exibindo exclusivamente credenciais ativas confirmadas (verified):
trufflehog git https://github.com/trufflesecurity/test_keys --results=verified
```

## Limites e trade-offs
Focar os alertas críticos de PagerDuty/SOC em `--results=verified` elimina o ruído de chaves de teste inválidas e prioriza credenciais que representam risco imediato de invasão.

## Como verificar
Execute `trufflehog --version` e teste a detecção verificada contra o repositório de chaves de demonstração `trufflesecurity/test_keys`.

## Conexões
- [[trufflehog-fontes-varredura-git-github-gitlab-s3-gcs-docker-filesystem]] — Veja também: TruffleHog Fontes de Varredura: inspeção nativa de `git`, `github`, `gitlab`, `s3`, `gcs`, `docker` (camadas OCI) e `filesystem`.

## Fontes
- [TruffleHog GitHub — README.md (4 Pillars: Discovery, Classification, Validation & Analysis, --results Filters, CI/CD & Custom Detectors)](https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/README.md) — README oficial do trufflesecurity/trufflehog documentando os 4 pilares, verificação ativa de credenciais, exit code 183 com --fail, verificação Cosign e detectores customizados; consultado em 2026-10-03.
- [TruffleHog GitHub — CONTRIBUTING.md (Architecture of Pipeline Stages, Aho-Corasick Keyword Matching, Detectors & Verification)](https://github.com/trufflesecurity/trufflehog/blob/main/CONTRIBUTING.md) — Guia técnico de arquitetura do TruffleHog detalhando o pipeline concorrente Source -> Chunker -> Matcher Aho-Corasick -> Detector -> Verifier -> Dispatcher; consultado em 2026-10-03.
- [TruffleHog — Official GitHub Repository (Truffle Security)](https://github.com/trufflesecurity/trufflehog) — Repositório oficial open-source do TruffleHog; consultado em 2026-10-03.
