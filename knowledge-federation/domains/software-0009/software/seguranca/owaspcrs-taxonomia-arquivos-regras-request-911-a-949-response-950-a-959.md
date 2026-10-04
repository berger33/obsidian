---
id: software.seguranca.tranche02.000115
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

# OWASP CRS Taxonomia Numerada de Regras (`901–999`): organização modular de `REQUEST-911..949` e `RESPONSE-950..959`

## Em uma frase
Os arquivos de regras do OWASP CRS seguem uma numeração padronizada de 3 dígitos que define tanto a ordem exata de execução quanto a categoria de ameaça (os 3 primeiros dígitos do `id:` de 6 dígitos da regra identificam o arquivo de origem, ex.: `942100` pertence a `REQUEST-942-APPLICATION-ATTACK-SQLI.conf`).

## Por que importa
Quando um alerta WAF aparece no SIEM informando `id: 932130` ou `id: 941100`, conhecer a tabela de prefixos do CRS permite identificar instantaneamente a família do ataque.

## Como funciona
As principais famílias de requisição são: **`901`** (Inicialização), **`911`** (Method Enforcement), **`913`** (Scanner Detection), **`920`** (Protocol Enforcement), **`921`** (Protocol Attack / HTTP Splitting / Smuggling), **`922`** (Multipart Bypass), **`930`** (LFI), **`931`** (RFI), **`932`** (RCE / Command Injection), **`933`** (PHP), **`934`** (Node.js/Generic RCE), **`941`** (XSS), **`942`** (SQLi), **`943`** (Session Fixation), **`944`** (Java/Log4j) e **`949`** (Blocking Evaluation Inbound). Já na resposta: **`950–955`** (Data/Error Leakages: SQL, PHP, IIS, Java, Web Shells) e **`959`** (Blocking Evaluation Outbound).

## Exemplo
```bash
# Listando os arquivos de regras do OWASP CRS v4 em ordem de avaliação:
ls -1 /etc/coraza/rules/
```

## Limites e trade-offs
Para desativar toda uma categoria irrelevante para sua stack apenas em um parâmetro específico, você pode usar intervalos ou prefixos de tag como `attack-php` ou `attack-java`.

## Como verificar
Inspecione o campo `id` e as `tag` de qualquer alerta do CRS para mapear sua categoria (`920`, `932`, `941`, `942`).

## Conexões
- [[owaspcrs-paranoia-levels-pl1-a-pl4-blocking-vs-detection-paranoia-level]] — Veja também: OWASP CRS Níveis de Paranoia (`PL1` a `PL4`): uso combinado de `tx.blocking_paranoia_level` e `tx.detection_paranoia_level`.
- [[owaspcrs-tratamento-falsos-positivos-ctl-ruleremovetargetbyid-before-after]] — Veja também: OWASP CRS Tuning de Falsos Positivos: `ctl:ruleRemoveTargetById` em tempo de execução (`BEFORE-CRS`) vs `SecRuleUpdateTargetById` (`AFTER-CRS`).

## Fontes
- [OWASP Core Rule SetOfficial Documentation — Anomaly Scoring Mode (Inbound/Outbound Scores, Thresholds, Severity Points & Collaborative Detection)](https://raw.githubusercontent.com/coreruleset/coreruleset/main/README.md) — Documentação oficial do OWASP CRS explicando o mecanismo de pontuação de anomalias (Inbound/Outbound), pesos por severidade (CRITICAL=5, ERROR=4, WARNING=3, NOTICE=2) e avaliação nas regras 949110 e 959100; consultado em 2026-10-03.
- [OWASP Core Rule Set GitHub — README.md (CRS v4 Architecture, Attack Categories, Paranoia Levels & False Positive Handling)](https://coreruleset.org/docs/2-how-crs-works/2-1-anomaly_scoring/) — README oficial do coreruleset/coreruleset apresentando a arquitetura do OWASP CRS v4, cobertura de ataques e integração com motores WAF; consultado em 2026-10-03.
- [OWASP Core Rule Set (CRS) — Official GitHub Repository](https://github.com/coreruleset/coreruleset) — Repositório oficial Apache-2.0 do OWASP Core Rule Set; consultado em 2026-10-03.
