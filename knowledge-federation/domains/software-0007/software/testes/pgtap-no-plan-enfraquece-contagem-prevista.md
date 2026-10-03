---
id: software.testes.tranche15.000941
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
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://pgtap.org/documentation.html", "https://pgtap.org/pg_prove.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# pgTAP: reservar no_plan para quantidade realmente indeterminada

## Em uma frase
`no_plan()` deixa o número de assertions em aberto, possibilitando testes cuja quantidade só é conhecida durante a execução, mas elimina a verificação prévia da contagem esperada.

## Por que importa
Sem um plano fixo, um loop pode executar menos casos por erro de seleção e ainda terminar sem a mesma evidência de cobertura estrutural.

## Como funciona
Quando os casos podem ser enumerados, declarar o número facilita detectar execução incompleta.

## Exemplo
Prefira `plan(n)` quando o conjunto de verificações for estático; se usar `no_plan()`, explique por que o número depende de dados e valide a contagem por outro mecanismo.

## Limites e trade-offs
Plano dinâmico não torna seguro gerar assertions a partir de dados não confiáveis nem substitui as verificações de resultado; ele só flexibiliza a quantidade do protocolo.

## Como verificar
Execute a função com coleção vazia e não vazia, confira o output TAP e decida se cada cenário ainda consegue demonstrar que a quantidade de verificações foi a esperada.

## Conexões
- [[pgtap-plano-fixo-e-finish]] — Veja também: pgTAP: declarar plano para detectar assertions não executadas.
- [[pgtap-assertions-de-esquema-antes-do-conteudo]] — Veja também: pgTAP: verificar contrato de schema com assertions específicas.

## Fontes
- [pgTAP — Documentation](https://pgtap.org/documentation.html) — assertions TAP, schema, comparações, diretivas e funções de teste; consultado em 2026-10-02.
- [pgTAP — pg_prove](https://pgtap.org/pg_prove.html) — execução de scripts SQL e funções xUnit pelo TAP::Harness; consultado em 2026-10-02.
