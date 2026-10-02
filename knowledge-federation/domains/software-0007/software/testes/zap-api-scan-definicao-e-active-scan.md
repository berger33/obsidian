---
id: software.testes.tranche10.000421
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-10.md"
fontes: ["https://www.zaproxy.org/docs/docker/api-scan/", "https://www.zaproxy.org/docs/desktop/addons/automation-framework/job-ascan/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# OWASP ZAP: tratar API scan como active scan

## Em uma frase
API Scan importa definições como OpenAPI, SOAP ou GraphQL e aplica varredura adaptada ao formato.

## Por que importa
Scans de segurança diferem no risco e na evidência que produzem; separar observação passiva de ataque ativo protege sistemas e melhora interpretação. A importação do contrato amplia descoberta de rotas, mas o modo padrão pode enviar payloads ativos ao serviço.

## Como funciona
Defina alvo, autorização, autenticação, política e espera de jobs em plano reproduzível; preserve alertas e resultados para triagem. Use uma definição atualizada, limite escopo e autorização e escolha explicitamente se active scanning será executado ou ignorado.

## Exemplo
A CI importa OpenAPI de uma aplicação de teste e executa o scan apenas no host autorizado da pipeline.

## Limites e trade-offs
ZAP encontra sinais sujeitos a falso positivo e cobertura incompleta; scan passivo não substitui análise ativa autorizada nem revisão manual. Uma especificação incompleta omite rotas ou autenticação; pular active scan reduz o tipo de evidência obtido.

## Como verificar
Revise target, origem da definição, usuários e opções do container, e confirme no log quais fases rodaram.

## Conexões
- [[zap-baseline-scan-passivo-sem-ataque]] — Veja também: OWASP ZAP: entender o limite do baseline scan.
- [[zap-active-scan-autorizacao-e-ambiente]] — Veja também: OWASP ZAP: limitar active scan a alvo autorizado.

## Fontes
- [OWASP ZAP — API scan](https://www.zaproxy.org/docs/docker/api-scan/) — importação de definições de API e active scanning direcionado; consultado em 2026-10-02.
- [OWASP ZAP — Active Scan job](https://www.zaproxy.org/docs/desktop/addons/automation-framework/job-ascan/) — ataque ativo que exige permissão, com parâmetros de contexto, política, escopo e duração; consultado em 2026-10-02.
