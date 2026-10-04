---
id: software.testes.tranche21.001523
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

# mutmut: explorar mutantes no browse

## Em uma frase
O mutmut browse abre uma interface de terminal com os mutantes encontrados, onde é possível inspecionar cada um e retestar funções ou módulos inteiros pelas teclas f e m.

## Por que importa
A triagem é o trabalho real do teste de mutação: a TUI mantém a lista de sobreviventes, o diff e a ação no mesmo lugar.

## Como funciona
Abra o browse após a corrida, navegue até um sobrevivente, leia a mutação aplicada e dispare o reteste do módulo após escrever o teste.

## Exemplo
A tecla m retestando o módulo inteiro fecha o loop de correção em poucos segundos por sobrevivente.

## Limites e trade-offs
TUI de terminal não é artefato de esteira: para registro, o resultado precisa ser extraído em relatório separado, não em print da tela.

## Como verificar
Deixe um mutante sobreviver de propósito, abra o browse e confirme que ele aparece como não morto na lista.

## Conexões
- [[mutmut-resume-and-retest]] — Veja também: mutmut: interromper, retomar e retestar.
- [[mutmut-apply-mutant]] — Veja também: mutmut: aplicar o mutante no disco.

## Fontes
- [mutmut — README oficial](https://github.com/boxed/mutmut) — instalação, browse, configuração e filtros; consultado em 2026-10-03.
- [mutmut — repositório oficial](https://github.com/boxed/mutmut/blob/main/README.rst) — material-fonte do README e das releases; consultado em 2026-10-03.
