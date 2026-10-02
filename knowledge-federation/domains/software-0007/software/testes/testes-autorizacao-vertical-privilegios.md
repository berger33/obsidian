---
id: software.testes.tranche07.000121
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-07.md"
fontes: ["https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/03-Testing_for_Privilege_Escalation", "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/02-Testing_for_Bypassing_Authorization_Schema"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Teste de autorização vertical e elevação de privilégios", "Teste: Teste de autorização vertical e elevação de privilégios"]
lote: software-testes-2000-0001
---

# Teste de autorização vertical e elevação de privilégios

## Em uma frase
Avalie se usuários de menor privilégio são impedidos de executar funções reservadas a papéis superiores, inclusive por chamadas diretas.

## Por que importa
Ocultar um botão na interface não protege o endpoint; falhas na checagem de papel podem permitir ações administrativas por clientes comuns.

## Como funciona
Construa matriz papel-operação-recurso e percorra endpoints e métodos HTTP com sessões de papéis distintos. Tente acesso direto, parâmetros de papel adulterados e fluxos alternativos, sem executar mudanças destrutivas fora de ambiente isolado.

## Exemplo
Compare usuário comum e administrador de teste ao chamar operação de alteração de permissões; confirme que servidor nega a primeira e permite a segunda somente com autorização correspondente.

## Limites e trade-offs
Papéis podem conter delegações e políticas específicas, então proibição ampla pode gerar falso positivo. Planeje rollback e use contas sintéticas; teste autorização no servidor, não apenas a renderização da UI.

## Como verificar
Registre matriz esperada, request/response sanitizados e estado final; confirme que a tentativa negada não criou nem modificou recurso e que o papel permitido continua funcional.

## Conexões
- [[risk-based-testing-priorizacao-risco]] — aprofundamento relacionado.
- [[testes-autorizacao-horizontal-objetos]] — aprofundamento relacionado.

## Fontes
- [OWASP WSTG — Privilege Escalation](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/03-Testing_for_Privilege_Escalation) — testes de elevação de privilégios e controles de autorização; consultado em 2026-10-01.
- [OWASP WSTG — Bypassing Authorization Schema](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/02-Testing_for_Bypassing_Authorization_Schema) — testes de autorização horizontal e vertical com contas e permissões distintas; consultado em 2026-10-01.
