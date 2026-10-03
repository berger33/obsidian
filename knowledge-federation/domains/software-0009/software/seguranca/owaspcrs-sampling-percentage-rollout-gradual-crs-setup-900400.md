---
id: software.seguranca.tranche02.000120
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

# OWASP CRS Sampling Mode (`tx.sampling_percentage`, Regra `900400`) e `coreruleset-cli`: rollout gradual por amostragem de tráfego

## Em uma frase
A regra **`900400`** do `crs-setup.conf` permite configurar **`tx.sampling_percentage`** (de `0` a `100`), instruindo o OWASP CRS a inspecionar apenas uma porcentagem estatística das requisições HTTP enquanto o restante faz bypass imediato na regra `901450`.

## Por que importa
Ao implantar o WAF pela primeira vez na frente de um serviço de altíssimo tráfego (dezenas de milhares de requisições por segundo), habilitar 100% da inspeção de imediato sem medir o impacto real de CPU e latência P99 no proxy traz risco operacional.

## Como funciona
Definindo `setvar:tx.sampling_percentage=10`, o CRS gera um número pseudo-aleatório por requisição e avalia o conjunto completo de regras em apenas 10% do tráfego, permitindo validar a capacidade de CPU, o volume de logs e a taxa de falsos positivos antes de escalar para `50` e `100`.

## Exemplo
```apache
# Regra 900400 no crs-setup.conf: avalia o CRS em 20% das requisições durante o canário de performance:
SecAction \
    "id:900400,\
    phase:1,\
    nolog,\
    pass,\
    t:none,\
    setvar:tx.sampling_percentage=20"
```

## Limites e trade-offs
Lembre-se de que `tx.sampling_percentage` inferior a `100` é apenas uma ferramenta temporária de rollout/canário de performance, não devendo permanecer abaixo de `100` após a estabilização.

## Como verificar
Verifique nos logs de métricas do proxy a proporção de transações avaliadas e promova `tx.sampling_percentage=100` após validar a latência.

## Conexões
- [[owaspcrs-inspecao-outbound-response-950-a-959-prevencao-vazamento-dados]] — Veja também: OWASP CRS Inspeção de Resposta Outbound (`RESPONSE-950` a `959`): bloqueio de vazamento de erros SQL, stack traces e web shells.

## Fontes
- [OWASP Core Rule SetOfficial Documentation — Anomaly Scoring Mode (Inbound/Outbound Scores, Thresholds, Severity Points & Collaborative Detection)](https://coreruleset.org/docs/2-how-crs-works/2-1-anomaly_scoring/) — Documentação oficial do OWASP CRS explicando o mecanismo de pontuação de anomalias (Inbound/Outbound), pesos por severidade (CRITICAL=5, ERROR=4, WARNING=3, NOTICE=2) e avaliação nas regras 949110 e 959100; consultado em 2026-10-03.
- [OWASP Core Rule Set GitHub — README.md (CRS v4 Architecture, Attack Categories, Paranoia Levels & False Positive Handling)](https://raw.githubusercontent.com/coreruleset/coreruleset/main/README.md) — README oficial do coreruleset/coreruleset apresentando a arquitetura do OWASP CRS v4, cobertura de ataques e integração com motores WAF; consultado em 2026-10-03.
- [OWASP Core Rule Set (CRS) — Official GitHub Repository](https://github.com/coreruleset/coreruleset) — Repositório oficial Apache-2.0 do OWASP Core Rule Set; consultado em 2026-10-03.
