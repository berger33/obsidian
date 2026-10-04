---
id: software.testes.tranche20.001426
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
fontes: ["https://github.com/mockk/mockk/blob/master/README.md", "https://notwoods.github.io/mockk-guidebook/docs/mocking/coroutines/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MockK: ajustar respostas padrão

## Em uma frase
Além do relaxamento comum, a biblioteca oferece relaxamento de funções sem retorno e possibilidade de configurar respostas padrão por tipo.

## Por que importa
Ajustar o padrão reduz configuração por caso mantendo a verificação explícita das chamadas que importam.

## Como funciona
Ative o relaxamento de funções sem retorno quando o código sob teste dispara efeitos sem valor devolvido e mantenha o restante estrito.

## Exemplo
Um serviço que registra auditoria sem retorno pode ser dublado sem configuração por chamada.

## Limites e trade-offs
Assumir que a resposta padrão é neutra esconde efeitos colaterais não verificados, e padrões amplos escondem erros de digitação em nomes de chamada.

## Como verificar
Chame uma função não configurada e observe a resposta padrão, avaliando se ela corresponde ao que o caso espera verificar.

## Conexões
- [[mockk-configuration]] — Veja também: MockK: configurar o comportamento padrão do projeto.
- [[mockk-chained-and-hierarchies]] — Veja também: MockK: encadear dublês e hierarquias.

## Fontes
- [MockK — README oficial](https://github.com/mockk/mockk/blob/master/README.md) — dublês, relaxamento, verificação, objetos e corrotinas; consultado em 2026-10-03.
- [MockK — Guia de corrotinas](https://notwoods.github.io/mockk-guidebook/docs/mocking/coroutines/) — uso das variantes para funções suspensas; consultado em 2026-10-03.
