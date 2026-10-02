---
id: software.testes.shrinking.000001
tipo: conceito
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://hypothesis.readthedocs.io/en/latest/reference/strategies.html", "https://hypothesis.readthedocs.io/en/latest/reference/api.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Shrinking, Failing example reduction, Contraexemplo mínimo]
lote: software-testes-2000-0001
---

# Shrinking de contraexemplos em testes gerativos

## Em uma frase
Shrinking tenta simplificar um exemplo que fez um teste falhar, para que a falha possa ser reproduzida e diagnosticada com menos ruído.

## Por que importa
Um gerador pode encontrar uma entrada grande e complexa que viola a propriedade. Uma forma mais simples frequentemente revela a condição de fronteira, elemento ou sequência que importa e pode ser convertida em um caso de regressão legível. A simplificação automatizada reduz esforço de diagnóstico, mas não explica sozinha a causa do defeito.

## Como funciona
Estratégias do Hypothesis definem não apenas que valores podem ser gerados, mas também como exemplos podem ser reduzidos. Por exemplo, listas podem tentar remover elementos e simplificar os valores restantes; inteiros podem ser reduzidos em direção a valores menores. Depois de encontrar falha, o framework tenta variantes mais simples que continuem reproduzindo o resultado, seguindo as regras de cada estratégia e as fases de execução configuradas.

## Exemplo
Uma propriedade falha para uma lista longa de entradas. O relatório pode reduzir essa lista a dois elementos que ainda produzem erro; esse contraexemplo menor pode ajudar a identificar que a função não preserva a ordem quando os valores são iguais. A causa ainda precisa ser confirmada pela análise do código e pela regra de negócio.

## Limites e trade-offs
O resultado não é necessariamente o menor contraexemplo global em uma métrica matemática, e estratégias personalizadas podem ter reduções pouco úteis. Efeitos não determinísticos ou estado externo podem impedir que uma falha seja repetida de forma consistente, prejudicando shrinking. Um exemplo simplificado é evidência reproduzível, não prova de que outros casos estejam corretos.

## Como verificar
Confirme que a falha original é reproduzível, observe o exemplo reduzido e verifique que ele ainda viola a mesma propriedade por uma razão relevante. Guarde os dados de reprodução e o seed/contexto informado pelo runner quando aplicável. Adicione teste explícito se ele comunicar claramente uma regressão importante; mantenha também a propriedade gerativa.

## Conexões
- [[property-based-testing-hypothesis]] — estratégias determinam como entradas são geradas e simplificadas.
- [[testes-stateful-model-based-hypothesis]] — sequências de regras com falha também podem ser reduzidas.
- [[testes-flaky-determinismo]] — não determinismo dificulta reproduzir e reduzir uma falha.

## Fontes
- [Hypothesis — Strategies Reference](https://hypothesis.readthedocs.io/en/latest/reference/strategies.html) — comportamento de shrinking por estratégia; acesso em 2026-10-01.
- [Hypothesis — API Reference](https://hypothesis.readthedocs.io/en/latest/reference/api.html) — fases de execução e tratamento de exemplos falsificadores; acesso em 2026-10-01.
