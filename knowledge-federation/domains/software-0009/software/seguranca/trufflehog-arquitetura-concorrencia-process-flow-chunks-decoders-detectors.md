---
id: software.seguranca.tranche01.000018
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
fontes: ["https://github.com/trufflesecurity/trufflehog/blob/main/CONTRIBUTING.md", "https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/README.md", "https://github.com/trufflesecurity/trufflehog"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# TruffleHog Arquitetura Interna de Concorrência: pipeline de `Sources`, `Chunks`, `Decoders`, `Aho-Corasick` e `Detectors`

## Em uma frase
Conforme detalhado no `CONTRIBUTING.md` e nos documentos de arquitetura do TruffleHog (`docs/process_flow.md` e `docs/concurrency.md`), o motor processa terabytes de dados com alta vazão dividindo o trabalho em um pipeline assíncrono de workers concorrentes: **Sources -> Chunks -> Decoders -> Aho-Corasick Keyword Matching -> Detectors -> Verifiers -> Notifiers**.

## Por que importa
Entender como o pipeline interno divide arquivos em blocos (*chunks*), decodifica formatos (Base64, UTF-16, Gzip) e agenda verificações de rede permite ajustar a concorrência (`--concurrency`) sem esgotar memória ou file descriptors.

## Como funciona
Cada `Source` lê os dados da origem e emite `Chunks`; o estágio de `Decoders` identifica e decodifica codificações aninhadas; um autômato **Aho-Corasick** varre cada chunk em uma única passada procurando as `keywords` de todos os 800+ detectores; e apenas os detectores cujas keywords bateram são acionados em goroutines controladas por `--concurrency`.

## Exemplo
```bash
# Ajustando o número de workers concorrentes e filtrando detectores específicos na execução:
trufflehog git file://. \
  --concurrency=20 \
  --include-detectors="AWS,Github,Slack,Stripe" \
  --results=verified
```

## Limites e trade-offs
As flags `--include-detectors` e `--exclude-detectors` permitem restringir a varredura apenas aos provedores de nuvem e SaaS utilizados pela sua empresa.

## Como verificar
Monitore métricas de execução e logs estruturados ajustando o nível de verbosidade `-v` (`0` a `5`, conforme `CONTRIBUTING.md`).

## Conexões
- [[trufflehog-custom-regex-detectors-webhook-verification-config]] — Veja também: TruffleHog Custom Detectors (`--config`): criação de detectores Regex customizados com verificação via servidor Webhook.
- [[trufflehog-filtros-exclusao-include-paths-exclude-paths-archive-limits]] — Veja também: TruffleHog Filtragem de Escopo e Limites de Arquivos: `--include-paths`, `--exclude-paths` e controle de archives.

## Fontes
- [TruffleHog GitHub — README.md (4 Pillars: Discovery, Classification, Validation & Analysis, --results Filters, CI/CD & Custom Detectors)](https://github.com/trufflesecurity/trufflehog/blob/main/CONTRIBUTING.md) — README oficial do trufflesecurity/trufflehog documentando os 4 pilares, verificação ativa de credenciais, exit code 183 com --fail, verificação Cosign e detectores customizados; consultado em 2026-10-03.
- [TruffleHog GitHub — CONTRIBUTING.md (Architecture of Pipeline Stages, Aho-Corasick Keyword Matching, Detectors & Verification)](https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/README.md) — Guia técnico de arquitetura do TruffleHog detalhando o pipeline concorrente Source -> Chunker -> Matcher Aho-Corasick -> Detector -> Verifier -> Dispatcher; consultado em 2026-10-03.
- [TruffleHog — Official GitHub Repository (Truffle Security)](https://github.com/trufflesecurity/trufflehog) — Repositório oficial open-source do TruffleHog; consultado em 2026-10-03.
