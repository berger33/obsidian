---
id: software.testes.tranche21.001497
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

# Sinon: servidor falso para requisições XHR

## Em uma frase
O fake server do Sinon intercepta requisições XMLHttp no navegador de teste, respondendo a roteamentos definidos pelo próprio teste.

## Por que importa
Testes de unidade de bibliotecas front-end não devem depender de rede real; responder no lugar do servidor mantém o ciclo rápido e offline.

## Como funciona
Ative o fake server, registre a resposta esperada para o pedido, dispare o código que busca e afirme contra a resposta simulada.

## Exemplo
A listagem de produtos recebe um JSON inventado e o componente renderiza as linhas sem nenhum backend em pé.

## Limites e trade-offs
Cobertura parcial de XHR deixa fetch moderno fora do cerco; o fake server clássico mira XMLHttpRequest e exige atenção ao stack atual.

## Como verificar
Interrompa a rede da máquina de teste e confirme que o caso com servidor falso continua passando sozinho.

## Conexões
- [[sinon-clock-fake-timers]] — Veja também: Sinon: relógio falso para aguardar sem espera.
- [[sinon-sandbox-restore]] — Veja também: Sinon: sandbox para devolver os originais.

## Fontes
- [Sinon.JS — repositório oficial](https://github.com/sinonjs/sinon) — código-fonte, guias de API e releases do projeto; consultado em 2026-10-03.
- [Sinon.JS — página oficial](https://sinonjs.org/) — instalação, escopo e início rápido; consultado em 2026-10-03.
- [Sinon.JS — releases publicadas](https://github.com/sinonjs/sinon/releases) — notas de versão e mudanças da API; consultado em 2026-10-03.
