---
id: software.seguranca.tranche05.000401
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

# sqlmap: Arquitetura do Motor de Detecção de SQL Injection e as Seis Técnicas (`--technique=BEUSTQ`)

## Em uma frase
`sqlmap` (GPLv2, Python 2.7/3.x) é a ferramenta open-source padrão para detecção automatizada, validação de explorabilidade e auditoria de vulnerabilidades de SQL Injection em múltiplos SGBDs (PostgreSQL, MySQL/MariaDB, Oracle, Microsoft SQL Server, SQLite, IBM DB2, CockroachDB).

## Por que importa
Permite validar com rigor técnico se um ponto de entrada suspeito sofre realmente de SQL Injection e por qual mecanismo o banco responde, diferenciando reflexões inofensivas de injeções exploráveis em testes autorizados.

## Como funciona
O motor de detecção avalia seis técnicas selecionáveis via `--technique=BEUSTQ`: **B** (*Boolean-based blind*, comparando respostas verdadeiras/falsas), **E** (*Error-based*, extraindo dados em mensagens de erro do SGBD), **U** (*UNION query-based*, concatenando resultados na mesma tabela), **S** (*Stacked queries*, executando múltiplas instruções separadas por `;`), **T** (*Time-based blind*, medindo atrasos de `SLEEP`/`PG_SLEEP`) e **Q** (*Inline queries*, subqueries embutidas).

## Exemplo
```bash
# Testar exclusivamente técnicas rápidas e seguras (Boolean e Error-based) sem Stacked Queries
python3 sqlmap.py -u "https://staging.internal.corp/orders?id=42" \
  -p id --technique=BE \
  --dbms=PostgreSQL --batch --flush-session
```

## Limites e trade-offs
Habilitar a técnica `S` (*Stacked queries*) em ambientes de homologação compartilhados pode acionar procedures ou modificar estado se combinada com opções de escrita; restrinja `--technique=BEU` durante triagens não destrutivas.

## Como verificar
Execute `python3 sqlmap.py --version` e rode o teste contra um laboratório local validando no log o banner do SGBD (`--banner`) sem erros de sintaxe.

## Conexões
- [[sqlmap-calibracao-level-risk-heuristica-falsos-positivos-comparacao]] — Veja também: sqlmap: Calibração de `--level` (1–5), `--risk` (1–3) e Ancoragem de Comparação (`--string`, `--code`, `--text-only`).
- [[sqlmap-fontes-alvo-request-file-openapi-swagger-burp-logs]] — Referência cruzada direta com sqlmap-fontes-alvo-request-file-openapi-swagger-burp-logs.
- [[sqlmap-validacao-remediacao-prepared-statements-ci-non-interactive]] — Referência cruzada direta com sqlmap-validacao-remediacao-prepared-statements-ci-non-interactive.

## Fontes
- [sqlmap Official GitHub — README & Architecture](https://raw.githubusercontent.com/sqlmapproject/sqlmap/master/README.md) — documentação oficial do projeto sqlmap cobrindo arquitetura, instalação e escopo; consultado em 2026-10-03.
- [sqlmap Official Wiki — Usage & Switches Reference](https://github.com/sqlmapproject/sqlmap/wiki/Usage) — manual oficial de opções da CLI, técnicas BEUSTQ, --level, --risk, --tamper e OOB DNS; consultado em 2026-10-03.
- [sqlmap Official Documentation — Portuguese Reference](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-pt-BR.md) — referência oficial traduzida do sqlmap; consultado em 2026-10-03.
