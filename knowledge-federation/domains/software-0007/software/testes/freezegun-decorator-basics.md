---
id: software.testes.tranche21.001511
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
fontes: ["https://pypi.org/project/freezegun/", "https://github.com/spulec/freezegun"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# freezegun: decorar o teste com o instante

## Em uma frase
freeze_time aceita uma string de data e funciona como decorator simples sobre a função de teste, valendo por toda a duração do caso.

## Por que importa
Uma linha no topo do teste documenta a premissa temporal do cenário melhor que qualquer comentário, e a data vira dado do teste.

## Como funciona
Decore o caso com o instante exato em que o comportamento deve ser observado e afirme as saídas sensíveis à hora.

## Exemplo
@freeze_time("2024-02-29 23:59:59") coloca o teste no último segundo de um ano bissexto.

## Limites e trade-offs
A data precisa vir como string ou datetime válido; um typo ali dentro vira falha confusa de parsing em tempo de coleta.

## Como verificar
Provoque um formato inválido e confirme que o erro aparece imediatamente na importação do decorator.

## Conexões
- [[freezegun-what-it-mocks]] — Veja também: freezegun: o que a biblioteca congela.
- [[freezegun-class-decorator]] — Veja também: freezegun: congelar uma classe de testes inteira.

## Fontes
- [freezegun — página no PyPI](https://pypi.org/project/freezegun/) — README oficial com uso, fusos, tick e limites; consultado em 2026-10-03.
- [freezegun — repositório oficial](https://github.com/spulec/freezegun) — código-fonte, testes e releases do projeto; consultado em 2026-10-03.
