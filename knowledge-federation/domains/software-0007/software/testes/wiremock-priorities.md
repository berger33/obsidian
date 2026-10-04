---
id: software.testes.tranche17.001120
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://wiremock.org/docs/stubbing/", "https://wiremock.org/docs/request-matching/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WireMock: resolver sobreposição com prioridades

## Em uma frase
Quando mais de um stub corresponde à mesma requisição, a prioridade decide qual deles responde, com padrão definido para os casos não declarados.

## Por que importa
Regras genéricas e específicas convivem no mesmo servidor, e sem prioridade explícita o resultado depende da ordem de carregamento.

## Como funciona
Atribua prioridade menor aos stubs específicos, mantenha as regras genéricas como fallback e documente a intenção de cada nível.

## Exemplo
Uma resposta de erro para identificador inexistente pode ter prioridade sobre a regra genérica que responde a qualquer identificador.

## Limites e trade-offs
Prioridades iguais deixam o comportamento indefinido, e regras específicas esquecidas deixam de ser exercitadas sem aviso.

## Como verificar
Declare dois stubs para a mesma rota com prioridades diferentes e confirme qual responde em cada caso.

## Conexões
- [[wiremock-stateful-scenarios]] — Veja também: WireMock: simular fluxos com estado.
- [[wiremock-fault-simulation]] — Veja também: WireMock: injetar falhas e atrasos.

## Fontes
- [WireMock — Stubbing](https://wiremock.org/docs/stubbing/) — mapeamentos de stub, respostas predefinidas e prioridades; consultado em 2026-10-03.
- [WireMock — Request matching](https://wiremock.org/docs/request-matching/) — critérios sobre rota, método, cabeçalhos e corpo; consultado em 2026-10-03.
