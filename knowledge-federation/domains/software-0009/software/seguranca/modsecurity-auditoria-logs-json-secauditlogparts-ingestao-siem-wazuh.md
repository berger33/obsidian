---
id: software.seguranca.tranche13.001258
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

# Logs de Auditoria Estruturados em **JSON (`SecAuditLogFormat JSON`)** e Anatomia de **`SecAuditLogParts` (`ABIJDEFHZ`)** para Ingestão em SIEM / Wazuh

## Em uma frase
Para investigar incidentes, fazer tuning de falsos positivos com precisão e enviar alertas de WAF para o **Wazuh**, **OpenSearch**, **ELK** ou **Splunk**, como configurar o sistema de auditoria do ModSecurity v3?

## Por que importa
No `modsecurity.conf`, três diretivas governam os logs de auditoria: **(1) `SecAuditEngine RelevantOnly`** (registra apenas transações que dispararam alguma regra com alerta/warning ou retornaram códigos de status HTTP relevantes configurados em `SecAuditLogRelevantStatus`, evitando encher o disco com requisições estáticas normais `200 OK`); **(2) `SecAuditLogFormat JSON`** (habilitado via biblioteca `yajl`, que substitui o antigo formato texto multilinhas difícil de parsear por objetos JSON estruturados prontos para SIEM!); e **(3) `SecAuditLogParts ABIJDEFHZ`**!

## Como funciona
Cada letra em **`SecAuditLogParts`** controla exatamente quais seções da transação HTTP serão gravadas no log: **`A`** (Cabeçalho do log com timestamp e ID único), **`B`** (Request Headers), **`C`** (Request Body completo — use com cautela se houver dados sensíveis!), **`E`** (Response Body intermediário), **`F`** (Response Headers finais), **`H`** (Audit Log Trailer: traz a lista exata de todas as regras `id` disparadas, mensagens `msg`, `matched_var_name` e `matched_var`!), **`I`** (Request Body compacto sem arquivos binários multipart), **`J`** (Metadados de arquivos enviados via upload) e **`Z`** (Marcador de fim)!

## Exemplo
```apache
# Configurar no modsecurity.conf logs de auditoria relevantes em formato JSON estruturado para ingestao direta em SIEM/Wazuh
SecAuditEngine RelevantOnly
SecAuditLogRelevantStatus "^(?:5|4(?!04))"
SecAuditLogParts ABIJDEFHZ
SecAuditLogType Serial
SecAuditLogFormat JSON
SecAuditLog /var/log/modsec_audit.json
```

## Limites e trade-offs
Com o `SecAuditLogFormat JSON` ativo, você pode usar o **`jq`** diretamente no terminal para listar em 2 segundos quais regras (`id`) e quais parâmetros (`matched_var_name`) mais dispararam alertas na última hora — acelerando em 10x a criação de exclusões `ctl:ruleRemoveTargetById`!

## Como verificar
Se você usar `SecAuditLogType Concurrent` em servidores de altíssimo tráfego, o ModSecurity grava cada transação em um arquivo separado dentro de subpastas de data/hora definidas em `SecAuditLogStorageDir` para eliminar contenção de lock em arquivo único.

## Conexões
- [[modsecurity-tuning-falsos-positivos-exclusoes-ctl-ruleremovetargetbyid]] — Veja também: Engenharia de Tuning e Eliminação Cirúrgica de Falsos Positivos no ModSecurity: **`ctl:ruleRemoveTargetById`** vs. `SecRuleRemoveById`.
- [[modsecurity-virtual-patching-cve-zero-day-mitigacao-imediata-borda]] — Veja também: Aplicando **Virtual Patching** no ModSecurity v3: Mitigando **Zero-Days e CVEs Críticas** na Borda em Minutos Enquanto o Código da Aplicação é Corrigido.
- [[modsecurity-arquitetura-libmodsecurity-v3-conectores-nginx-apache-envoy]] — Referência cruzada direta com modsecurity-arquitetura-libmodsecurity-v3-conectores-nginx-apache-envoy.
- [[hayabusa-geracao-timelines-csv-json-jsonl-perfis-saida-timesketch]] — Referência cruzada direta com hayabusa-geracao-timelines-csv-json-jsonl-perfis-saida-timesketch.

## Fontes
- [OWASP ModSecurity v3 (`libmodsecurity`) Official GitHub](https://raw.githubusercontent.com/owasp-modsecurity/ModSecurity/v3/master/README.md) — repositório oficial do OWASP ModSecurity v3 detalhando a arquitetura standalone da biblioteca `libmodsecurity`, conectores Nginx/Apache, PCRE2, `libinjection` e YAJL JSON; consultado em 2026-10-03.
- [OWASP ModSecurity v3 Recommended Configuration (`modsecurity.conf-recommended`)](https://raw.githubusercontent.com/owasp-modsecurity/ModSecurity/v3/master/modsecurity.conf-recommended) — configuração oficial recomendada do ModSecurity v3 cobrindo `SecRuleEngine`, `SecRequestBodyAccess`, processadores XML/JSON, limites anti-DoS e `SecAuditLogFormat JSON`; consultado em 2026-10-03.
