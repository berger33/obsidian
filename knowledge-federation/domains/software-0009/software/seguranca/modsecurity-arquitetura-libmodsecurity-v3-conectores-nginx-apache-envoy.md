---
id: software.seguranca.tranche13.001251
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

# Arquitetura do **OWASP ModSecurity v3 (`libmodsecurity`)**: Motor WAF Standalone em C++17 e Conectores para **Nginx, Apache e Envoy**

## Em uma frase
Como proteger aplicações Web e APIs HTTP/JSON contra ataques de **SQL Injection (SQLi)**, **Cross-Site Scripting (XSS)**, **Remote Code Execution (RCE / Log4Shell)**, **Local File Inclusion (LFI)** e **Server-Side Request Forgery (SSRF)** diretamente no proxy reverso de borda antes que a requisição maliciosa chegue ao código da aplicação?

## Por que importa
Mantido oficialmente sob a égide da **OWASP (`owasp-modsecurity/ModSecurity`)**, o **ModSecurity v3** é o motor open-source de **Web Application Firewall (WAF)** mais implantado do mundo!

## Como funciona
Diferente do antigo ModSecurity 2.9 (que era fortemente acoplado às bibliotecas internas do servidor Apache `APR`), o **ModSecurity v3 (`libmodsecurity`)** foi completamente reescrito do zero como uma **biblioteca standalone multiplataforma em C++17**, desacoplada do servidor HTTP! Assim, servidores de alta performance como **Nginx (`ModSecurity-nginx`)**, **Apache HTTP Server**, **Envoy Proxy** e **HAProxy** integram-se à `libmodsecurity` através de **Conectores leves**, enquanto o motor central compila e avalia regras **`SecRules`** (como o famoso **OWASP Core Rule Set — CRS**) usando **PCRE2**, **`libinjection`** (detecção léxica de SQLi e XSS sem regex!), **`libxml2`** e **`yajl` (JSON)**!

## Exemplo
```nginx
# Habilitar o conector ModSecurity v3 e carregar o arquivo de configuracao principal dentro de um virtual host do Nginx
load_module modules/ngx_http_modsecurity_module.so;

http {
    server {
        listen 443 ssl;
        modsecurity on;
        modsecurity_rules_file /etc/nginx/modsec/main.conf;
    }
}
```

## Limites e trade-offs
Essa separação arquitetural entre **Motor (`libmodsecurity`)** e **Conector (`ModSecurity-nginx`)** garante que você possa usar exatamente o mesmo conjunto de regras `SecRule` e o mesmo **OWASP CRS** independentemente de sua infraestrutura de borda rodar Nginx, Apache ou Ingress Controllers no Kubernetes!

## Como verificar
Sempre parta do arquivo oficial **`modsecurity.conf-recommended`** do repositório `owasp-modsecurity/ModSecurity` como base segura para sua configuração.

## Conexões
- [[modsecurity-modos-operacao-secruleengine-detectiononly-on-tuning]] — Veja também: Implantação Segura do ModSecurity em Produção: **`SecRuleEngine DetectionOnly` vs. `On`** e Inspeção dos Corpos de Requisição e Resposta.
- [[modsecurity-anatomia-secrule-variaveis-operadores-transformacoes-acoes]] — Referência cruzada direta com modsecurity-anatomia-secrule-variaveis-operadores-transformacoes-acoes.
- [[modsecurity-deteccao-sqli-xss-libinjection-detectsqli-detectxss]] — Referência cruzada direta com modsecurity-deteccao-sqli-xss-libinjection-detectsqli-detectxss.

## Fontes
- [OWASP ModSecurity v3 (`libmodsecurity`) Official GitHub](https://raw.githubusercontent.com/owasp-modsecurity/ModSecurity/v3/master/README.md) — repositório oficial do OWASP ModSecurity v3 detalhando a arquitetura standalone da biblioteca `libmodsecurity`, conectores Nginx/Apache, PCRE2, `libinjection` e YAJL JSON; consultado em 2026-10-03.
- [OWASP ModSecurity v3 Recommended Configuration (`modsecurity.conf-recommended`)](https://raw.githubusercontent.com/owasp-modsecurity/ModSecurity/v3/master/modsecurity.conf-recommended) — configuração oficial recomendada do ModSecurity v3 cobrindo `SecRuleEngine`, `SecRequestBodyAccess`, processadores XML/JSON, limites anti-DoS e `SecAuditLogFormat JSON`; consultado em 2026-10-03.
