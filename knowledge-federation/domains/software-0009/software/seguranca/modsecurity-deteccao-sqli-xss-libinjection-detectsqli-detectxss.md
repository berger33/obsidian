---
id: software.seguranca.tranche13.001255
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

# Detecção Léxica de **SQL Injection (`@detectSQLi`)** e **XSS (`@detectXSS`)** com **`libinjection`** no ModSecurity v3: Além das Expressões Regulares

## Em uma frase
Por que depender apenas de expressões regulares (`@rx`) para detectar **SQL Injection (SQLi)** e **Cross-Site Scripting (XSS)** historicamente gerava uma corrida de gato e rato contra atacantes que usam comentários SQL inline (`UN/**/ION SEL/**/ECT`), funções equivalentes ou variações sintáticas de tags HTML/JavaScript?

## Por que importa
Porque SQL e HTML/JavaScript são linguagens formais com gramáticas completas, e não meros padrões regulares de texto! Para resolver isso na raiz, o **ModSecurity v3** integra nativamente em C a biblioteca **`libinjection`** através de dois operadores dedicados de altíssima velocidade: **`@detectSQLi`** e **`@detectXSS`**!

## Como funciona
Em vez de tentar casar uma expressão regular, o operador **`@detectSQLi`** transforma a entrada do usuário em uma sequência de **Tokens Léxicos SQL (*SQL Fingerprints* de até 5 tokens, ex.: `s&1c` = string + operador lógico + número + comentário)** e consulta em tempo constante $O(1)$ uma tabela de mais de 8.000 *fingerprints* sintáticos conhecidos de injeção SQL! Da mesma forma, o **`@detectXSS`** faz a tokenização léxica de contextos HTML5/DOM/JavaScript para identificar vetores de execução de script independentemente de espaçamentos ou ofuscações de atributos!

## Exemplo
```apache
# Detectar ataques de SQL Injection e Cross-Site Scripting em todos os argumentos HTTP e chaves JSON usando os analisadores lexicos da libinjection
SecRule ARGS|ARGS_NAMES|REQUEST_COOKIES "@detectSQLi" \
    "id:100010,phase:2,deny,status:403,log,t:none,t:urlDecodeUni,msg:'SQL Injection detectado via tokenizador lexico libinjection'"

SecRule ARGS|ARGS_NAMES|REQUEST_COOKIES "@detectXSS" \
    "id:100011,phase:2,deny,status:403,log,t:none,t:urlDecodeUni,t:htmlEntityDecode,msg:'XSS detectado via tokenizador lexico libinjection'"
```

## Limites e trade-offs
Como o `libinjection` não utiliza *backtracking* de expressões regulares, os operadores `@detectSQLi` e `@detectXSS` executam em microssegundos com custo de CPU previsível e imunidade total a ataques de *Regular Expression Denial of Service (ReDoS)*!

## Como verificar
No **OWASP Core Rule Set (CRS)**, as regras `942100` (`@detectSQLi`) e `941100` (`@detectXSS`) são as primeiras linhas de defesa executadas no Paranoia Level 1 (`PL1`).

## Conexões
- [[modsecurity-processadores-body-json-xml-limites-anti-dos-pcre]] — Veja também: Inspeção Nativa de **APIs JSON e XML (`ctl:requestBodyProcessor`)** e Proteção contra **ReDoS / JSON Bomb** no ModSecurity v3.
- [[modsecurity-integracao-owasp-crs-anomaly-scoring-paranoia-level]] — Veja também: Integração do ModSecurity com o **OWASP Core Rule Set (`CRS`)**: Modelo de **Pontuação de Anomalia (*Anomaly Scoring*)** e **Paranoia Levels (`PL1`–`PL4`)**.
- [[modsecurity-arquitetura-libmodsecurity-v3-conectores-nginx-apache-envoy]] — Referência cruzada direta com modsecurity-arquitetura-libmodsecurity-v3-conectores-nginx-apache-envoy.
- [[modsecurity-anatomia-secrule-variaveis-operadores-transformacoes-acoes]] — Referência cruzada direta com modsecurity-anatomia-secrule-variaveis-operadores-transformacoes-acoes.

## Fontes
- [OWASP ModSecurity v3 (`libmodsecurity`) Official GitHub](https://raw.githubusercontent.com/owasp-modsecurity/ModSecurity/v3/master/README.md) — repositório oficial do OWASP ModSecurity v3 detalhando a arquitetura standalone da biblioteca `libmodsecurity`, conectores Nginx/Apache, PCRE2, `libinjection` e YAJL JSON; consultado em 2026-10-03.
- [OWASP ModSecurity v3 Recommended Configuration (`modsecurity.conf-recommended`)](https://raw.githubusercontent.com/owasp-modsecurity/ModSecurity/v3/master/modsecurity.conf-recommended) — configuração oficial recomendada do ModSecurity v3 cobrindo `SecRuleEngine`, `SecRequestBodyAccess`, processadores XML/JSON, limites anti-DoS e `SecAuditLogFormat JSON`; consultado em 2026-10-03.
