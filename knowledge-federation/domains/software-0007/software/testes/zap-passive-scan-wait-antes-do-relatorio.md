---
id: software.testes.tranche10.000425
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
fontes: ["https://www.zaproxy.org/docs/desktop/addons/automation-framework/job-pscanwait/", "https://www.zaproxy.org/docs/automate/automation-framework/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# OWASP ZAP: aguardar a fila passiva antes de finalizar

## Em uma frase
O job passiveScan-wait aguarda que o scanner passivo termine de processar a fila atual.

## Por que importa
Scans de segurança diferem no risco e na evidência que produzem; separar observação passiva de ataque ativo protege sistemas e melhora interpretação. Gerar relatório antes da fila esvaziar pode omitir alertas de respostas já visitadas.

## Como funciona
Defina alvo, autorização, autenticação, política e espera de jobs em plano reproduzível; preserve alertas e resultados para triagem. Coloque a espera após crawling/importação que produz mensagens e antes do relatório ou avaliação final.

## Exemplo
O plano importa OpenAPI, executa as requisições, aguarda processamento passivo e só então salva os alertas.

## Limites e trade-offs
ZAP encontra sinais sujeitos a falso positivo e cobertura incompleta; scan passivo não substitui análise ativa autorizada nem revisão manual. Essa espera cobre a fila passiva atual, não garante que todas as rotas do alvo tenham sido descobertas.

## Como verificar
Confira ordem dos jobs e confirme que a contagem de mensagens não cresce após a geração do relatório.

## Conexões
- [[zap-automation-framework-plano-yaml]] — Veja também: OWASP ZAP: versionar o Automation Framework como plano.
- [[zap-autenticacao-verificar-sessao-do-scan]] — Veja também: OWASP ZAP: verificar autenticação efetiva durante o scan.

## Fontes
- [OWASP ZAP — Passive Scan Wait job](https://www.zaproxy.org/docs/desktop/addons/automation-framework/job-pscanwait/) — espera a conclusão do processamento da fila passiva atual; consultado em 2026-10-02.
- [OWASP ZAP — Automation Framework](https://www.zaproxy.org/docs/automate/automation-framework/) — planos YAML, ambiente, jobs, autenticação e testes de resultado; consultado em 2026-10-02.
