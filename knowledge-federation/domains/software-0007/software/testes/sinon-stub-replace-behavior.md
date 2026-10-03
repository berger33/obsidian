---
id: software.testes.tranche21.001492
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
fontes: ["https://github.com/sinonjs/sinon", "https://sinonjs.org/", "https://github.com/sinonjs/sinon/releases"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Sinon: stubs substituem o resultado

## Em uma frase
Um stub troca o comportamento de uma função por um resultado escolhido: valores fixos, exceções lançadas ou callbacks disparados sob demanda.

## Por que importa
Forçar o ramo raro de um erro de rede não deveria depender de derrubar a rede no meio da esteira; o stub fabrica o cenário inteiro.

## Como funciona
Crie sinon.stub() para a função, encadeie .returns ou .throws para o efeito desejado e injete o dublê no módulo sob teste.

## Exemplo
A busca de preços pode lançar uma exceção de timeout para provar que a página renderiza o aviso correspondente.

## Limites e trade-offs
Stub bem demais apaga o contrato real do módulo substituído: quando a API muda, o teste continua verde porque ninguém exercita mais o original.

## Como verificar
Substitua a função por um stub que lança e confirme que o caminho de erro pretendido do código é coberto pela asserção.

## Conexões
- [[sinon-spy-observation]] — Veja também: Sinon: observar chamadas com spies.
- [[sinon-stub-on-existing-method]] — Veja também: Sinon: aplicar stub a um método real.

## Fontes
- [Sinon.JS — repositório oficial](https://github.com/sinonjs/sinon) — código-fonte, guias de API e releases do projeto; consultado em 2026-10-03.
- [Sinon.JS — página oficial](https://sinonjs.org/) — instalação, escopo e início rápido; consultado em 2026-10-03.
- [Sinon.JS — releases publicadas](https://github.com/sinonjs/sinon/releases) — notas de versão e mudanças da API; consultado em 2026-10-03.
