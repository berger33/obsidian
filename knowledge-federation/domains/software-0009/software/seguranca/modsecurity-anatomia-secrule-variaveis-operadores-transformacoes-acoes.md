---
id: software.seguranca.tranche13.001253
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

# Anatomia da Linguagem **`SecRule`** e as **5 Fases de Processamento HTTP** no ModSecurity: `VARIABLES`, `@OPERATOR`, `t:transform` e `ACTIONS`

## Em uma frase
Como funciona a sintaxe de uma regra **`SecRule`** no ModSecurity e em que momento exato do ciclo de vida de uma requisição HTTP ela é avaliada?

## Por que importa
Toda regra do ModSecurity segue a estrutura **`SecRule VARIABLES "OPERATOR" "ACTIONS"`**, e é executada em uma das **5 Fases de Processamento HTTP (`phase:1` a `phase:5`)**: **`phase:1` (Request Headers)** — roda assim que os cabeçalhos HTTP chegam, antes mesmo de ler o corpo da requisição!; **`phase:2` (Request Body)** — analisa os argumentos `POST`, JSON, XML e uploads multipart; **`phase:3` (Response Headers)** — analisa cabeçalhos devolvidos pelo backend; **`phase:4` (Response Body)** — inspeciona o corpo da resposta contra vazamento de dados; e **`phase:5` (Logging)** — fase final de auditoria!

## Como funciona
Dentro da regra: **(1) `VARIABLES`** seleciona onde buscar (ex.: `ARGS`, `ARGS_NAMES`, `REQUEST_HEADERS:User-Agent`, `REQUEST_URI`, `REQUEST_COOKIES`, `XML:/*`); **(2) `OPERATOR`** define o teste (ex.: `@rx <regex>`, `@detectSQLi`, `@detectXSS`, `@pmFromFile`, `@ipMatch`); e **(3) `ACTIONS`** define o **`id`** único obrigatório, a **`phase`**, as funções de **Transformação/Desofuscação (`t:none,t:urlDecodeUni,t:lowercase,t:htmlEntityDecode`)** aplicadas antes do operador e a decisão (`deny,status:403,log,msg:'...'`)!

## Exemplo
```apache
# Exemplo de SecRule customizada na phase:2 que decodifica URL/lowercase e bloqueia tentativas de acesso a arquivos .env ou .git
SecRule REQUEST_URI "@rx (?:\.env|\.git/config)" \
    "id:100001,phase:1,deny,status:403,log,t:none,t:urlDecodeUni,t:normalizePath,t:lowercase,msg:'Bloqueio de tentativa de leitura de .env ou .git'"
```

## Limites e trade-offs
Por que a cadeia de **Transformações (`t:urlDecodeUni,t:normalizePath,t:lowercase`)** dentro da `SecRule` é fundamental contra técnicas de evasão de WAF? Porque se o atacante enviar `GET /%2e%2e/%2e%65%6e%76`, o ModSecurity primeiro decodifica o URL-encoding (`t:urlDecodeUni`), normaliza barras e caminhos relativos (`t:normalizePath`) e converte para minúsculas (`t:lowercase`) **em um buffer temporário de inspeção antes de aplicar o operador `@rx`** — impedindo que codificações triviais burlem a regra!

## Como verificar
Regras que só inspecionam URL, IP de origem ou cabeçalhos HTTP devem sempre ser colocadas na **`phase:1`**: assim o WAF rejeita o ataque instantaneamente antes mesmo do servidor gastar banda e memória recebendo o corpo da requisição!

## Conexões
- [[modsecurity-modos-operacao-secruleengine-detectiononly-on-tuning]] — Veja também: Implantação Segura do ModSecurity em Produção: **`SecRuleEngine DetectionOnly` vs. `On`** e Inspeção dos Corpos de Requisição e Resposta.
- [[modsecurity-processadores-body-json-xml-limites-anti-dos-pcre]] — Veja também: Inspeção Nativa de **APIs JSON e XML (`ctl:requestBodyProcessor`)** e Proteção contra **ReDoS / JSON Bomb** no ModSecurity v3.
- [[modsecurity-arquitetura-libmodsecurity-v3-conectores-nginx-apache-envoy]] — Referência cruzada direta com modsecurity-arquitetura-libmodsecurity-v3-conectores-nginx-apache-envoy.
- [[modsecurity-deteccao-sqli-xss-libinjection-detectsqli-detectxss]] — Referência cruzada direta com modsecurity-deteccao-sqli-xss-libinjection-detectsqli-detectxss.
- [[modsecurity-tuning-falsos-positivos-exclusoes-ctl-ruleremovetargetbyid]] — Referência cruzada direta com modsecurity-tuning-falsos-positivos-exclusoes-ctl-ruleremovetargetbyid.

## Fontes
- [OWASP ModSecurity v3 (`libmodsecurity`) Official GitHub](https://raw.githubusercontent.com/owasp-modsecurity/ModSecurity/v3/master/README.md) — repositório oficial do OWASP ModSecurity v3 detalhando a arquitetura standalone da biblioteca `libmodsecurity`, conectores Nginx/Apache, PCRE2, `libinjection` e YAJL JSON; consultado em 2026-10-03.
- [OWASP ModSecurity v3 Recommended Configuration (`modsecurity.conf-recommended`)](https://raw.githubusercontent.com/owasp-modsecurity/ModSecurity/v3/master/modsecurity.conf-recommended) — configuração oficial recomendada do ModSecurity v3 cobrindo `SecRuleEngine`, `SecRequestBodyAccess`, processadores XML/JSON, limites anti-DoS e `SecAuditLogFormat JSON`; consultado em 2026-10-03.
