---
id: software.testes.tranche07.000127
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
fontes: ["https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html", "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/01-Testing_for_Session_Management_Schema"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Teste de limitação de tentativas de autenticação", "Teste: Teste de limitação de tentativas de autenticação"]
lote: software-testes-2000-0001
---

# Teste de limitação de tentativas de autenticação

## Em uma frase
Verifique que tentativas automatizadas são limitadas sem expor a existência de contas nem permitir que um teste cause bloqueio de usuários reais.

## Por que importa
Controles insuficientes podem facilitar tentativa repetida de credenciais; respostas distintas podem revelar quais identificadores correspondem a contas.

## Como funciona
Em QA, use contas sintéticas e taxas baixas acordadas. Teste sequência de falhas, janela de reset, resposta, monitoramento e comportamento para login válido; examine se a política evita bloqueio fácil de terceiros e se aplica a caminhos alternativos.

## Exemplo
Compare respostas para usuário sintético existente e inexistente após erros controlados, e verifique que o limite documentado é aplicado sem revelar estado da conta nem deixar a sessão válida bloqueada indefinidamente.

## Limites e trade-offs
Não há limiar universal e bloqueios podem causar negação de serviço. Regras precisam equilibrar risco, experiência e recuperação; não rode força bruta nem faça testes de volume em produção.

## Como verificar
Use uma conta disposable, limite tentativas conforme plano aprovado, confira resposta e telemetria, espere o período de reset e prove que login legítimo retorna ao funcionamento esperado.

## Conexões
- [[risk-based-testing-priorizacao-risco]] — aprofundamento relacionado.
- [[testes-logs-redaction-injection]] — aprofundamento relacionado.

## Fontes
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) — controles de autenticação, respostas e defesa contra abuso automatizado; consultado em 2026-10-01.
- [OWASP WSTG — Session Management Schema](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/01-Testing_for_Session_Management_Schema) — análise do ciclo de vida e das propriedades do identificador de sessão; consultado em 2026-10-01.
