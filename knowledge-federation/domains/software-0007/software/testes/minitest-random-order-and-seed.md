---
id: software.testes.tranche15.000887
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://docs.seattlerb.org/minitest/Minitest/Test.html", "https://docs.seattlerb.org/minitest/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Minitest: reproduzir a ordem aleatória

## Em uma frase
O Minitest executa os testes em ordem aleatória por padrão e informa a semente usada, permitindo repetir a mesma sequência em caso de falha.

## Por que importa
Ordem aleatória expõe dependências escondidas, mas a falha só é investigável quando a semente registrada pelo relatório é reaproveitada corretamente.

## Como funciona
Reproduza a falha informando a semente observada e reordene o caso para depender apenas do próprio `setup`, não do teste executado antes.

## Exemplo
`ruby test/calculadora_test.rb --seed 12345` repete a sequência que falhou, e métodos que exigem ordem fixa podem declará-la explicitamente como exceção.

## Limites e trade-offs
Fixar ordem de forma geral esconde acoplamentos em vez de resolvê-los; a declaração de dependência de ordem deve ser tratada como dívida técnica visível.

## Como verificar
Rode a suíte várias vezes com sementes distintas e verifique se algum caso muda de resultado; se mudar, investigue o estado compartilhado.

## Conexões
- [[minitest-parallelize-me]] — Veja também: Minitest: paralelizar testes com segurança.
- [[minitest-skip-and-flunk]] — Veja também: Minitest: usar skip e flunk com intenção.

## Fontes
- [Minitest — Test](https://docs.seattlerb.org/minitest/Minitest/Test.html) — classes de teste, ciclos de vida, ordem aleatória e paralelização; consultado em 2026-10-02.
- [Minitest — README](https://docs.seattlerb.org/minitest/) — visão geral do projeto, plugins e formas de execução; consultado em 2026-10-02.
