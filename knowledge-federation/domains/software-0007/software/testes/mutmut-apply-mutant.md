---
id: software.testes.tranche21.001524
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md"
fontes: ["https://github.com/boxed/mutmut", "https://github.com/boxed/mutmut/blob/main/README.rst"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# mutmut: aplicar o mutante no disco

## Em uma frase
Um mutante pode ser gravado no arquivo-fonte via browse ou pelo comando mutmut apply <mutante>, materializando a mudança exatamente como a corrida a viu.

## Por que importa
Reproduzir a falha ausente na mão é o jeito mais rápido de entender por que o teste não pega o bug que a mutação provocou.

## Como funciona
Aplique o mutante, rode o teste que deveria matá-lo, observe a ausência de falha e escreva a asserção que falta antes de reverter.

## Exemplo
O apply transforma qualquer sobrevivente em caso de estudo com o arquivo sujo nas suas mãos.

## Limites e trade-offs
O próprio README grita em maiúsculas: tenha o arquivo sob controle de versão e commitado antes de aplicar, porque o apply não pede permissão para sobrescrever.

## Como verificar
Aplique um mutante em cópia de trabalho limpa e reverta com git checkout, confirmando o fluxo de segurança.

## Conexões
- [[mutmut-browse-tui]] — Veja também: mutmut: explorar mutantes no browse.
- [[mutmut-fork-requirement]] — Veja também: mutmut: requisito de fork e plataformas.

## Fontes
- [mutmut — README oficial](https://github.com/boxed/mutmut) — instalação, browse, configuração e filtros; consultado em 2026-10-03.
- [mutmut — repositório oficial](https://github.com/boxed/mutmut/blob/main/README.rst) — material-fonte do README e das releases; consultado em 2026-10-03.
