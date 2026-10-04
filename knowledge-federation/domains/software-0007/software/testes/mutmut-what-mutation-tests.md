---
id: software.testes.tranche21.001520
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
fontes: ["https://github.com/boxed/mutmut", "https://kodare.net/2016/12/01/mutmut-a-python-mutation-testing-system.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# mutmut: medir testes por defeitos injetados

## Em uma frase
A mutação altera sistematicamente o código-fonte e verifica se a suíte falha; um mutante que sobrevive indica comportamento não realmente testado.

## Por que importa
Cobertura declara quais linhas foram alcançadas, não o que foi asserido; o mutante pergunta pelo poder de detecção do teste, que é o que importa na regressão.

## Como funciona
Use o mutmut para enumerar mutantes por função e trate cada sobrevivente como convite: criar o teste que o mataria.

## Exemplo
Trocar == por != num validador deveria quebrar algum teste — se nada quebra, o teste que existe não lê essa decisão.

## Limites e trade-offs
Corridas de mutação consomem tempo de CPU proporcional a mutantes vezes suíte; rodar toda a suíte por mutante sem filtro explode a esteira.

## Como verificar
Rode a mutação em um módulo pequeno e confirme que a lista de mutantes bate com o número de funções encontradas.

## Conexões
- [[mutmut-install-first-run]] — Veja também: mutmut: instalar e rodar sem setup.

## Fontes
- [mutmut — README oficial](https://github.com/boxed/mutmut) — instalação, browse, configuração e filtros; consultado em 2026-10-03.
- [mutmut — artigo introdutório](https://kodare.net/2016/12/01/mutmut-a-python-mutation-testing-system.html) — explicação do que é teste de mutação, linkada pelo projeto; consultado em 2026-10-03.
