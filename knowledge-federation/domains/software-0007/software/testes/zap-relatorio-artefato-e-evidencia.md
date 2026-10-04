---
id: software.testes.tranche10.000428
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
fontes: ["https://www.zaproxy.org/docs/desktop/addons/report-generation/", "https://www.zaproxy.org/docs/automate/automation-framework/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# OWASP ZAP: preservar relatório como evidência de uma execução

## Em uma frase
O add-on de Report Generation produz relatórios em formatos configuráveis e tem suporte ao Automation Framework.

## Por que importa
Scans de segurança diferem no risco e na evidência que produzem; separar observação passiva de ataque ativo protege sistemas e melhora interpretação. Sem artefato e identificação do scan, um finding não pode ser correlacionado com versão, alvo ou política usados.

## Como funciona
Defina alvo, autorização, autenticação, política e espera de jobs em plano reproduzível; preserve alertas e resultados para triagem. Arquive relatório, versão do ZAP, plano, alvo autorizado e metadados de build sem incluir tokens ou dados sensíveis.

## Exemplo
A pipeline gera relatórios HTML e Markdown com um template configurado, vincula os artifacts ao commit e mantém credenciais fora dos arquivos publicados.

## Limites e trade-offs
ZAP encontra sinais sujeitos a falso positivo e cobertura incompleta; scan passivo não substitui análise ativa autorizada nem revisão manual. Relatório pode conter URLs, parâmetros ou evidências sensíveis e precisa de política de retenção e acesso.

## Como verificar
Abra o artefato de uma execução conhecida, confira timestamp e commit e verifique a sanitização antes de compartilhá-lo.

## Conexões
- [[zap-alert-filter-excecao-com-justificativa]] — Veja também: OWASP ZAP: aplicar alert filter com contexto e justificativa.
- [[zap-separar-passive-active-pipeline]] — Veja também: OWASP ZAP: separar passivo e ativo em etapas de risco distinto.

## Fontes
- [OWASP ZAP — Report Generation](https://www.zaproxy.org/docs/desktop/addons/report-generation/) — templates em formatos variados e suporte ao Automation Framework; consultado em 2026-10-02.
- [OWASP ZAP — Automation Framework](https://www.zaproxy.org/docs/automate/automation-framework/) — planos YAML, ambiente, jobs, autenticação e testes de resultado; consultado em 2026-10-02.
