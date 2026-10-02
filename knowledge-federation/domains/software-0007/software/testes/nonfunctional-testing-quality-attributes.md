---
id: software.testes.nonfunctional.000001
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-06.md"
revisor: ""
fontes: ["https://astqb.org/2-2-test-levels-and-test-types/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Non-functional testing", "Teste não funcional avalia como o sistema se comporta"]
lote: software-testes-2000-0001
---

# Teste não funcional avalia como o sistema se comporta

## Em uma frase
Teste não funcional avalia características de qualidade diferentes da funcionalidade, isto é, quão bem o sistema se comporta.

## Por que importa
Um sistema pode retornar a resposta correta e ainda ser inseguro, lento, inacessível ou indisponível para o uso esperado. Características não funcionais afetam risco e experiência mesmo quando as funções existem.

## Como funciona
O CTFL usa o contraste “como o sistema se comporta” em relação ao “que” funcional. Exemplos de características incluem eficiência de desempenho, compatibilidade, usabilidade, confiabilidade, segurança, manutenibilidade, portabilidade e safety. Algumas verificações podem começar cedo — por exemplo em revisão ou teste de componente — mas muitas exigem ambiente ou medidas específicas.

## Exemplo
Um endpoint pode retornar JSON válido em todos os testes funcionais e ultrapassar o limite de latência sob concorrência. Um teste de performance precisa de workload e critério medível para que o resultado seja interpretável.

## Limites e trade-offs
Uma métrica isolada não resume uma característica inteira; resultados dependem de ambiente, carga, dados e perfil de uso. Testar cedo não elimina a necessidade de avaliação em sistema representativo quando o risco assim exige.

## Como verificar
Escolha característica, cenário, escala e critério de aceitação; documente ambiente e limitações e complemente com verificações funcionais relacionadas.

## Conexões
- [[performance-testing-modelagem-carga]] — aprofunda eficiência de desempenho.
- [[teste-acessibilidade-automatizada-revisao-humana]] — combina tecnologia e avaliação de acessibilidade.

## Fontes
- [ASTQB — CTFL §2.2.2, Test Types](https://astqb.org/2-2-test-levels-and-test-types/) — objetivo de teste não funcional e qualidades; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — §2.2.2 e ISO/IEC 25010; acesso em 2026-10-01.
