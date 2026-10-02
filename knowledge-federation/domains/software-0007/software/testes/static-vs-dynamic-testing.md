---
id: software.testes.static-dynamic.000001
tipo: conceito
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: estavel
status: candidata
revisao_humana: nao_solicitada
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-05.md"
revisor: ""
fontes: ["https://astqb.org/3-1-static-testing-basics/", "https://istqb.org/wp-content/uploads/sdm-uploads/ISTQB_CTFL_v4.0_Sample-Exam-C-Answers_v1.6.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Static versus dynamic testing, Static testing, Dynamic testing]
lote: software-testes-2000-0001
---

# Teste estático e dinâmico são complementares

## Em uma frase
Teste estático examina work products sem execução; teste dinâmico executa software e observa resultados, revelando falhas que ajudam a localizar defeitos.

## Por que importa
Cada abordagem encontra classes diferentes de problema. Uma especificação contraditória pode ser detectada antes de existir código; tempo de resposta excessivo requer executar o sistema em condições apropriadas. Usar apenas uma abordagem deixa evidências importantes sem coleta.

## Como funciona
O CTFL descreve que teste estático encontra defeitos diretamente em work products, enquanto teste dinâmico pode provocar falhas a partir das quais defeitos são investigados. Estático pode examinar documentação, modelos e código não executado; dinâmico exige objeto executável. Ambos podem avaliar qualidade e detectar defeitos, mas medem propriedades diferentes: manutenibilidade pode ser avaliada estaticamente, enquanto eficiência de desempenho depende de execução/medição.

## Exemplo
Uma análise estática aponta que um ramo do programa nunca pode ser alcançado. Um teste de carga, por outro lado, mede a latência sob um workload definido. O primeiro não demonstra a latência do sistema; o segundo não necessariamente encontra a contradição numa especificação de interface.

## Limites e trade-offs
“Estático” não significa necessariamente manual e “dinâmico” não significa necessariamente automatizado. Um analisador pode gerar falsos positivos e testes dinâmicos dependem de ambiente, dados e oracle. Usar resultados de uma abordagem como substituto da outra cria uma lacuna de cobertura.

## Como verificar
Classifique cada pergunta de qualidade: o work product pode ser inspecionado sem execução ou precisa observar comportamento? Combine revisão/análise com execução conforme risco; registre o que cada método detectou e quais limitações permanecem.

## Conexões
- [[static-testing-work-products]] — lista alvos e atividades estáticas.
- [[test-oracles-resultados-esperados]] — execução dinâmica exige critério para interpretar saída.
- [[cobertura-branches-statement-interpretacao]] — métrica de execução é evidência dinâmica limitada.

## Fontes
- [ASTQB — ISTQB CTFL §3.1: Static Testing Basics](https://astqb.org/3-1-static-testing-basics/) — distinções e complementaridade entre testes estático e dinâmico; acesso em 2026-10-01.
- [ISTQB — CTFL v4.0 Sample Exam C Answers, version 1.6](https://istqb.org/wp-content/uploads/sdm-uploads/ISTQB_CTFL_v4.0_Sample-Exam-C-Answers_v1.6.pdf) — exemplos de defeitos detectáveis estaticamente ou apenas em execução; acesso em 2026-10-01.
