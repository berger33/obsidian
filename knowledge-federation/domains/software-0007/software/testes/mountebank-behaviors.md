---
id: software.testes.tranche19.001282
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://www.mbtest.org/docs/api/behaviors", "https://www.mbtest.org/docs/api/stubs"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mountebank: ajustar respostas com comportamentos

## Em uma frase
Comportamentos modificam a resposta, adicionando atraso, substituindo conteúdo por dados da requisição e repetindo respostas sem avançar a sequência.

## Por que importa
Atraso e repetição permitem verificar limites de tempo e sequências de chamada que o cliente executa em ordem definida.

## Como funciona
Use atraso para simular latência, cópia de campos para respostas dependentes da entrada e repetição quando a mesma resposta deve ser estável.

## Exemplo
Um comportamento pode fazer a resposta ecoar o identificador enviado na requisição, permitindo verificar o fluxo de correlação.

## Limites e trade-offs
Atrasos longos tornam a suíte lenta, e comportamentos combinados sem critério produzem respostas difíceis de prever.

## Como verificar
Aplique atraso acima do limite do cliente e confirme que o teste de tempo esgotado é exercitado.

## Conexões
- [[mountebank-proxies]] — Veja também: Mountebank: gravar e reproduzir com proxies.
- [[mountebank-injection]] — Veja também: Mountebank: calcular respostas com injeção.

## Fontes
- [Mountebank — Behaviors](https://www.mbtest.org/docs/api/behaviors) — atraso, cópia de valores e repetição de respostas; consultado em 2026-10-03.
- [Mountebank — Stubs](https://www.mbtest.org/docs/api/stubs) — stubs, respostas, sequências e stub padrão; consultado em 2026-10-03.
