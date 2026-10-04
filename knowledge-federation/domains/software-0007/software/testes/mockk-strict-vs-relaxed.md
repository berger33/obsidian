---
id: software.testes.tranche20.001420
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://github.com/mockk/mockk/blob/master/README.md", "https://github.com/mockk/mockk"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MockK: escolher entre modo estrito e relaxado

## Em uma frase
No modo estrito, chamadas sem resposta definida falham; no modo relaxado, o dublê devolve valores vazios ou neutros automaticamente.

## Por que importa
O modo estrito expõe dependências implícitas, enquanto o relaxado reduz configuração quando o caso só se importa com parte do comportamento.

## Como funciona
Comece estrito no caso principal, relaxe dublês auxiliares cujas respostas não influenciam a verificação e documente a escolha.

## Exemplo
Um dublê de registrador de eventos pode ser relaxado, enquanto o repositório que devolve o dado verificado permanece estrito.

## Limites e trade-offs
Relaxar tudo esconde chamadas inesperadas, e manter tudo estrito torna casos simples pesados de configurar.

## Como verificar
Execute o caso com o dublê relaxado e confirme que ele deixa de falhar por chamadas não configuradas, como pretendido.

## Conexões
- [[mockk-basics]] — Veja também: MockK: criar dublês e definir respostas.
- [[mockk-verification]] — Veja também: MockK: verificar chamadas realizadas.

## Fontes
- [MockK — README oficial](https://github.com/mockk/mockk/blob/master/README.md) — dublês, relaxamento, verificação, objetos e corrotinas; consultado em 2026-10-03.
- [MockK — repositório oficial](https://github.com/mockk/mockk) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
