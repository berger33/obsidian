---
id: software.seguranca.tranche05.000402
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

# sqlmap: Calibração de `--level` (1–5), `--risk` (1–3) e Ancoragem de Comparação (`--string`, `--code`, `--text-only`)

## Em uma frase
O `sqlmap` controla a profundidade dos vetores testados através de `--level` (`1` a `5`, padrão `1`) e a probabilidade de efeitos colaterais das cláusulas SQL através de `--risk` (`1` a `3`, padrão `1`), estabilizando a comparação booleana com `--string`, `--not-string`, `--regexp`, `--code` ou `--text-only`.

## Por que importa
Compreender a matriz `level × risk` evita tanto falsos negativos (quando a injeção reside em cabeçalhos `Cookie`, `User-Agent`, `Referer` ou `Host` só testados em níveis superiores) quanto sobrecarga desnecessária ou queries `OR` pesadas.

## Como funciona
Em `--level=2`, o `sqlmap` passa a testar cookies HTTP; em `--level=3`, inclui `User-Agent` e `Referer`; e em `--level=5`, testa o cabeçalho `Host` e centenas de limites de delimitadores (`prefix`/`suffix`). Já `--risk=2` adiciona testes *time-based* pesados e `--risk=3` adiciona payloads `OR`-based (que em cláusulas `UPDATE` ou `DELETE` sem filtro poderiam afetar todas as linhas de uma tabela se a aplicação não usar transações seguras).

## Exemplo
```bash
# Testar parâmetro com ancoragem explícita na string de resposta verdadeira para evitar ruído de página dinâmica
python3 sqlmap.py -u "https://staging.internal.corp/catalog?item=105" \
  -p item --level=2 --risk=1 \
  --string="Produto em estoque" --text-only --batch
```

## Limites e trade-offs
Nunca execute `--risk=3` contra endpoints HTTP que realizem operações de escrita (`POST`, `PUT`, `DELETE`) ou atualizem tabelas de usuários, pois um payload `OR 1=1` em uma cláusula `WHERE` de `UPDATE` altera todos os registros da tabela.

## Como verificar
Verifique com `-v 3` os payloads exatos enviados pelo `sqlmap` em `--risk=1` e confirme que nenhuma cláusula `OR` tautológica ampla é injetada.

## Conexões
- [[sqlmap-arquitetura-motor-deteccao-sql-injection-tecnicas-beustq]] — Veja também: sqlmap: Arquitetura do Motor de Detecção de SQL Injection e as Seis Técnicas (`--technique=BEUSTQ`).
- [[sqlmap-fontes-alvo-request-file-openapi-swagger-burp-logs]] — Veja também: sqlmap: Ingestão de Alvos via Requisição Raw (`-r`), Especificações `--openapi`, Marcadores `*` e Logs de Proxy (`-l`).
- [[sqlmap-injecao-second-order-csrf-tokens-sessoes-autenticadas]] — Referência cruzada direta com sqlmap-injecao-second-order-csrf-tokens-sessoes-autenticadas.
- [[sqlmap-otimizacao-threads-keep-alive-null-connection-rate-delay]] — Referência cruzada direta com sqlmap-otimizacao-threads-keep-alive-null-connection-rate-delay.

## Fontes
- [sqlmap Official GitHub — README & Architecture](https://raw.githubusercontent.com/sqlmapproject/sqlmap/master/README.md) — documentação oficial do projeto sqlmap cobrindo arquitetura, instalação e escopo; consultado em 2026-10-03.
- [sqlmap Official Wiki — Usage & Switches Reference](https://github.com/sqlmapproject/sqlmap/wiki/Usage) — manual oficial de opções da CLI, técnicas BEUSTQ, --level, --risk, --tamper e OOB DNS; consultado em 2026-10-03.
- [sqlmap Official Documentation — Portuguese Reference](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-pt-BR.md) — referência oficial traduzida do sqlmap; consultado em 2026-10-03.
