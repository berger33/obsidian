---
id: software.testes.tranche16.001008
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

# nyc: ajustar a medição para código transpilado

## Em uma frase
Quando o teste executa código traduzido, os relatórios precisam mapear posições de volta ao original para apontar linhas úteis.

## Por que importa
Sem esse mapeamento, o relatório aponta para o artefato gerado e a investigação perde a referência do código-fonte.

## Como funciona
Inclua as extensões usadas no projeto, ative o suporte a mapas de origem e confirme a correspondência entre o que roda e o que é exibido.

## Exemplo
Um projeto em linguagem com tipos precisa que os arquivos compilados sejam associados aos fontes correspondentes antes de qualquer conclusão sobre cobertura.

## Limites e trade-offs
O mapeamento depende de configuração de compilação e pode deslocar linhas quando o código é minificado; a verificação direta evita conclusão errada.

## Como verificar
Provove uma falha de asserção e confirme que o relatório aponta a linha correta do arquivo-fonte.

## Conexões
- [[nyc-temp-dir-and-merge]] — Veja também: nyc: consolidar dados de várias execuções.
- [[nyc-project-root-and-monorepo]] — Veja também: nyc: resolver raízes em repositório com múltiplos pacotes.

## Fontes
- [nyc — repositório oficial](https://github.com/istanbuljs/nyc) — linha de comando, filtros, relatórios, limites e mesclagem de dados; consultado em 2026-10-03.
- [nyc — pacote npm](https://www.npmjs.com/package/nyc) — opções documentadas e exemplos de uso do publicador; consultado em 2026-10-03.
