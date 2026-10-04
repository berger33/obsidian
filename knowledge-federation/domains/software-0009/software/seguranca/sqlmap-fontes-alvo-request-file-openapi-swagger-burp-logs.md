---
id: software.seguranca.tranche05.000403
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
fontes: ["https://raw.githubusercontent.com/sqlmapproject/sqlmap/master/README.md", "https://github.com/sqlmapproject/sqlmap/wiki/Usage", "https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-pt-BR.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# sqlmap: Ingestão de Alvos via Requisição Raw (`-r`), Especificações `--openapi`, Marcadores `*` e Logs de Proxy (`-l`)

## Em uma frase
Além de URLs simples (`-u`), o `sqlmap` ingere requisições HTTP completas capturadas em arquivo (`-r req.http`), especificações OpenAPI/Swagger (`--openapi`), logs de proxies Burp/ZAP (`-l`) e pontos de injeção arbitrários demarcados pelo caractere asterisco (`*`).

## Por que importa
APIs modernas utilizam JSON aninhado, XML/SOAP, GraphQL ou parâmetros embutidos em rotas REST (`/api/v2/orgs/12/invoices/99`) onde a sintaxe tradicional `?id=1` não existe.

## Como funciona
Ao inserir o marcador `*` diretamente no caminho da URL (`https://api.corp/v2/users/*/profile`) ou dentro de uma chave específica de um arquivo `-r request.http` contendo JSON/XML, o `sqlmap` injeta os payloads exatamente na posição do asterisco. Já `--openapi=https://api.corp/openapi.json` (combinado com `--openapi-base` e `--openapi-tags`) deriva automaticamente todas as rotas e parâmetros documentados na especificação.

## Exemplo
```bash
# Auditar rotas derivadas diretamente de uma especificação OpenAPI 3.0 filtrando pela tag "billing"
python3 sqlmap.py --openapi="https://api.staging.corp/v3/api-docs.json" \
  --openapi-base="https://api.staging.corp" \
  --openapi-tags="billing" \
  --technique=BE --level=1 --risk=1 --batch
```

## Limites e trade-offs
Ao usar `-r request.http` com sessões autenticadas, lembre-se de excluir o parâmetro de sessão ou token CSRF dos testes de injeção usando `--param-exclude="csrf|session|token"` para não invalidar a própria sessão no primeiro payload.

## Como verificar
Execute `python3 sqlmap.py -r /tmp/search-json.http -p query --batch --parse-errors` e confirme que o parser identifica `JSON` e injeta apenas na propriedade indicada.

## Conexões
- [[sqlmap-calibracao-level-risk-heuristica-falsos-positivos-comparacao]] — Veja também: sqlmap: Calibração de `--level` (1–5), `--risk` (1–3) e Ancoragem de Comparação (`--string`, `--code`, `--text-only`).
- [[sqlmap-injecao-second-order-csrf-tokens-sessoes-autenticadas]] — Veja também: sqlmap: Detecção de *Second-Order SQL Injection* (`--second-url`), Renovação de `--csrf-token` e `--eval`.
- [[sqlmap-arquitetura-motor-deteccao-sql-injection-tecnicas-beustq]] — Referência cruzada direta com sqlmap-arquitetura-motor-deteccao-sql-injection-tecnicas-beustq.
- [[httpxpd-matchers-filters-status-length-string-regex-cdn-time]] — Referência cruzada direta com httpxpd-matchers-filters-status-length-string-regex-cdn-time.

## Fontes
- [sqlmap Official GitHub — README & Architecture](https://raw.githubusercontent.com/sqlmapproject/sqlmap/master/README.md) — documentação oficial do projeto sqlmap cobrindo arquitetura, instalação e escopo; consultado em 2026-10-03.
- [sqlmap Official Wiki — Usage & Switches Reference](https://github.com/sqlmapproject/sqlmap/wiki/Usage) — manual oficial de opções da CLI, técnicas BEUSTQ, --level, --risk, --tamper e OOB DNS; consultado em 2026-10-03.
- [sqlmap Official Documentation — Portuguese Reference](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-pt-BR.md) — referência oficial traduzida do sqlmap; consultado em 2026-10-03.
