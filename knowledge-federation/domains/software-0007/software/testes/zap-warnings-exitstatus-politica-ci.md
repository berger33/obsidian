---
id: software.testes.tranche10.000423
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
fontes: ["https://www.zaproxy.org/docs/desktop/addons/automation-framework/job-exitstatus/", "https://www.zaproxy.org/docs/automate/automation-framework/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# OWASP ZAP: declarar política de alertas e status de saída

## Em uma frase
Automation Framework oferece job exitStatus para derivar o status da execução dos resultados configurados.

## Por que importa
Scans de segurança diferem no risco e na evidência que produzem; separar observação passiva de ataque ativo protege sistemas e melhora interpretação. A presença de alertas pode aparecer como warning sem interromper a pipeline, dependendo do modo e da política escolhida.

## Como funciona
Defina alvo, autorização, autenticação, política e espera de jobs em plano reproduzível; preserve alertas e resultados para triagem. Defina quais alertas, severidades ou condições reprovam o job e mantenha essa decisão versionada junto ao plano.

## Exemplo
A CI falha somente para findings de risco acordado e ainda publica o relatório completo para triagem.

## Limites e trade-offs
ZAP encontra sinais sujeitos a falso positivo e cobertura incompleta; scan passivo não substitui análise ativa autorizada nem revisão manual. Status de saída não comprova ausência de falhas de segurança nem substitui leitura de evidência e contexto.

## Como verificar
Injete um alerta controlado e confirme código de saída, mensagem e artefato produzidos pelo job.

## Conexões
- [[zap-active-scan-autorizacao-e-ambiente]] — Veja também: OWASP ZAP: limitar active scan a alvo autorizado.
- [[zap-automation-framework-plano-yaml]] — Veja também: OWASP ZAP: versionar o Automation Framework como plano.

## Fontes
- [OWASP ZAP — Exit Status job](https://www.zaproxy.org/docs/desktop/addons/automation-framework/job-exitstatus/) — níveis de alerta e valores configuráveis para o código de saída do plano; consultado em 2026-10-02.
- [OWASP ZAP — Automation Framework](https://www.zaproxy.org/docs/automate/automation-framework/) — planos YAML, ambiente, jobs, autenticação e testes de resultado; consultado em 2026-10-02.
