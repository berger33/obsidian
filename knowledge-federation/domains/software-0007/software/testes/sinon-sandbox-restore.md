---
id: software.testes.tranche21.001498
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

# Sinon: sandbox para devolver os originais

## Em uma frase
O sandbox agrupa espiões, stubs e relógios criados a partir dele e devolve todos os objetos ao estado original num único restore.

## Por que importa
Limpeza feita à mão em cada teste é a primeira coisa que quebra quando alguém copia um caso; o agregador de dublês torna o esquecimento difícil.

## Como funciona
Crie um sinon.createSandbox(), construa todos os dublês pelo sandbox e chame sandbox.restore na finalização do framework.

## Exemplo
beforeEach cria o sandbox do caso e afterEach restaura tudo sem que nenhum teste declare o que usou.

## Limites e trade-offs
Dublês criados fora do sandbox escapam da restauração em bloco; misturar as duas origens anula o benefício central.

## Como verificar
Vaze um stub propositalmente além do restore e confirme que o sandbox limpou todos os dublês registrados nele.

## Conexões
- [[sinon-fake-server-xhr]] — Veja também: Sinon: servidor falso para requisições XHR.
- [[sinon-assert-framework-agnostic]] — Veja também: Sinon: asserções próprias, sem refém do framework.

## Fontes
- [Sinon.JS — repositório oficial](https://github.com/sinonjs/sinon) — código-fonte, guias de API e releases do projeto; consultado em 2026-10-03.
- [Sinon.JS — página oficial](https://sinonjs.org/) — instalação, escopo e início rápido; consultado em 2026-10-03.
- [Sinon.JS — releases publicadas](https://github.com/sinonjs/sinon/releases) — notas de versão e mudanças da API; consultado em 2026-10-03.
