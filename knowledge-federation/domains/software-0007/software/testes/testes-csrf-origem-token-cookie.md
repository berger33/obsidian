---
id: software.testes.tranche07.000124
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
fontes: ["https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/05-Testing_for_Cross_Site_Request_Forgery", "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/02-Testing_for_Bypassing_Authorization_Schema"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Testes de CSRF com origem, token e cookies", "Teste: Testes de CSRF com origem, token e cookies"]
lote: software-testes-2000-0001
---

# Testes de CSRF com origem, token e cookies

## Em uma frase
Examine se uma operação que altera estado rejeita solicitações cross-site não autorizadas e se proteções são avaliadas no contexto real dos cookies.

## Por que importa
Browsers podem anexar credenciais de sessão automaticamente; uma ação induzida por site externo pode operar sob a identidade já autenticada.

## Como funciona
Use contas e ambiente de teste. Compare solicitação legítima com versões sem token, token inválido, origem não confiável e método/state change alternativo; confira atributos SameSite e comportamento em browsers compatíveis, sem considerar uma única falha de PoC prova de proteção.

## Exemplo
Em staging, submeta uma alteração de preferência pela origem autorizada e repita por uma página de teste em outra origem; confirme que apenas a solicitação legítima muda o estado.

## Limites e trade-offs
CORS e SameSite não substituem toda análise de CSRF. Comportamento padrão de navegadores varia; ações não idempotentes e autenticação por mecanismos diferentes exigem interpretação específica.

## Como verificar
Verifique cabeçalhos e cookies emitidos, resultado persistido, token e política de origem; use navegador e configuração de teste documentados e mantenha o teste isolado.

## Conexões
- [[csrf-token-protecao-web]] — aprofundamento relacionado.
- [[testes-autorizacao-horizontal-objetos]] — aprofundamento relacionado.

## Fontes
- [OWASP WSTG — Cross-Site Request Forgery](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/05-Testing_for_Cross_Site_Request_Forgery) — dependência de cookies e proteção de operações que alteram estado; consultado em 2026-10-01.
- [OWASP WSTG — Bypassing Authorization Schema](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/02-Testing_for_Bypassing_Authorization_Schema) — testes de autorização horizontal e vertical com contas e permissões distintas; consultado em 2026-10-01.
