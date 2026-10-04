---
id: software.testes.tranche10.000426
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
fontes: ["https://www.zaproxy.org/docs/getting-further/authentication/authentication-methods/", "https://www.zaproxy.org/docs/automate/automation-framework/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# OWASP ZAP: verificar autenticação efetiva durante o scan

## Em uma frase
ZAP suporta métodos de autenticação e verificações de sessão configurados no ambiente e no contexto.

## Por que importa
Scans de segurança diferem no risco e na evidência que produzem; separar observação passiva de ataque ativo protege sistemas e melhora interpretação. Um scan que recebe somente páginas de login pode parecer concluído enquanto endpoints autenticados ficaram invisíveis.

## Como funciona
Defina alvo, autorização, autenticação, política e espera de jobs em plano reproduzível; preserve alertas e resultados para triagem. Configure usuário e mecanismo, inclua sinal de sessão válida e confirme requisições autenticadas no histórico.

## Exemplo
A pipeline verifica endpoint de identidade e amostra uma rota protegida antes de interpretar cobertura do restante da API.

## Limites e trade-offs
ZAP encontra sinais sujeitos a falso positivo e cobertura incompleta; scan passivo não substitui análise ativa autorizada nem revisão manual. Automatizar login pode falhar por MFA, CSRF ou fluxo interativo; não exponha credenciais no relatório.

## Como verificar
Inspecione requests e responses com dados sensíveis mascarados e valide que o scanner permaneceu autenticado durante a execução.

## Conexões
- [[zap-passive-scan-wait-antes-do-relatorio]] — Veja também: OWASP ZAP: aguardar a fila passiva antes de finalizar.
- [[zap-alert-filter-excecao-com-justificativa]] — Veja também: OWASP ZAP: aplicar alert filter com contexto e justificativa.

## Fontes
- [OWASP ZAP — Authentication methods](https://www.zaproxy.org/docs/getting-further/authentication/authentication-methods/) — métodos de autenticação e verificação de sessão; consultado em 2026-10-02.
- [OWASP ZAP — Automation Framework](https://www.zaproxy.org/docs/automate/automation-framework/) — planos YAML, ambiente, jobs, autenticação e testes de resultado; consultado em 2026-10-02.
