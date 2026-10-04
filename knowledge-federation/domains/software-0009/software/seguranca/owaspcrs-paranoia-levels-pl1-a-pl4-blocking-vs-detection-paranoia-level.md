---
id: software.seguranca.tranche02.000114
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

# OWASP CRS Níveis de Paranoia (`PL1` a `PL4`): uso combinado de `tx.blocking_paranoia_level` e `tx.detection_paranoia_level`

## Em uma frase
O OWASP CRS classifica todas as suas regras em quatro **Níveis de Paranoia (*Paranoia Levels — PL1, PL2, PL3 e PL4*)** e permite configurar separadamente **`tx.blocking_paranoia_level`** (quais níveis efetivamente contam para bloquear requisições) e **`tx.detection_paranoia_level`** (quais níveis adicionais rodam apenas emitindo alertas de telemetria).

## Por que importa
Subir diretamente o `blocking_paranoia_level` de `1` para `3` em uma API que recebe textos livres ou código gerará bloqueios imediatos em usuários legítimos; porém, como saber quais regras do `PL2` dariam falso positivo antes de ativá-lo?

## Como funciona
Configurando **`tx.blocking_paranoia_level=1`** e **`tx.detection_paranoia_level=2`** (conhecido na documentação oficial como *Executing Paranoia Level*), o CRS bloqueia apenas com base nas regras seguras do `PL1` (`tx.anomaly_score_pl1`), mas executa e loga em paralelo as regras do `PL2` (`tx.anomaly_score_pl2`) sem somá-las na decisão de bloqueio!

## Exemplo
```apache
# Regra 900000 e 900001 no crs-setup.conf: bloqueia em PL1 enquanto testa PL2 em modo de observação:
SecAction \
    "id:900000,\
    phase:1,\
    nolog,\
    pass,\
    t:none,\
    setvar:tx.blocking_paranoia_level=1"

SecAction \
    "id:900001,\
    phase:1,\
    nolog,\
    pass,\
    t:none,\
    setvar:tx.detection_paranoia_level=2"
```

## Limites e trade-offs
Resumo dos níveis: **PL1** (padrão para todos os sites, quase zero falsos positivos), **PL2** (aplicações corporativas/e-commerce que lidam com dados sensíveis, requer algum tuning), **PL3** (bancos/fintechs de alta segurança, exige tuning intenso) e **PL4** (ambientes extremos de segurança máxima).

## Como verificar
Filtre nos seus logs de auditoria a tag `paranoia-level/2` para revisar e tratar falsos positivos antes de subir `blocking_paranoia_level` para `2`.

## Conexões
- [[owaspcrs-thresholds-severidades-critical-error-warning-notice-calibragem]] — Veja também: OWASP CRS Limiares de Anomalia e Severidades (`CRITICAL=5`, `ERROR=4`, `WARNING=3`, `NOTICE=2`): por que a meta de produção é Threshold `5`.
- [[owaspcrs-taxonomia-arquivos-regras-request-911-a-949-response-950-a-959]] — Veja também: OWASP CRS Taxonomia Numerada de Regras (`901–999`): organização modular de `REQUEST-911..949` e `RESPONSE-950..959`.

## Fontes
- [OWASP Core Rule SetOfficial Documentation — Anomaly Scoring Mode (Inbound/Outbound Scores, Thresholds, Severity Points & Collaborative Detection)](https://coreruleset.org/docs/2-how-crs-works/2-1-anomaly_scoring/) — Documentação oficial do OWASP CRS explicando o mecanismo de pontuação de anomalias (Inbound/Outbound), pesos por severidade (CRITICAL=5, ERROR=4, WARNING=3, NOTICE=2) e avaliação nas regras 949110 e 959100; consultado em 2026-10-03.
- [OWASP Core Rule Set GitHub — README.md (CRS v4 Architecture, Attack Categories, Paranoia Levels & False Positive Handling)](https://raw.githubusercontent.com/coreruleset/coreruleset/main/README.md) — README oficial do coreruleset/coreruleset apresentando a arquitetura do OWASP CRS v4, cobertura de ataques e integração com motores WAF; consultado em 2026-10-03.
- [OWASP Core Rule Set (CRS) — Official GitHub Repository](https://github.com/coreruleset/coreruleset) — Repositório oficial Apache-2.0 do OWASP Core Rule Set; consultado em 2026-10-03.
