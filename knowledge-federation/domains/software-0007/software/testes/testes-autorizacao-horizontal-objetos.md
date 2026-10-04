---
id: software.testes.tranche07.000120
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
fontes: ["https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/02-Testing_for_Bypassing_Authorization_Schema", "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/03-Testing_for_Privilege_Escalation"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Teste de autorização horizontal por objeto", "Teste: Teste de autorização horizontal por objeto"]
lote: software-testes-2000-0001
---

# Teste de autorização horizontal por objeto

## Em uma frase
Verifique se uma conta autenticada consegue ler ou alterar somente os objetos pertencentes ao seu próprio escopo.

## Por que importa
Autenticação prova identidade, não autorização para cada objeto; identificadores previsíveis ou filtragem incompleta podem expor dados de outra conta ou tenant.

## Como funciona
Prepare duas contas equivalentes e dados distintos; para cada operação de leitura, atualização e exclusão, substitua o identificador pelo do outro usuário mantendo a própria sessão. Teste rotas diretas, APIs e caminhos em lote.

## Exemplo
A conta A solicita seu próprio pedido e depois tenta consultar e cancelar o pedido de B usando o identificador de teste. A aprovação exige ausência de dados de B e nenhuma alteração colateral.

## Limites e trade-offs
Execute somente em ambiente e dados autorizados. Resposta 404 ou 403 não basta se informação vaza em mensagens, timing ou efeitos laterais; regras legítimas de compartilhamento devem estar explícitas.

## Como verificar
Compare corpo, código, cabeçalhos e estado persistido após cada tentativa; repita para endpoints relacionados e valide tanto acesso negado quanto autorização positiva do proprietário.

## Conexões
- [[risk-based-testing-priorizacao-risco]] — aprofundamento relacionado.
- [[test-data-privacidade-sinteticos]] — aprofundamento relacionado.

## Fontes
- [OWASP WSTG — Bypassing Authorization Schema](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/02-Testing_for_Bypassing_Authorization_Schema) — testes de autorização horizontal e vertical com contas e permissões distintas; consultado em 2026-10-01.
- [OWASP WSTG — Privilege Escalation](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/03-Testing_for_Privilege_Escalation) — testes de elevação de privilégios e controles de autorização; consultado em 2026-10-01.
