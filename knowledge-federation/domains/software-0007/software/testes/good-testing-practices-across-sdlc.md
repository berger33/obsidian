---
id: software.testes.sdlc-good-practices.000001
tipo: pratica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: estavel
status: candidata
revisao_humana: nao_solicitada
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-06.md"
revisor: ""
fontes: ["https://astqb.org/2-1-testing-in-the-context-of-a-software-development-lifecycle-sdlc/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Good testing practices across SDLCs", "Práticas de teste úteis em diferentes SDLCs"]
lote: software-testes-2000-0001
---

# Práticas de teste úteis em diferentes SDLCs

## Em uma frase
Algumas práticas continuam valiosas em vários SDLCs: associar controle de qualidade às atividades de desenvolvimento e definir objetivos distintos por nível.

## Por que importa
Uma abordagem iterativa ou sequencial pode mudar a cadência, mas não torna requisitos, desenho, integração ou documentação imunes a defeitos. Práticas transversais reduzem lacunas sem prescrever um processo uniforme.

## Como funciona
O CTFL recomenda correspondência entre atividades de desenvolvimento e teste, objetivos específicos para níveis diferentes, início de análise e desenho durante a fase de desenvolvimento correspondente e envolvimento de testers na revisão de rascunhos assim que estejam disponíveis. Isso permite detectar problemas cedo e evita redundância quando as evidências dos níveis são complementares.

## Exemplo
Enquanto uma regra de negócio é refinada, testers ajudam a identificar condições verificáveis. Durante a implementação, testes de componente acompanham o código; depois, testes integrados examinam contratos que não poderiam ser confirmados isoladamente.

## Limites e trade-offs
“Uma atividade de teste para cada atividade de desenvolvimento” não exige uma reunião ou artefato separado para cada tarefa. A forma de demonstrar controle varia com risco, contexto e SDLC.

## Como verificar
Associe cada etapa e work product a uma atividade de qualidade; confira se o nível cobre um objetivo próprio e se revisões ocorrem enquanto alterações ainda são viáveis.

## Conexões
- [[fundamental-test-activities]] — organiza análise, desenho, implementação e outras atividades.
- [[static-testing-work-products]] — descreve a revisão de rascunhos sem execução.

## Fontes
- [ASTQB — CTFL §2.1, SDLC and Good Testing Practices](https://astqb.org/2-1-testing-in-the-context-of-a-software-development-lifecycle-sdlc/) — práticas que independem do modelo de ciclo; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — §2.1.2; acesso em 2026-10-01.
