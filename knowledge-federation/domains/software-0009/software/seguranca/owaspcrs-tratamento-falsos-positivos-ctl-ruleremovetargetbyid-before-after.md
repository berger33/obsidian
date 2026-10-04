---
id: software.seguranca.tranche02.000116
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

# OWASP CRS Tuning de Falsos Positivos: `ctl:ruleRemoveTargetById` em tempo de execução (`BEFORE-CRS`) vs `SecRuleUpdateTargetById` (`AFTER-CRS`)

## Em uma frase
Para tratar falsos positivos no OWASP CRS sem enfraquecer a segurança global, existem dois mecanismos precisos: 1) **Runtime Exclusion** (usando `ctl:ruleRemoveTargetById=942100;ARGS:content` no arquivo `REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf`, quando a exceção depende da URI ou método HTTP); e 2) **Configure-time Exclusion** (usando `SecRuleUpdateTargetById 942100 "!ARGS:content"` no arquivo `RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf`).

## Por que importa
Um erro gravíssimo e comum é usar `SecRuleRemoveById 942100` globalmente (o que desliga a regra de SQLi para **todos** os endpoints e parâmetros da aplicação) ou colocar uma regra com `ctl:ruleRemoveById` **depois** que as regras do CRS já foram executadas!

## Como funciona
A regra de ouro da ordem de inclusão do CRS é: regras que usam ações dinâmicas **`ctl:`** (`ctl:ruleRemoveById`, `ctl:ruleRemoveTargetById`, `ctl:ruleRemoveTargetByTag`) **devem vir ANTES das regras do CRS (`BEFORE-CRS`)**; já diretivas de configuração que modificam regras já carregadas (**`SecRuleRemoveById`**, **`SecRuleUpdateTargetById`**) **devem vir DEPOIS das regras do CRS (`AFTER-CRS`)**!

## Exemplo
```apache
# Exemplo em REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf:
# Ignora apenas o parâmetro ARGS:markdown_body na regra 941100 exclusivamente na rota POST /api/v1/articles:
SecRule REQUEST_URI "@beginsWith /api/v1/articles" \
    "id:100010,\
    phase:1,\
    pass,\
    nolog,\
    ctl:ruleRemoveTargetById=941100;ARGS:markdown_body"
```

## Limites e trade-offs
Prefira sempre `ctl:ruleRemoveTargetById=<ID>;ARGS:<campo>` escopado por `REQUEST_URI` em vez de remover a regra inteira.

## Como verificar
Envie um payload de teste no campo `markdown_body` para `/api/v1/articles` (deve passar) e para `/api/v1/login` (deve continuar bloqueado).

## Conexões
- [[owaspcrs-taxonomia-arquivos-regras-request-911-a-949-response-950-a-959]] — Veja também: OWASP CRS Taxonomia Numerada de Regras (`901–999`): organização modular de `REQUEST-911..949` e `RESPONSE-950..959`.
- [[owaspcrs-exclusion-packages-pre-construidos-wordpress-nextcloud-dokuwiki]] — Veja também: OWASP CRS Rule Exclusion Packages e CRS v4 Plugins: perfis oficiais de exclusão para WordPress, Nextcloud, Drupal e cPanel.

## Fontes
- [OWASP Core Rule SetOfficial Documentation — Anomaly Scoring Mode (Inbound/Outbound Scores, Thresholds, Severity Points & Collaborative Detection)](https://coreruleset.org/docs/2-how-crs-works/2-1-anomaly_scoring/) — Documentação oficial do OWASP CRS explicando o mecanismo de pontuação de anomalias (Inbound/Outbound), pesos por severidade (CRITICAL=5, ERROR=4, WARNING=3, NOTICE=2) e avaliação nas regras 949110 e 959100; consultado em 2026-10-03.
- [OWASP Core Rule Set GitHub — README.md (CRS v4 Architecture, Attack Categories, Paranoia Levels & False Positive Handling)](https://raw.githubusercontent.com/coreruleset/coreruleset/main/README.md) — README oficial do coreruleset/coreruleset apresentando a arquitetura do OWASP CRS v4, cobertura de ataques e integração com motores WAF; consultado em 2026-10-03.
- [OWASP Core Rule Set (CRS) — Official GitHub Repository](https://github.com/coreruleset/coreruleset) — Repositório oficial Apache-2.0 do OWASP Core Rule Set; consultado em 2026-10-03.
