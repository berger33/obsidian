---
id: software.testes.tranche16.001003
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

# nyc: incluir arquivos não carregados

## Em uma frase
A opção de instrumentar tudo faz a medição abranger arquivos que a suíte não carregou, e os filtros de inclusão e exclusão delimitam esse conjunto.

## Por que importa
Sem essa opção, um módulo nunca importado desaparece do relatório e a ausência de testes passa a não contar contra o projeto.

## Como funciona
Ative a instrumentação completa, restrinja a um diretório de código-fonte e exclua explicitamente testes, artefatos de build e declarações de tipo.

## Exemplo
Um conjunto de utilitários sem nenhum caso de teste aparece com zero por cento quando a instrumentação completa está ativa, evidenciando a lacuna.

## Limites e trade-offs
Padrões de exclusão fornecidos por padrão deixam de valer quando a configuração define lista própria, então a substituição precisa ser consciente.

## Como verificar
Remova a opção e compare o total de arquivos do relatório com o obtido com ela, verificando quantos módulos estavam invisíveis.

## Conexões
- [[nyc-wrap-command]] — Veja também: nyc: instrumentar um comando existente.
- [[nyc-negated-excludes]] — Veja também: nyc: reabrir caminhos com padrões negados.

## Fontes
- [nyc — repositório oficial](https://github.com/istanbuljs/nyc) — linha de comando, filtros, relatórios, limites e mesclagem de dados; consultado em 2026-10-03.
- [nyc — pacote npm](https://www.npmjs.com/package/nyc) — opções documentadas e exemplos de uso do publicador; consultado em 2026-10-03.
