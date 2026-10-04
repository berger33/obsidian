---
id: software.testes.tranche10.000422
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
fontes: ["https://www.zaproxy.org/docs/desktop/addons/automation-framework/job-ascan/", "https://www.zaproxy.org/docs/automate/automation-framework/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# OWASP ZAP: limitar active scan a alvo autorizado

## Em uma frase
Active Scan envia requisições de ataque para identificar vulnerabilidades e pode alterar ou sobrecarregar o sistema alvo.

## Por que importa
Scans de segurança diferem no risco e na evidência que produzem; separar observação passiva de ataque ativo protege sistemas e melhora interpretação. Apontar acidentalmente um scanner ativo a produção pode afetar dados, disponibilidade ou terceiros.

## Como funciona
Defina alvo, autorização, autenticação, política e espera de jobs em plano reproduzível; preserve alertas e resultados para triagem. Obtenha autorização, use ambiente isolado com dados descartáveis, restrinja contexto, duração, taxa e regras habilitadas.

## Exemplo
Um pipeline executa active scan apenas em staging efêmero, com janela aprovada e conta de teste sem privilégios.

## Limites e trade-offs
ZAP encontra sinais sujeitos a falso positivo e cobertura incompleta; scan passivo não substitui análise ativa autorizada nem revisão manual. Reduzir strength ou duração não transforma um scan ativo em observação sem risco.

## Como verificar
Teste a configuração contra hostname permitido e confirme que o plano bloqueia destinos externos antes da execução.

## Conexões
- [[zap-api-scan-definicao-e-active-scan]] — Veja também: OWASP ZAP: tratar API scan como active scan.
- [[zap-warnings-exitstatus-politica-ci]] — Veja também: OWASP ZAP: declarar política de alertas e status de saída.

## Fontes
- [OWASP ZAP — Active Scan job](https://www.zaproxy.org/docs/desktop/addons/automation-framework/job-ascan/) — ataque ativo que exige permissão, com parâmetros de contexto, política, escopo e duração; consultado em 2026-10-02.
- [OWASP ZAP — Automation Framework](https://www.zaproxy.org/docs/automate/automation-framework/) — planos YAML, ambiente, jobs, autenticação e testes de resultado; consultado em 2026-10-02.
