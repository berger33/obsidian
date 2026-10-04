---
id: software.seguranca.tranche02.000111
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
fontes: ["https://raw.githubusercontent.com/coreruleset/coreruleset/main/README.md", "https://coreruleset.org/docs/2-how-crs-works/2-1-anomaly_scoring/", "https://github.com/coreruleset/coreruleset"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OWASP CRS (Core Rule Set v4): arquitetura do conjunto de regras de detecção genérica para ModSecurity e Coraza

## Em uma frase
O **OWASP CRS (*Core Rule Set*)** (projeto *Flagship* da OWASP licenciado sob Apache 2.0) é o conjunto padrão da indústria de regras genéricas de detecção de ataques para Web Application Firewalls compatíveis com SecLang (como **OWASP Coraza** e **OWASP ModSecurity**), protegendo aplicações contra o OWASP Top 10 com o mínimo de falsos alertas.

## Por que importa
Um motor WAF recém-instalado (como Coraza ou ModSecurity) sem um conjunto de regras é apenas um interpretador vazio: ele não bloqueia nenhum ataque até que regras de inspeção sejam carregadas.

## Como funciona
O OWASP CRS v4 fornece centenas de regras curadas e testadas continuamente contra regressões para detectar **SQL Injection (SQLi)**, **Cross-Site Scripting (XSS)**, **Local/Remote File Inclusion (LFI/RFI)**, **Remote Code Execution (RCE / Shellshock / Command Injection)**, **PHP/Java/Node.js Injection**, **SSRF**, **Scanners/Bots** e **vazamento de dados/erros na resposta**.

## Exemplo
```apache
# Ordem padrão de carregamento do OWASP CRS v4 em um motor SecLang (Coraza ou ModSecurity):
Include /etc/coraza/crs-setup.conf
Include /etc/coraza/plugins/*-config.conf
Include /etc/coraza/plugins/*-before.conf
Include /etc/coraza/rules/*.conf
Include /etc/coraza/plugins/*-after.conf
```

## Limites e trade-offs
Nunca edite diretamente os arquivos dentro da pasta `rules/*.conf` do CRS (pois isso impediria atualizar o CRS quando saem novas versões); faça todas as customizações em `crs-setup.conf`, `REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf` e `RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf`!

## Como verificar
Verifique nos logs de auditoria a tag `ver:'OWASP_CRS/4...'` confirmando que o CRS v4 está carregado e ativo.

## Conexões
- [[owaspcrs-anomaly-scoring-mode-collaborative-detection-delayed-blocking]] — Veja também: OWASP CRS Anomaly Scoring Mode: detecção colaborativa (`setvar`) e bloqueio adiado em `949` (Inbound) e `959` (Outbound).

## Fontes
- [OWASP Core Rule SetOfficial Documentation — Anomaly Scoring Mode (Inbound/Outbound Scores, Thresholds, Severity Points & Collaborative Detection)](https://raw.githubusercontent.com/coreruleset/coreruleset/main/README.md) — Documentação oficial do OWASP CRS explicando o mecanismo de pontuação de anomalias (Inbound/Outbound), pesos por severidade (CRITICAL=5, ERROR=4, WARNING=3, NOTICE=2) e avaliação nas regras 949110 e 959100; consultado em 2026-10-03.
- [OWASP Core Rule Set GitHub — README.md (CRS v4 Architecture, Attack Categories, Paranoia Levels & False Positive Handling)](https://coreruleset.org/docs/2-how-crs-works/2-1-anomaly_scoring/) — README oficial do coreruleset/coreruleset apresentando a arquitetura do OWASP CRS v4, cobertura de ataques e integração com motores WAF; consultado em 2026-10-03.
- [OWASP Core Rule Set (CRS) — Official GitHub Repository](https://github.com/coreruleset/coreruleset) — Repositório oficial Apache-2.0 do OWASP Core Rule Set; consultado em 2026-10-03.
