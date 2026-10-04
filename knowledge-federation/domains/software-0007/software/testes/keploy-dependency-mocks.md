---
id: software.testes.tranche20.001390
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://keploy.io/docs/", "https://keploy.io/api-testing"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Keploy: registrar dependências como mocks

## Em uma frase
Durante a gravação, as chamadas de saída da aplicação são capturadas e gravadas como mocks, incluindo banco, cache, filas e serviços externos.

## Por que importa
Conter as respostas das dependências torna a repetição determinística e dispensa provisionar banco e serviços externos na esteira.

## Como funciona
Exercite o fluxo completo durante a gravação, revise os mocks gerados e versione-os junto dos casos.

## Exemplo
A consulta ao banco pode ser substituída pela resposta gravada, permitindo repetir o fluxo sem instância real.

## Limites e trade-offs
Mocks gravados a partir de dados desatualizados mascaram mudanças de esquema, e o excesso de dependências virtuais afasta o teste do comportamento real de integração.

## Como verificar
Altere o esquema do banco em ambiente de teste e confirme que a repetição com mocks não detecta a mudança, evidenciando o limite.

## Conexões
- [[keploy-record-replay]] — Veja também: Keploy: gerar testes a partir de tráfego real.
- [[keploy-replay-in-ci]] — Veja também: Keploy: repetir na esteira de integração.

## Fontes
- [Keploy — Documentação](https://keploy.io/docs/) — instalação, gravação de tráfego, repetição e integração; consultado em 2026-10-03.
- [Keploy — Testes de API](https://keploy.io/api-testing) — geração de casos a partir de tráfego e cobertura de interface; consultado em 2026-10-03.
