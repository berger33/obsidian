---
id: software.seguranca.tranche05.000408
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

# sqlmap: Otimização de Rede (`-o`, `--keep-alive`, `--null-connection`, `--predict-output`) e Controle de Taxa (`--delay`)

## Em uma frase
O `sqlmap` oferece switches de otimização de tráfego HTTP (`--keep-alive`, `--null-connection`, `--predict-output` e `--threads`, agrupados em `-o`) e controles de cadência (`--delay`, `--timeout`, `--retries`, `--safe-url`).

## Por que importa
Permite reduzir drasticamente a largura de banda consumida durante testes autorizados (usando conexões persistentes e leitura apenas do tamanho `Content-Length` sem baixar o corpo HTML) ou limitar a taxa de requisições para não degradar o ambiente de homologação.

## Como funciona
A flag `--keep-alive` reutiliza conexões TCP/TLS persistentes; `--null-connection` utiliza requisições `HEAD` ou cabeçalhos `Range: bytes=0-0` para comparar o tamanho da resposta em injeções booleanas sem transferir megabytes de HTML; e `--threads=5` (máximo 10) paraleliza a inferência de caracteres em *Boolean-based blind*.

## Exemplo
```bash
# Executar verificação com conexões HTTP persistentes, delay de 0.5s entre requisições e limite de retries
python3 sqlmap.py -u "https://staging.internal.corp/reports?filter=active" \
  -p filter --keep-alive \
  --delay=0.5 --timeout=15 --retries=2 \
  --technique=BE --batch
```

## Limites e trade-offs
A flag `-o` (ou `--threads > 1`) é incompatível com `--delay` e não deve ser usada durante testes *Time-based blind* (`--technique=T`), pois a concorrência de múltiplas queries pesadas no banco distorce as medições de latência e gera falsos positivos.

## Como verificar
Verifique nos logs de tráfego que `--delay=0.5` força execução single-thread cadenciada a no máximo 2 requisições por segundo.

## Conexões
- [[sqlmap-auditoria-privilegios-dba-file-system-os-shell-riscos]] — Veja também: sqlmap: Auditoria de Privilégios Excessivos de SGBD (`--is-dba`, `--privileges`, `--roles` e Vetores de File/OS Access).
- [[sqlmap-api-rest-sqlmapapi-automacao-remota-ipc-json]] — Veja também: sqlmap: Automação Programática com `sqlmapapi.py` (Servidor REST JSON de Tasks Efêmeras).
- [[sqlmap-arquitetura-motor-deteccao-sql-injection-tecnicas-beustq]] — Referência cruzada direta com sqlmap-arquitetura-motor-deteccao-sql-injection-tecnicas-beustq.
- [[sqlmap-calibracao-level-risk-heuristica-falsos-positivos-comparacao]] — Referência cruzada direta com sqlmap-calibracao-level-risk-heuristica-falsos-positivos-comparacao.
- [[ffuf-rate-limiting-threads-delay-stop-flags-sa-sf-se-interativo]] — Referência cruzada direta com ffuf-rate-limiting-threads-delay-stop-flags-sa-sf-se-interativo.

## Fontes
- [sqlmap Official GitHub — README & Architecture](https://raw.githubusercontent.com/sqlmapproject/sqlmap/master/README.md) — documentação oficial do projeto sqlmap cobrindo arquitetura, instalação e escopo; consultado em 2026-10-03.
- [sqlmap Official Wiki — Usage & Switches Reference](https://github.com/sqlmapproject/sqlmap/wiki/Usage) — manual oficial de opções da CLI, técnicas BEUSTQ, --level, --risk, --tamper e OOB DNS; consultado em 2026-10-03.
- [sqlmap Official Documentation — Portuguese Reference](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-pt-BR.md) — referência oficial traduzida do sqlmap; consultado em 2026-10-03.
