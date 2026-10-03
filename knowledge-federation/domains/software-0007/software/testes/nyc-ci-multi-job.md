---
id: software.testes.tranche16.001010
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://github.com/istanbuljs/nyc", "https://github.com/istanbuljs/istanbuljs"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# nyc: consolidar cobertura entre trabalhos do pipeline

## Em uma frase
Cada trabalho do pipeline publica seu diretório de dados brutos como artefato, e uma etapa final baixa todos, mescla e publica o resultado consolidado.

## Por que importa
Distribuir a suíte reduz o tempo total, mas exige reunir os pedaços para que a verificação reflita a execução completa.

## Como funciona
Padronize o nome do artefato por trabalho, preserve o diretório bruto, mescle na etapa de consolidação e só então aplique os limites.

## Exemplo
Um trabalho de testes unitários e outro de integração podem publicar dados distintos, unidos por um trabalho final que gera o relatório publicado.

## Limites e trade-offs
Falhas parciais deixam o conjunto incompleto e o total consolidado passa a descrever menos do que o esperado sem que ninguém perceba.

## Como verificar
Compare a quantidade de arquivos recebidos com a esperada por trabalho e faça a etapa de consolidação falhar quando faltar algum.

## Conexões
- [[nyc-project-root-and-monorepo]] — Veja também: nyc: resolver raízes em repositório com múltiplos pacotes.
- [[nyc-excludes-and-generated-code]] — Veja também: nyc: excluir código gerado com critério.

## Fontes
- [nyc — repositório oficial](https://github.com/istanbuljs/nyc) — linha de comando, filtros, relatórios, limites e mesclagem de dados; consultado em 2026-10-03.
- [Istanbul — monorepo oficial](https://github.com/istanbuljs/istanbuljs) — instrumentação JavaScript, bibliotecas de cobertura e geradores de relatório; consultado em 2026-10-03.
