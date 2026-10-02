---
id: software.testes.system-testing.000001
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-05.md"
revisor: ""
fontes: ["https://astqb.org/2-2-test-levels-and-test-types/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [System testing, Teste de sistema]
lote: software-testes-2000-0001
---

# Teste de sistema contra requisitos do produto integrado

## Em uma frase
System testing avalia o comportamento e as capacidades do sistema integrado como um todo contra sua especificação e características de qualidade relevantes.

## Por que importa
Testes de componente e integração não demonstram que o produto completo satisfaz requisitos de ponta a ponta. Testes de sistema verificam fluxos, regras e atributos que emergem do conjunto, fornecendo evidência para stakeholders e decisões de release.

## Como funciona
O CTFL lista system testing como nível cujo objeto é o sistema inteiro e cuja base costuma incluir especificações de sistema e requisitos não funcionais. Pode abranger testes funcionais e não funcionais. Uma equipe independente pode executar testes, mas independência e responsabilidades dependem do contexto. O ambiente deve ser apropriado ao objetivo; teste de performance, por exemplo, requer condições que permitam interpretar medições.

## Exemplo
Para um serviço de reservas, system testing pode executar jornada de busca, reserva, pagamento e cancelamento contra requisitos do sistema, observando que o estado final e as comunicações ao usuário sejam consistentes. Medir disponibilidade em um ambiente minúsculo não representa automaticamente produção.

## Limites e trade-offs
Falhas no nível de sistema podem ser difíceis de localizar em um componente específico. O teste não substitui verificações de integração de interfaces externas nem aceitação por usuários. “Sistema completo” deve ser delimitado: serviços fora do escopo podem permanecer simulados.

## Como verificar
Declare sistema e dependências sob teste, requisitos, tipos de teste e ambiente. Registre caminhos cobertos, resultados esperados, defeitos e limitações. Relacione as falhas às fronteiras e complemente com níveis mais baixos para melhorar diagnóstico.

## Conexões
- [[test-levels-overview]] — organiza objetivos dos níveis.
- [[performance-testing-modelagem-carga]] — detalha testes não funcionais de desempenho.
- [[test-oracles-resultados-esperados]] — sistema integrado precisa de oracles para avaliar resultados.

## Fontes
- [ASTQB — ISTQB CTFL §2.2: Test Levels and Test Types](https://astqb.org/2-2-test-levels-and-test-types/) — atributos de distinção entre níveis; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — seção 2.2.1, system testing como teste do sistema completo; acesso em 2026-10-01.
