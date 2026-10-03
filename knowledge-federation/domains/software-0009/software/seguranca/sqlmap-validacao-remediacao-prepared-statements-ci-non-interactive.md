---
id: software.seguranca.tranche05.000410
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

# sqlmap: Validação de Remediação (Prepared Statements / Parameterized Queries) e Regressão em CI/CD (`--batch` e `--results-file`)

## Em uma frase
Após corrigir uma vulnerabilidade de SQL Injection substituindo concatenação de strings por *Prepared Statements* (consultas parametrizadas) e validação estrita de tipos/allowlists para identificadores (`ORDER BY`), o `sqlmap` é usado em modo não-interativo (`--batch`) para comprovar a eficácia da correção.

## Por que importa
Apenas adicionar um filtro de palavras-chave (`REPLACE(input, "'", "")`) frequentemente deixa brechas exploráveis por codificação ou injeção numérica; reexecutar o `sqlmap` com `--flush-session` comprova empiricamente que o ponto de injeção foi eliminado.

## Como funciona
Em testes de regressão de segurança, o comando é executado com `--batch --flush-session --output-dir=/tmp/sqlmap-ci --results-file=/tmp/sqlmap-ci/results.csv`, falhando o job de verificação caso o arquivo `results.csv` registre qualquer ponto vulnerável encontrado.

## Exemplo
```bash
# Revalidar endpoint após refatoração para Prepared Statements garantindo zero vulnerabilidades no CSV
python3 sqlmap.py -u "https://staging.internal.corp/orders?id=42&sort=created_at" \
  -p id,sort --level=3 --risk=2 \
  --batch --flush-session \
  --results-file=/tmp/sqlmap-regression.csv

test $(wc -l < /tmp/sqlmap-regression.csv) -le 1
```

## Limites e trade-offs
Prepared Statements parametrizam **valores** (`WHERE id = $1`), mas o protocolo de banco de dados não aceita parâmetros de bind para nomes de tabelas, nomes de colunas ou direção `ASC`/`DESC` em `ORDER BY`; esses identificadores devem ser validados contra uma *allowlist* estática no código antes da query.

## Como verificar
Confirme que o log final do `sqlmap` imprime `all tested parameters do not appear to be injectable` e que `/tmp/sqlmap-regression.csv` contém apenas a linha de cabeçalho.

## Conexões
- [[sqlmap-api-rest-sqlmapapi-automacao-remota-ipc-json]] — Veja também: sqlmap: Automação Programática com `sqlmapapi.py` (Servidor REST JSON de Tasks Efêmeras).
- [[sqlmap-arquitetura-motor-deteccao-sql-injection-tecnicas-beustq]] — Referência cruzada direta com sqlmap-arquitetura-motor-deteccao-sql-injection-tecnicas-beustq.
- [[brakeman-prevencao-sql-injection-activerecord-interpolacao-arel]] — Referência cruzada direta com brakeman-prevencao-sql-injection-activerecord-interpolacao-arel.
- [[gosec-taint-analysis-g701-a-g710-sqli-cmdi-ssrf-xss-path-traversal]] — Referência cruzada direta com gosec-taint-analysis-g701-a-g710-sqli-cmdi-ssrf-xss-path-traversal.

## Fontes
- [sqlmap Official GitHub — README & Architecture](https://raw.githubusercontent.com/sqlmapproject/sqlmap/master/README.md) — documentação oficial do projeto sqlmap cobrindo arquitetura, instalação e escopo; consultado em 2026-10-03.
- [sqlmap Official Wiki — Usage & Switches Reference](https://github.com/sqlmapproject/sqlmap/wiki/Usage) — manual oficial de opções da CLI, técnicas BEUSTQ, --level, --risk, --tamper e OOB DNS; consultado em 2026-10-03.
- [sqlmap Official Documentation — Portuguese Reference](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-pt-BR.md) — referência oficial traduzida do sqlmap; consultado em 2026-10-03.
