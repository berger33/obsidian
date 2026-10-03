---
id: software.seguranca.tranche02.000113
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

# OWASP CRS Limiares de Anomalia e Severidades (`CRITICAL=5`, `ERROR=4`, `WARNING=3`, `NOTICE=2`): por que a meta de produção é Threshold `5`

## Em uma frase
No OWASP CRS, cada regra possui uma severidade que soma pontos ao score da transação: **`CRITICAL` = 5 pontos**, **`ERROR` = 4 pontos**, **`WARNING` = 3 pontos** e **`NOTICE` = 2 pontos**, enquanto os limiares padrão em `crs-setup.conf` são **`tx.inbound_anomaly_score_threshold = 5`** (Inbound) e **`tx.outbound_anomaly_score_threshold = 4`** (Outbound).

## Por que importa
Conforme alerta a documentação oficial de *Anomaly Scoring*, aumentar o limiar inbound para `10` ou `20` para "esconder" falsos positivos deixa a aplicação desprotegida contra ataques específicos cobertos por uma única regra `CRITICAL` (que soma exatamente 5 pontos).

## Como funciona
A prática recomendada oficial do CRS para rollout em produção é: começar com um limiar alto (ex.: `100` ou `DetectionOnly`), analisar os logs reais, escrever regras de exclusão cirúrgicas para os falsos positivos e **reduzir progressivamente o limiar até atingir a meta padrão de `inbound_anomaly_score_threshold = 5` e `outbound_anomaly_score_threshold = 4`**.

## Exemplo
```apache
# Configuração padrão recomendada no arquivo crs-setup.conf (Regra 900110):
SecAction \
    "id:900110,\
    phase:1,\
    nolog,\
    pass,\
    t:none,\
    setvar:tx.inbound_anomaly_score_threshold=5,\
    setvar:tx.outbound_anomaly_score_threshold=4"
```

## Limites e trade-offs
Se a sua equipe desejar bloquear já na Fase 1 as violações encontradas nos cabeçalhos HTTP sem esperar a Fase 2 (economizando processamento de body), habilite a opção **`tx.early_blocking=1`** na regra `900120` do `crs-setup.conf`.

## Como verificar
Verifique o valor ativo de `tx.inbound_anomaly_score_threshold` no seu `crs-setup.conf`.

## Conexões
- [[owaspcrs-anomaly-scoring-mode-collaborative-detection-delayed-blocking]] — Veja também: OWASP CRS Anomaly Scoring Mode: detecção colaborativa (`setvar`) e bloqueio adiado em `949` (Inbound) e `959` (Outbound).
- [[owaspcrs-paranoia-levels-pl1-a-pl4-blocking-vs-detection-paranoia-level]] — Veja também: OWASP CRS Níveis de Paranoia (`PL1` a `PL4`): uso combinado de `tx.blocking_paranoia_level` e `tx.detection_paranoia_level`.

## Fontes
- [OWASP Core Rule SetOfficial Documentation — Anomaly Scoring Mode (Inbound/Outbound Scores, Thresholds, Severity Points & Collaborative Detection)](https://coreruleset.org/docs/2-how-crs-works/2-1-anomaly_scoring/) — Documentação oficial do OWASP CRS explicando o mecanismo de pontuação de anomalias (Inbound/Outbound), pesos por severidade (CRITICAL=5, ERROR=4, WARNING=3, NOTICE=2) e avaliação nas regras 949110 e 959100; consultado em 2026-10-03.
- [OWASP Core Rule Set GitHub — README.md (CRS v4 Architecture, Attack Categories, Paranoia Levels & False Positive Handling)](https://raw.githubusercontent.com/coreruleset/coreruleset/main/README.md) — README oficial do coreruleset/coreruleset apresentando a arquitetura do OWASP CRS v4, cobertura de ataques e integração com motores WAF; consultado em 2026-10-03.
- [OWASP Core Rule Set (CRS) — Official GitHub Repository](https://github.com/coreruleset/coreruleset) — Repositório oficial Apache-2.0 do OWASP Core Rule Set; consultado em 2026-10-03.
