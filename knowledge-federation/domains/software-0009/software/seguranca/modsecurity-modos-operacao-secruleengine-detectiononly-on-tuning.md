---
id: software.seguranca.tranche13.001252
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

# Implantação Segura do ModSecurity em Produção: **`SecRuleEngine DetectionOnly` vs. `On`** e Inspeção dos Corpos de Requisição e Resposta

## Em uma frase
Qual é o erro clássico ao colocar um WAF novo em frente a uma aplicação Web ou API de produção pela primeira vez? Ligar imediatamente o bloqueio ativo sem antes observar o tráfego legítimo da aplicação — o que pode bloquear um payload JSON legítimo que contenha caracteres especiais, trechos de código Markdown ou cookies grandes!

## Por que importa
No arquivo `modsecurity.conf`, a diretiva **`SecRuleEngine`** controla o modo global de operação do WAF com três estados possíveis: **(1) `SecRuleEngine DetectionOnly`** (o estado padrão recomendado no `modsecurity.conf-recommended`: o ModSecurity processa 100% das regras sobre cada requisição e resposta e gera todos os logs de auditoria de possíveis ataques, mas **não bloqueia nenhuma requisição**!); **(2) `SecRuleEngine On`** (modo de prevenção ativa: bloqueia imediatamente com `403 Forbidden` qualquer transação que atinja o limiar de anomalia ou dispare uma regra de bloqueio); e **(3) `SecRuleEngine Off`**!

## Como funciona
Além disso, para que o WAF enxergue payloads enviados via `POST`/`PUT`/`PATCH`, a diretiva **`SecRequestBodyAccess On`** deve estar obrigatoriamente ativa!

## Exemplo
```apache
# Configuracao inicial recomendada em modsecurity.conf: iniciar em DetectionOnly com inspecao completa do corpo da requisicao HTTP
SecRuleEngine DetectionOnly
SecRequestBodyAccess On
SecResponseBodyAccess On
SecResponseBodyMimeType text/plain text/html text/xml application/json
```

## Limites e trade-offs
Siga o ciclo de vida padrão ouro de implantação de WAF: **(1)** Implante com **`SecRuleEngine DetectionOnly`** por 7 a 14 dias em produção; **(2)** Analise os alertas no log JSON do ModSecurity e crie exclusões cirúrgicas (`SecRuleRemoveById` / `ctl:ruleRemoveTargetById`) para eventuais falsos positivos da sua API; e **(3)** Mude para **`SecRuleEngine On`** com confiança total!

## Como verificar
A diretiva **`SecResponseBodyAccess On`** (restrita aos `SecResponseBodyMimeType` de texto/JSON/HTML para não desperdiçar CPU/RAM tentando analisar imagens JPEG ou vídeos MP4!) permite ao WAF detectar **Data Leakage** (como vazamento de stack traces de banco de dados, chaves privadas ou números de cartão de crédito na resposta HTTP!).

## Conexões
- [[modsecurity-arquitetura-libmodsecurity-v3-conectores-nginx-apache-envoy]] — Veja também: Arquitetura do **OWASP ModSecurity v3 (`libmodsecurity`)**: Motor WAF Standalone em C++17 e Conectores para **Nginx, Apache e Envoy**.
- [[modsecurity-anatomia-secrule-variaveis-operadores-transformacoes-acoes]] — Veja também: Anatomia da Linguagem **`SecRule`** e as **5 Fases de Processamento HTTP** no ModSecurity: `VARIABLES`, `@OPERATOR`, `t:transform` e `ACTIONS`.
- [[modsecurity-processadores-body-json-xml-limites-anti-dos-pcre]] — Referência cruzada direta com modsecurity-processadores-body-json-xml-limites-anti-dos-pcre.
- [[modsecurity-integracao-owasp-crs-anomaly-scoring-paranoia-level]] — Referência cruzada direta com modsecurity-integracao-owasp-crs-anomaly-scoring-paranoia-level.

## Fontes
- [OWASP ModSecurity v3 (`libmodsecurity`) Official GitHub](https://raw.githubusercontent.com/owasp-modsecurity/ModSecurity/v3/master/README.md) — repositório oficial do OWASP ModSecurity v3 detalhando a arquitetura standalone da biblioteca `libmodsecurity`, conectores Nginx/Apache, PCRE2, `libinjection` e YAJL JSON; consultado em 2026-10-03.
- [OWASP ModSecurity v3 Recommended Configuration (`modsecurity.conf-recommended`)](https://raw.githubusercontent.com/owasp-modsecurity/ModSecurity/v3/master/modsecurity.conf-recommended) — configuração oficial recomendada do ModSecurity v3 cobrindo `SecRuleEngine`, `SecRequestBodyAccess`, processadores XML/JSON, limites anti-DoS e `SecAuditLogFormat JSON`; consultado em 2026-10-03.
