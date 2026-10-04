---
id: software.seguranca.tranche01.000017
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

# TruffleHog Custom Detectors (`--config`): criação de detectores Regex customizados com verificação via servidor Webhook

## Em uma frase
Quando uma organização possui formatos próprios de tokens internos ou chaves de API que não fazem parte dos 800+ detectores públicos, o TruffleHog permite definir **Custom Regex Detectors** em um arquivo YAML (`--config`), incluindo suporte a **verificação ativa via Webhook HTTP**.

## Por que importa
Detectar um token interno apenas por regex gera falsos positivos se não houver como validar no serviço interno de IAM se aquela string é realmente um token válido.

## Como funciona
No arquivo de configuração passado em `--config`, você define `detectors` com `name`, `keywords` (pré-filtro Aho-Corasick obrigatório para alta performance), `regex` nomeada e opcionalmente `verify` apontando para um endpoint HTTP interno (`webhook`) que recebe o token capturado e retorna HTTP `200 OK` se o token estiver ativo!

## Exemplo
```yaml
detectors:
  - name: CorpInternalTokenDetector
    keywords:
      - corp_tok_
    regex:
      token: '\b(corp_tok_[a-zA-Z0-9]{40})\b'
    verify:
      - endpoint: https://iam-verifier.internal.corp/verify
        headers:
          - "Authorization: Bearer secret-webhook-token"
```

## Limites e trade-offs
Inclua sempre pelo menos uma string literal distintiva na lista `keywords:` do detector customizado: o motor do TruffleHog só executa a `regex` em trechos de dados onde uma das `keywords` foi encontrada primeiro.

## Como verificar
Execute `trufflehog filesystem ./test-dir --config custom-detectors.yaml --json` para testar seu detector customizado.

## Conexões
- [[trufflehog-verificacao-assinatura-cosign-checksums-supply-chain]] — Veja também: TruffleHog Supply Chain Security: verificação criptográfica de binários e `checksums.txt` com Sigstore `cosign verify-blob`.
- [[trufflehog-arquitetura-concorrencia-process-flow-chunks-decoders-detectors]] — Veja também: TruffleHog Arquitetura Interna de Concorrência: pipeline de `Sources`, `Chunks`, `Decoders`, `Aho-Corasick` e `Detectors`.

## Fontes
- [TruffleHog GitHub — README.md (4 Pillars: Discovery, Classification, Validation & Analysis, --results Filters, CI/CD & Custom Detectors)](https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/README.md) — README oficial do trufflesecurity/trufflehog documentando os 4 pilares, verificação ativa de credenciais, exit code 183 com --fail, verificação Cosign e detectores customizados; consultado em 2026-10-03.
- [TruffleHog GitHub — CONTRIBUTING.md (Architecture of Pipeline Stages, Aho-Corasick Keyword Matching, Detectors & Verification)](https://github.com/trufflesecurity/trufflehog/blob/main/CONTRIBUTING.md) — Guia técnico de arquitetura do TruffleHog detalhando o pipeline concorrente Source -> Chunker -> Matcher Aho-Corasick -> Detector -> Verifier -> Dispatcher; consultado em 2026-10-03.
- [TruffleHog — Official GitHub Repository (Truffle Security)](https://github.com/trufflesecurity/trufflehog) — Repositório oficial open-source do TruffleHog; consultado em 2026-10-03.
