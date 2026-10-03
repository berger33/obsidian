---
id: software.testes.tranche21.001495
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

# Sinon: mocks com expectativas verificadas

## Em uma frase
O mock do Sinon declara expectativas de chamada sobre o objeto e cobra o cumprimento no fim do teste, em vez de só observar passivamente.

## Por que importa
Quando o contrato é "o arquivo de log deve ser escrito exatamente uma vez com este conteúdo", a verificação explícita pega violações que a asserção solta deixaria passar.

## Como funciona
Chame obj.expects("metodo").once(), execute o fluxo e termine com verify para confirmar que cada expectativa foi satisfeita.

## Exemplo
A expectativa de fechar a conexão em finally vira regra executável e o teste falha se o código abandonar o recurso.

## Limites e trade-offs
Mocks rígidos transformam refatorações inofensivas em bateria de testes vermelhos; o próprio guia de dublês recomenda-os para contratos estreitos.

## Como verificar
Omita a chamada esperada e confirme que verify produz uma falha indicando a expectativa não atendida.

## Conexões
- [[sinon-withargs-per-call]] — Veja também: Sinon: um stub, vários comportamentos.
- [[sinon-clock-fake-timers]] — Veja também: Sinon: relógio falso para aguardar sem espera.

## Fontes
- [Sinon.JS — repositório oficial](https://github.com/sinonjs/sinon) — código-fonte, guias de API e releases do projeto; consultado em 2026-10-03.
- [Sinon.JS — página oficial](https://sinonjs.org/) — instalação, escopo e início rápido; consultado em 2026-10-03.
- [Sinon.JS — releases publicadas](https://github.com/sinonjs/sinon/releases) — notas de versão e mudanças da API; consultado em 2026-10-03.
