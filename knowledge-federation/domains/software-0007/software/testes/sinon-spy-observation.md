---
id: software.testes.tranche21.001491
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
fontes: ["https://sinonjs.org/", "https://github.com/sinonjs/sinon", "https://github.com/sinonjs/sinon/releases"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Sinon: observar chamadas com spies

## Em uma frase
sinon.spy(objeto, "metodo") envolve o método mantendo o comportamento original e registra tudo o que aconteceu com ele durante o teste.

## Por que importa
Muitas perguntas de teste são apenas "este colateral foi acionado com quais argumentos?", e o espião responde sem substituir a implementação real.

## Como funciona
Envolva o método, execute o fluxo de produção e afirme contagens e argumentos antes de restaurar o objeto com o próprio método restore.

## Exemplo
Após myAPI.doSomething(), t.ok(spy.calledOnce, "spy was called once") documenta exatamente o que o teste verificou.

## Limites e trade-offs
O espião só existe enquanto não for restaurado; esquecer restore vaza o embrulho para o próximo teste do mesmo objeto compartilhado.

## Como verificar
Consulte o espião antes e depois do restore e confirme que o objeto volta à implementação original intacta.

## Conexões
- [[sinon-purpose-scope]] — Veja também: Sinon: dublês para qualquer framework.
- [[sinon-stub-replace-behavior]] — Veja também: Sinon: stubs substituem o resultado.

## Fontes
- [Sinon.JS — página oficial](https://sinonjs.org/) — instalação, escopo e início rápido; consultado em 2026-10-03.
- [Sinon.JS — repositório oficial](https://github.com/sinonjs/sinon) — código-fonte, guias de API e releases do projeto; consultado em 2026-10-03.
- [Sinon.JS — releases publicadas](https://github.com/sinonjs/sinon/releases) — notas de versão e mudanças da API; consultado em 2026-10-03.
