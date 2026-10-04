---
id: software.seguranca.tranche13.001256
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

# Integração do ModSecurity com o **OWASP Core Rule Set (`CRS`)**: Modelo de **Pontuação de Anomalia (*Anomaly Scoring*)** e **Paranoia Levels (`PL1`–`PL4`)**

## Em uma frase
Embora você possa escrever regras `SecRule` próprias, o verdadeiro poder do ModSecurity em produção vem da sua combinação com o **OWASP Core Rule Set (`coreruleset/coreruleset`)** — o conjunto comunitário oficial de regras WAF que protege contra o **OWASP Top 10** (`913` Scanner Detection, `920` Protocol Enforcement, `930` LFI, `931` RFI, `932` RCE/Command Injection, `933` PHP, `934` Node.js/Generic, `941` XSS, `942` SQLi, `944` Java/Log4Shell e `951–955` Data Leakages)!

## Por que importa
Como o OWASP CRS moderno evita que uma única regra de baixa confiança bloqueie um usuário legítimo por engano? Através do modo **Collaborative Anomaly Scoring (`tx.inbound_anomaly_score_threshold` e `tx.outbound_anomaly_score_threshold`)**: cada regra que casa adiciona pontos ao contador da transação (`CRITICAL = +5`, `ERROR = +4`, `WARNING = +3`, `NOTICE = +2`), e a regra de avaliação final (`949110` para entrada, `959100` para saída) só bloqueia a requisição se a soma total atingir ou ultrapassar o limiar configurado (por padrão **`5` pontos**)!

## Como funciona
Além disso, o CRS permite calibrar a agressividade das regras através dos **4 Níveis de Paranoia (`tx.blocking_paranoia_level` de `1` a `4`)**: **`PL1`** (padrão para todas as aplicações web, quase zero falsos positivos), **`PL2`** (recomendado para e-commerce e sistemas corporativos com tuning básico), **`PL3`** (para sistemas financeiros/bancários de alta criticidade) e **`PL4`** (máxima restrição)!

## Exemplo
```apache
# Configurar no crs-setup.conf o Paranoia Level 2 para observacao (detection_paranoia_level=2) mantendo o bloqueio ativo apenas para PL1
SecAction "id:900000,phase:1,nolog,pass,t:none,setvar:tx.blocking_paranoia_level=1"
SecAction "id:900001,phase:1,nolog,pass,t:none,setvar:tx.detection_paranoia_level=2"
SecAction "id:900110,phase:1,nolog,pass,t:none,setvar:tx.inbound_anomaly_score_threshold=5,setvar:tx.outbound_anomaly_score_threshold=4"
```

## Limites e trade-offs
Olhe que estratégia brilhante nas regras `900000` e `900001` acima: você pode configurar **`tx.blocking_paranoia_level=1`** (para bloquear ativamente apenas regras `PL1` de altíssima certeza) enquanto define **`tx.detection_paranoia_level=2`** (para que as regras mais rigorosas do `PL2` rodem apenas gerando logs sem somar pontos de bloqueio até você concluir o tuning de falsos positivos do `PL2`)!

## Como verificar
Nunca edite diretamente os arquivos dentro da pasta `rules/REQUEST-9*.conf` do CRS (pois isso impediria atualizar o CRS via Git/pacote); faça todas as customizações nos arquivos `crs-setup.conf`, `REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf` e `RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf`!

## Conexões
- [[modsecurity-deteccao-sqli-xss-libinjection-detectsqli-detectxss]] — Veja também: Detecção Léxica de **SQL Injection (`@detectSQLi`)** e **XSS (`@detectXSS`)** com **`libinjection`** no ModSecurity v3: Além das Expressões Regulares.
- [[modsecurity-tuning-falsos-positivos-exclusoes-ctl-ruleremovetargetbyid]] — Veja também: Engenharia de Tuning e Eliminação Cirúrgica de Falsos Positivos no ModSecurity: **`ctl:ruleRemoveTargetById`** vs. `SecRuleRemoveById`.
- [[modsecurity-arquitetura-libmodsecurity-v3-conectores-nginx-apache-envoy]] — Referência cruzada direta com modsecurity-arquitetura-libmodsecurity-v3-conectores-nginx-apache-envoy.

## Fontes
- [OWASP ModSecurity v3 (`libmodsecurity`) Official GitHub](https://raw.githubusercontent.com/owasp-modsecurity/ModSecurity/v3/master/README.md) — repositório oficial do OWASP ModSecurity v3 detalhando a arquitetura standalone da biblioteca `libmodsecurity`, conectores Nginx/Apache, PCRE2, `libinjection` e YAJL JSON; consultado em 2026-10-03.
- [OWASP ModSecurity v3 Recommended Configuration (`modsecurity.conf-recommended`)](https://raw.githubusercontent.com/owasp-modsecurity/ModSecurity/v3/master/modsecurity.conf-recommended) — configuração oficial recomendada do ModSecurity v3 cobrindo `SecRuleEngine`, `SecRequestBodyAccess`, processadores XML/JSON, limites anti-DoS e `SecAuditLogFormat JSON`; consultado em 2026-10-03.
