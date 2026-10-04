---
id: software.testes.tranche12.000633
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://github.com/postmanlabs/newman/blob/develop/README.md", "https://learning.postman.com/docs/tests-and-scripts/running-collections/test-data/working-with-data-files/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Newman: controlar iterações com arquivo de dados

## Em uma frase
`--iteration-data` fornece arquivo JSON ou CSV às iterações de uma collection, e `--iteration-count` define a quantidade de execuções quando usado com esses dados.

## Por que importa
Dados externos permitem exercitar a mesma sequência contra entradas variadas sem duplicar requests e assertions dentro da coleção.

## Como funciona
Mantenha cabeçalhos estáveis no CSV ou estrutura consistente no JSON, declare o contador quando precisar limitar a execução e valide o conteúdo antes do job consumir o arquivo.

## Exemplo
Um CSV pode alimentar casos de CEP e expectativa de status, enquanto scripts da collection usam cada linha para montar uma request específica.

## Limites e trade-offs
A quantidade de dados e de iterações afeta a duração e pode repetir efeitos remotos; coleções não idempotentes precisam preparar ou limpar cada entrada.

## Como verificar
Rode uma amostra curta, confira que as variáveis de linha chegaram à request e confirme a quantidade de iterações reportada.

## Conexões
- [[newman-environment-global-precedence]] — Veja também: Newman: separar environment e globals.
- [[newman-folder-selection]] — Veja também: Newman: restringir execução a pastas da collection.

## Fontes
- [Newman — README e opções](https://github.com/postmanlabs/newman/blob/develop/README.md) — estado de manutenção, CLI, opções, reporters e uso como biblioteca; consultado em 2026-10-02.
- [Postman — Data files in collection runs](https://learning.postman.com/docs/tests-and-scripts/running-collections/test-data/working-with-data-files/) — formatação de arquivos CSV/JSON e escopos de dados em collection runs; consultado em 2026-10-02.
