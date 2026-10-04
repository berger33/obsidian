---
id: software.seguranca.tranche13.001254
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

# Inspeção Nativa de **APIs JSON e XML (`ctl:requestBodyProcessor`)** e Proteção contra **ReDoS / JSON Bomb** no ModSecurity v3

## Em uma frase
Em arquiteturas modernas de microsserviços, Single-Page Applications (React/Vue) e aplicativos móveis, quase todo o tráfego de entrada chega com `Content-Type: application/json` ou `application/xml`. Se o ModSecurity não souber fazer o *parse* estruturado do JSON ou do XML, ele enxergará o corpo apenas como um texto bruto ou deixará de popular a coleção `ARGS`!

## Por que importa
No `modsecurity.conf-recommended`, duas regras padrão na **`phase:1`** (`id:200000` e `id:200001`) inspecionam o cabeçalho `REQUEST_HEADERS:Content-Type` e acionam automaticamente os processadores nativos em C/C++: **`ctl:requestBodyProcessor=XML`** (via `libxml2`) e **`ctl:requestBodyProcessor=JSON`** (via biblioteca `yajl`, que achata todas as chaves e valores da árvore JSON para dentro de `ARGS` e `ARGS_NAMES`!)!

## Como funciona
E para impedir que um atacante derrube o WAF com um **JSON Bomb** (milhares de chaves ou objetos profundamente aninhados), um upload gigante ou uma expressão regular catastrófica (**ReDoS**), o `modsecurity.conf-recommended` define limites estritos de engenharia: **`SecRequestBodyLimit`** (`13107200` = 12,5 MB), **`SecRequestBodyNoFilesLimit`** (`131072` = 128 KB), **`SecRequestBodyJsonDepthLimit 512`**, **`SecArgumentsLimit 1000`** e **`SecPcreMatchLimit 1000`**!

## Exemplo
```apache
# Ativar automaticamente o parser JSON nativo (id:200001) e impor limites estritos contra JSON Bomb, Argument Flooding e ReDoS
SecRule REQUEST_HEADERS:Content-Type "^application/([a-z0-9.-]+[+]json|json)" \
    "id:200001,phase:1,t:none,t:lowercase,pass,nolog,ctl:requestBodyProcessor=JSON"

SecRequestBodyLimit 13107200
SecRequestBodyNoFilesLimit 131072
SecRequestBodyJsonDepthLimit 512
SecArgumentsLimit 1000
SecPcreMatchLimit 1000
```

## Limites e trade-offs
E o que acontece se um atacante enviar um JSON propositalmente malformado tentando causar um *Parser Differential Bypass* (onde o WAF falha no parse do JSON, mas o framework backend aceita)? A regra oficial **`id:200002`** (`SecRule REQBODY_ERROR "!@eq 0" "id:200002,phase:2,deny,status:400..."`) intercepta qualquer erro do parser de body (`REQBODY_ERROR != 0`) e **rejeita a requisição imediatamente com HTTP 400**!

## Como verificar
Da mesma forma, a regra **`id:200003`** (`MULTIPART_STRICT_ERROR`) bloqueia uploads `multipart/form-data` com fronteiras (*boundaries*) adulteradas usadas para tentar esconder arquivos executáveis de WAFs.

## Conexões
- [[modsecurity-anatomia-secrule-variaveis-operadores-transformacoes-acoes]] — Veja também: Anatomia da Linguagem **`SecRule`** e as **5 Fases de Processamento HTTP** no ModSecurity: `VARIABLES`, `@OPERATOR`, `t:transform` e `ACTIONS`.
- [[modsecurity-deteccao-sqli-xss-libinjection-detectsqli-detectxss]] — Veja também: Detecção Léxica de **SQL Injection (`@detectSQLi`)** e **XSS (`@detectXSS`)** com **`libinjection`** no ModSecurity v3: Além das Expressões Regulares.
- [[modsecurity-arquitetura-libmodsecurity-v3-conectores-nginx-apache-envoy]] — Referência cruzada direta com modsecurity-arquitetura-libmodsecurity-v3-conectores-nginx-apache-envoy.
- [[modsecurity-modos-operacao-secruleengine-detectiononly-on-tuning]] — Referência cruzada direta com modsecurity-modos-operacao-secruleengine-detectiononly-on-tuning.

## Fontes
- [OWASP ModSecurity v3 (`libmodsecurity`) Official GitHub](https://raw.githubusercontent.com/owasp-modsecurity/ModSecurity/v3/master/README.md) — repositório oficial do OWASP ModSecurity v3 detalhando a arquitetura standalone da biblioteca `libmodsecurity`, conectores Nginx/Apache, PCRE2, `libinjection` e YAJL JSON; consultado em 2026-10-03.
- [OWASP ModSecurity v3 Recommended Configuration (`modsecurity.conf-recommended`)](https://raw.githubusercontent.com/owasp-modsecurity/ModSecurity/v3/master/modsecurity.conf-recommended) — configuração oficial recomendada do ModSecurity v3 cobrindo `SecRuleEngine`, `SecRequestBodyAccess`, processadores XML/JSON, limites anti-DoS e `SecAuditLogFormat JSON`; consultado em 2026-10-03.
