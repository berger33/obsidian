---
id: software.testes.tranche16.001011
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
fontes: ["https://github.com/istanbuljs/nyc", "https://www.npmjs.com/package/nyc"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# nyc: excluir código gerado com critério

## Em uma frase
Artefatos produzidos por geradores de contrato e de esquema entram na medição quando os padrões não os alcançam.

## Por que importa
Código gerado infla o denominador e esconde o comportamento do código mantido manualmente, além de mudar a cada regeneração.

## Como funciona
Exclua diretórios gerados de forma explícita, confirme o efeito no relatório e revise a regra quando a estrutura do projeto mudar.

## Exemplo
Um cliente de serviço produzido por ferramenta pode ser excluído enquanto os adaptadores escritos pelo time permanecem medidos.

## Limites e trade-offs
Exclusões amplas podem remover módulos de domínio junto do código gerado, então cada padrão precisa ser verificado por amostragem.

## Como verificar
Regenere o código, rode a medição e confirme que o total de arquivos permaneceu estável e que nenhum módulo manual desapareceu.

## Conexões
- [[nyc-ci-multi-job]] — Veja também: nyc: consolidar cobertura entre trabalhos do pipeline.
- [[nyc-interpreting-numbers]] — Veja também: nyc: interpretar as quatro métricas.

## Fontes
- [nyc — repositório oficial](https://github.com/istanbuljs/nyc) — linha de comando, filtros, relatórios, limites e mesclagem de dados; consultado em 2026-10-03.
- [nyc — pacote npm](https://www.npmjs.com/package/nyc) — opções documentadas e exemplos de uso do publicador; consultado em 2026-10-03.
