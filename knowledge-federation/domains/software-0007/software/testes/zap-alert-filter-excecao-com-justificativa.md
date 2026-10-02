---
id: software.testes.tranche10.000427
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
fontes: ["https://www.zaproxy.org/docs/desktop/addons/alert-filters/", "https://www.zaproxy.org/docs/desktop/addons/report-generation/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# OWASP ZAP: aplicar alert filter com contexto e justificativa

## Em uma frase
Alert Filters podem sobrescrever o risco de alertas de scans ativos e passivos; há regras globais e associadas a contexto.

## Por que importa
Scans de segurança diferem no risco e na evidência que produzem; separar observação passiva de ataque ativo protege sistemas e melhora interpretação. Filtro amplo pode esconder novo achado real junto com a condição que motivou a exceção original.

## Como funciona
Defina alvo, autorização, autenticação, política e espera de jobs em plano reproduzível; preserve alertas e resultados para triagem. Restrinja a regra ao contexto e ao padrão de alerta pretendidos, documente motivo, responsável e revisão; teste também o efeito em alertas já existentes.

## Exemplo
Um falso positivo conhecido em staging recebe uma reclassificação limitada ao contexto e à regra, com rationale e data para reavaliação.

## Limites e trade-offs
ZAP encontra sinais sujeitos a falso positivo e cobertura incompleta; scan passivo não substitui análise ativa autorizada nem revisão manual. Por padrão o filtro se aplica a novos alertas; alterar risco não corrige nem prova ausência da causa, e uma regra ampla pode reduzir a visibilidade de findings reais.

## Como verificar
Teste alertas dentro e fora do escopo e confirme o comportamento em alertas novos e existentes; preserve evidência bruta para triagem e auditoria.

## Conexões
- [[zap-autenticacao-verificar-sessao-do-scan]] — Veja também: OWASP ZAP: verificar autenticação efetiva durante o scan.
- [[zap-relatorio-artefato-e-evidencia]] — Veja também: OWASP ZAP: preservar relatório como evidência de uma execução.

## Fontes
- [OWASP ZAP — Alert Filters](https://www.zaproxy.org/docs/desktop/addons/alert-filters/) — sobrescrita de risco por filtros globais ou contextuais aplicados a alertas; consultado em 2026-10-02.
- [OWASP ZAP — Report Generation](https://www.zaproxy.org/docs/desktop/addons/report-generation/) — templates em formatos variados e suporte ao Automation Framework; consultado em 2026-10-02.
