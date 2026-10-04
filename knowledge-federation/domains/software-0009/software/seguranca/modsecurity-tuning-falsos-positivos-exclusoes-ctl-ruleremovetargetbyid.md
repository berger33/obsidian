---
id: software.seguranca.tranche13.001257
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/owasp-modsecurity/ModSecurity/v3/master/README.md", "https://raw.githubusercontent.com/owasp-modsecurity/ModSecurity/v3/master/modsecurity.conf-recommended"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Engenharia de Tuning e Eliminação Cirúrgica de Falsos Positivos no ModSecurity: **`ctl:ruleRemoveTargetById`** vs. `SecRuleRemoveById`

## Em uma frase
Imagine que a sua aplicação possui um endpoint `/api/v1/artigos` onde editores autenticados enviam um campo JSON `ARGS:conteudo_html` contendo código HTML rico e exemplos de comandos SQL para um blog técnico, e a regra `941100` (XSS) do OWASP CRS está bloqueando esse campo específico.Qual é o jeito **errado** e qual é o jeito **certo (cirúrgico)** de resolver esse falso positivo no ModSecurity?

## Por que importa
O jeito **errado** é usar `SecRuleRemoveById 941100` globalmente — porque isso **desliga a proteção contra XSS para todas as URLs e todos os parâmetros da aplicação inteira**!

## Como funciona
O jeito **certo e cirúrgico** é criar uma regra de exclusão em `REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf` que verifica se o `REQUEST_URI` é exatamente `/api/v1/artigos` e usa a ação de controle em tempo de execução **`ctl:ruleRemoveTargetById=941100;ARGS:conteudo_html`**! Com isso, a regra `941100` **continua protegendo 100% das outras URLs da aplicação e até mesmo todos os outros campos de `/api/v1/artigos` (`ARGS:titulo`, `ARGS:autor`, cookies e headers)**, ignorando exclusivamente o parâmetro `ARGS:conteudo_html` naquela rota específica!

## Exemplo
```apache
# Exclusao cirurgica em tempo de execucao (BEFORE-CRS): remove apenas o parametro ARGS:conteudo_html da inspecao das regras 941100 e 942100 na rota /api/v1/artigos
SecRule REQUEST_URI "@beginsWith /api/v1/artigos" \
    "id:100100,phase:1,pass,nolog,t:none,\
    ctl:ruleRemoveTargetById=941100;ARGS:conteudo_html,\
    ctl:ruleRemoveTargetById=942100;ARGS:conteudo_html"
```

## Limites e trade-offs
Regra importante sobre a ordem de carregamento no ModSecurity: ações dinâmicas **`ctl:ruleRemoveById`** e **`ctl:ruleRemoveTargetById`** são avaliadas durante a transação HTTP e, portanto, **devem ser declaradas ANTES das regras do CRS (`REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf`)**, enquanto diretivas estáticas de tempo de compilação como `SecRuleRemoveById` ou `SecRuleUpdateTargetById` devem ser declaradas **DEPOIS das regras do CRS (`RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf`)**!

## Como verificar
Para aplicações populares como WordPress, Nextcloud, Drupal, DokuWiki e XenForo, o OWASP CRS já inclui **Application Exclusion Plugins** oficiais prontos que podem ser habilitados no `crs-setup.conf`!

## Conexões
- [[modsecurity-integracao-owasp-crs-anomaly-scoring-paranoia-level]] — Veja também: Integração do ModSecurity com o **OWASP Core Rule Set (`CRS`)**: Modelo de **Pontuação de Anomalia (*Anomaly Scoring*)** e **Paranoia Levels (`PL1`–`PL4`)**.
- [[modsecurity-auditoria-logs-json-secauditlogparts-ingestao-siem-wazuh]] — Veja também: Logs de Auditoria Estruturados em **JSON (`SecAuditLogFormat JSON`)** e Anatomia de **`SecAuditLogParts` (`ABIJDEFHZ`)** para Ingestão em SIEM / Wazuh.
- [[modsecurity-arquitetura-libmodsecurity-v3-conectores-nginx-apache-envoy]] — Referência cruzada direta com modsecurity-arquitetura-libmodsecurity-v3-conectores-nginx-apache-envoy.

## Fontes
- [OWASP ModSecurity v3 (`libmodsecurity`) Official GitHub](https://raw.githubusercontent.com/owasp-modsecurity/ModSecurity/v3/master/README.md) — repositório oficial do OWASP ModSecurity v3 detalhando a arquitetura standalone da biblioteca `libmodsecurity`, conectores Nginx/Apache, PCRE2, `libinjection` e YAJL JSON; consultado em 2026-10-03.
- [OWASP ModSecurity v3 Recommended Configuration (`modsecurity.conf-recommended`)](https://raw.githubusercontent.com/owasp-modsecurity/ModSecurity/v3/master/modsecurity.conf-recommended) — configuração oficial recomendada do ModSecurity v3 cobrindo `SecRuleEngine`, `SecRequestBodyAccess`, processadores XML/JSON, limites anti-DoS e `SecAuditLogFormat JSON`; consultado em 2026-10-03.
