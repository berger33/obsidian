---
id: software.testes.tranche21.001493
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

# Sinon: aplicar stub a um método real

## Em uma frase
O Sinon permite stubar um método específico de um objeto existente, mantendo os demais métodos da instância funcionando como sempre.

## Por que importa
Substituir a interface inteira por um objeto falso fabricado no teste esconde renomeações e novos métodos; o stub pontual denuncia o contrato intacto.

## Como funciona
Chame sinon.stub(servico, "metodo") dentro do teste, defina o comportamento, e devolva o objeto à normalidade na limpeza.

## Exemplo
Um serviço de faturamento pode manter todos os métodos reais enquanto só o envio do e-mail vira um stub silencioso.

## Limites e trade-offs
Stubs pontuais em objetos compartilhados entre arquivos exigem restauração garantida, ou o segundo teste herdará o comportamento mutilado.

## Como verificar
Rode dois testes seguidos, o primeiro com stub, e confirme que o segundo vê a implementação original restaurada.

## Conexões
- [[sinon-stub-replace-behavior]] — Veja também: Sinon: stubs substituem o resultado.
- [[sinon-withargs-per-call]] — Veja também: Sinon: um stub, vários comportamentos.

## Fontes
- [Sinon.JS — repositório oficial](https://github.com/sinonjs/sinon) — código-fonte, guias de API e releases do projeto; consultado em 2026-10-03.
- [Sinon.JS — página oficial](https://sinonjs.org/) — instalação, escopo e início rápido; consultado em 2026-10-03.
- [Sinon.JS — releases publicadas](https://github.com/sinonjs/sinon/releases) — notas de versão e mudanças da API; consultado em 2026-10-03.
