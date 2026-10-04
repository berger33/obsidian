---
id: software.seguranca.tranche02.000119
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
fontes: ["https://coreruleset.org/docs/2-how-crs-works/2-1-anomaly_scoring/", "https://raw.githubusercontent.com/coreruleset/coreruleset/main/README.md", "https://github.com/coreruleset/coreruleset"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OWASP CRS Inspeção de Resposta Outbound (`RESPONSE-950` a `959`): bloqueio de vazamento de erros SQL, stack traces e web shells

## Em uma frase
Os arquivos **`RESPONSE-950-DATA-LEAKAGES.conf`** a **`RESPONSE-955-WEB-SHELLS.conf`** do OWASP CRS inspecionam os cabeçalhos e o corpo da resposta HTTP retornada pelo servidor de aplicação (Fases 3 e 4) para detectar vazamentos de mensagens de erro de banco de dados (`951`), erros de Java (`952`), erros e código-fonte PHP (`953`), erros do IIS (`954`) e saídas conhecidas de Web Shells (`955`).

## Por que importa
Em ataques de *Error-based SQL Injection* ou falhas de configuração em produção (`APP_DEBUG=true`), a resposta HTTP devolve ao invasor a mensagem exata do driver PostgreSQL/MySQL ou o stack trace completo com caminhos internos do servidor.

## Como funciona
Quando as regras `950–955` detectam uma assinatura crítica de erro de banco ou stack trace na resposta, elas incrementam o `tx.outbound_anomaly_score_pl*`, e o arquivo **`RESPONSE-959-BLOCKING-EVALUATION.conf`** intercepta a resposta antes de enviá-la à rede, substituindo-a por um erro genérico `403`/`500` seguro!

## Exemplo
```apache
# Garantindo que o motor WAF inspecione respostas textuais e JSON para as regras 950-959 do CRS:
SecResponseBodyAccess On
SecResponseBodyMimeType text/plain text/html application/json
SecResponseBodyLimit 524288
SecResponseBodyLimitAction ProcessPartial
```

## Limites e trade-offs
Para que as regras `950–959` funcionem sobre APIs REST que retornam JSON, certifique-se de que `application/json` consta na diretiva `SecResponseBodyMimeType` do motor WAF.

## Como verificar
Simule em ambiente de teste o retorno de uma string de erro `You have an error in your SQL syntax;` e verifique o acionamento da família `951` e `959100`.

## Conexões
- [[owaspcrs-validacao-protocolo-http-911-920-metodos-content-type-charset]] — Veja também: OWASP CRS Políticas de Protocolo HTTP (`900200–900250` e `REQUEST-911`/`920`): restrição de métodos HTTP, `Content-Type` e versões TLS/HTTP.
- [[owaspcrs-sampling-percentage-rollout-gradual-crs-setup-900400]] — Veja também: OWASP CRS Sampling Mode (`tx.sampling_percentage`, Regra `900400`) e `coreruleset-cli`: rollout gradual por amostragem de tráfego.

## Fontes
- [OWASP Core Rule SetOfficial Documentation — Anomaly Scoring Mode (Inbound/Outbound Scores, Thresholds, Severity Points & Collaborative Detection)](https://coreruleset.org/docs/2-how-crs-works/2-1-anomaly_scoring/) — Documentação oficial do OWASP CRS explicando o mecanismo de pontuação de anomalias (Inbound/Outbound), pesos por severidade (CRITICAL=5, ERROR=4, WARNING=3, NOTICE=2) e avaliação nas regras 949110 e 959100; consultado em 2026-10-03.
- [OWASP Core Rule Set GitHub — README.md (CRS v4 Architecture, Attack Categories, Paranoia Levels & False Positive Handling)](https://raw.githubusercontent.com/coreruleset/coreruleset/main/README.md) — README oficial do coreruleset/coreruleset apresentando a arquitetura do OWASP CRS v4, cobertura de ataques e integração com motores WAF; consultado em 2026-10-03.
- [OWASP Core Rule Set (CRS) — Official GitHub Repository](https://github.com/coreruleset/coreruleset) — Repositório oficial Apache-2.0 do OWASP Core Rule Set; consultado em 2026-10-03.
