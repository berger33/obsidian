---
id: software.testes.tranche07.000125
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
fontes: ["https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting", "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/02-Testing_for_Bypassing_Authorization_Schema"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Teste de saída refletida e codificação contra XSS", "Teste: Teste de saída refletida e codificação contra XSS"]
lote: software-testes-2000-0001
---

# Teste de saída refletida e codificação contra XSS

## Em uma frase
Siga entradas controladas até o contexto de saída e verifique se texto não confiável é exibido como dado, sem execução de conteúdo ativo.

## Por que importa
Entradas refletidas em HTML, atributo, URL ou script podem alterar a interpretação da página se não forem codificadas para o contexto correto.

## Como funciona
Use marcadores benignos e contas de teste para mapear parâmetros e respostas; inspecione HTML/DOM e codificação contextual em diferentes templates. Confira se filtros não são a única barreira e se o conteúdo permanece dado após ida e volta.

## Exemplo
Pesquise um identificador de teste que contenha caracteres de marcação inofensivos, depois procure sua reflexão em título, aviso e campo; confirme que o browser apresenta texto e não cria elemento executável.

## Limites e trade-offs
Teste apenas sistemas autorizados, sem payloads destrutivos nem dados de terceiros. Codificação apropriada depende do contexto; uma resposta escapada em um lugar não prova que outras saídas são seguras.

## Como verificar
Repita por métodos e parâmetros relevantes, registre contexto e codificação observada e valide com analisador de DOM e revisão manual dos templates afetados.

## Conexões
- [[schema-based-api-testing-schemathesis-openapi]] — aprofundamento relacionado.
- [[testes-autorizacao-vertical-privilegios]] — aprofundamento relacionado.

## Fontes
- [OWASP WSTG — Reflected Cross-Site Scripting](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting) — entrada refletida deve ser examinada nos contextos de saída; consultado em 2026-10-01.
- [OWASP WSTG — Bypassing Authorization Schema](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/02-Testing_for_Bypassing_Authorization_Schema) — testes de autorização horizontal e vertical com contas e permissões distintas; consultado em 2026-10-01.
