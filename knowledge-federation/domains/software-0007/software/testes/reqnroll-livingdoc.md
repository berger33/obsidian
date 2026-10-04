---
id: software.testes.tranche22.001586
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://docs.reqnroll.net/latest/guides/migrating-from-specflow.html", "https://github.com/orgs/reqnroll/discussions/196"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Reqnroll: Living Documentation ficou de fora

## Em uma frase
O SpecFlow+ LivingDoc era parte fechada do SpecFlow e não pôde ser absorvido pelo Reqnroll; o projeto está reconstruindo uma ferramenta parecida e enquanto isso publica um workaround com o CLI generator do Living Doc do SpecFlow.

## Por que importa
Relatórios de documentação viva são o artefato de BDD para stakeholders; saber que essa peça exige contorno muda o planejamento de quem adota o Reqnroll em régua de negócio.

## Como funciona
Use o workaround recomendado: gerar a documentação com o tooling legado apontando para a saída do seu projeto Reqnroll, acompanhando a discussão oficial do plano de reconstrução.

## Exemplo
A própria guia de migração trata o assunto como atenção dedicada, com link para o tópico de discussão no GitHub da organização.

## Limites e trade-offs
Workaround com ferramenta legada fecha o gap hoje, mas não ganha correções do projeto novo; trate o relatório como artefato opcional até a versão nativa sair.

## Como verificar
Inscreva-se na issue de discussão listada na guia e verifique se o gerador alternativo produz HTML a partir do seu output de teste.

## Conexões
- [[reqnroll-plugins-actions]] — Veja também: Reqnroll: plugins portados e Actions de automação.
- [[reqnroll-mstest-outline]] — Veja também: Reqnroll: Scenario Outlines sob MsTest geram testes data-driven.

## Fontes
- [Reqnroll — Migrating from SpecFlow](https://docs.reqnroll.net/latest/guides/migrating-from-specflow.html) — renomeações, compat package, atenções MsTest e LivingDoc; consultado em 2026-10-03.
- [Reqnroll — discussão Living Documentation](https://github.com/orgs/reqnroll/discussions/196) — tópico oficial sobre o plano do LivingDoc; consultado em 2026-10-03.
