---
id: software.seguranca.tranche02.000112
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-02.md"
fontes: ["https://coreruleset.org/docs/2-how-crs-works/2-1-anomaly_scoring/", "https://raw.githubusercontent.com/coreruleset/coreruleset/main/README.md", "https://github.com/coreruleset/coreruleset"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OWASP CRS Anomaly Scoring Mode: detecção colaborativa (`setvar`) e bloqueio adiado em `949` (Inbound) e `959` (Outbound)

## Em uma frase
Conforme documentado na página oficial *Anomaly Scoring* do CRS (`coreruleset.org/docs/2-how-crs-works/2-1-anomaly_scoring/`), o modo de **Pontuação de Anomalia (*Anomaly Scoring Mode*)** desacopla a lógica de **detecção** da ação de **bloqueio**, combinando *Collaborative Detection* com *Delayed Blocking*.

## Por que importa
No modo tradicional legado (*Self-Contained Mode*), a primeira regra que casasse bloqueava imediatamente a requisição, impedindo você de saber quais outras regras teriam disparado e causando bloqueios abruptos por uma única violação menor de protocolo.

## Como funciona
No *Anomaly Scoring Mode*: 1) cada regra de detecção que casa apenas incrementa uma variável transacional de pontuação via `setvar:'tx.anomaly_score_pl1=+%{tx.critical_anomaly_score}'` e registra o log; 2) ao final das regras de requisição, o arquivo **`REQUEST-949-BLOCKING-EVALUATION.conf`** soma a pontuação inbound total e bloqueia se ela atingir o `tx.inbound_anomaly_score_threshold`; e 3) ao final das regras de resposta, o arquivo **`RESPONSE-959-BLOCKING-EVALUATION.conf`** avalia a pontuação outbound contra `tx.outbound_anomaly_score_threshold`!

## Exemplo
```apache
# Exemplo oficial da documentação do CRS mostrando como uma regra incrementa o anomaly score por nível de paranoia:
SecRule REQUEST_HEADERS:Content-Length "!@rx ^\d+$" \
    "id:920160,\
    phase:1,\
    block,\
    t:none,\
    msg:'Content-Length HTTP header is not numeric',\
    tag:'paranoia-level/1',\
    severity:'CRITICAL',\
    setvar:'tx.anomaly_score_pl1=+%{tx.critical_anomaly_score}'"
```

## Limites e trade-offs
Note que, quando o bloqueio ocorre no `RESPONSE-959-BLOCKING-EVALUATION.conf` (Outbound), a requisição **já foi processada pelo backend**, mas a resposta contendo o vazamento (ex.: stack trace SQL ou código-fonte) é impedida de chegar ao cliente.

## Como verificar
Inspecione nos logs a regra `949110` (*Inbound Anomaly Score Exceeded*) para ver a soma final que disparou o bloqueio.

## Conexões
- [[owaspcrs-arquitetura-core-rule-set-v4-protecao-owasp-top-ten]] — Veja também: OWASP CRS (Core Rule Set v4): arquitetura do conjunto de regras de detecção genérica para ModSecurity e Coraza.
- [[owaspcrs-thresholds-severidades-critical-error-warning-notice-calibragem]] — Veja também: OWASP CRS Limiares de Anomalia e Severidades (`CRITICAL=5`, `ERROR=4`, `WARNING=3`, `NOTICE=2`): por que a meta de produção é Threshold `5`.

## Fontes
- [OWASP Core Rule SetOfficial Documentation — Anomaly Scoring Mode (Inbound/Outbound Scores, Thresholds, Severity Points & Collaborative Detection)](https://coreruleset.org/docs/2-how-crs-works/2-1-anomaly_scoring/) — Documentação oficial do OWASP CRS explicando o mecanismo de pontuação de anomalias (Inbound/Outbound), pesos por severidade (CRITICAL=5, ERROR=4, WARNING=3, NOTICE=2) e avaliação nas regras 949110 e 959100; consultado em 2026-10-03.
- [OWASP Core Rule Set GitHub — README.md (CRS v4 Architecture, Attack Categories, Paranoia Levels & False Positive Handling)](https://raw.githubusercontent.com/coreruleset/coreruleset/main/README.md) — README oficial do coreruleset/coreruleset apresentando a arquitetura do OWASP CRS v4, cobertura de ataques e integração com motores WAF; consultado em 2026-10-03.
- [OWASP Core Rule Set (CRS) — Official GitHub Repository](https://github.com/coreruleset/coreruleset) — Repositório oficial Apache-2.0 do OWASP Core Rule Set; consultado em 2026-10-03.
