---
id: software.testes.tranche07.000123
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
fontes: ["https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/03-Testing_for_Session_Fixation", "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/01-Testing_for_Session_Management_Schema"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Teste de regeneração contra session fixation", "Teste: Teste de regeneração contra session fixation"]
lote: software-testes-2000-0001
---

# Teste de regeneração contra session fixation

## Em uma frase
Confirme que uma sessão pré-autenticação não conserva o mesmo identificador depois que a identidade ou o privilégio da conta muda.

## Por que importa
Se o identificador conhecido antes do login continua válido após autenticação, uma sessão previamente escolhida pode herdar privilégios.

## Como funciona
Em ambiente de teste, inicie sessão anônima, registre cookie, autentique uma conta controlada e compare o identificador. Teste também elevação de privilégio e logout; o token anterior não deve acessar a sessão autenticada.

## Exemplo
Abra carrinho anônimo, anote seu cookie, autentique o usuário de QA e confirme que um novo identificador é emitido e que o cookie inicial não recupera conteúdo protegido.

## Limites e trade-offs
Aplicações podem ter múltiplos cookies e armazenamento distribuído; compare o identificador que efetivamente vincula o estado autenticado. Não compartilhe tokens nem tente fixar sessão de usuários reais.

## Como verificar
Automatize a comparação de identidade antes/depois e a tentativa com token anterior, verificando resposta e estado server-side; teste login e mudanças de privilégio relevantes.

## Conexões
- [[cookies-seguranca-sessao-http]] — aprofundamento relacionado.
- [[testes-sessao-idle-timeout-replay]] — aprofundamento relacionado.

## Fontes
- [OWASP WSTG — Session Fixation](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/03-Testing_for_Session_Fixation) — identificador não deve permanecer igual ao atravessar autenticação; consultado em 2026-10-01.
- [OWASP WSTG — Session Management Schema](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/01-Testing_for_Session_Management_Schema) — análise do ciclo de vida e das propriedades do identificador de sessão; consultado em 2026-10-01.
