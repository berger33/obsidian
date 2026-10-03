---
id: software.seguranca.tranche05.000418
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/hahwul/dalfox/main/README.md", "https://dalfox.hahwul.com/reference/cli/", "https://github.com/hahwul/dalfox/releases"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Dalfox: Operação em Pipeline (`--input-type pipe`), Deduplicação (`--dedup-urls signature`) e Retomada (`--state-file`)

## Em uma frase
Em pipelines de reconhecimento contínuo (`subfinder | httpx | katana | dalfox`), o Dalfox consome milhares de URLs via `stdin` (`--input-type pipe`), colapsa rotas com mesma assinatura de parâmetros (`--dedup-urls signature`) e salva o progresso em `--state-file` para retomada resiliente.

## Por que importa
Sem `--dedup-urls signature`, se um crawler fornecer 500 URLs `/product?id=1` até `/product?id=500`, o scanner testaria os mesmos payloads XSS 500 vezes contra o mesmo controlador; o modo `signature` testa a combinação `caminho + nomes de parâmetros` uma única vez.

## Como funciona
Adicionalmente, `--state-file /var/lib/dast/dalfox.state` grava o *fingerprint* de cada alvo concluído (ignorando variações de cookies/headers globais de sessão renovada), permitindo que uma varredura interrompida retome exatamente de onde parou sem reescanear os alvos anteriores.

## Exemplo
```bash
# Encadear katana com dalfox deduplicando assinaturas de parâmetros e persistindo estado de execução
katana -u https://app.staging.corp -d 3 -jc -f qurl -silent \
  | dalfox scan --input-type pipe \
    --dedup-urls signature \
    --state-file /tmp/dalfox-staging.state \
    --silence --format jsonl --output /tmp/dalfox-pipeline.jsonl
```

## Limites e trade-offs
Se os valores específicos dos parâmetros de entrada alteram a rota interna do backend (ex.: `?action=view_profile` vs `?action=list_orders`), usar `--dedup-urls signature` descartará a segunda variação; nesses casos de *front-controller*, use `--dedup-urls exact`.

## Como verificar
Execute o comando duas vezes seguidas com o mesmo `--state-file` e confirme que a segunda execução pula imediatamente os alvos já concluídos.

## Conexões
- [[dalfox-waf-fingerprinting-evasao-custom-payloads-encoders]] — Veja também: Dalfox: Fingerprinting de WAF (`--waf-min-confidence`), Rastreamento de Bypass e `--custom-payload`.
- [[dalfox-modos-server-rest-api-mcp-stdio-integracao-automacao]] — Veja também: Dalfox: Subcomandos `dalfox server` (REST API) e `dalfox mcp` (Model Context Protocol stdio Server).
- [[dalfox-arquitetura-scanner-xss-analise-parametros-rust-go]] — Referência cruzada direta com dalfox-arquitetura-scanner-xss-analise-parametros-rust-go.
- [[katana-extracao-campos-field-extraction-custom-regex-jsonl]] — Referência cruzada direta com katana-extracao-campos-field-extraction-custom-regex-jsonl.
- [[httpxpd-encadeamento-dast-subfinder-httpx-katana-nuclei]] — Referência cruzada direta com httpxpd-encadeamento-dast-subfinder-httpx-katana-nuclei.

## Fontes
- [Dalfox Official GitHub — README & Key Features](https://raw.githubusercontent.com/hahwul/dalfox/main/README.md) — documentação oficial do Dalfox cobrindo subcomandos, parameter mining, DOM/AST e WAF; consultado em 2026-10-03.
- [Dalfox Official Documentation — CLI Reference](https://dalfox.hahwul.com/reference/cli/) — referência completa de flags, exit codes, monitoramento de sessão, escopo e baseline; consultado em 2026-10-03.
- [Dalfox GitHub Releases](https://github.com/hahwul/dalfox/releases) — notas de versão e distribuição oficial do Dalfox; consultado em 2026-10-03.
