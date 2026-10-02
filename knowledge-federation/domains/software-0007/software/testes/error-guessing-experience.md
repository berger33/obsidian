---
id: software.testes.error-guessing.000001
tipo: pratica
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
fontes: ["https://astqb.org/4-4-experience-based-test-techniques/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Error guessing", "Error guessing transforma experiência em hipóteses de teste"]
lote: software-testes-2000-0001
---

# Error guessing transforma experiência em hipóteses de teste

## Em uma frase
Error guessing antecipa erros, defeitos e falhas possíveis com base no histórico e no conhecimento do tester.

## Por que importa
Padrões de falha repetidos podem não estar descritos em requisitos ou critérios de cobertura. Transformar esses padrões em casos dirigidos ajuda a testar entradas e interações que a especificação não enfatizou.

## Como funciona
O CTFL indica fontes como o comportamento passado da aplicação, tipos de erro que desenvolvedores costumam cometer e falhas observadas em aplicações semelhantes. Hipóteses podem se referir a entrada, saída, lógica, cálculo, interface ou dados. A técnica não é adivinhação aleatória: o raciocínio e os exemplos que o motivaram devem ser preservados.

## Exemplo
Se integrações anteriores falharam quando o servidor respondia lentamente, teste timeout, repetição e resposta tardia, verificando que a operação não seja duplicada.

## Limites e trade-offs
Uma lista de bugs antigos pode enviesar o esforço para o passado e ignorar novas ameaças. Suspeita não é defeito confirmado; resultados precisam ser reproduzíveis e avaliados contra um oracle.

## Como verificar
Anote a hipótese, fonte de experiência, caso, comportamento esperado e resultado. Compare falhas previstas com os riscos atuais e atualize a base quando o produto muda.

## Conexões
- [[test-oracles-resultados-esperados]] — define como interpretar o resultado.
- [[defect-report-reproducibility-severity-priority]] — registra achados confirmados.

## Fontes
- [ASTQB — CTFL §4.4.1, Error Guessing](https://astqb.org/4-4-experience-based-test-techniques/) — bases da técnica e áreas típicas de falha; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — §4.4.1; acesso em 2026-10-01.
