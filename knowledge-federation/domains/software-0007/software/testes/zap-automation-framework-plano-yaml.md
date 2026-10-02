---
id: software.testes.tranche10.000424
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
fontes: ["https://www.zaproxy.org/docs/automate/automation-framework/", "https://www.zaproxy.org/docs/desktop/addons/report-generation/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# OWASP ZAP: versionar o Automation Framework como plano

## Em uma frase
Automation Framework executa jobs sequenciais a partir de um plano YAML com ambiente e configuração definidos.

## Por que importa
Scans de segurança diferem no risco e na evidência que produzem; separar observação passiva de ataque ativo protege sistemas e melhora interpretação. Repetir comandos manuais em máquinas diferentes pode produzir alvos, autenticação e fases de scan inconsistentes.

## Como funciona
Defina alvo, autorização, autenticação, política e espera de jobs em plano reproduzível; preserve alertas e resultados para triagem. Versione o plano, declare contexto e jobs necessários e fixe add-ons e imagem conforme a política de execução.

## Exemplo
Um plano importa API, aguarda spider e passive scan, gera relatório e avalia status final.

## Limites e trade-offs
ZAP encontra sinais sujeitos a falso positivo e cobertura incompleta; scan passivo não substitui análise ativa autorizada nem revisão manual. Jobs disponíveis podem depender de add-ons instalados e da versão do ZAP usada pela imagem.

## Como verificar
Execute o mesmo arquivo localmente e em CI e compare job list, target e configuração efetivamente carregada.

## Conexões
- [[zap-warnings-exitstatus-politica-ci]] — Veja também: OWASP ZAP: declarar política de alertas e status de saída.
- [[zap-passive-scan-wait-antes-do-relatorio]] — Veja também: OWASP ZAP: aguardar a fila passiva antes de finalizar.

## Fontes
- [OWASP ZAP — Automation Framework](https://www.zaproxy.org/docs/automate/automation-framework/) — planos YAML, ambiente, jobs, autenticação e testes de resultado; consultado em 2026-10-02.
- [OWASP ZAP — Report Generation](https://www.zaproxy.org/docs/desktop/addons/report-generation/) — templates em formatos variados e suporte ao Automation Framework; consultado em 2026-10-02.
