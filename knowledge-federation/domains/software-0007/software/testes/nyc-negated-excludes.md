---
id: software.testes.tranche16.001004
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

# nyc: reabrir caminhos com padrões negados

## Em uma frase
Na lista de exclusão, um padrão iniciado por exclamação restaura caminhos que seriam removidos pela regra anterior ou padrão.

## Por que importa
Projetos com convenções específicas precisam manter código de produção dentro da medição mesmo quando o padrão geral apontaria para fora.

## Como funciona
Ordene os padrões de modo que a negação venha depois da exclusão correspondente e documente cada exceção com o motivo.

## Exemplo
Excluir todo o diretório de testes e depois reabrir um arquivo de utilitário compartilhado permite medir esse arquivo sem incluir os casos.

## Limites e trade-offs
Negação mal posicionada não tem efeito, e padrões conflitantes produzem resultado que ninguém consegue explicar meses depois.

## Como verificar
Liste os arquivos efetivamente instrumentados e confirme a presença do caminho reaberto e a ausência dos demais.

## Conexões
- [[nyc-all-and-filters]] — Veja também: nyc: incluir arquivos não carregados.
- [[nyc-reporters]] — Veja também: nyc: escolher relatórios e destino.

## Fontes
- [nyc — repositório oficial](https://github.com/istanbuljs/nyc) — linha de comando, filtros, relatórios, limites e mesclagem de dados; consultado em 2026-10-03.
- [nyc — pacote npm](https://www.npmjs.com/package/nyc) — opções documentadas e exemplos de uso do publicador; consultado em 2026-10-03.
