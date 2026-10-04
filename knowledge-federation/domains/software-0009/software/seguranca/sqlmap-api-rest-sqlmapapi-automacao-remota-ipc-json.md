---
id: software.seguranca.tranche05.000409
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

# sqlmap: Automação Programática com `sqlmapapi.py` (Servidor REST JSON de Tasks Efêmeras)

## Em uma frase
O repositório oficial do `sqlmap` inclui o servidor e cliente REST **`sqlmapapi.py`**, que expõe o motor de detecção via API HTTP JSON para orquestração automatizada de scans em pipelines de segurança.

## Por que importa
Permite que plataformas internas de DAST criem *tasks* isoladas (`/task/new`), configurem opções tipadas em JSON (`/option/<taskid>/set`), iniciem varreduras assíncronas (`/scan/<taskid>/start`), consultem o status (`/scan/<taskid>/status`) e coletem os achados estruturados (`/scan/<taskid>/data`).

## Como funciona
Por segurança, o servidor `sqlmapapi.py -s` deve escutar exclusivamente na interface de loopback (`-H 127.0.0.1 -p 8775`) ou exigir credenciais administrativas (`--username` / `--password`), limpando as tasks concluídas com `/task/<taskid>/delete`.

## Exemplo
```bash
# Iniciar o servidor REST do sqlmap apenas em loopback e criar uma task via curl
python3 sqlmapapi.py -s -H 127.0.0.1 -p 8775 &

TASK_ID=$(curl -sS http://127.0.0.1:8775/task/new | jq -r '.taskid')
curl -sS -X POST "http://127.0.0.1:8775/scan/${TASK_ID}/start" \
  -H "Content-Type: application/json" \
  -d '{"url":"https://staging.internal.corp/items?id=1","technique":"BE","level":1,"risk":1}'
```

## Limites e trade-offs
Expor `sqlmapapi.py -s -H 0.0.0.0` em uma rede acessível sem autenticação permite que qualquer atacante utilize o servidor como proxy de ataque ou leia arquivos locais via opções da task.

## Como verificar
Verifique com `ss -tulnp | grep 8775` que o `sqlmapapi.py` está vinculado estritamente a `127.0.0.1:8775` e encerre a task após ler `/scan/<taskid>/data`.

## Conexões
- [[sqlmap-otimizacao-threads-keep-alive-null-connection-rate-delay]] — Veja também: sqlmap: Otimização de Rede (`-o`, `--keep-alive`, `--null-connection`, `--predict-output`) e Controle de Taxa (`--delay`).
- [[sqlmap-validacao-remediacao-prepared-statements-ci-non-interactive]] — Veja também: sqlmap: Validação de Remediação (Prepared Statements / Parameterized Queries) e Regressão em CI/CD (`--batch` e `--results-file`).
- [[sqlmap-arquitetura-motor-deteccao-sql-injection-tecnicas-beustq]] — Referência cruzada direta com sqlmap-arquitetura-motor-deteccao-sql-injection-tecnicas-beustq.
- [[dalfox-modos-server-rest-api-mcp-stdio-integracao-automacao]] — Referência cruzada direta com dalfox-modos-server-rest-api-mcp-stdio-integracao-automacao.

## Fontes
- [sqlmap Official GitHub — README & Architecture](https://raw.githubusercontent.com/sqlmapproject/sqlmap/master/README.md) — documentação oficial do projeto sqlmap cobrindo arquitetura, instalação e escopo; consultado em 2026-10-03.
- [sqlmap Official Wiki — Usage & Switches Reference](https://github.com/sqlmapproject/sqlmap/wiki/Usage) — manual oficial de opções da CLI, técnicas BEUSTQ, --level, --risk, --tamper e OOB DNS; consultado em 2026-10-03.
- [sqlmap Official Documentation — Portuguese Reference](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-pt-BR.md) — referência oficial traduzida do sqlmap; consultado em 2026-10-03.
