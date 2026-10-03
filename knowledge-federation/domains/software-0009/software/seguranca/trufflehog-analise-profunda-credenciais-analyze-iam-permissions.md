---
id: software.seguranca.tranche01.000014
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

# TruffleHog Credential Analysis (`trufflehog analyze`): mapeamento de identidade, recursos acessíveis e permissões de chaves vazadas

## Em uma frase
O quarto pilar do TruffleHog — **Analysis (`trufflehog analyze`)** — vai além de responder "esta chave está ativa?" para os mais de 20 tipos de credenciais mais vazados do mercado: ele interroga de forma não-destrutiva as APIs do provedor para descobrir **quem criou a chave, a quais recursos ela tem acesso e quais permissões específicas ela detém**.

## Por que importa
Durante um incidente de segurança às 02:00 da manhã, encontrar uma chave da AWS, GCP, GitHub ou Stripe ativa levanta imediatamente a pergunta: "é uma chave somente-leitura de um bucket de homologação ou um token de administrador de produção?".

## Como funciona
Ao executar o analisador do TruffleHog para a credencial identificada, a ferramenta emite um relatório detalhado enumerando a conta/organização proprietária, os papéis/escopos anexados e a superfície de impacto (*blast radius*), acelerando a triagem e a contenção pelo SOC.

## Exemplo
```bash
# Iniciando o analisador interativo do TruffleHog para inspecionar as permissões de uma credencial:
trufflehog analyze
```

## Limites e trade-offs
Execute o `trufflehog analyze` apenas sobre credenciais pertencentes à sua própria organização ou dentro do escopo formalmente autorizado de um pentest / programa de Bug Bounty.

## Como verificar
Consulte a documentação de comando com `trufflehog analyze --help`.

## Conexões
- [[trufflehog-verificacao-ativa-credenciais-results-verified-unverified-no-verification]] — Veja também: TruffleHog Políticas de Verificação: controle de `--results=verified,unknown,unverified` e modo offline `--no-verification`.
- [[trufflehog-ci-cd-github-actions-gitlab-ci-since-commit-branch-fail]] — Veja também: TruffleHog em Pipelines CI/CD: varredura diferencial com `--since-commit`, `--branch` e código de saída `--fail` (`183`).

## Fontes
- [TruffleHog GitHub — README.md (4 Pillars: Discovery, Classification, Validation & Analysis, --results Filters, CI/CD & Custom Detectors)](https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/README.md) — README oficial do trufflesecurity/trufflehog documentando os 4 pilares, verificação ativa de credenciais, exit code 183 com --fail, verificação Cosign e detectores customizados; consultado em 2026-10-03.
- [TruffleHog GitHub — CONTRIBUTING.md (Architecture of Pipeline Stages, Aho-Corasick Keyword Matching, Detectors & Verification)](https://github.com/trufflesecurity/trufflehog/blob/main/CONTRIBUTING.md) — Guia técnico de arquitetura do TruffleHog detalhando o pipeline concorrente Source -> Chunker -> Matcher Aho-Corasick -> Detector -> Verifier -> Dispatcher; consultado em 2026-10-03.
- [TruffleHog — Official GitHub Repository (Truffle Security)](https://github.com/trufflesecurity/trufflehog) — Repositório oficial open-source do TruffleHog; consultado em 2026-10-03.
